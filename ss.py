import tkinter as tk
from tkinter import messagebox, filedialog
from pytube import YouTube
def download_video():
    url = entry.get()
    resolution = resolution_var.get()
    try:
        
        yt = YouTube(url)
        video = yt.streams.filter(res=resolution, file_extension='mp4', progressive=True).first()

        if not video:
            messagebox.showwarning("Alert", f"I can not find selected resolution.  be downloaded in the best possible resolution")

            video = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first()

        if video:
            save_path = filedialog.askdirectory()
            if save_path:
                video.download(output_path=save_path)
                messagebox.showinfo("All Done", "Download Video Successfuly!")
            else:
                messagebox.showwarning("Alert", "Please Select destination!")
        else:
            messagebox.showwarning("Alert", "I can not find video or I can not download it!")
    except Exception as e:
        messagebox.showerror("Error", f"Error during downloading please try again:\n{str(e)}")

root = tk.Tk()
root.title("YouTube Video Downloader by nurxan02")

label = tk.Label(root, text="YouTube Video URL:", font=("Arial", 12))
label.pack()
entry = tk.Entry(root, width=50, font=("Arial", 12))
entry.pack()

resolutions = ["2160p", "1440p", "1080p", "720p", "480p", "360p", "240p", "144p"]
resolution_var = tk.StringVar(root)
resolution_var.set(resolutions[0])
resolution_menu = tk.OptionMenu(root, resolution_var, *resolutions)
resolution_menu.config(font=("Arial", 12))
resolution_menu.pack()

button = tk.Button(root, text="Download Video", command=download_video, font=("Arial", 12), bg="blue", fg="black")
button.pack(pady=10)

root.mainloop()
