
class CreditTracking {
    //set up the class for the js to be called from

    static onLoadFunctions() {
        CreditTracking.getCredits();
    }

    //Function that calls the database to get all credits
    static getCredits() {

        const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
        xhttp.open("GET", "/getCredits", true); //set method and the url and if it asynchornus
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

        xhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) { //200 = server is okay
                const response = JSON.parse(this.responseText); // passing back the server response
                console.log(response)
                for (let i = 0; i < response.length; i++) {
                    document.getElementById("chooseCredit").innerHTML += `<option value="${response[i]}"> ${response[i]} </option>`;
                }
            }
        };
        xhttp.send();
    }

    static getChosenCreditTransaction() {
        console.log("Running")
        const chosenCredit = document.getElementById("chooseCredit").value;

        const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
        xhttp.open("POST", "/getChosenCreditTransactions", true); //set method and the url and if it asynchornus
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
        xhttp.send(JSON.stringify(chosenCredit));

        xhttp.onreadystatechange = function () {
            if (this.readyState === 4) { // checks its ready
                if (this.status === 200) { //200 = server is okay
                    const response = JSON.parse(this.responseText); // passing back the server response
                    console.log(response);

                    for (let i = 0; i < response.length; i++) {
                    document.getElementById("displayTransactionsDiv").innerHTML += `<p value="${response[i]}"> Transaction ${i} ${response[i]} </p>`;
                }
                }
            }
        };

    }

}

