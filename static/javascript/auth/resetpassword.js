class ResetPassword {
    static overrideForm(code = null) {
        /* urlParams method was taken from https://www.sitepoint.com/get-url-parameters-with-javascript/ */
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

    }

    static submitResetForm() {

    }
}