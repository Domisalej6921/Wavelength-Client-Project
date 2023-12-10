class CreditDeletion {
    //set up the class for the js to be called from

    static onLoadFunctions() { //Function that calls the functions to run when the page loads
        CreditDeletion.createGraph()
        CreditDeletion.totalCredits()
    }

    // function that generates the graph of all the inactive credits
    static createGraph() {
        const allInactiveCredits = CreditDeletion.getInactiveCredits()
        console.log(allInactiveCredits)
        const lastUsedOptions = {"30+":2592000,"60+":5184000,"90+":7776000,"4M+":10368000,"5M+":12960000,"6M+":15552000,"7M+":18144000,"8M+":20736000,"9M+":23328000,"10M+":25920000,"11M+":28512000,"1Y+":31104000}
        const currentTime = ((new Date().getTime()) / 1000)
        const lastUsed = [];
        let option;

        for (const credit of allInactiveCredits) {
            if (credit && credit.length > 1) {
                option = Object.keys(lastUsedOptions).find(
                    option => (credit[1] - lastUsedOptions[option]) < (currentTime - lastUsedOptions[option])
                );
                if (option) {
                    lastUsed.push(option);
                    break;
                }
            }
        }

        if (lastUsed.length === 0) {
            console.log("Passed token recently used");
        } else {
            console.log(lastUsed);
        }

        // Count occurrences of each option
        // Learnt From:
        // https://stackoverflow.com/questions/6120931/how-to-count-certain-elements-in-array#:~:text=I%20would%20consider%20this%20an%20optimal%202017%20solution%3A,instances%20of%20crazyValue%20in%20the%20array%20of%20objects.
        // 10/12/2023
        const optionCreditsCounts = lastUsed.reduce((acc, option) => {
            acc[option] = (acc[option] || 0) + 1;
            // initializes as 0 if not already an option.
            // if it is an option just adds 1
            return acc;
        }, {});

        new Chart("inactiveCreditChart", {
          type: "line",
          data: {
            labels: lastUsed,
              datasets: [{
                backgroundColor:"#C0B3DA",
                borderColor: "#FFFFFF",
                data: optionCreditsCounts,
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
            if (this.readyState === 4) {
                if (this.status === 200) {
                    try {
                        const response = JSON.parse(this.responseText);
                        const allInactiveCredits = response.result;

                        // Ensure the response is an array before resolving
                        if (Array.isArray(allInactiveCredits)) {
                            resolve(allInactiveCredits);
                        } else {
                            reject("Invalid response format");
                        }
                    } catch (error) {
                        reject("Error parsing response JSON");
                    }
                } else {
                    reject("HTTP status: " + this.status);
                }
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