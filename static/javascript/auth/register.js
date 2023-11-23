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

        // Get the form data
        const data = {
            username: document.getElementById("username").value,
            email: document.getElementById("email").value,
            password: document.getElementById("password").value,
            repeatPassword: document.getElementById("repeatPassword").value,
            accountType: document.getElementById("accountType").value
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
    }
}