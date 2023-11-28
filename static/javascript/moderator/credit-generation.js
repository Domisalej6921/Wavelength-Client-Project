class CreditGeneration {
    static submitForm() {

        document.addEventListener("DOMContentLoaded",function() {
            const unlock = document.getElementById("existingCommunity");
            const chooseCommunityDiv = document.getElementById("chooseCommunityDiv");
            const createCommunityDiv = document.getElementById("createCommunityDiv");
            const numCreditsDiv = document.getElementById("numCreditsDiv");
            const numGroupsDiv = document.getElementById("numGroupsDiv");
            const generateButtonDiv = document.getElementById("generateButtonDiv");

            unlock.addEventListener("change",function() {
                if (unlock.checked) {
                    chooseCommunityDiv.style.display = "block";
                    createCommunityDiv.style.display = "none";

                } else {
                    chooseCommunityDiv.style.display = "none";
                    numCreditsDiv.style.display = "none";
                    numGroupsDiv.style.display = "none";
                    generateButtonDiv.style.display = "none";
                    createCommunityDiv.style.display = "block";
                }
            })
        })

        const data = {
            username: document.getElementById("numCredits").value,
            name: document.getElementById("numGroups").value,
            email: document.getElementById("chooseCommunity").value,
        }


    }
}

document.addEventListener("DOMContentLoaded",function() {
    CreditGeneration.submitForm()
});