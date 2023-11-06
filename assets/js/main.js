// // JavaScript
// const textElement = document.getElementById("typed-text");
// const text = textElement.textContent;
// textElement.textContent = ""; // Clear the text initially

// let i = 0;
// function typeText() {
//   if (i < text.length) {
//     textElement.textContent += text.charAt(i);
//     i++;
//     setTimeout(typeText, 50); // Adjust the speed by changing the timeout value (milliseconds)
//   }
// }

// typeText(); // Start the typing animation



window.addEventListener('scroll', () => {
    console.log('scrolled')
  document.querySelector('header').classList.toggle('window-scroll', window.scrollY > 0)
})
