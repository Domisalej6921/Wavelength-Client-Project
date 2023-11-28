class Modals {
    static header(title) {
        return `<div className="modal-header">
            <h5 className="modal-title" id="exampleModalLabel">${title}</h5>
            <button type="button" className="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>`
    }

    static editProfile() {
        return `<div id="formAlerts"></div>
        <form className="form-floating" id="loginForm">
            <div className="form-floating mb-3">
                <input type="text" className ="form-control" id="modalUsername" placeholder="Username">
                <label htmlFor="text" >Username</label>
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
        <div className="align-content" id="loginFormSubmit">
            <button className="btn btn-pastel btn-lg" onClick="Profile.editFormSubmit()">Edit</button>
        </div>`
    }
}