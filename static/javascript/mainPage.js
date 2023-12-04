async function loadIntoTable(url, card) {
    const mentorImage = card.querySelector("img");
    const mentorTitle = card.querySelector("h5");
    const mentorDesc = card.querySelector("p");
    const response = await fetch(url);
    const { img, title, desc } = await response.json();

    // Clear the table
    mentorImage.innerHTML = "<img src='...' alt='...'>";
    mentorTitle.innerHTML = "<h5></h5>";
    mentorDesc.innerHTML = "<p></p>";

    //Populate Headers
    for (const imageData of img) {
        const imgDisplay = document.createElement("img");

        imgDisplay.textContent = imageData;
        mentorImage.querySelector("img").appendChild(imgDisplay);
    }
}

loadIntoTable(/mainPage.json, document.querySelector("card"));