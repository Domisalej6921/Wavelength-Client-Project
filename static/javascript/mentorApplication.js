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
}

function submitMentorApp() {
    console.log("form pending......")
}