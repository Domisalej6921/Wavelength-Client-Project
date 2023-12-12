
class CreditTracking {
    //set up the class for the js to be called from

    static onLoadFunctions() {
        CreditTracking.getCredits();
    }

    //Function that calls the database to get all credits that haven't been used in over 1 month(30 days) or more
    static getCredits() {

        const xhttp = new XMLHttpRequest();
        xhttp.open("POST", "/getCredits", false);
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

    //Function which sorts the inactive credits by the time the mod wants
    static getChosenCreditTransactions() {
        
        const xhttp = new XMLHttpRequest();
        xhttp.open("POST", "/getCredits", false);
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

