class Verify {
    static loadPage() {
        document.getElementById("formAlerts").innerHTML = Alerts.warningAlert("The verification code you've entered is not valid", "Invalid Code!")
    }
}