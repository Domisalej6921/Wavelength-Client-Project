class Profile {
    static renderEditForm () {
        document.getElementById("formModalHeader").innerHTML = Modals.header("Edit Profile");
        document.getElementById("formModalBody").innerHTML = Modals.editProfile();

        document.getElementById("root").innerHTML = `<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#formModal">Open modal</button>`;
    }

    static editFormSubmit() {
        // Define a local variable to store file uploads
        let formData = {
            profilePicture: null,
            profileBanner: null
        };

        // Get the file input element
        let profilePicture = document.getElementById("profilePicture");
        const profileFile = profilePicture.files[0];
        FileUploads.format(profileFile).then((result) => {
            formData.profilePicture = result;
            console.log(result)
        });
    }
}