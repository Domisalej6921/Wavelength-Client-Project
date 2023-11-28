class CreditGeneration {
    //set up the class for the js to be called from
    static checkCheckbox() {

        // the event listener that will get the elements then change them depending on the checkbox
        const unlock = document.getElementById("existingCommunity").checked;
        const chooseCommunityDiv = document.getElementById("chooseCommunityDiv");
        const createCommunityDiv = document.getElementById("createCommunityDiv");
        const numCreditsDiv = document.getElementById("numCreditsDiv");
        const numGroupsDiv = document.getElementById("numGroupsDiv");
        const generateButtonDiv = document.getElementById("generateButtonDiv");
        // adds an event listener to the unlock checkbox for the "change" event.

        if (unlock === true) {
            // When the checkbox is checked this should run
            chooseCommunityDiv.style.display = "block";
            numCreditsDiv.style.display = "block";
            numGroupsDiv.style.display = "block";
            generateButtonDiv.style.display = "block";
            createCommunityDiv.style.display = "none"; //makes this not visible
        }
        else {
            // When the checkbox is not checked
            chooseCommunityDiv.style.display = "none";
            numGroupsDiv.style.display = "none";
            numCreditsDiv.style.display = "none";
            generateButtonDiv.style.display = "none";
            createCommunityDiv.style.display = "block"; //makes this visible
        }

    }

    //Used to calculate and update the display of the number of credits being generated
    static totalCredits () {
        var numCredits = document.getElementById("numCredits").value;
        var numGroups = document.getElementById("numGroups").value;

        if (numCredits === null) {
            numCredits = 0
        }
        if (numGroups === null) {
            numGroups = 0
        }

        var creditTotal = numCredits * numGroups
        document.getElementById("creditTotal").innerHTML = creditTotal;
        console.log(creditTotal)
    }

    static submitForm () { //submit form that will get the data from the form elements

        const checked = document.getElementById("existingCommunity").checked;
        if (checked === true) {

            const data = {
                numCredits: document.getElementById("numCredits").value,
                numGroups: document.getElementById("numGroups").value,
                chosenCommunity: document.getElementById("chooseCommunity").value,
            }
        }

        else {
            return null
        }
    }
}