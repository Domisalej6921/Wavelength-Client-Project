class MentorTokenDonation {
    static async renderTable() {
        const response = await fetch("/api/community/approved/donate", {
            method: "GET"
        })

        if (response.ok) {
            let renderData = "";
            const data = await response.json();
            // Clear the table
            document.getElementById("mentorDonateTable").innerHTML = "";

            // Maps the data needed from the database so that it can be pasted into the table body
            data.map(function (community) {
                document.getElementById("mentorDonateTable").innerHTML += `
                <tr>
                    <td>${community.name}</td>
                    <td>${community.description}</td>
                    <td>${community.created}</td>
                    <td id="tableButton${community.entityID}"><button class="btn btn-pastel btn-lg" onclick="MentorTokenDonation.renderDetails(${community.entityID})">Select</button></td>
                </tr>
                `;
            })
        }
    }


    static async renderDetails(entityID) {
        const url = new URL("/api/community/approved/donate/selected", window.location.origin);
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
            document.getElementById("CommunityDataModal").innerHTML = "";

            // Clear the modal footer
            document.getElementById("tokenDonationModal").innerHTML = "";

            // Maps the data needed from the database so that it can be pasted into the modal body and buttons for modal footer
            data.map(function (community, entityID) {
                document.getElementById("CommunityDataModal").innerHTML += `
                    <h3>Name: ${community.name}</h3>
                    <h5>Description: ${community.description}</h5>
                    <p>Profile Picture: <img src="/static/uploads/${community.profilePicture}.jpeg" alt="Profile Picture" class="profilePicture"></p>
                    <p>Profile Banner: <img src="/static/uploads/${community.profileBanner}.jpeg" alt="Profile Banner" class="profileBanner"></p>
                    <h6>Is this a Company?: ${community.isCompany}</h6>
                `;

                document.getElementById("tokenDonationModal").innerHTML += `
                <label for="amount" ><h7>Enter Amount:</h7></label>
                <input type="number" id="amount">
                <script>
                
                </script>
                <button type="button" class="btn btn-pastel btn-lg" data-bs-dismiss="modal" onClick="MentorTokenDonation.donateAmount(${community.entityID}, amount.value)">Donate</button>
                `;
            })

            // Display modal
            // Learnt from "https://getbootstrap.com/docs/5.2/components/modal/"
            const mentorDonateModal = new bootstrap.Modal(document.getElementById("mentorDonateModal"));
            mentorDonateModal.show();
        }
    }


    static async donateAmount(entityID, amount){
        console.log(entityID, amount)
        // Appends the UserID and moderator decision into JSON format
        let donateData = {
            community: entityID,
            amount: amount
        }
        // Passes the data into the backend so that the decision can be processed and the correct result returned to the user
        const response = await fetch("/api/community/approved/donate/selected/action", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            },
            body: JSON.stringify(donateData)
        })
        // Once the backend data-handling has been done, the table is reloaded, so it can show the most updated state of the database
        if (response.ok) {
            MentorTokenDonation.renderTable()
        }
    }
}