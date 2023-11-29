class Modals {
    static header(title) {
        return `<div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">${title}</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>`
    }

    static editProfile() {
        return `<div id="formAlerts"></div>
        <form class="form-floating" id="loginForm">
            <div class="form-floating mb-3">
                <input type="text" class="form-control" id="modalUsername" placeholder="Username">
                <label class="text" >Username</label>
            </div>
            <div class="mb-3">
                <label for="profilePicture" class="FormText">Profile Picture</label>
                <input type="file" class="form-control" id="profilePicture">
            </div>
            <div class="mb-3">
                <label for="profileBanner" class="FormText">Profile Banner</label>
                <input type="file" class="form-control" id="profileBanner">
            </div>
        </form>
        <div class="align-content" id="loginFormSubmit">
            <button class="btn btn-pastel btn-lg" onClick="Profile.editFormSubmit()">Edit</button>
        </div>`
    }
}