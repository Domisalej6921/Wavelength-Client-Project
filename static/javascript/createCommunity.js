class CreateCommunity {
    //Peer programmed component; handeling profile picture and banner: Tom & Akshay
    /* To help understand what this file should contain, I got insipation from my teammates branches
    looking throught there javascript file to help understand what needs to be done here.*/
    /* Learnt about resolving async promises from:
    https://www.w3schools.com/Js/js_async.asp */
    static async submitForm() {
        // Set the form button to a loading state
        document.getElementById("submitButton").innerHTML = Buttons.getPastelButtonLoading('Loading...', 'lg');

        // Gets form data
        const data = {
            name: document.getElementById("name").value,
            description: document.getElementById("description").value,
            profilePicture: document.getElementById("profilePicture"),
            profileBanner: document.getElementById("profileBanner"),
            isCompany: $("#isCompany").is(':checked') /* Learnt this from:
            "https://stackoverflow.com/questions/9887360/how-can-i-check-if-a-checkbox-is-checked"*/
        }

        /* Checks that there is a file uploaded for the profile picture
        and if so puts it through 'FileUploads' to get the encodded version*/
        if (data.profilePicture) {
            data.profilePicture = await FileUploads.format(data.profilePicture.files[0]);
            console.log("Profile Picture Result:", data.profilePicture);
        } else {
            console.log("No file selected for profile picture");
        }
        /* Checks that there is a file uploaded for the profile banner
        and if so puts it through 'FileUploads' to get the encodded version*/
        if (data.profileBanner) {
            data.profileBanner = await FileUploads.format(data.profileBanner.files[0]);
            console.log("Profile Banner:", data.profileBanner);
        } else {
            console.log("No file selected for profile banner");
        }

        // Returning the dictionary to the console, which helps with debugging
        console.log("Form submitted with data:", data);
    
        let issue = "";

        /*The following code for sending the form data to the server
          was adapted from the login page*/
        const xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState === 4) {
                // If the seeturns a 200 status code (Success)
                if (this.status === 200) {
                    // redirect to main page
                    window.location.href = "";
                }
                // If the server returns a 401 status code (Unauthorized)
                else if (this.status === 401) {
                    issue = "You need to be authenticated to preform this task.";
                }
                // If the server returns a 403 status code (Forbidden)
                else if (this.status === 403) {
                    issue = "Your account does not have permissions for this action.";
                }    
                // If the server returns a 406 status code (Not Acceptable)
                else if (this.status === 406) {
                    issue = "There is an incorrect file type or a file which is too large.";
                }
                // If the server returns a 400 status code (Bad Request)
                else if (this.status === 400) {
                    issue = "Missing or incorrect field(s).";
                }
                // For an unexpected server status code
                else {
                    issue = "An internal server error occurred. Please try again later."
                }
                // If we get here then an error occurred
                document.getElementById("submitButton").innerHTML = Buttons.getPastelButton('Submit', 'createCommunity.submitForm()', 'lg');
                if (this.status === 401 || this.status === 403 || this.status === 406) {
                    document.getElementById("formAlerts").innerHTML = Alerts.warningAlert(issue, "Not Authorised for this action");
                }
                else {
                    document.getElementById("formAlerts").innerHTML = Alerts.errorAlert(issue, "System Error!");
                }

            }
        }
        xhttp.open("POST", "/api/community/create", true);
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhttp.send(JSON.stringify(data))
    }
    
}
