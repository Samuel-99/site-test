const button = document.querySelector("#color-button");

// Keep the palette dark enough for the white button text.
const colors = ["#1d4ed8", "#047857", "#b91c1c", "#7e22ce", "#9a3412"];
let currentColor;

button.addEventListener("click", () => {
  // Exclude the current color so every click makes a visible change.
  const availableColors = colors.filter((color) => color !== currentColor);
  const randomIndex = Math.floor(Math.random() * availableColors.length);

  currentColor = availableColors[randomIndex];
  button.style.backgroundColor = currentColor;
});
