# String Quartet Generator
Trains a neural network to generate string quartets

## How to use
1. Train the model (or use the existing weights in `textgenrnn_weights.hdf5`). Modify the parameters in `index.py` to your liking and run the file.
2. Run `generate()` in `generate.py` to generate samples.
3. Run `folder_text_to_midi()` in `data/convert_all.py` to convert the generated text files to usable midi files.
4. Play the midi files in the program of your choice (I use MuseScore, but any similar program should work).

## How the network works
To be usable by the network, the midi files must first be converted into text. The network is trained to use the following format:
`a b c d|e f g h|i j k l`
Each beat is separated by a pipe (|). Within each beat, the notes played by each instrument are separated by spaces. So, the first violin plays `a` in the first beat, `e` in the second beat, and `i` for the third beat. The second violin plays `b`, `f`, and `j` and the viola and cello play the third and fourth notes in each beat, respectively.

Each note is represented by an ASCII character (codes 0-127). Rests are represented by a `~`. Although pipes, tildes, and spaces are in this range and could be confused for notes, all three are extremely low or extremely high notes and will most likely not be played.

The formatted text is fed to a neural network powered by `textgenrnn` (which uses TensorFlow under the hood). The neural network outputs a string of text that (ideally) has the same format. The text can be converted back to a midi file and played.

## Credits
Data comes from stringquartets.org

Inspired by [carykh](https://www.youtube.com/watch?v=SacogDL_4JU)