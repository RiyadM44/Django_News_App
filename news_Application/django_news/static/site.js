let slideIndex = 0;
showSlides();

function showSlides() {
    let slides = document.getElementsByClassName("carousel-slide");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.left = "100%"; // Initially position slides outside container
    }
    slideIndex++;
    if (slideIndex > slides.length) {slideIndex = 1}
    slides[slideIndex-1].style.left = "0"; // Move current slide into view
    setTimeout(showSlides, 4000); // Change image every 4 seconds
}

function moveSlide(n) {
    slideIndex += n;
    let slides = document.getElementsByClassName("carousel-slide");
    if (slideIndex > slides.length) {slideIndex = 1}
    if (slideIndex < 1) {slideIndex = slides.length}
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.left = "100%"; // Move all slides outside container
    }
    slides[slideIndex-1].style.left = "0"; // Move current slide into view
}

// let slideIndex = 0;
// showSlides();

// function showSlides() {
//     let slides = document.getElementsByClassName("carousel-slide");
//     for (let i = 0; i < slides.length; i++) {
//         slides[i].style.display = "none";
//     }
//     slideIndex++;
//     if (slideIndex > slides.length) {slideIndex = 1}
//     slides[slideIndex-1].style.display = "block";
//     setTimeout(showSlides, 4000); // Change image every 4 seconds
// }

// function moveSlide(n) {
//     slideIndex += n;
//     let slides = document.getElementsByClassName("carousel-slide");
//     if (slideIndex > slides.length) {slideIndex = 1}
//     if (slideIndex < 1) {slideIndex = slides.length}
//     for (let i = 0; i < slides.length; i++) {
//         slides[i].style.display = "none";
//     }
//     slides[slideIndex-1].style.display = "block";
// }
