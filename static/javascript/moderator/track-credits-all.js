
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

        // removes the old search results
        // Learnt via https://bobbyhadz.com/blog/javascript-remove-all-elements-with-class#:~:text=Use%20the%20document.querySelectorAll%20%28%29%20method%20to%20select%20the,each%20element%20to%20remove%20it%20from%20the%20DOM.
        // 07/12/23
        const temp = document.querySelectorAll(".temporary");
        temp.forEach(temp => {
            temp.remove();
        });

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
                        console.log(i)
                        if (i === 0) {
                            document.getElementById("displayTransactionsDiv").innerHTML +=
                                `<p value="${response[i]}" class="temporary"> Transaction ${i+1}: Transaction Id: ${response[i][0]} Reciever Id: ${response[i][1]} Was Transfered: ${response[i][3]}</p>`;
                        }
                        else {
                            document.getElementById("displayTransactionsDiv").innerHTML +=
                                `<p value="${response[i]}" class="temporary"> Transaction ${i+1}: Transaction Id: ${response[i][0]} Sender Id:${response[i][1]} Reciever Id: ${response[i][3]} Was Transfered: ${response[i][5]}</p>`;
                        }
                        document.getElementById("creditTotalUses").innerHTML = i+1;
                    }
                }
            }
        };

    }

}

