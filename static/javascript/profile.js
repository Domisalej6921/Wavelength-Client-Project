let data = {
    username: null,
    profilePicture: null,
    profileBanner: null
};

class Profile {
    static renderEditForm () {
        document.getElementById("formModalHeader").innerHTML = Modals.header("Edit Profile");
        document.getElementById("formModalBody").innerHTML = Modals.editProfile();

        document.getElementById("root").innerHTML = `<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#formModal">Open modal</button>`;
    }

    static handleUpload(documentID, cacheID) {
        // Make the submit button a loading state
        document.getElementById("modalEditProfileSubmit").innerHTML = Buttons.getPastelButtonLoading("Formatting file...", "lg");
        let picture = document.getElementById(documentID);
        const file = picture.files[0];
        FileUploads.format(file).then((result) => {
            data[cacheID] = result;
            // Reset the submit button
            document.getElementById("modalEditProfileSubmit").innerHTML = Buttons.getPastelButton("Edit", "Profile.editFormSubmit()", "lg");
        });
    }

    static editFormSubmit() {
        // Make the submit button a loading state
        document.getElementById("modalEditProfileSubmit").innerHTML = Buttons.getPastelButtonLoading("Editing...", "lg");

        // Get the username input
        data.username = document.getElementById("modalUsername").value;

        // Local input validation
        let issue = "";

        // Check if the username is not empty
        if (data.username.length > 0) {
            // Check if the username is at least 3 characters long
            if (data.username.length < 3) {
                issue = "Username must be at least 3 characters long.";
            }
            // Check if the username has whitespace
            else if (data.username.includes(" ")) {
                issue = "Username cannot contain whitespace.";
            }
        }
        // If it is empty, set it to null
        else {
            data.username = null;
        }

        // Check if anything is being uploaded
        if (data.username === null && data.profilePicture === null && data.profileBanner === null) {
            issue = "You must change at least one field.";
        }

        if (issue.length > 0) {
            // Set the form button to a default state and display an error alert
            document.getElementById("modalEditProfileSubmit").innerHTML = Buttons.getPastelButton("Edit", "Profile.editFormSubmit()", "lg");
            document.getElementById("modalEditProfileFormAlerts").innerHTML = Alerts.warningAlert(issue, "Invalid Input!");

            return
        }

        // Send the form data to the server
        const xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState === 4) {
                // If the server returns a 200 status code (OK)
                if (this.status === 200) {
                    // Clear the form and display a success message
                    document.getElementById("modalEditProfileForm").reset();
                    data = {username: null, profilePicture: null, profileBanner: null};

                    document.getElementById("modalEditProfileFormAlerts").innerHTML = Alerts.successAlert(
                        "Your profile has been updated.",
                        "Success!"
                    );
                }
                // If the server returns a 401 status code (Unauthorized)
                else if (this.status === 401) {
                    issue = "The credentials you've entered are not valid.";
                }
                // If the server returns a 406 status code (Not Acceptable)
                else if (this.status === 406) {
                    issue = this.responseText;
                }
                // If the server returns a 400 status code (Bad Request)
                else if (this.status === 400) {
                    issue = "An unknown error occurred. Please try again later.";
                }
                else {
                    issue = "An internal server error occurred. Please try again later."
                }

                // If we get here then an error occurred
                // Reset the submit button
                document.getElementById("modalEditProfileSubmit").innerHTML = Buttons.getPastelButton("Edit", "Profile.editFormSubmit()", "lg");
                if (this.status === 401 || this.status === 406) {
                    document.getElementById("modalEditProfileFormAlerts").innerHTML = Alerts.warningAlert(issue, "Invalid Input!");
                }
                else {
                    document.getElementById("modalEditProfileFormAlerts").innerHTML = Alerts.errorAlert(issue, "System Error!");
                }
            }
        };
        xhttp.open("POST", "/api/profile-edit", true);
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhttp.send(JSON.stringify(data));
    }
}