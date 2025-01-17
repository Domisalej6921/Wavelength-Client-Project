class Modals {
    /* Used examples of modals from:
    https://www.w3schools.com/bootstrap5/bootstrap_modal.php */
    static header(title) {
        return `<h4 class="modal-title">${title}</h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>`
    }

    static editProfile() {
        return `<div id="editProfileFormModalAlerts"></div>
        <form class="form-floating" id="editProfileModalForm">
            <div class="mb-3">
                <p class="h6"><b>Note: </b>Fields you do not wish to edit should be left empty.</p>
            </div>
            <div class="form-floating mb-3">
                <input type="text" class="form-control" id="editProfileFormModalUsername" placeholder="Username">
                <label class="text" >Username</label>
            </div>
            <div class="form-floating mb-3">
                  <textarea type="text" class="form-control" id="editProfileFormModalDescription"></textarea>
                  <label for="editProfileFormModalDescription">Description</label>
               </div>
            <div class="mb-3">
                <label for="editProfileFormModalProfilePicture" class="FormText">Profile Picture</label>
                <input type="file" class="form-control" id="editProfileFormModalProfilePicture">
            </div>
            <div class="mb-3">
                <label for="editProfileFormModalBanner" class="FormText">Profile Banner</label>
                <input type="file" class="form-control" id="editProfileFormModalProfileBanner">
            </div>
        </form>
        <div class="align-content" id="editProfileFormModalSubmit">
            <button class="btn btn-pastel btn-lg" onClick="EditProfile.formSubmit()">Edit</button>
        </div>`
    }

    static clearTagSubmit() {
        try {
            document.getElementById("editTagsModalFormSubmit").remove();
        }
        catch {}
        try {
            document.getElementById("createTagFormModalSubmit").remove();
        }
        catch {}
    }

    static editTags() {
        Modals.clearTagSubmit()
        return `<div id="editTagsFormModalAlerts"></div>
        <form class="form-floating" id="editTagsModalForm">
            <div class="form-floating mb-3">
                <input type="text" class="form-control" id="editTagsFormModalSearch" placeholder="Tag" onchange="ManageTags.searchTags()">
                <label class="text" >Tag Name</label>
            </div>
            <div class="form-floating mb-3">
                <select class="form-select mb-3" aria-label=".form-select example" id="editTagsFormModalSelect">
                </select>
                <label for="editTagsFormModalSelect">Choose a Tag</label>
            </div>
        </form>
        <div class="align-content" id="editTagsModalFormSubmit">
            <button class="btn btn-pastel btn-lg" onClick="ManageTags.assignTagFormSubmit()">Assign</button>
        </div>`;
    }

    static createTag() {
        Modals.clearTagSubmit()
        return `<div id="createTagFormModalAlerts"></div>
        <form class="form-floating" id="createTagModalForm">
            <div class="form-floating mb-3">
                <input type="text" class="form-control" id="createTagFormModalName" placeholder="Name">
                <label class="text" >Tag Name</label>
            </div>
            <div class="form-floating mb-3">
                <input type="text" class="form-control" id="createTagFormModalColour" placeholder="Example: #3390FF">
                <label class="text" >Tag HEX Colour Code</label>
            </div>
        </form>
        <div class="align-content" id="createTagFormModalSubmit">
            <button class="btn btn-pastel btn-lg" onClick="ManageTags.createTagFormSubmit()">Create Tag</button>
        </div>`;
    }
}