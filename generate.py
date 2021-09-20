from textgenrnn import textgenrnn
textgen = textgenrnn()

def generate(model_weights_path: str, output_dir: str, model_name: str, n=5, temperature=[2, 1.5, 1.0, 0.5]):
    """Generates samples given the weights of a neural network

    Args:
        model_weights_path (str): The path to the .hdf5 file containing the weights of the neural
        output_dir (str): The folder in which to place the outputted samples
        model_name (str): The prefix of each sample file
        n (int, optional): How many samples to generate. Defaults to 5.
        temperature (list, optional): How closely the samples should mirror the inputs. Raising this value gives more creative and chaotic music. Defaults to [2, 1.5, 1.0, 0.5].
    """
    textgen.load(model_weights_path)
    samples = textgen.generate(n=n, return_as_list=True, temperature=temperature)

    for i, sample in enumerate(samples):
        file = open(f"{output_dir}/{model_name}_{i + 1}.txt", "w+")
        file.write(sample)
        file.close()
