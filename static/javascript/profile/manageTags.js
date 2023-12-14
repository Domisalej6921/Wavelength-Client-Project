class ManageTags {
    static renderEditForm() {
        const content = `<div class="modal fade" id="editTagsFormModal">
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

        if (document.getElementById("modals") !== null) {
            document.getElementById("modals").innerHTML += content
        }
        else {
            document.getElementById("modals").innerHTML = content
        }
    }

    static async searchTags() {
        // Get the data from the search box
        let search;
        try {
            search = document.getElementById("editTagsFormModalSearch").value;

            if (search === null) {
                search = "";
            }
        }
        catch {
            search = "";
        }

        // Send the form data to the server using the fetch API
        const response = await fetch('/api/tags-search', {
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

            // Clear the select element
            document.getElementById("editTagsFormModalSelect").innerHTML = "";

            // Loop through the tags and add them to the select element
            for (let i = 0; i < data.length; i++) {
                document.getElementById("editTagsFormModalSelect").innerHTML += `<option value="${data[i].tagID}">${data[i].name}</option>`;
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
        // Set the form button to a loading state
        document.getElementById("createTagFormModalSubmit").innerHTML = Buttons.getPastelButtonLoading('Creating...', 'lg');

        // Create data variable
        let data = {};

        // Get the form data
        try {
            data = {
                name: document.getElementById("createTagFormModalName").value,
                colour: document.getElementById("createTagFormModalColour").value,
            }
        }
        catch {
            // Display an error alert
            document.getElementById("createTagFormModalAlerts").innerHTML = Alerts.errorAlert('Failed to create tag. Please try again later...', 'System Error!');

            // Reset the button to a default state
            document.getElementById("createTagFormModalSubmit").innerHTML = Buttons.getPastelButton('Create Tag', 'ManageTags.createTagFormSubmit()', 'lg');

            return;
        }

        // Local input validation - check if the HEX colour code is valid
        if (!/^#[0-9A-F]{6}$/i.test(data.colour)) {
            // Display an error alert
            document.getElementById("createTagFormModalAlerts").innerHTML = Alerts.warningAlert('Invalid HEX colour code. Please try again...', 'Invalid Input!');

            // Reset the button to a default state
            document.getElementById("createTagFormModalSubmit").innerHTML = Buttons.getPastelButton('Create Tag', 'ManageTags.createTagFormSubmit()', 'lg');

            return;
        }

        // Send the form data to the server using the fetch API
        const response = await fetch('/api/tags-add', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })

        // If the server returns a 200 status code (OK)
        if (response.ok) {
            // Reset the form and display a success alert
            document.getElementById("editTagsModalForm").innerHTML = Modals.editTags();
            manageTags.searchTags();
            document.getElementById("createTagFormModalAlerts").innerHTML = Alerts.successAlert('Tag created successfully.', 'Success!');
        }
        // If the response is due to an unauthorised request, redirect to the login page
        else if (response.status === 401) {
            window.location.href = '/login';
        }
        // If it is any other status code, display an error alert
        else {
            document.getElementById("createTagFormModalAlerts").innerHTML = Alerts.errorAlert('Failed to create tag. Please try again later...', 'System Error!');
        }

        // Reset the button to a default state
            document.getElementById("createTagFormModalSubmit").innerHTML = Buttons.getPastelButton('Create Tag', 'ManageTags.createTagFormSubmit()', 'lg');
    }

    static async assignTagFormSubmit() {
        // Set the form button to a loading state
        document.getElementById("editTagsModalFormSubmit").innerHTML = Buttons.getPastelButtonLoading('Assigning...', 'lg');

        // Create data variable
        let data = {};

        // Get the form data
        try {
            data = {
                tagID: parseInt(document.getElementById("editTagsFormModalSelect").value, 10),
            }
        }
        catch {
            // Display an error alert
            document.getElementById("editTagsFormModalAlerts").innerHTML = Alerts.errorAlert('Failed to assign tag. Please try again later...', 'System Error!');

            // Reset the button to a default state
            document.getElementById("editTagsModalFormSubmit").innerHTML = Buttons.getPastelButton('Assign Tag', 'ManageTags.assignTagFormSubmit()', 'lg');

            return;
        }

        // Send the form data to the server using the fetch API
        const response = await fetch('/api/tags-assign', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })

        // If the server returns a 200 status code (OK)
        if (response.ok) {
            // Reset the form and display a success alert
            document.getElementById("editTagsModalForm").reset();
            document.getElementById("editTagsFormModalAlerts").innerHTML = Alerts.successAlert('Tag assigned successfully.', 'Success!');
        }
        // If the response is due to a not acceptable request, display an error alert
        else if (response.status === 406) {
            document.getElementById("editTagsFormModalAlerts").innerHTML = Alerts.warningAlert(await response.text(), 'Invalid Input!');
        }
        // If the response is due to an unauthorised request, redirect to the login page
        else if (response.status === 401) {
            window.location.href = '/login';
        }
        // If it is any other status code, display an error alert
        else {
            document.getElementById("editTagsFormModalAlerts").innerHTML = Alerts.errorAlert('Failed to assign tag. Please try again later...', 'System Error!');
        }

        // Reset the button to a default state
        document.getElementById("editTagsModalFormSubmit").innerHTML = Buttons.getPastelButton('Assign Tag', 'ManageTags.assignTagFormSubmit()', 'lg');
    }
}