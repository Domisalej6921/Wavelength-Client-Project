class BecomeMentor {
    static async submitMentorshipForm() {

        let formData = {
            username: null,
            desc: null,
        }

        try {
            formData.username = document.getElementById("username")
            formData.desc = document.getElementById("description")
        }

        const response = await fetch("/api/account/become_mentor", {
            method: "POST",
            headers: {
                "Content-Type": "application/json;charset=UTF-8"
            },
            body: JSON.stringify(formData))
    }
}