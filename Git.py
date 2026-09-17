try:
    import tkinter as tk
except ModuleNotFoundError:
    tk = None
import random
import time

# Sample text list
sentences = [
    "Hi, Shall we begin our journey.",
    "Balance.",
    "conversions.",
    "Improve.",
    "Seeing you makes me happy.",
    "It hurts a lot.",
    "Your Parents are your strength and weakness.",
    "Try to make yourself happy.",
    "Pretend to be happy.",
    "Missing My World.",
    "Your smile is very beautiful.",
    "Nuvvu naku chala istam.",
    "Social Engineering.",
    "Communication.",
    "Professional.",
    "Occassionally.",
    "Express your desire.",
    "Encourage Others.",
    "Open-Ended.",
    "Call-to-Action.",
    "Demanding.",
    "Attention Grabing.",
    "Coherent Structure.",
    "Emotional Connection.",
    "Respond thoughtfully.",
    "Dominating.",
    "Talking excessively.",
    "Be approachable.",
    "Budgeting Templates.",
    "This Universe has a lot of secret things.",
    "Would you like to have a coffee.",
    "What is your qualification?",
    "Are you getting interest for typing and increasing your speed?",
    "Foxnuts are a type of aquatic plant-based snack.",
    "Focus on short-term goals and objectives.",
    "Mitigate weakness and threats.",
    "Authenticity is key in building relationships.",
    "Program Evaluation and Review Technique.",
    "Internal attributes that are unfavourable to the business.",
    "Data Well Logger Record.",
    "Typing speed is measured in words per minute.",
    "Python is a versatile programming language.",
    "Practice makes a person perfect in typing.",
    "Tkinter makes GUI development simple and fast.",
    "Artificial Intelligence is shaping the future."
]

# Global variables
start_time = 0
selected_sentence = ""
root = None
sentence_label = None
entry = None
result_label = None


def calculate_wpm(typed_text, elapsed_seconds):
    if elapsed_seconds <= 0:
        return 0
    word_count = len(typed_text.strip().split())
    return round((word_count / elapsed_seconds) * 60)


def build_result_message(typed_text, target_sentence, elapsed_seconds):
    if typed_text.strip() == "":
        return "Please type something!"

    wpm = calculate_wpm(typed_text, elapsed_seconds)
    if typed_text.strip() == target_sentence:
        return f"Correct! Your typing speed is {wpm} WPM."
    return f"Incorrect! You typed {wpm} WPM."

# Function to start the test
def start_test():
    global start_time, selected_sentence
    selected_sentence = random.choice(sentences)
    sentence_label.config(text=selected_sentence)
    entry.delete(0, tk.END)
    result_label.config(text="")
    start_time = time.time()

# Function to check typing speed
def check_speed():
    if start_time == 0 or selected_sentence == "":
        result_label.config(text="Click 'Start Test' first!")
        return

    end_time = time.time()
    typed_text = entry.get()
    time_taken = end_time - start_time

    result_label.config(text=build_result_message(typed_text, selected_sentence, time_taken))


def create_ui():
    global root, sentence_label, entry, result_label
    if tk is None:
        raise RuntimeError("Tkinter is not available in this Python environment.")

    root = tk.Tk()
    root.title("Typing Speed Test")
    root.geometry("600x300")
    root.config(bg="white")

    instruction = tk.Label(root, text="Click 'Start Test' and type the sentence as fast as you can.", bg="white")
    instruction.pack(pady=10)

    sentence_label = tk.Label(root, text="", font=("Arial", 14), wraplength=500, bg="white")
    sentence_label.pack(pady=10)

    entry = tk.Entry(root, font=("Arial", 12), width=70)
    entry.pack(pady=10)

    start_btn = tk.Button(root, text="Start Test", command=start_test, bg="#4CAF50", fg="white")
    start_btn.pack(pady=5)

    check_btn = tk.Button(root, text="Check Speed", command=check_speed, bg="#2196F3", fg="white")
    check_btn.pack(pady=5)

    result_label = tk.Label(root, text="", font=("Arial", 12), fg="black", bg="white")
    result_label.pack(pady=10)

    return root


def run_app():
    app = create_ui()
    app.mainloop()


if __name__ == "__main__":
    run_app()
