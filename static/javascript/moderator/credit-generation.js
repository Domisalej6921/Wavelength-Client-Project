class CreditGeneration {
    static submitForm() {

        document.addEventListener(type: "DOMContentLoaded", listener:function() {
            var unlock = document.getElementById(elementId: "existingCommunity");
            var chooseCommunityDiv = document.getElementById(elementId:"chooseCommunityDiv");
            var createCommunityDiv = document.getElementById(elementId:"createCommunityDiv");

            unlock.addEventListener(type:"change", listener:function() {
                if (unlock.checked) {
                    chooseCommunityDiv.style.display = "block";
                    createCommunityDiv.style.display = "None";

                } else {
                    chooseCommunityDiv.style.display = "None";
                    createCommunityDiv.style.display = "block";
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
