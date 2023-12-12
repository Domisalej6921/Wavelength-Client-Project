
class CreditTracking {
    //set up the class for the js to be called from

    static onLoadFunctions() {
        CreditTracking.getCredits();
    }

    //Function that calls the database to get all credits that haven't been used in over 1 month(30 days) or more
    static getCredits() {

        const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
        xhttp.open("GET", "/getCredits", true); //set method and the url and if it asynchornus
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

        xhttp.onreadystatechange = function () {
            if (this.readyState === 4 && this.status === 200) { //200 = server is okay
                const response = JSON.parse(this.responseText); // passing back the server response
                console.log(response)
            }
        };
        xhttp.send()
    }

    //Function which sorts the inactive credits by the time the mod wants
    static getChosenCredit() {

        const xhttp = new XMLHttpRequest();
        xhttp.open("POST", "/getChosenCredit", false);
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");


        xhttp.onreadystatechange = function () {
            if (this.readyState === 4) {
                if (this.status === 200) {
                    const response = JSON.parse(this.responseText); // passing back the server response
                    console.log(response);
                } else {
                    console.log("HTTP status: " + this.status);
                }
            }
        };

        xhttp.send();
    }

    static getChosenCreditTransaction() {

        const xhttp = new XMLHttpRequest();
        xhttp.open("POST", "/getChosenCreditTransactions", false);
        xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");


        xhttp.onreadystatechange = function () {
            if (this.readyState === 4) {
                if (this.status === 200) {
                    const response = JSON.parse(this.responseText); // passing back the server response
                    console.log(response);
                } else {
                    console.log("HTTP status: " + this.status);
                }
            }
        };

        xhttp.send();
    }

}

