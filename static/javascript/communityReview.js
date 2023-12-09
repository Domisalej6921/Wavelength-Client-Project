class CommunityReview {
    static async renderTable() {
        const response = await fetch("/api/community/listNotApproved", {
            method: "GET"
        })

        if (response.ok) {
            let renderData = "";
            const data = await response.json();

            // Clear the table
            document.getElementById("communityTable").innerHTML = "";

            // Maps the data needed from the database so that it can be pasted into the table body
            data.map(function (entity) {
                document.getElementById("communityTable").innerHTML += `
                <tr>
                    <td>${entity.name}</td>
                    <td>${entity.created}</td>
                    <td id="tableButton${entity.entityID}"><button class="btn btn-pastel btn-lg" onclick="CommunityReview.renderDetails(${entity.entityID})">Select</button></td>
                </tr>
                `;
            })
        }
    }


    static async renderDetails(entityID) {
        const url = new URL("/api/community/listNotApproved/selected", window.location.origin);
        url.searchParams.append("entityID", JSON.stringify(entityID)); //Learnt from "https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams"

        const response = await fetch(url, {
            method: "GET",
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            }
        });

        if (response.ok) {
            const data = await response.json();
            // Clear the table
            document.getElementById("communityModal").innerHTML = "";

            // Clear the modal footer
            document.getElementById("communityDecisionModal").innerHTML = "";

            // Maps the data needed from the database so that it can be pasted into the modal body and buttons for modal footer
            data.map(function (entity, entityID) {
                document.getElementById("communityModal").innerHTML += `
                    <h3>Name: ${entity.name}</h3>
                    <h5>Description: ${entity.description}</h5>
                    <p>Profile Picture: <img src="/static/uploads/${entity.profilePicture}.jpeg" alt="Profile Picture" class="profilePicture"></p>
                    <p>Profile Banner: <img src="/static/uploads/${entity.profileBanner}.jpeg" alt="Profile Banner" class="profileBanner"></p>
                    <h6>Is this a Company?: ${entity.isCompany}</h6>
                `;

                document.getElementById("communityDecisionModal").innerHTML += `
                <button type="button" class="btn btn-pastel btn-lg" data-bs-dismiss="modal" onClick="CommunityReview.reviewDecision(${entity.entityID}, 1)">Accept</button>
                <button type="button" class="btn btn-pastel btn-lg" data-bs-dismiss="modal" onClick="CommunityReview.reviewDecision(${entity.entityID}, 0)">Reject</button>
                `;
            })

            // Display modal
            // Learnt from "https://getbootstrap.com/docs/5.2/components/modal/"
            const reviewModal = new bootstrap.Modal(document.getElementById("reviewModal"));
            reviewModal.show();
        }
    }


    static async reviewDecision(entityID, decision){
        // Appends the EntityID and moderator decision into JSON format
        let decisionData = {
            entityID: entityID,
            decision: decision
        }
        // Passes the data into the backend so that the decision can be processed and the correct result returned to the user
        const response = await fetch("/api/community/listNotApproved/selected/decision", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            },
            body: JSON.stringify(decisionData)
        })
        // Once the backend data-handling has been done, the table is reloaded, so it can show the most updated state of the database
        if (response.ok) {
            CommunityReview.renderTable()
        }
    }
}