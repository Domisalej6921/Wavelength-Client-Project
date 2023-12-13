class Login {
    static renderPreDefinedAlerts() {
        // urlParams method was taken from https://www.sitepoint.com/get-url-parameters-with-javascript/
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);

        if (urlParams.get('verified') !== null) {
            document.getElementById("formAlerts").innerHTML = Alerts.successAlert(
                "Your account has been verified. You may now login.",
                "Success!"
            );
        }
        else if (urlParams.get('reset') !== null) {
            document.getElementById("formAlerts").innerHTML = Alerts.successAlert(
                "Your password has been reset. You may now login.",
                "Success!"
            );
        }
    }

    static submitForm() {
        // Set the form button to a loading state
        document.getElementById("loginFormSubmit").innerHTML = Buttons.getPastelButtonLoading('Authenticating...', 'lg');

        // Get the form data
        const data = {
            email: document.getElementById("email").value,
            password: document.getElementById("password").value,
        }

        let issue = "";

        // Send the form data to the server
        const xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState === 4) {
                // If the server returns a 200 status code (OK)
                if (this.status === 200) {
                    // redirect to the dashboard
                    window.location.href = "/account/dashboard";
                }
                // If the server returns a 401 status code (Unauthorized)
                else if (this.status === 401) {
                    issue = "The credentials you've entered are not valid.";
                }
                // If the server returns a 403 status code (Forbidden)
                else if (this.status === 403) {
                    issue = "Your account has not been verified. Please check your email for the verification code.";
                }
                // If the server returns a 400 status code (Bad Request)
                else if (this.status === 400) {
                    issue = "An unknown error occurred. Please try again later.";
                }
                else {
                    issue = "An internal server error occurred. Please try again later."
                }

                // If we get here then an error occurred
                document.getElementById("loginFormSubmit").innerHTML = Buttons.getPastelButton('Login', 'Login.submitForm()', 'lg');
                if (this.status === 401 || this.status === 403) {
                    document.getElementById("formAlerts").innerHTML = Alerts.warningAlert(issue, "Invalid Input!");
                }
                else {
                    document.getElementById("formAlerts").innerHTML = Alerts.errorAlert(issue, "System Error!");
                }

                // Clear the password field
                document.getElementById("password").value = "";
            }
        };
        xhttp.open("POST", "/auth/login", true);
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhttp.send(JSON.stringify(data));
    }
}