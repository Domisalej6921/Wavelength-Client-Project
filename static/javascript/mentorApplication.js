class Mentor {
    static async displayMentor() {
        let limit = 1
        const response = await fetchMentors.getWithLimit(limit)

        console.log("working") // delete after

        if (response.status === 200) {

            // Get data from the response
            let data = await response.json()

            let mentor = "";
            mentor += Mentors.renderMentor(data)

            // Render it onto the page
            document.getElementById('pageContent').innerHTML = mentor;

        else
            if (response.status === 401) {
                window.location.href = "/login"
            } else {
                document.getElementById('pageContent').innerHTML = Alerts.errorAlert("Error! Mentors failed to render. Please try again later!");
            }
        }
    }
    static async submitApplicationForMentorship() {
        //Initialising formData variable
        let formData = {
            firstName: null,
            lastName: null,
            email: null,
            desc: null,
        }

        try {
            formData.firstName = document.getElementById("firstName")
            formData.lastName = document.getElementById("lastName")
            formData.email = document.getElementById("email")
            formData.desc = document.getElementById("description")
        }

        const response = await fetch("/api/account/mentor_apply", {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            },
            body: JSON.stringify(formData)
        });

        // Check if the response was successful
        if (response.status === 200) {
            // Display a success alert
            document.getElementById("formAlerts").innerHTML = Alerts.successAlert("Your community has been created and is now awaiting approval!", "Success!");
        }
        else {
            document.getElementById("formAlerts").innerHTML = Alerts.warningAlert(await response.text(), "We are unable to carry out the is request now. Try again later!");
        }
    }
}