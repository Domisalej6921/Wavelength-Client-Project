class BecomeMentor {
    static async submitMentorshipForm() {

        let formData = {
            username: null,
            desc: null,
        }

        try {
            formData.username = document.getElementById("username")
            formData.desc = document.getElementById("description")
        }

        const response = await fetch("/api/account/become_mentor", {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            },
            body: JSON.stringify(formData))
        }

        // Check if the response was successful
        if (response.status === 200) {
            // Display a success alert
            document.getElementById("formAlerts").innerHTML = Alerts.successAlert("Congrats, You have signed up to be a mentor!");
        }
        else {
            document.getElementById("formAlerts").innerHTML = Alerts.warningAlert(await response.text(), "We are unable to carry out the is request now. Try again later!");
        }
    }
}