class ResetPassword {
    static overrideForm(code = null) {
        // urlParams method was taken from https://www.sitepoint.com/get-url-parameters-with-javascript/
        const queryString = window.location.search;
        const urlParams = new URLSearchParams(queryString);
        code = urlParams.get('code')

        if (code !== null) {
            // Override the form with the reset password form
            document.getElementById("passwordResetForm").innerHTML = `
                <p class="fs-1 align-content">Password Reset</p>
                <div class="form-floating mb-3">
                    <input type="text" class="form-control" id="code" placeholder="807c8afbbe614385">
                    <label for="code">Password Reset Code</label>
                </div>
                <div class="form-floating mb-3">
                        <input type="password" class="form-control" id="password" placeholder="Enter a password">
                        <label for="password">New Password</label>
                </div>
                <div class="form-floating mb-3">
                    <input type="password" class="form-control" id="repeatPassword" placeholder="Re-enter your password">
                    <label for="repeatPassword">Confirm New Password</label>
                </div>
                <div class="align-content" id="passwordResetFormSubmit">
                    ${Buttons.getPastelButton("Reset Password", "ResetPassword.submitResetForm()", "lg")}
                </div>
            `

            // Set the code field to the code in the URL
            document.getElementById("code").value = code;
        }
    }

    static submitInitiateForm() {
        // Set the form button to a loading state
        document.getElementById("passwordResetFormSubmit").innerHTML = Buttons.getPastelButtonLoading('Sending Reset Code...', 'lg');

        // Get the form data
        const data = {
            email: document.getElementById("email").value
        }

        let issue = "";

        // Send the form data to the server
        const xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState === 4) {
                // If the server returns a 200 status code (OK)
                if (this.status === 200) {
                    // Delete the form and display a success alert
                    document.getElementById("passwordResetFormSubmit").remove()
                    document.getElementById("passwordResetForm").remove()
                    document.getElementById("formAlerts").innerHTML = Alerts.successAlert(
                        "A password reset code has been sent to your email address. Please check your email and follow the instructions provided.",
                        "Success!"
                    );
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
                document.getElementById("passwordResetFormSubmit").innerHTML = Buttons.getPastelButton('Get Reset Code', 'ResetPassword.submitInitiateForm()', 'lg');
                if (this.status === 401 || this.status === 403) {
                    document.getElementById("formAlerts").innerHTML = Alerts.warningAlert(issue, "Invalid Input!");
                }
                else {
                    document.getElementById("formAlerts").innerHTML = Alerts.errorAlert(issue, "System Error!");
                }
            }
        };
        xhttp.open("POST", "/auth/passwordreset-initiate", true);
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhttp.send(JSON.stringify(data));
    }

    static submitResetForm() {
        // Set the form button to a loading state
        document.getElementById("passwordResetFormSubmit").innerHTML = Buttons.getPastelButtonLoading('Updating Password...', 'lg');

        // Get the form data
        const data = {
            code: document.getElementById("code").value,
            password: document.getElementById("password").value,
            repeatPassword: document.getElementById("repeatPassword").value,
        }

        let issue = "";

        // Send the form data to the server
        const xhttp = new XMLHttpRequest();
        xhttp.onreadystatechange = function() {
            if (this.readyState === 4) {
                // If the server returns a 200 status code (OK)
                if (this.status === 200) {
                    // Redirect to the login page
                    window.location.href = "/login?reset=true";
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
                document.getElementById("passwordResetFormSubmit").innerHTML = Buttons.getPastelButton("Reset Password", "ResetPassword.submitResetForm()", "lg")
                if (this.status === 401 || this.status === 403) {
                    document.getElementById("formAlerts").innerHTML = Alerts.warningAlert(issue, "Invalid Input!");
                }
                else {
                    document.getElementById("formAlerts").innerHTML = Alerts.errorAlert(issue, "System Error!");
                }
            }
        };
        xhttp.open("PUT", "/auth/passwordreset", true);
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhttp.send(JSON.stringify(data));
    }
}