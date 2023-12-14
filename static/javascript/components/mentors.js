
class Mentors {
    static renderCard(data) {
        return `
            <div id="mentor#${data.userID}" class="card" style="width: 18rem;">
                <img src="/static/uploads/${data.profilePicture.path}" class="card-img-top" alt="${data.profilePicture.alt}">
                <div class="card-body">
                    <h5 class="card-title">${data.name}</h5>
                    <p class="card-text">${data.description}</p>
                    <p class="card-text">Tags Insert here....</p>
<!--                    Used here to understand how to redirect flask pages in js/html-->
<!--                    https://stackoverflow.com/questions/61625290/flask-make-a-button-direct-to-another-page-->
                    <a href="/account/mentor_apply" class="btn btn-primary">Apply</a>
                </div>
            </div>
        `;
    }
    static renderMentor(data) {
        return `
            <div id="mentor#${data.userID}" class="page-contents" style="width: 18rem;">
                <div class="mentor-heading">
                    <h1>${data.name}</h1>
                </div>
                <div class="tags-container">
                    <p>Tags go here...........</p>
                </div>
                <div class="mentor-page-text">
                    <div class="mentor-image">
                        <img src="/static/uploads/${data.profilePicture.path}" alt="${data.profilePicture.alt}">
                    </div>
                    <div class="mentor-desc">
                        <p>${data.description}</p>
                    </div>
                </div>
            </div>
        `;
    }
}