import numpy as np
import librosa
import time
import tkinter
#from tkinter import filedialog -- TypeError: Invalid file?


np.set_printoptions(threshold=np.inf)
#root=tkinter.Tk()
#file_path=filedialog.askopenfilenames(title="Choose a song",filetypes=(("WAV Files", "*.wav"),("All files(unsupported)", "*.*")))
file_path = input(f'Type in the path to the song (remove quotes on the side if present): ')
#with open("E:\website\musiconway\output.txt", "w") as f:
#    print(output, file=f) #maybe I don't need to make a txt file? what about just data array? I do need something to database it...

#librosa variables:
y, sr = librosa.load(file_path)
hop_length = 512
# compute tempo and beat frames
onset_env = librosa.onset.onset_strength(y=y, sr=sr, aggregate=np.median)
tempo, beat_frames = librosa.beat.beat_track(onset_envelope=onset_env, sr=sr)
#tempogram = librosa.feature.tempogram(onset_envelope=onset_env, sr=sr, hop_length=hop_length, win_length=400)
#print('Tempo: {:.2f}'.format(tempo)) #formatting var instead of f" and round()
activation_times = librosa.frames_to_time(beat_frames, sr=sr)

#np.savetxt('activation.csv', activation_times, delimiter=';') it converts timestamps to text... how to still create a template file?
#print(activation_times)
#print(np.shape(tempogram)) a tempogram is too complex
#with open("E:\website\output.txt", "w") as f:
#    print(activation_times, file=f)

def process_time():
    print (time.process_time())

