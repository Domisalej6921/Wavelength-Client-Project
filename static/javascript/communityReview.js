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

        // Retrieves reviewal data when the response from the server is successful
        if (response.ok) {
            const data = await response.json();

            // Clear the table
            document.getElementById("communityModal").innerHTML = "";

            // Maps the data needed from the database so that it can be pasted into the modal body
            data.map(function (entity) {
                document.getElementById("communityModal").innerHTML += `
                    <h3>Name: ${entity.name}</h3>
                    <h5>Description: ${entity.description}</h5>
                    <p>Profile Picture: <img src="/static/uploads/${entity.profilePicture}.jpeg" alt="Profile Picture" style="max-width: 100%; max-height: 200px; border-radius: 45%;"></p>
                    <p>Profile Banner: <img src="/static/uploads/${entity.Background}.jpeg" alt="Profile Banner" style="max-width: 100%; max-height: 200px;"></p>
                    <h5>Is this a Company?: ${entity.isCompany}</h5>
                `;
            });

            // Display modal
            // Learnt from "https://getbootstrap.com/docs/5.2/components/modal/"
            const reviewModal = new bootstrap.Modal(document.getElementById("reviewModal"));
            reviewModal.show();
        }
    }
}