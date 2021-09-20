import pretty_midi

def midi_to_text(filename: str, beats_per_minute: int or None = None, saveTo: str or None = None, beats_per_measure=4, precision=8) -> str:
    """Converts a midi file to formatted text

    Args:
        filename (str): The path to the midi file
        beats_per_minute (intorNone, optional): The tempo of the piece. If not given, estimates the tempo based on the midi file. Defaults to None.
        saveTo (strorNone, optional): The path of the file to save the text to. If not given, the text is not saved. Defaults to None.
        beats_per_measure (int, optional): The time signature of the piece. Defaults to 4.
        precision (int, optional): How precise the formatted text file should be. Defaults to 8.

    Returns:
        str: A formatted string containing the data in the midi files
    """
    midi_data = pretty_midi.PrettyMIDI(filename)

    if not beats_per_minute:
        beats_per_minute = midi_data.estimate_tempo()

    fs = precision * beats_per_measure * 60 / beats_per_minute

    first_violin_roll = midi_data.instruments[0].get_piano_roll(fs)
    second_violin_roll = midi_data.instruments[1].get_piano_roll(fs)
    viola_roll = midi_data.instruments[2].get_piano_roll(fs)
    cello_roll = midi_data.instruments[3].get_piano_roll(fs)

    combined_roll = []

    overall_length = len(midi_data.get_piano_roll(fs)[0])
    for i in range(0, 128):
        combined_roll.append([])
        for j in range(0, overall_length):
            combined_roll[i].append([])
            combined_roll[i][j] = [
                first_violin_roll[i][j] if len(first_violin_roll[i]) > j else 0,
                second_violin_roll[i][j]if len(second_violin_roll[i]) > j else 0,
                viola_roll[i][j] if len(viola_roll[i]) > j else 0,
                cello_roll[i][j] if len(cello_roll[i]) > j else 0
            ]

    beats = []
    for i in range(0, overall_length):
        beat = [[], [], [], []]

        for j in range(0, 128):
            for k in range(0, 4):
                if combined_roll[j][i][k] > 0:
                    beat[k].append(j)
        
        beats.append(beat)

    beats_as_str = "|".join([" ".join(["".join([chr(note) for note in instrument]).rjust(1, "~") for instrument in beat]) for beat in beats])

    if saveTo:
        file = open(saveTo, "w+")
        file.write(beats_as_str)
        file.close()
    
    return beats_as_str