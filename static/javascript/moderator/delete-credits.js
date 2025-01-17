

class CreditDeletion {
    //set up the class for the js to be called from

    static onLoadFunctions() {
        CreditDeletion.getInactiveCredits();
    }

    // function that generates the graph of all the inactive credits
    static createGraph(allInactiveCredits) {
        if (!Array.isArray(allInactiveCredits)) {
            console.error("Invalid response for inactive credits");
            return;
        }

        // console.log(allInactiveCredits)
        const lastUsedOptions = {"1Y+": 31104000, "11M+": 28512000, "10M+": 25920000, "9M+": 23328000, "8M+": 20736000, "7M+": 18144000, "6M+": 15552000, "5M+": 12960000, "4M+": 10368000, "90+": 7776000, "60+": 5184000, "30+": 2592000}
        const currentTime = new Date().getTime() / 1000;
        const lastUsed = [];

        for (const credit of allInactiveCredits) {
            // console.log(credit[1])
            // console.log(Object.keys(lastUsedOptions))
            const option = Object.keys(lastUsedOptions).find(
                option => credit[1] < currentTime - lastUsedOptions[option]
            );
            // console.log(credit[1] - lastUsedOptions[option] < currentTime - lastUsedOptions[option])
            // console.log(option)
            if (option) {
                lastUsed.push(option);
            }
        }

        if (lastUsed.length === 0) {
            console.log("Passed token recently used");
        } else {
            // console.log(lastUsed);
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
        // console.log(optionCreditsCounts)
        // console.log(Object.values(optionCreditsCounts))
        // console.log(Object.keys(optionCreditsCounts))

        document.getElementById("creditGraphDiv").innerHTML += '<canvas id="inactiveCreditChart" style="width:100%;max-width:700px"></canvas>';
        const canvas = document.getElementById("inactiveCreditChart");
        // console.log("Canvas element:", canvas);

        // checking if the canvas element exists
        if (!canvas) {
            console.error("Canvas element not found.");
            return;
        }

        // setting up the chart configuration
        const chartConfig = {
            type: "line",
            data: {
                labels: Object.keys(optionCreditsCounts),
                datasets: [{
                    label: "Credits Last Use:",
                    data: Object.values(optionCreditsCounts),
                    fill: false,
                    backgroundColor: "#C0B3DA",
                    borderColor: "#B095D7",
                    tension: 0.1
                }]
            }
        };

        new Chart(canvas, chartConfig);
        // console.log("chart created successfully");

    }

    //Function that calls the database to get all credits that haven't been used in over 1 month(30 days) or more
    static getInactiveCredits() {

        const xhttp = new XMLHttpRequest();
        xhttp.open("POST", "/getInactiveCredits", false);
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");


        xhttp.onreadystatechange = function () {
            if (this.readyState === 4) {
                if (this.status === 200) {
                    const response = JSON.parse(this.responseText); // passing back the server response
                    // console.log(response);
                    CreditDeletion.createGraph(response)
                } else {
                    console.log("HTTP status: " + this.status);
                }
            }
        };

        xhttp.send();
    }

    //Function which sorts the inactive credits by the time the mod wants
    static getChosenInactiveCredits() {
        return new Promise((resolve, reject) => {
            const creditAge = document.getElementById("chooseAge").value;
            const creditAgeOptions = {"1 Year or more!": 31104000, "11 Months": 28512000, "10 Months": 25920000, "9 Months": 23328000, "8 Months": 20736000, "7 Months": 18144000, "6 Months": 15552000, "5 Months": 12960000, "4 Months": 10368000, "90 Days": 7776000, "60 Days": 5184000, "30 Days": 2592000};
            const creditAgeValue = creditAgeOptions[creditAge];

            const xhttp = new XMLHttpRequest();
            xhttp.open("POST", "/getChosenInactiveCredits", true);
            xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

            xhttp.onreadystatechange = function () {
                if (this.readyState === 4) {
                    if (this.status === 200) {
                        const response = JSON.parse(this.responseText);
                        console.log(response);
                        document.getElementById("creditTotal").innerHTML = response.length;
                        resolve(response); // Resolve the promise with the server response
                    } else {
                        console.log("HTTP status: " + this.status);
                        reject("Failed to fetch chosen inactive credits");
                    }
                }
            };

            xhttp.send(JSON.stringify(creditAgeValue));
        });
    }

    // Function to delete the credits
    static deleteCredits() {
        CreditDeletion.getChosenInactiveCredits()
            .then(tokensToDelete => {
                console.log(tokensToDelete);
                const tokensToDeleteIds = tokensToDelete.map(tokens => tokens[0]);

                const xhttp = new XMLHttpRequest();
                xhttp.open("POST", "/deleteInactiveCredits", true);
                xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

                xhttp.onreadystatechange = function () {
                    if (this.readyState === 4 && this.status === 200) {
                        const response = JSON.parse(this.responseText);
                        console.log(response);
                    }
                };

                xhttp.send(JSON.stringify(tokensToDeleteIds));
            })
            .catch(error => {
                console.error(error);
            });
    }

}

