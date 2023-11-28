class CreateCommunity {
    static submitForm() {
        let path = document.getElementById("profilePicture").value;
        let profilePicture = FileUploads.format(path);
        console.log(profilePicture);
    }
}