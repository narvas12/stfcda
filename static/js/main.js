
const textElement = document.getElementById("typed-text");
const text = textElement.textContent;
textElement.textContent = ""; // Clear the text initially

let i = 0;
function typeText() {
    if (i < text.length) {
        textElement.textContent += text.charAt(i);
        i++;
        setTimeout(typeText, 50); // Adjust the speed by changing the timeout value (milliseconds)
    }
}

typeText(); // Start the typing animation




document.addEventListener('DOMContentLoaded', function () {
  window.addEventListener('scroll', revealOnScroll);
});



function revealOnScroll() {
  var reveals = document.querySelectorAll('.scroll-display');
  
  for (var i = 0; i < reveals.length; i++) {
    var windowHeight = window.innerHeight;
    var revealTop = reveals[i].getBoundingClientRect().top;
    var revealPoint = 150; // Adjust this value as needed

    if (revealTop < windowHeight - revealPoint) {
      reveals[i].classList.add('show');
    }
  }
}


document.addEventListener("DOMContentLoaded", function () {
  const starryDiv = document.getElementById("starry-div");

  for (let i = 1; i <= 7; i++) {
    const star = document.createElement("div");
    star.classList.add("star", `star${i}`);
    starryDiv.appendChild(star);
    setRandomPosition(star);
  }
});

function setRandomPosition(element) {
  const maxX = window.innerWidth - 50; // Adjust as needed
  const maxY = window.innerHeight - 50; // Adjust as needed

  const randomX = Math.floor(Math.random() * maxX);
  const randomY = Math.floor(Math.random() * maxY);

  element.style.left = `${randomX}px`;
  element.style.top = `${randomY}px`;
}



document.addEventListener("DOMContentLoaded", function () {
  const fallingStarsContainer = document.getElementById("falling-stars");

  for (let i = 0; i < 30; i++) {
    const star = document.createElement("div");
    star.classList.add("star");
    fallingStarsContainer.appendChild(star);
    setRandomPosition(star);
    setRandomAnimationDuration(star);
  }
});

function setRandomPosition(element) {
  const maxX = window.innerWidth;
  const randomX = Math.floor(Math.random() * maxX);
  const randomY = Math.floor(Math.random() * window.innerHeight);

  element.style.left = `${randomX}px`;
  element.style.top = `${randomY}px`;
}

function setRandomAnimationDuration(element) {
  const duration = Math.random() * 5 + 2; // Adjust as needed
  element.style.animationDuration = `${duration}s`;
}
