class EditProfile {
    static renderEditForm () {
        const content = `<div class="modal fade" id="editProfileFormModal">
                <div class="modal-dialog modal-dialog-centered">
                    <div class="modal-content">
    
                        <div class="modal-header" id="editProfileFormModalHeader">
                            ${Modals.header("Edit your profile")}
                        </div>
    
                        <div class="modal-body" id="editProfileFormModalBody">
                            ${Modals.editProfile()}
                        </div>
    
                        <div class="modal-footer"></div>
                    </div>
                </div>
            </div>`

        if (document.getElementById("modals") !== null) {
            document.getElementById("modals").innerHTML += content
        }
        else {
            document.getElementById("modals").innerHTML = content
        }
    }

    static async formSubmit() {
        // Make the submit button a loading state
        document.getElementById("editProfileFormModalSubmit").innerHTML = Buttons.getPastelButtonLoading("Editing...", "lg");

        let data = {
            username: null,
            description: null,
            profilePicture: null,
            profileBanner: null
        };

        // Get the form data
        data.username = document.getElementById("editProfileFormModalUsername").value;
        data.description = document.getElementById("editProfileFormModalDescription").value;
        try {
            data.profilePicture = await FileUploads.format(document.getElementById("editProfileFormModalProfilePicture").files[0]);
        } catch {
            data.profilePicture = null;
        }
        try {
            data.profileBanner = await FileUploads.format(document.getElementById("editProfileFormModalProfileBanner").files[0]);
        } catch {
            data.profileBanner = null;
        }

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
        if (data.username === null && data.description === null && data.profilePicture === null && data.profileBanner === null) {
            issue = "You must change at least one field.";
        }

        // Check if there is an issue, if so, display it and reset the submit button
        if (issue.length > 0) {
            // Set the form button to a default state and display an error alert
            document.getElementById("editProfileFormModalSubmit").innerHTML = Buttons.getPastelButton("Edit", "EditProfile.formSubmit()", "lg");
            document.getElementById("editProfileFormModalAlerts").innerHTML = Alerts.warningAlert(issue, "Invalid Input!");

            return
        }

        // Send the form data to the server using the fetch API
        // Used: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
        const response = await fetch("/api/profile-edit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            },
            body: JSON.stringify(data)
        });

        // Check if the response was successful
        if (response.ok) {
            // Clear the form and display a success message
            document.getElementById("editProfileModalForm").reset();
            document.getElementById("editProfileFormModalAlerts").innerHTML = Alerts.successAlert(
                "Your profile has been updated.",
                "Success!"
            );
        } else {
            // If the response was not successful, display an error alert
            if (response.status === 403 || response.status === 406) {
                document.getElementById("editProfileFormModalAlerts").innerHTML = Alerts.warningAlert(await response.text(), "Invalid Input!");
            }
            // If the response is due to an unauthorized request, redirect to the login page
            else if (response.status === 401) {
                window.location.href = "/login";
            }
            // If the response is due to a bad request, display an error alert
            else if (response.status === 400) {
                document.getElementById("editProfileFormModalAlerts").innerHTML = Alerts.errorAlert("An unknown error occurred. Please try again later.", "Invalid Input!");
            }
            // Any other response is due to a system error
            else {
                document.getElementById("editProfileFormModalAlerts").innerHTML = Alerts.errorAlert("An internal server error occurred. Please try again later.", "System Error!");
            }
        }
        // Reset the form button
        document.getElementById("editProfileFormModalSubmit").innerHTML = Buttons.getPastelButton("Edit", "EditProfile.formSubmit()", "lg");
    }
}