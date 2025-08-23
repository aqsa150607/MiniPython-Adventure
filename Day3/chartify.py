import tkinter as tk
from tkinter import ttk
from collections import Counter
import matplotlib.pyplot as plt


# Function to analyze text
def analyze_text():
    user_text = text_widget.get("1.0", "end-1c")  # grab input
    if not user_text.strip():
        return
    words = user_text.split()
    counts = Counter(words)

    top_n = 10  # Show top 10 word
    most_common = counts.most_common(top_n)
    words_list, freq_list = zip(*most_common)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.bar(words_list, freq_list, color="skyblue")
    plt.xticks(rotation=45)
    plt.title(f"Top {top_n} Word Frequencies")
    plt.xlabel("Words")
    plt.ylabel("Count")
    plt.show()


# Function to clear text
def clear_text():
    text_widget.delete("1.0", "end")


# Tkinter window
root = tk.Tk()
root.title("Day 3 - Word Frequency Visualizer")
root.geometry("600x400")

# Frame for layout
frame = ttk.Frame(root, padding=10)
frame.pack(fill="both", expand=True)

# Text widget
text_widget = tk.Text(frame, width=60, height=10)
text_widget.pack(pady=5)

# Buttons
analyze_btn = ttk.Button(frame, text="Analyze", command=analyze_text)
analyze_btn.pack(pady=5)

clear_btn = ttk.Button(frame, text="Clear", command=clear_text)
clear_btn.pack(pady=5)

root.mainloop()
