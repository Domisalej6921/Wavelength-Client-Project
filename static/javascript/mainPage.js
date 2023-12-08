class MainPage {
    static async renderMentors(limit = 12){
        const response = await fetchMentors.getWithLimit(limit)

        if (response.status === 200) {
            console.log("F*** OFF AKSHAY")

            // Get data from the response
            let data = await response.json()

            console.log(data[0])

            // Render mentors onto the page
            let mentors = "";
            for (let i = 0; i < data.length; i++) {
                mentors += Mentors.renderCard(data[i])
            }

            // Render it onto the page
            document.getElementById('mentorList').innerHTML = mentors;
        }
        else if (response.status === 401) {
            window.location.href = "/login"
        }
        else {
            document.getElementById('mentorList').innerHTML = Alerts.errorAlert("Error! Mentors failed to render. Please try again later!");
        }
    }
}

function loadMoreButton() {
    let originalContainer = document.getElementById("mentorList");
    let newItemsContainer = document.createElement("div");
    newItemsContainer.className = "card";
    newItemsContainer.textContent = "tygscfgscvhgscv"
    originalContainer.appendChild(newItemsContainer);
}