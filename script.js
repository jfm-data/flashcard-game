const flashcards = [
  { english: "fault", spanish: "faulta", phonetic: "fal-ta" },
  { english: "house", spanish: "casa", phonetic: "ka-sa" },
  { english: "water", spanish: "agua", phonetic: "a-gwa" },
];

const flashcardButton = document.getElementById("flashcard");
const nextCardButton = document.getElementById("next-card");

let cardIndex = 0;
let isRevealed = false;

function updateCard() {
  const card = flashcards[cardIndex];

  if (isRevealed) {
    flashcardButton.textContent = `${card.spanish} (${card.phonetic})`;
    flashcardButton.classList.add("revealed");
    flashcardButton.setAttribute("aria-label", `${card.english}: ${card.spanish} (${card.phonetic})`);
    return;
  }

  flashcardButton.textContent = card.english;
  flashcardButton.classList.remove("revealed");
  flashcardButton.setAttribute("aria-label", card.english);
}

flashcardButton.addEventListener("click", () => {
  isRevealed = !isRevealed;
  updateCard();
});

nextCardButton.addEventListener("click", () => {
  cardIndex = (cardIndex + 1) % flashcards.length;
  isRevealed = false;
  updateCard();
});

updateCard();
