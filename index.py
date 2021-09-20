from textgenrnn import textgenrnn
import os

textgen = textgenrnn()

texts = []
for filename in os.listdir("data/text"):
    file = open(f"data/text/{filename}")
    print(f"Reading from {filename}")
    texts.append(file.read())
    file.close()

textgen.load("textgenrnn_weights.hdf5")
textgen.train_on_texts(texts)