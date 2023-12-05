async function loadIntoContainer(url, card) {
    const mentorImage = card.querySelector("img");
    const mentorTitle = card.querySelector("h5");
    const mentorDesc = card.querySelector("p");
    const response = await fetch(url);
    const { img, title, desc } = await response.json();

    // Clear the table
    mentorImage.innerHTML = "<img src='...' alt='...'>";
    mentorTitle.innerHTML = "<h5></h5>";
    mentorDesc.innerHTML = "<p></p>";

    //Populate images
    for (const imageData of img) {
        const imgDisplay = document.createElement("img");

        imgDisplay.textContent = imageData;
        mentorImage.querySelector("img").appendChild(imgDisplay);
    }

    //Populate the titles
    for (const titleData of title) {
        const titleDisplay = document.createElement("h5");

        titleDisplay.textContent = titleData;
        mentorTitle.querySelector("h5").appendChild(titleDisplay);
    }

    //Populate the Description
    for (const descData of desc) {
        const descDisplay = document.createElement("p");

        descDisplay.textContent = descData;
        mentorDesc.querySelector("p").appendChild(descDisplay);
    }
}

 function loadAdditionalRow() {
    let newContainer = document.createElement('div');
    newContainer.className = 'card';

    newContainer.innerHTML = "<p>Loading....</p>";

    let parentContainer = document.getElementById('mentorFrame');

    let lastRowContainer = parentContainer.lastElementChild;
    if(!lastRowContainer || lastRowContainer.childElementCount === 3) {
        lastRowContainer = document.createElement('div');
        lastRowContainer.className = 'row-container';
        parentContainer.appendChild(lastRowContainer);
    }

    lastRowContainer.appendChild(newContainer);
}

document.getElementById('LoadMoreButton').addEventListener('click', loadAdditionalRow)

loadIntoContainer(/mainpage.json, document.querySelector("card"));