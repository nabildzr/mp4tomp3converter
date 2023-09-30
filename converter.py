import tkinter as tk
from tkinter import filedialog
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_audio

# Exit
def exit():
  app.destroy()

# Converter
def converter():
  input_file = filedialog.askopenfile(title = 'Select Mp4 File', file_types = [('Video files', '*.mp4')]

  if input_file:
		output_file = input_file.replace('.mp4', '.mp3')
		ffmpeg_extract_audio(input_file, output_file)
		result_label.config(text = 'Convert is completed. File mp3 saved in ' + output_file)

app.tk.Tk()
app.title('Converter Mp4 to Mp3')

# Select Button, This Button used for Select mp4 file so that convert to mp3
select_button = tk.Button(app, text = 'Select File', command = converter)
select_button.pack(pady = 20)
select_button.configure(background = 'blue', foreground = 'white')

# Exit Button, For better experience after waiting convert
exit_button = tk.Button(app, text = 'Exit', command = exit)
exit_button.pack()
exit_button.configure(background = 'yellow', foreground = 'white')

# Result View
result_label = tk.Label(app, text = '')
result_label.pack

# Run App
app.mainloop()
