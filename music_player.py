import os
import tkinter as tk
from tkinter import filedialog
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Function to load and play a selected song
def play_music():
    file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3;*.wav")])
    if file_path:
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()

# Function to pause the music
def pause_music():
    pygame.mixer.music.pause()

# Function to resume the music
def resume_music():
    pygame.mixer.music.unpause()

# Function to stop the music
def stop_music():
    pygame.mixer.music.stop()

# GUI Setup
root = tk.Tk()
root.title("Music Player")
root.geometry("400x300")

# Buttons
play_button = tk.Button(root, text="Play", command=play_music, width=10)
play_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause", command=pause_music, width=10)
pause_button.pack(pady=10)

resume_button = tk.Button(root, text="Resume", command=resume_music, width=10)
resume_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop", command=stop_music, width=10)
stop_button.pack(pady=10)

# Run the application
root.mainloop()
