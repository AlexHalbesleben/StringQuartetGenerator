import os
from midi_to_text import midi_to_text
from text_to_midi import text_to_midi


def folder_midi_to_text(input_dir: str, output_dir: str, replace_existing=False):
    """Converts all of the midi files in one folder to formatted text files in another folder.

    Args:
        input_dir (str): The folder containing the midi files to be converted
        output_dir (str): The folder in which to place the converted text files
        replace_existing (bool, optional): Whether converted files that already exist in the output folder should be converted again. Defaults to False.
    """
    already_exists = os.listdir(output_dir)
    for filename in os.listdir(input_dir):
        if not replace_existing and (filename[:-4] + ".txt") in already_exists:
            continue 
        print(f"Converting {input_dir}/{filename} to text")
        midi_to_text(f"{input_dir}/{filename}", None, f"{output_dir}/{filename[:-4]}.txt")

def folder_text_to_midi(input_dir: str, output_dir: str, replace_existing=False):
    """Converts all of the formatted text files in one folder to midi files in another folder.

    Args:
        input_dir (str): The folder containing the text files to be converted
        output_dir (str): The folder in which to place the converted midi files
        replace_existing (bool, optional): Whether converted files that already exist in the output folder should be converted again. Defaults to False.
    """
    already_exists = os.listdir(output_dir)
    for filename in os.listdir(input_dir):
        if not replace_existing and (filename[:-4] + ".mid") in already_exists:
            continue 
        print(f"Converting {input_dir}/{filename} to midi")
        text_to_midi(f"{input_dir}/{filename}", 60, f"{output_dir}/{filename[:-4]}.mid")
