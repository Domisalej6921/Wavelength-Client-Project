class CreditDeletion {
    //set up the class for the js to be called from

    static onLoadFunctions() { //Function that calls the functions to run when the page loads
        CreditDeletion.getInactiveCredits()
        CreditDeletion.totalCredits()
    }

    //Function that calls the database to get all credits that haven't been used in over 1 month or more
    static getInactiveCredits() {

        const xhttp = new XMLHttpRequest(); // creates new XMLHttp request
            xhttp.open("POST", "/getInactiveCredits", true); //set method and the url and if it asynchornus
            xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");

            xhttp.onreadystatechange = function () {
                if (this.readyState === 4 && this.status === 200) { //200 = server is okay
                    const response = JSON.parse(this.responseText); // passing back the server response
                    console.log(response.result);
                }
            };

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