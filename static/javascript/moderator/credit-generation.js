class CreditGeneration {
    static submitForm() {

        document.addEventListener(type: "DOMContentLoaded", listener: function() {
            const unlock = document.getElementById(elementId: "existingCommunity");
            const chooseCommunityDiv = document.getElementById(elementId:"chooseCommunityDiv");
            const createCommunityDiv = document.getElementById(elementId:"createCommunityDiv");
            const numCreditsDiv = document.getElementById(elementId:"numCreditsDiv");
            const numGroupsDiv = document.getElementById(elementId;:"numGroupsDiv");

            unlock.addEventListener(type: "change", listener: function() {
                if (unlock.checked) {
                    chooseCommunityDiv.style.display = "block";
                    createCommunityDiv.style.display = "None";

                } else {
                    chooseCommunityDiv.style.display = "None";
                    numCreditsDiv.style.display = "None";
                    numGroupsDiv.style.display = "None";
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
