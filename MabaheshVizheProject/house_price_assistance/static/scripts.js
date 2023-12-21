var delayInMilliseconds = 500;

setTimeout(function () {
  var dropdown = document.getElementById("dropdown");
  dropdown.addEventListener("change", function () {
    var selectedIndex = dropdown.selectedIndex;
    console.log("Selected index:", selectedIndex);
  });
}, delayInMilliseconds);

// const inputs = document.querySelectorAll('input[type="radio"]');
// inputs.forEach((input) => {
//   input.addEventListener("change", () => {
//     inputs.forEach((otherInput) => {
//       if (otherInput !== input) {
//         otherInput.removeAttribute("checked");
//       }
//     });
//   });
// });
