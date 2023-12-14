class Profile {
    static async renderPage() {
        // Get the requested user ID from the URL
        const urlParams = new URLSearchParams(window.location.search);
        const userID = parseInt(urlParams.get('id'));

        // Send the form data to the server using the fetch API
        const response = await fetch('/api/profile', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({userID: userID})
        })

        // If the server returns a 200 status code (OK)
        if (response.ok) {
            // Get the response's data
            const data = await response.json();

            // Add the div for modals to load into
            document.getElementById('root').innerHTML = `
                <div id="modals"></div>
            `;

            // Load the modals into the page
            EditProfile.renderEditForm();
            ManageTags.renderEditForm();

            // Add tags to the select element
            await ManageTags.searchTags();

            // Check images and set to defaults if they do not exist
            if (data.profilePicture === null) {
                data.profilePicture = {
                    "path": "/static/images/blank-pfp.png",
                    "description": "Default Profile Picture"
                };
            }

            if (data.profileBanner === null) {
                data.profileBanner = {
                    "path": "/static/images/background-image.png",
                    "description": "Default Profile banner"
                };
            }

            // Load the profile into the page
            document.getElementById('root').innerHTML += `
            <div class="d-flex flex-wrap bg-light">
                <div class="d-flex flex-wrap" style="max-height: 15vh; max-width: 20%">
                    <img src="${data.profilePicture.path}" class="img-fluid" style="width: 100%; max-height: 15vh" alt="${data.profilePicture.description}" />
                </div>
                <div class="d-flex flex-wrap" style="max-height: 15vh; max-width: 80%">
                    <img src="${data.profileBanner.path}" class="img-fluid" style="width: 100%; max-height: 15vh" alt="${data.profileBanner.description}" />
                </div>
            </div>
            `;

            // Load a different profile if the user is logged in
            if (data.isMyAccount) {
                document.getElementById('root').innerHTML += `
                <div class="profile-container align-content" id="profileHeader">
                    <button class="btn btn-pastel" data-bs-toggle="modal" data-bs-target="#editTagsFormModal">Assign Tags</button>
                    <button class="btn btn-pastel" data-bs-toggle="modal" data-bs-target="#editProfileFormModal">Edit Profile</button>
                </div>
                `;

                // Load a button for a user to become a mentor if they are not already
                if (!data.isMentor) {
                    document.getElementById('profileHeader').innerHTML += `
                    <button class="btn btn-pastel" disabled>Become Mentor</button>
                    `;
                }
            }

            // Load the profile into the page
            document.getElementById('root').innerHTML += `
            <div class="profile-container align-content">
                <h1 class="display-4">#${data.username}</h1>
                <p class="h6">${data.description}</p>
            </div>
            `;

            // Load a button for a user to enquire about the profile being their mentor
            if (!data.isMyAccount && data.isMentor) {
                document.getElementById('root').innerHTML += `
                <div class="profile-container align-content">
                    <button class="btn btn-pastel" disabled>Enquire Mentorship</button>
                </div>
                `;
            }
        }
        // If the response is due to a not found error, display an error alert
        else if (response.status === 404) {
            document.getElementById('root').innerHTML = Alerts.warningAlert('The requested user does not exist..', 'Not Found!');
        }
        // If the response is due to an unauthorized request, redirect to the login page
        else if (response.status === 401) {
            window.location.href = '/login';
        }
        // The profile has failed to load
        else {
            document.getElementById('root').innerHTML = Alerts.errorAlert('Failed to load profile. Please try again later...', 'System Error!');
        }
    }
}