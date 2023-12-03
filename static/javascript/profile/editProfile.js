class EditProfile {
    static renderEditForm () {
        document.getElementById("formModalHeader").innerHTML = Modals.header("Edit your profile");
        document.getElementById("formModalBody").innerHTML = Modals.editProfile();

        document.getElementById("root").innerHTML = `<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#formModal">Open modal</button>`;
    }

    static async formSubmit() {
        // Make the submit button a loading state
        document.getElementById("modalEditProfileSubmit").innerHTML = Buttons.getPastelButtonLoading("Editing...", "lg");

        let data = {
            username: null,
            profilePicture: null,
            profileBanner: null
        };

        // Get the form data
        data.username = document.getElementById("modalUsername").value;
        try {
            data.profilePicture = await FileUploads.format(document.getElementById("modalProfilePicture").files[0]);
        } catch {
            data.profilePicture = null;
        }
        try {
            data.profileBanner = await FileUploads.format(document.getElementById("modalProfileBanner").files[0]);
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
        if (data.username === null && data.profilePicture === null && data.profileBanner === null) {
            issue = "You must change at least one field.";
        }

        // Check if there is an issue, if so, display it and reset the submit button
        if (issue.length > 0) {
            // Set the form button to a default state and display an error alert
            document.getElementById("modalEditProfileSubmit").innerHTML = Buttons.getPastelButton("Edit", "EditProfile.formSubmit()", "lg");
            document.getElementById("modalEditProfileFormAlerts").innerHTML = Alerts.warningAlert(issue, "Invalid Input!");

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
            document.getElementById("modalEditProfileForm").reset();
            document.getElementById("modalEditProfileFormAlerts").innerHTML = Alerts.successAlert(
                "Your profile has been updated.",
                "Success!"
            );
        } else {
            // If the response was not successful, display an error alert
            if (response.status === 403 || response.status === 406) {
                document.getElementById("modalEditProfileFormAlerts").innerHTML = Alerts.warningAlert(await response.text(), "Invalid Input!");
            }
            // If the response is due to an unauthorized request, redirect to the login page
            else if (response.status === 401) {
                window.location.href = "/login";
            }
            // If the response is due to a bad request, display an error alert
            else if (response.status === 400) {
                document.getElementById("modalEditProfileFormAlerts").innerHTML = Alerts.errorAlert("An unknown error occurred. Please try again later.", "Invalid Input!");
            }
            // Any other response is due to a system error
            else {
                document.getElementById("modalEditProfileFormAlerts").innerHTML = Alerts.errorAlert("An internal server error occurred. Please try again later.", "System Error!");
            }
        }
        // Reset the form button
        document.getElementById("modalEditProfileSubmit").innerHTML = Buttons.getPastelButton("Edit", "EditProfile.formSubmit()", "lg");
    }
}