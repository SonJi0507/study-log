const images = [
    "0.jpg",
    "1.jpg",
    "2.jpg"
];

const todayImage = images[Math.floor(Math.random()*images.length)]
const bgImage = document.createElement("img");

bgImage.src = `img/${todayImage}`;

document.body.appendChild(bgImage);