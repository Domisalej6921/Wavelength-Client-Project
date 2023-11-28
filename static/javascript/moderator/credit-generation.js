class CreditGeneration {
    //set up the class for the js to be called from
    static checkCheckbox() {

        print("gaming")
        
        document.addEventListener("DOMContentLoaded", function () {
            // the event listener that will get the elements then change them depending on the checkbox
            const unlock = document.getElementById("existingCommunity");
            const chooseCommunityDiv = document.getElementById("chooseCommunityDiv");
            const createCommunityDiv = document.getElementById("createCommunityDiv");
            const numCreditsDiv = document.getElementById("numCreditsDiv");
            const numGroupsDiv = document.getElementById("numGroupsDiv");
            const generateButtonDiv = document.getElementById("generateButtonDiv");

            // adds an event listener to the unlock checkbox for the "change" event.
            unlock.addEventListener("change", function () {
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
    }

    static submitForm () { //submit form that will get the data from the form elements
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