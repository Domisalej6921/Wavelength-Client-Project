class Register {
    /* Initialize all tooltips on the page
    Source: https://getbootstrap.com/docs/5.2/components/tooltips/ */
    static activateTooltips() {
        const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
        const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl,))
    }

    static submitForm() {
        // Set the form button to a loading state
        document.getElementById("registerFormSubmit").innerHTML = Buttons.getPastelButtonLoading('Registering...', 'lg');

        // Get the mentor status
        let isMentor = false;
        if (document.getElementById("accountType").value === "mentor") {
            isMentor = true;
        }

        // Get the form data
        const data = {
            username: document.getElementById("username").value,
            name: document.getElementById("name").value,
            email: document.getElementById("email").value,
            password: document.getElementById("password").value,
            repeatPassword: document.getElementById("repeatPassword").value,
            isMentor: isMentor
        }

        // Local input validation
        let issue = "";

        // Check if the password is at least 8 characters long
        if (data.password.length < 8) {
            issue = "Password must be at least 8 characters long.";
        }
        // Check if the passwords match
        else if (data.password !== data.repeatPassword) {
            issue = "Passwords do not match.";
        }
        // Check if the username is at least 3 characters long
        else if (data.username.length < 3) {
            issue = "Username must be at least 3 characters long.";
        }
        // Check if the username has whitespace
        else if (data.username.includes(" ")) {
            issue = "Username cannot contain whitespace.";
        }

        if (issue.length > 0) {
            // Set the form button to a default state and display an error alert
            document.getElementById("registerFormSubmit").innerHTML = Buttons.getPastelButton('Register', 'Register.submitForm()', 'lg');
            document.getElementById("formAlerts").innerHTML = Alerts.warningAlert(issue, "Invalid Input!");

            return
        }

        // Send the form data to the server
        // Used: https://www.w3schools.com/xml/ajax_xmlhttprequest_send.asp as an AJAX tutorial
        const xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState === 4) {
                // If the server returns a 200 status code (OK)
                if (this.status === 200) {
                    // Delete the form and display a success alert
                    document.getElementById("registerFormSubmit").remove()
                    document.getElementById("registerForm").remove()
                    document.getElementById("formAlerts").innerHTML = Alerts.successAlert(
                        "You have registered successfully. A verification code has been sent to your email inbox please follow the instructions provided on the email.",
                        "Success!"
                    );
                    return
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
                document.getElementById("registerFormSubmit").innerHTML = Buttons.getPastelButton('Register', 'Register.submitForm()', 'lg');
                if (this.status === 406) {
                    document.getElementById("formAlerts").innerHTML = Alerts.warningAlert(issue, "Invalid Input!");
                }
                else {
                    document.getElementById("formAlerts").innerHTML = Alerts.errorAlert(issue, "System Error!");
                }
            }
        };
        xhttp.open("POST", "/auth/register", true);
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhttp.send(JSON.stringify(data));
    }
}