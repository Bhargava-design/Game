import random
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("Hangman")

# Initialize the difficulty variable
difficulty = StringVar()
difficulty.set("Easy")

# Function to select a word based on difficulty
def select_word(difficulty):
    word_list = {
        "Easy": ["python", "hangman", "programming", "computer", "game"],
        "Medium": ["apple", "banana", "orange", "grape", "melon"],
        "Hard": ["elephant", "giraffe", "rhinoceros", "hippopotamus", "crocodile"]
    }
    return random.choice(word_list[difficulty])

# Update the word label with guessed letters
def update_word_label():
    guessed_word = [letter if letter in guessed_letters else "_" for letter in word]
    # Display the first letter as a hint
    hint_word = word[0] + " " + " ".join(guessed_word[1:])
    word_label.configure(text=hint_word)


# Start a new game
def start_game():
    global word, attempts, guessed_letters, wrong_letters
    word = select_word(difficulty.get())
    attempts = 3
    guessed_letters = []
    wrong_letters = []

    word_label.config(text="")
    attempts_label.config(text="Attempts left: " + str(attempts))
    message_label.config(text="")
    game_over_text.config(text="")

    update_word_label()
    
# Handle the word entered by the player
def guess_word():
    global attempts
    guess = guess_entry.get().lower()
    guess_entry.delete(0, END)
    if len(guess) == 0 or not guess.isalpha():
        message_label.config(text="Invalid input. Please enter a valid word.", fg="red")
    else:
        if guess == word:
            message_label.config(text="Congratulations! You guessed the word:", fg="green")
            attempts_label.config(text="Attempts left: " + str(attempts), fg="black")
            game_over_text.config(text=word, fg="green")
            root.after(3000, start_game)# Start a new game after 2 seconds
        else:
            attempts -= 1
            attempts_label.config(text="Attempts left: " + str(attempts), fg="black")
            if attempts == 0:
                message_label.config(text="Game over! You ran out of attempts.", fg="red")
                game_over_text.config(text="The word was: " + word, fg="red")
                root.after(3000, start_game)



# GUI
root.geometry("400x500")
root.config(bg="white")

# Background Image
#background_image = ImageTk.PhotoImage(Image.open(r"C:\Users\Dell\Downloads\wallpaperflare.com_wallpaper.jpg"))
#background_label = Label(root, image=background_image)
#background_label.place(x=0, y=0, relwidth=1, relheight=1)

main_frame = Frame(root, bg="white")
main_frame.pack(pady=20)

header_label = Label(main_frame, text="Hangman Game", font=("Helvetica", 20), bg="white")
header_label.pack()

difficulty_frame = Frame(main_frame, bg="white")
difficulty_frame.pack(pady=10)

difficulty_label = Label(difficulty_frame, text="Select difficulty:", font=("Helvetica", 12), bg="white")
difficulty_label.pack(side=LEFT, padx=10)

difficulty_menu = ttk.Combobox(difficulty_frame, textvariable=difficulty, values=["Easy", "Medium", "Hard"], state="readonly", font=("Helvetica", 12))
difficulty_menu.pack(side=LEFT, padx=10)
difficulty_menu.current(0)

start_button = ttk.Button(main_frame, text="Start Game", command=start_game)
start_button.pack(pady=10)

hangman_frame = Frame(main_frame, bg="white")
hangman_frame.pack()

hangman_label = Label(hangman_frame, bg="white")
hangman_label.pack()

word_label = Label(root, text="", bg="white", font=("Helvetica", 16))
word_label.pack(pady=10)

guess_frame = Frame(root, bg="white")
guess_frame.pack()

guess_label = Label(guess_frame, text="Enter the word:", font=("Helvetica", 12), bg="white")
guess_label.pack(side=LEFT, padx=10)

guess_entry = Entry(guess_frame, font=("Helvetica", 12))
guess_entry.pack(side=LEFT, padx=10)

guess_button = ttk.Button(guess_frame, text="Enter", command=guess_word)
guess_button.pack(side=LEFT, padx=10)

attempts_label = Label(root, text="Attempts left: 6", bg="white", font=("Helvetica", 12))
attempts_label.pack(pady=10)

message_label = Label(root, text="", bg="white", font=("Helvetica", 12))
message_label.pack()

game_over_text = Label(root, text="", bg="white", font=("Helvetica", 12))
game_over_text.pack(pady=10)

root.mainloop()
