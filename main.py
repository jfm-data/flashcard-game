import random
import tkinter as tk
from dataclasses import dataclass


@dataclass(frozen=True)
class Flashcard:
	english: str
	spanish: str
	phonetic: str


FLASHCARDS = [
	Flashcard("always", "siempre", "syem-pre"),
	Flashcard("hello", "hola", "oh-lah"),
	Flashcard("please", "por favor", "por fah-vor"),
	Flashcard("thank you", "gracias", "grah-syahs"),
	Flashcard("goodbye", "adios", "ah-dee-ohs"),
	Flashcard("friend", "amigo", "ah-mee-go"),
	Flashcard("water", "agua", "ah-gwah"),
	Flashcard("food", "comida", "koh-mee-dah"),
]


class FlashcardGame:
	def __init__(self, root: tk.Tk) -> None:
		self.root = root
		self.root.title("English to Spanish Flashcards")
		self.root.geometry("560x340")
		self.root.resizable(False, False)

		self.cards = FLASHCARDS[:]
		random.shuffle(self.cards)
		self.index = 0
		self.revealed = False

		self.title_label = tk.Label(
			root,
			text="Flashcard Game",
			font=("Helvetica", 24, "bold"),
			pady=16,
		)
		self.title_label.pack()

		self.card_frame = tk.Frame(root, bd=2, relief="ridge", padx=24, pady=24)
		self.card_frame.pack(fill="both", expand=True, padx=20, pady=10)

		self.word_label = tk.Label(self.card_frame, text="", font=("Helvetica", 28, "bold"))
		self.word_label.pack(pady=(24, 12))

		self.translation_label = tk.Label(self.card_frame, text="", font=("Helvetica", 20))
		self.translation_label.pack(pady=8)

		self.hint_label = tk.Label(
			root,
			text="Click Reveal Translation to show Spanish + phonetic spelling.",
			font=("Helvetica", 11),
			fg="#444444",
			pady=6,
		)
		self.hint_label.pack()

		self.button_frame = tk.Frame(root, pady=8)
		self.button_frame.pack()

		self.reveal_button = tk.Button(
			self.button_frame,
			text="Reveal Translation",
			width=20,
			command=self.reveal_translation,
		)
		self.reveal_button.grid(row=0, column=0, padx=8)

		self.next_button = tk.Button(
			self.button_frame,
			text="Next Card",
			width=12,
			command=self.next_card,
		)
		self.next_button.grid(row=0, column=1, padx=8)

		self.root.bind("<Return>", self.on_enter)
		self.show_card()

	@property
	def current_card(self) -> Flashcard:
		return self.cards[self.index]

	def show_card(self) -> None:
		card = self.current_card
		self.word_label.config(text=card.english)
		self.translation_label.config(text="")
		self.revealed = False

	def reveal_translation(self) -> None:
		if self.revealed:
			return
		card = self.current_card
		self.translation_label.config(text=f"{card.spanish} ({card.phonetic})")
		self.revealed = True

	def next_card(self) -> None:
		self.index += 1
		if self.index >= len(self.cards):
			random.shuffle(self.cards)
			self.index = 0
		self.show_card()

	def on_enter(self, _event: tk.Event) -> None:
		if self.revealed:
			self.next_card()
		else:
			self.reveal_translation()


def main() -> None:
	root = tk.Tk()
	FlashcardGame(root)
	root.mainloop()


if __name__ == "__main__":
	main()
