import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pydub import AudioSegment
import numpy as np
import os

def load_files():
    files = filedialog.askopenfilenames(filetypes=[("Audio Files", "*.wav")])
    if files:
        file_list.delete(0, tk.END)
        for file in files:
            file_list.insert(tk.END, file)

def choose_output_folder():
    folder = filedialog.askdirectory()
    if folder:
        output_folder_entry.delete(0, tk.END)
        output_folder_entry.insert(0, folder)

def process_files():
    files = file_list.get(0, tk.END)
    output_folder = output_folder_entry.get()
    freq_diff = float(freq_diff_entry.get())
    mode = mode_var.get()

    if not files:
        messagebox.showwarning("Warning", "Please select at least one audio file.")
        return

    if not output_folder:
        messagebox.showwarning("Warning", "Please select an output folder.")
        return

    progress_bar['maximum'] = len(files)
    progress_bar['value'] = 0

    for i, file in enumerate(files):
        process_file(file, output_folder, freq_diff, mode)
        progress_bar['value'] += 1
        root.update_idletasks()

    messagebox.showinfo("Info", "Processing complete!")

def process_file(file, output_folder, freq_diff, mode):
    audio = AudioSegment.from_wav(file)
    samples = np.array(audio.get_array_of_samples())

    if audio.channels == 2:
        left_channel = samples[::2]
        right_channel = samples[1::2]
    else:
        left_channel = samples
        right_channel = samples

    if mode == "add_frequency":
        left_channel = add_frequency(left_channel, audio.frame_rate, freq_diff)
        right_channel = add_frequency(right_channel, audio.frame_rate, -freq_diff)
    elif mode == "modify_frequency":
        left_channel = modify_frequency(left_channel, audio.frame_rate, freq_diff)
        right_channel = modify_frequency(right_channel, audio.frame_rate, freq_diff)
    elif mode == "phase_shift":
        left_channel, right_channel = phase_shift(left_channel, right_channel, audio.frame_rate, freq_diff)

    # Ensure both channels have the same length
    min_len = min(len(left_channel), len(right_channel))
    left_channel = left_channel[:min_len]
    right_channel = right_channel[:min_len]

    output_samples = np.column_stack((left_channel, right_channel)).ravel()
    output_audio = audio._spawn(output_samples)

    output_file = os.path.join(output_folder, os.path.basename(file))
    output_audio.export(output_file, format="wav")

def add_frequency(channel, frame_rate, freq_diff):
    t = np.arange(len(channel)) / frame_rate
    new_channel = channel + 0.1 * np.sin(2 * np.pi * freq_diff * t) * np.max(channel)
    return new_channel.astype(np.int16)

def modify_frequency(channel, frame_rate, freq_diff):
    t = np.arange(len(channel)) / frame_rate
    new_channel = np.interp(t, t * (1 + freq_diff / frame_rate), channel)
    return new_channel.astype(np.int16)

def phase_shift(left_channel, right_channel, frame_rate, freq_diff):
    shift_amount = int(frame_rate / freq_diff)
    right_channel = np.roll(right_channel, shift_amount)
    return left_channel, right_channel

root = tk.Tk()
root.title("Binaural Beats Audio Processor")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

file_list = tk.Listbox(frame, selectmode=tk.MULTIPLE, width=50)
file_list.pack(padx=5, pady=5)

btn_select_files = tk.Button(frame, text="Select Files", command=load_files)
btn_select_files.pack(padx=5, pady=5)

output_folder_entry = tk.Entry(frame, width=50)
output_folder_entry.pack(padx=5, pady=5)

btn_choose_output = tk.Button(frame, text="Choose Output Folder", command=choose_output_folder)
btn_choose_output.pack(padx=5, pady=5)

freq_diff_label = tk.Label(frame, text="Frequency Difference (Hz):")
freq_diff_label.pack(padx=5, pady=5)

freq_diff_entry = tk.Entry(frame)
freq_diff_entry.pack(padx=5, pady=5)

mode_var = tk.StringVar(value="add_frequency")
mode_label = tk.Label(frame, text="Select Mode:")
mode_label.pack(padx=5, pady=5)

mode_frame = tk.Frame(frame)
mode_frame.pack(padx=5, pady=5)

modes = [("Add Frequency", "add_frequency"), ("Modify Frequency", "modify_frequency"), ("Phase Shift", "phase_shift")]
for text, mode in modes:
    radio_btn = tk.Radiobutton(mode_frame, text=text, variable=mode_var, value=mode)
    radio_btn.pack(side=tk.LEFT, padx=5, pady=5)

btn_process = tk.Button(frame, text="Process and Export", command=process_files)
btn_process.pack(padx=5, pady=5)

progress_bar = ttk.Progressbar(frame, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(padx=5, pady=5)

root.mainloop()
