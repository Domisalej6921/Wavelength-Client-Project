class Profile {
    static renderPage() {
        // Get the requested user ID from the URL
        const urlParams = new URLSearchParams(window.location.search);
        const userID = urlParams.get('id');
    }
}