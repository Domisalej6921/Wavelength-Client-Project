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

            data.map(function(entity) {
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

    static async renderDetails(entityID){}
}