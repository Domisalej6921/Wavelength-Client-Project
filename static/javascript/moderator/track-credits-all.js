
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

    static async getReceiverName(receiverId, isEntity) {

        return new Promise((resolve, reject) => {

            const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
            xhttp.open("POST", "/getReceiverName", true); //set method and the url and if it asynchornus
            xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xhttp.send(JSON.stringify({
                "receiverId": receiverId, "isEntity": isEntity
            }));

            xhttp.onreadystatechange = function () {
                if (this.readyState === 4){
                    if (this.status === 200) { //200 = server is okay
                        const response = JSON.parse(this.responseText); // passing back the server response
                        console.log(response)
                        resolve(response);
                    }
                    else {
                        console.log("HTTP status: " + this.status);
                        reject("Failed to fetch Receivers Name");
                    }
                }
            };
        });
    }

    static async getSenderName(senderId, isEntity) {

        return new Promise((resolve, reject) => {

            const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
            xhttp.open("POST", "/getSenderName", true); //set method and the url and if it asynchornus
            xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
            xhttp.send(JSON.stringify({
                "senderId": senderId, "isEntity": isEntity
            }));

            xhttp.onreadystatechange = function () {
                if (this.readyState === 4) {
                    if (this.status === 200) { //200 = server is okay
                        const response = JSON.parse(this.responseText); // passing back the server response
                        console.log(response)
                        resolve(response);
                    }
                    else {
                        console.log("HTTP status: " + this.status);
                        reject("Failed to fetch Senders Name");
                    }
                }
            };
        });
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

        xhttp.onreadystatechange = async function () {
            if (this.readyState === 4) { // checks its ready
                if (this.status === 200) { //200 = server is okay
                    const response = JSON.parse(this.responseText); // passing back the server response
                    console.log(response);

                    for (let i = 0; i < response.length; i++) {
                        // console.log(i)

                        const receiver = await CreditTracking.getReceiverName(response[i][4], response[i][5])
                        console.log(receiver)
                        const sender = await CreditTracking.getSenderName(response[i][2], response[i][3])
                        console.log(sender)

                        document.getElementById("displayTransactionsTable").innerHTML +=
                            `<tr value="${response[i]}" class="temporary">
                            <td>${i+1}</td>
                            <td>${response[i][0]}</td>
                            <td>${response[i][2]}</td>
                            <td>${sender}</td>
                            <td>${response[i][4]}</td>
                            <td>${receiver}</td>
                            <td>${response[i][7]}</td>
                            <td>${response[i][6]}</td>
                            </tr>`;

                        document.getElementById("creditTotalUses").innerHTML = i+1;
                    }
                }
            }
        };

    }

}

