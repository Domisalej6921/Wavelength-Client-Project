class Profile {
    static async renderPage() {
        // Get the requested user ID from the URL
        const urlParams = new URLSearchParams(window.location.search);
        const userID = urlParams.get('id');

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
            await ManageTags.searchTags(true);

            // Load the profile into the page
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