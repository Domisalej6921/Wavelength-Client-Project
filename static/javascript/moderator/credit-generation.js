class CreditGeneration {
    static submitForm() {

        document.addEventListener(type: "DOMContentLoaded", listener:function() {
            var unlock = document.getElementById(elementId: "existingCommunity");
            var optionsDiv = document.getElementById(elementId:"optionsDiv");

            unlock.addEventListener(type:"change", listener:function() {
                if (unlock.checked) {
                    optionsDiv.style.display = "block";
                } else {
                    optionsDiv.style.display = "None";
                }
            })
        })

        const data = {
            username: document.getElementById("numCredits").value,
            name: document.getElementById("numGroups").value,
            email: document.getElementById("chooseCommunity").value,
        }


    }
}
