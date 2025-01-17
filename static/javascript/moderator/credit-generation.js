class CreditGeneration {
    //set up the class for the js to be called from

    static onLoadFunctions() { //Function that calls the functions to run when the page loads
        CreditGeneration.getCommunities()
        CreditGeneration.checkCheckbox()
    }

    static getCommunities() { //Function for getting a list of the first x communities to put in the dropdown

        const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
        xhttp.open("GET", "/listCommunities", true); //set method and the url and if it asynchornus
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

        xhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) { //200 = server is okay
                const response = JSON.parse(this.responseText); // passing back the server response

                for (let i = 0; i < response.length; i++) {
                    document.getElementById("chooseCommunity").innerHTML += `<option value="${response[i]}"> ${response[i]} </option>`;
                }
            }
        };
        xhttp.send()
    }

    static checkValid() { // Input validation for the credits
        const numCredits = Number(document.getElementById("numCredits").value);
        let reasonInvalid = "";
        // console.log(typeof numCredits)
        // console.log(Number.isInteger(numCredits))

        if (Number.isInteger(numCredits)) { //Checks if the value is an integer

            if (numCredits > 200) { // Limits the number of credits to 200
                reasonInvalid = "That is too many credits to generate at once!";
                // console.log(reasonInvalid)
            }

            else if (numCredits <= 0) { //Checks if the value is positive
                reasonInvalid = "Please do not generate negative credits!"
                // console.log(reasonInvalid)
            }

            else {
                reasonInvalid = false
                // console.log(reasonInvalid)
            }
        }
        else {
            reasonInvalid = "Please Input a integer!"
            // console.log(reasonInvalid)
        }

        if (reasonInvalid === false) {
            this.totalCredits()
        }

        else {
            // console.log("Invalid Input", reasonInvalid)
            document.getElementById("formAlerts").innerHTML = Alerts.warningAlert(reasonInvalid, "Invalid Input!");
        }
    }

    static checkCheckbox() {

        // the event listener that will get the elements then change them depending on the checkbox
        const unlock = document.getElementById("existingCommunity").checked;
        const chooseCommunityDiv = document.getElementById("chooseCommunityDiv");
        const createCommunityDiv = document.getElementById("createCommunityDiv");
        const numCreditsDiv = document.getElementById("numCreditsDiv");
        const numGroupsDiv = document.getElementById("numGroupsDiv");
        const generateButtonDiv = document.getElementById("generateButtonDiv");
        const displayCreditsDiv = document.getElementById("displayCreditsDiv");
        const searchCommunityDiv = document.getElementById("searchCommunityDiv");
        const chooseCommunitySearchedDiv = document.getElementById("chooseCommunitySearchedDiv");
        // adds an event listener to the unlock checkbox for the "change" event.

        if (unlock === true) {
            // When the checkbox is checked this should run
            chooseCommunityDiv.style.display = "block";
            numCreditsDiv.style.display = "block";
            numGroupsDiv.style.display = "block";
            generateButtonDiv.style.display = "block";
            displayCreditsDiv.style.display = "block";
            createCommunityDiv.style.display = "none"; //makes this not visible
        }
        else {
            // When the checkbox is not checked
            chooseCommunityDiv.style.display = "none";
            numGroupsDiv.style.display = "none";
            numCreditsDiv.style.display = "none";
            generateButtonDiv.style.display = "none";
            displayCreditsDiv.style.display = "none";
            searchCommunityDiv.style.display = "none";
            chooseCommunitySearchedDiv.style.display = "none";
            createCommunityDiv.style.display = "block"; //makes this visible
        }

    }

    //Used to calculate and update the display of the number of credits being generated
    static totalCredits () {

        let numCredits = document.getElementById("numCredits").value;
        let numGroups = document.getElementById("numGroups").value;

        if (numCredits === null) {
            numCredits = 0
        }
        if (numGroups === null) {
            numGroups = 0
        }

        document.getElementById("creditTotal").innerHTML = numCredits * numGroups;
        // console.log(creditTotal)
    }

    static showSearchBar () { // function used to hide and show the search function
        // console.log("Here");
        const selected = document.getElementById("chooseCommunity").value;
        const searchCommunityDiv = document.getElementById("searchCommunityDiv");
        const chooseCommunitySearchedDiv = document.getElementById("chooseCommunitySearchedDiv");
        // console.log(selected);

        if (selected === "Other") { // Shows the search bar if they choose the "other" option
            searchCommunityDiv.style.display = "block";
            chooseCommunitySearchedDiv.style.display = "block";
        }
        else { // Hides the search bar if a community has been chosen
            searchCommunityDiv.style.display = "none";
            chooseCommunitySearchedDiv.style.display = "none";
        }

    }

    static search () { // function to search the database for communities

        // removes the old search results
        // Learnt via https://bobbyhadz.com/blog/javascript-remove-all-elements-with-class#:~:text=Use%20the%20document.querySelectorAll%20%28%29%20method%20to%20select%20the,each%20element%20to%20remove%20it%20from%20the%20DOM.
        // 07/12/23
        const temp = document.querySelectorAll(".temporary");
        temp.forEach(temp => {
            temp.remove();
        });

        // console.log("here");
        const searchTerm = document.getElementById("searchBar").value;
        const chooseCommunitySearchedDiv = document.getElementById("chooseCommunitySearchedDiv");
        // console.log(searchTerm)
        const data = {searchTerm}; // creates an object for the searchterm

        const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
        xhttp.open("POST", "/search", true); //set method and the url and if it asynchornus
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhttp.send(JSON.stringify(data));

        xhttp.onreadystatechange = function () {
            if (this.readyState === 4) { // checks its ready
                if (this.status === 200) { //200 = server is okay
                    const response = JSON.parse(this.responseText); // passing back the server response
                    console.log(response.result);
                    console.log(response);

                    for (let i = 0; i < response.length; i++) {
                        document.getElementById("chooseCommunitySearched").innerHTML += `<option value="${response[i]}" class=temporary> ${response[i]} </option>`;
                    }

                    chooseCommunitySearchedDiv.style.display = "block";
                }
            }
        };
    }

    static generateCredits () { //submit form that will get the data from the form elements

        const numCredits = Number(document.getElementById("numCredits").value);
        const numGroups = Number(document.getElementById("numGroups").value);
        const chosenCommunity = document.getElementById("chooseCommunity").value;
        const chosenCommunitySearched = document.getElementById("chooseCommunitySearched").value;

        console.log(numCredits)
        console.log(numGroups)
        console.log(Number.isInteger(numCredits))
        console.log(chosenCommunitySearched)

        if (chosenCommunitySearched.length === 0) {
            if (chosenCommunity === "Other") {
                document.getElementById("formAlerts").innerHTML = Alerts.warningAlert("Please Choose A Community!", "Invalid Input!");
            }

            else {
                if (!(Number.isInteger(numCredits)) || (numCredits === 0)) {
                    CreditGeneration.checkValid()
                    console.log("First Invalid")
                }
                else if (!(Number.isInteger(numGroups)) || (numCredits === 0)) {
                    CreditGeneration.checkValid()
                    console.log("Second Invalid")
                }
                else {
                    const totalNumCredits = numGroups * numCredits;
                    const data = {
                        chosenCommunity: chosenCommunity,
                        numGroups: numGroups,
                        numCredits: numCredits,
                        totalNumCredits: totalNumCredits,
                    }
                    console.log(data)

                    const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
                    xhttp.open("POST", "/create", false); //set method and the url and if it asynchornus
                    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                    xhttp.send(JSON.stringify(data));

                    xhttp.onreadystatechange = function () {
                        if (this.readyState === 4) { // checks its ready
                            if (this.status === 200) { //200 = server is okay
                                const response = JSON.parse(this.responseText); // passing back the server response
                                console.log(response.result);
                            }
                        }
                    };
                }
            }
        }

        else {
            if (!(Number.isInteger(numCredits)) || (numCredits === 0)) {
                CreditGeneration.checkValid()
                console.log("First Invalid")
            }
            else if (!(Number.isInteger(numGroups)) || (numCredits === 0)) {
                CreditGeneration.checkValid()
                console.log("Second Invalid")
            }
            else {
                const totalNumCredits = numGroups * numCredits;
                const data = {
                    chosenCommunity: chosenCommunitySearched,
                    numGroups: numGroups,
                    numCredits: numCredits,
                    totalNumCredits: totalNumCredits,
                }
                console.log(data)

                const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
                xhttp.open("POST", "/create", false); //set method and the url and if it asynchornus
                xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
                xhttp.send(JSON.stringify(data));

                xhttp.onreadystatechange = function () {
                    if (this.readyState === 4) { // checks its ready
                        if (this.status === 200) { //200 = server is okay
                            const response = JSON.parse(this.responseText); // passing back the server response
                            console.log(response.result);
                        }
                    }
                };
            }
        }
    }
}