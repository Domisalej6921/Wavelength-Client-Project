let formData = {
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
            formData[cacheID] = result;
            // Reset the submit button
            document.getElementById("modalEditProfileSubmit").innerHTML = Buttons.getPastelButton("Edit", "Profile.editFormSubmit()", "lg");
        });
    }

    static editFormSubmit() {
        // Make the submit button a loading state
        document.getElementById("modalEditProfileSubmit").innerHTML = Buttons.getPastelButtonLoading("Editing...", "lg");
        // Get the username input
        formData.username = document.getElementById("modalUsername").value;

        let issue = "";

        // Send the form data to the server
        const xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState === 4) {
                // If the server returns a 200 status code (OK)
                if (this.status === 200) {
                    // Clear the form and display a success message
                    document.getElementById("modalEditProfileForm").reset();
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

                // Clear the password field
                document.getElementById("password").value = "";
            }
        };
        xhttp.open("POST", "/api/profile-edit", true);
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhttp.send(JSON.stringify(formData));
    }
}