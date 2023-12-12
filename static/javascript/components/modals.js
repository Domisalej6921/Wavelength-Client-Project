class Modals {
    /* Used examples of modals from:
    https://www.w3schools.com/bootstrap5/bootstrap_modal.php */
    static header(title) {
        return `<h4 class="modal-title">${title}</h4>
        <button type="button" class="btn-close" data-bs-dismiss="modal"></button>`
    }

    static editProfile() {
        return `<div id="modalEditProfileFormAlerts"></div>
        <form class="form-floating" id="modalEditProfileForm">
            <div class="mb-3">
                <p class="h6"><b>Note: </b>Fields you do not wish to edit should be left empty.</p>
            </div>
            <div class="form-floating mb-3">
                <input type="text" class="form-control" id="modalUsername" placeholder="Username">
                <label class="text" >Username</label>
            </div>
            <div class="mb-3">
                <label for="modalProfilePicture" class="FormText">Profile Picture</label>
                <input type="file" class="form-control" id="modalProfilePicture" onchange="Profile.handleUpload('modalProfilePicture', 'profilePicture')">
            </div>
            <div class="mb-3">
                <label for="modalProfileBanner" class="FormText">Profile Banner</label>
                <input type="file" class="form-control" id="modalProfileBanner" onchange="Profile.handleUpload('modalProfileBanner', 'profileBanner')">
            </div>
        </form>
        <div class="align-content" id="modalEditProfileSubmit">
            <button class="btn btn-pastel btn-lg" onClick="Profile.editFormSubmit()">Edit</button>
        </div>`
    }
}