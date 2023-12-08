class fetchMentors {
     static async getWithLimit(limit) {
        // Define JSON payload for mentors
        const data = {
            "limit": limit
        };

        // Send the form data to the server using the fetch API
        // Used: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
        return await fetch("/api/mentors", {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            },
            body: JSON.stringify(data)
        });
    }
}