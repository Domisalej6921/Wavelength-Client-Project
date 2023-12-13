class ManageTags {
    static renderEditForm() {
        document.getElementById("modals").innerHTML += `<div class="modal fade" id="editTagsFormModal">
            <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">

                    <div class="modal-header" id="editTagsFormModalHeader">
                        ${Modals.header("Edit your account tags")}
                    </div>

                    <div class="modal-body" id="editTagsFormModalBody">
                        ${Modals.editTags()}
                    </div>

                    <div class="modal-footer"></div>
                </div>
            </div>
        </div>`;
    }

    static async searchTags() {
        // Get the data from the search box
        try {
            const search = document.getElementById("editTagsFormModalSearch").value.toString();
        }
        catch {
            const search = "";
        }

        // Send the form data to the server using the fetch API
        const response = await fetch('/api/tags/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({search: search})
        })

        // If the server returns a 200 status code (OK)
        if (response.ok) {
            // Get the response's data
            const data = await response.json();

            // If there are no tags, display an alert and replace the form with items to create a new tag
            if (data.length === 0) {
                // Then replace the form with items to create a new tag
                document.getElementById("editTagsModalForm").innerHTML = Modals.createTag();

                // Display an alert
                document.getElementById("createTagFormModalAlerts").innerHTML = Alerts.warningAlert('No tags found. Please create a new tag.', 'No Tags Found!');

                return
            }

            // Add the default option to the select element
            document.getElementById("editTagsFormModalTags").innerHTML = `<option selected>Select a Tag</option>`;

            // Loop through the tags and add them to the select element
            for (let i = 0; i < data.length; i++) {
                document.getElementById("editTagsFormModalTags").innerHTML += `<option value="${data[i].tagID}">${data[i].name}</option>`;
            }
        }
        // If the response is due to an unauthorised request, redirect to the login page
        else if (response.status === 401) {
            window.location.href = '/login';
        }
        // If it is any other status code, display an error alert
        else {
            document.getElementById("editTagsFormModalAlerts").innerHTML = Alerts.errorAlert('Failed to load tags. Please try again later...', 'System Error!');
        }
    }

    static async createTagFormSubmit() {

    }

    static async assignTagFormSubmit() {

    }
}