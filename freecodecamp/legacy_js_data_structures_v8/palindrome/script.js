const textInput = document.getElementById("text-input");
const checkBtn = document.getElementById("check-btn");
const result = document.getElementById("result");

checkBtn.addEventListener("click", () => {
  if (textInput.value === "") {
    alert("Please input a value");
    return;
  }
  const originalText = textInput.value;
  const cleanedText = originalText.replace(/[^a-z0-9]/gi, "").toLowerCase();
  const reversedText = cleanedText.split("").reverse().join("");
   if (cleanedText === reversedText) {
    result.textContent = `${originalText} is a palindrome`;
  } else {
    result.textContent = `${originalText} is not a palindrome`;
  }
});