class CreditDeletion {
    //set up the class for the js to be called from

    static onLoadFunctions() { //Function that calls the functions to run when the page loads
        CreditDeletion.createGraph()
        CreditDeletion.totalCredits()
    }

    static createGraph() {
        const allInactiveCredits = CreditDeletion.getInactiveCredits()
        const lastUsedOptions = {"30+":2592000,"60+":5184000,"90+":7776000,"4M+":10368000,"5M+":12960000,"6M+":15552000,"7M+":18144000,"8M+":20736000,"9M+":23328000,"10M+":25920000,"11M+":28512000,"1Y+":31104000}

        for (let j = 0; j < lastUsedOptions.length; j++){
            for (let i = 0; i < allInactiveCredits.length; i++) {
                while (allInactiveCredits[i][1] < lastUsedOptions[j])
                allInactiveCredits[i][1]
            }
        }

        const lastUsed = ["January","Febuary","March", "April", "May", "June", "July","August","September","October","November","December"];
        const numCredits = [1, 13, 3, 5, 5, 23, 11, 2, 9, 10, 2, 1];

        new Chart("inactiveCreditChart", {
          type: "line",
          data: {
            labels: lastUsed,
              datasets: [{
                backgroundColor:"#c0b3da",
                borderColor: "#FFFFFF",
                data: numCredits
            }]
          },
          options: {
            legend: {display: false},
            title: {
              display: true,
              text: "Credits Last Use:"
            }
          }
        });
        document.getElementById("creditGraphDiv").innerHTML += '<canvas id="inactiveCreditChart" style="width:100%;max-width:700px"></canvas>';

    }

    //Function that calls the database to get all credits that haven't been used in over 1 month(30 days) or more
    static getInactiveCredits() {

        const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
        xhttp.open("POST", "/getInactiveCredits", true); //set method and the url and if it asynchornus
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

        xhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) { // 200 = server is okay
                const response = JSON.parse(this.responseText); // passing back the server response
                console.log(response.result);
            }
        };
        xhttp.send();
    }

    static totalCredits () { //Function to count the total credits being deleted

    }

    //Function which sorts the inactive credits by the time the mod wants
    static sortInactiveCredits() {

        CreditDeletion.totalCredits()
    }

    static getSelectedInactiveCredits() {

        const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
            xhttp.open("POST", "/getSelectedInactiveCredits", true); //set method and the url and if it asynchornus
            xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

            xhttp.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200) { //200 = server is okay
                    const response = JSON.parse(this.responseText); // passing back the server response
                    console.log(response.result);
                }
            };
    }

    //Function to delete the credits
    static deleteCredits() {

        let tokensToDelete = CreditDeletion.getSelectedInactiveCredits()

        const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
            xhttp.open("POST", "/deleteInactiveCredits", true); //set method and the url and if it asynchornus
            xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xhttp.send(JSON.stringify(tokensToDelete));

            xhttp.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200) { //200 = server is okay
                    const response = JSON.parse(this.responseText); // passing back the server response
                    console.log(response.result);
                }
            };

    }
}