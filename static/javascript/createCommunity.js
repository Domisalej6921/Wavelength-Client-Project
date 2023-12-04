class CreateCommunity {
    //Peer programmed component; handling profile picture and banner: Tom & Akshay
    /* To help understand what this file should contain, I got inspiration from my teammates branches
    looking through their javascript file to help understand what needs to be done here.*/
    /* Learnt about resolving async promises from:
    https://www.w3schools.com/Js/js_async.asp */
    static async submitForm() {
        // Set the form button to a loading state
        document.getElementById("createCommunitySubmit").innerHTML = Buttons.getPastelButtonLoading('Creating...', 'lg');

        // Create a variable to store issues and create a variable to store the form data
        let issue = "";
        let data = {
            name: null,
            description: null,
            profilePicture: null,
            profileBanner: null,
            isCompany: null
        }

        // Get the form data
        try {
            data.name = document.getElementById("name").value;
            data.description = document.getElementById("description").value;
            data.profilePicture = await FileUploads.format(document.getElementById("profilePicture").files[0]);
            data.profileBanner = await FileUploads.format(document.getElementById("profileBanner").files[0]);
            data.isCompany = $("#isCompany").is(':checked') /* Learnt this from:
            "https://stackoverflow.com/questions/9887360/how-can-i-check-if-a-checkbox-is-checked"*/
        }
        catch (e) {
            // Set the form button to a default state and display an error alert
            document.getElementById("createCommunitySubmit").innerHTML = Buttons.getPastelButton('Create', 'CreateCommunity.submitForm()', 'lg');
            document.getElementById("formAlerts").innerHTML = Alerts.warningAlert("One or more fields are empty or contain invalid data.", "Invalid Input!");
            return
        }
        
        // Ensures that the name and description is not only comprised of numbers or empty strings
        // Learnt how to do this check from "https://stackoverflow.com/questions/1779013/check-if-string-contains-only-digits
        if (/^\d+$/.test(data.name) || /^\d+$/.test(data.description) || data.name === "" || data.description === "") {
            document.getElementById("createCommunitySubmit").innerHTML = Buttons.getPastelButton('Create', 'CreateCommunity.submitForm()', 'lg');
            document.getElementById("formAlerts").innerHTML = Alerts.warningAlert("One or more fields are empty or contain invalid data.", "Invalid Input!");
            return;
        }
        
        /*The following code for sending the form data to the server
          was adapted from the login page*/

        // Send the form data to the server using the fetch API
        // Used: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
        const response = await fetch("/api/community/create", {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            },
            body: JSON.stringify(data)
        });

        // Check if the response was successful
        if (response.status === 200) {
            // Display a success alert
            document.getElementById("formAlerts").innerHTML = Alerts.successAlert("Your community has been created and is now awaiting approval!", "Success!");
        }
        else {
            // If the response was not successful, display an error alert
            if (response.status === 403 || response.status === 406) {
                document.getElementById("formAlerts").innerHTML = Alerts.warningAlert(await response.text(), "Invalid Input!");
            }
            // If the response is due to an unauthorized request, redirect the user to the login page
            else if (response.status === 401) {
                window.location.href = "/login";
            }
            // If the response is due to a bad request, display an error alert
            else if (response.status === 400) {
                document.getElementById("formAlerts").innerHTML = Alerts.errorAlert("An unknown error occurred. Please try again later.", "Invalid Input!");
            }
            // Any other response is due to a system error
            else {
                document.getElementById("formAlerts").innerHTML = Alerts.errorAlert("An internal server error occurred. Please try again later.", "System Error!");
            }
            document.getElementById("createCommunitySubmit").innerHTML = Buttons.getPastelButton('Create', 'CreateCommunity.submitForm()', 'lg');
        }
        // Reset the form button
        document.getElementById("createCommunitySubmit").innerHTML = Buttons.getPastelButton('Create', 'CreateCommunity.submitForm()', 'lg');
    }
    
}
