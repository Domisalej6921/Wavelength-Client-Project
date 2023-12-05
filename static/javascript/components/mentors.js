class Mentors {
    static renderCard(data) {
        return `
            <div id="mentor#${data.userID}" class="card" style="width: 18rem;">
                <img id="image" class="card-img-top" alt="${data.description}">
                <div class="card-body">
                    <h5 class="card-title">${data.name}</h5>
                    <p class="card-text">${data.description}</p>
                    <p class="card-text">Tags Insert here....</p>
                    <a href="#" class="btn btn-primary">Apply</a>
                </div>
            </div>
        `;
    }
}