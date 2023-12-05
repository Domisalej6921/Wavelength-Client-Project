class MainPage {
    static async renderMentors(){
        const response = await fetchMentors.getWithLimit()

        if (response.status === 200) {
            console.log("FUCK OFF AKSHAY")
        }
        else if (response.status === 401) {
            window.location.href = "/login"
        }
        else {
            document.getElementById('mentorList').innerHTML = Alerts.errorAlert("Error! Mentors failed to render. Please try again later!");
        }
    }
}