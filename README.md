# musiconway
The earliest version of Musiconway.
A musical cell pattern generator using librosa and pygame

Many features TBA, but for a start, this is simply a random pattern that dissipates along the tempo of your song, (which suddenly sounds more pessimistic than fun now that I think about it). Development was hindered since librosa on my Windows could not locate the path to ffmpeg binaries, even after a $PATH has been added.

The Conway code belongs to Coder Space in his Conway GOL tutorial (https://www.youtube.com/watch?v=lk1_h2_GLv8) - the cleanest Python Conway code I've seen. :)

# Controls:
- Enter file location into opening shell prompt.
- When the game window opens, press SPACE to begin.
- Press P to pause/unpause.

To-do list:

- Tidy up my conditionals (dictionaries...?)
- Change patterns depending on amplitude/energy using librosa.
- Read binary from lexicon file (I've seen a Rust parser (https://github.com/scastiel/lexicon-rs), and I'd love to try writing one in Py too)
- Write a neat music player to play along with the GOL (what else would I call the "musiconway"? It's intended to be something like a party piece.)
- A more friendly GUI
- Colors for different notes.
