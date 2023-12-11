class AccountReview {
    static async renderTable() {
        const response = await fetch("/api/account/listNotApproved", {
            method: "GET"
        })

        if (response.ok) {
            let renderData = "";
            const data = await response.json();

            // Clear the table
            document.getElementById("accountTable").innerHTML = "";

            // Maps the data needed from the database so that it can be pasted into the table body
            data.map(function (account) {
                document.getElementById("accountTable").innerHTML += `
                <tr>
                    <td>${account.name}</td>
                    <td>${account.created}</td>
                    <td id="tableButton${account.userID}"><button class="btn btn-pastel btn-lg" onclick="accountReview.renderDetails(${account.userID})">Select</button></td>
                </tr>
                `;
            })
        }
    }


    static async renderDetails(userID) {
        const url = new URL("/api/account/listNotApproved/selected", window.location.origin);
        url.searchParams.append("userID", JSON.stringify(userID)); //Learnt from "https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams"

        const response = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            }
        });

        if (response.ok) {
            const data = await response.json();
            // Clear the table
            document.getElementById("accountModal").innerHTML = "";

            // Clear the modal footer
            document.getElementById("accountDecisionModal").innerHTML = "";

            // Maps the data needed from the database so that it can be pasted into the modal body and buttons for modal footer
            data.map(function (account, userID) {
                document.getElementById("accountModal").innerHTML += `
                    <h4>Name: ${account.name}</h4>
                    <h6>User Name: ${account.userName}</h6>
                    <h6>User Email: ${account.userEmail}</h6>
                    <h6>Is this user a mentor?: ${account.isMentor}</h6>
                    <p>Profile Picture: <img src="/static/uploads/${account.ProfilePictureID}.jpeg" alt="Profile Picture" class="profilePicture"></p>
                    <p>Profile Banner: <img src="/static/uploads/${account.BackgroundID}.jpeg" alt="Profile Background" class="profileBanner"></p>
                `;

                document.getElementById("communityDecisionModal").innerHTML += `
                <button type="button" class="btn btn-pastel btn-lg" data-bs-dismiss="modal" onClick="AccountReview.reviewDecision(${account.userID}, 1)">Accept</button>
                <button type="button" class="btn btn-pastel btn-lg" data-bs-dismiss="modal" onClick="AccountReview.reviewDecision(${account.userID}, 0)">Reject</button>
                `;
            })

            // Display modal
            // Learnt from "https://getbootstrap.com/docs/5.2/components/modal/"
            const reviewModal = new bootstrap.Modal(document.getElementById("reviewModal"));
            reviewModal.show();
        }
    }


    static async reviewDecision(userID, decision){
        // Appends the UserID and moderator decision into JSON format
        let decisionData = {
            entityID: userID,
            decision: decision
        }
        // Passes the data into the backend so that the decision can be processed and the correct result returned to the user
        const response = await fetch("/api/account/listNotApproved/selected/decision", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            },
            body: JSON.stringify(decisionData)
        })
        // Once the backend data-handling has been done, the table is reloaded, so it can show the most updated state of the database
        if (response.ok) {
            AccountReview.renderTable()
        }
    }
}
