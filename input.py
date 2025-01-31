import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return

    folder = filedialog.askdirectory()
    if not folder:
        messagebox.showerror("Error", "Please select a download folder")
        return

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        stream.download(folder)
        messagebox.showinfo("Success", f"Downloaded '{yt.title}' successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to download video: {e}")

app = tk.Tk()
app.title("YouTube Downloader")

tk.Label(app, text="YouTube URL:").pack(pady=5)
url_entry = tk.Entry(app, width=50)
url_entry.pack(pady=5)

download_button = tk.Button(app, text="Download", command=download_video)
download_button.pack(pady=20)

app.mainloop()