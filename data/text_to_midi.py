import pretty_midi

def text_to_midi(filename: str, beats_per_minute: int, saveTo: str or None = None, beats_per_measure=4, precision=8) -> pretty_midi.PrettyMIDI:
    """Converts a text file to a midi file

    Args:
        filename (str): The path to the text file
        beats_per_minute (int): The tempo of the piece
        saveTo (strorNone, optional): The path of the midi file to save to. If not given, the data is not saved. Defaults to None.
        beats_per_measure (int, optional): The time signature of the piece. Defaults to 4.
        precision (int, optional): The precision of the formatted text file. Defaults to 8.

    Returns:
        pretty_midi.PrettyMIDI: A midi object representing the music in the text file
    """
    file = open(filename)
    text = file.read()
    file.close()

    # Add an empty measure so the loop works correctly
    beats = ["~ ~ ~ ~"] + text.split("|") + ["~ ~ ~ ~"]
    time_increment = beats_per_minute / (60 * precision * beats_per_measure)

    mid = pretty_midi.PrettyMIDI(initial_tempo=beats_per_minute)
    mid.instruments.append(pretty_midi.Instrument(40, name="First Violin"))
    mid.instruments.append(pretty_midi.Instrument(40, name="Second Violin"))
    mid.instruments.append(pretty_midi.Instrument(41, name="Viola"))
    mid.instruments.append(pretty_midi.Instrument(42, name="Cello"))

    for b in range(1, len(beats)):
        prev_beat = beats[b - 1]
        beat = beats[b]

        instrs = beat.split(" ") # The notes each instrument plays are separated by spaces
        prev_instrs = prev_beat.split(" ")

        print(instrs)

        for i in range(0, 4):
            # If the file is formatted incorrectly
            if len(prev_instrs) <= i:
                prev_instrs.append("~")
            
            if len(instrs) <= i:
                instrs.append("~")


            instr = instrs[i]
            prev_instr = prev_instrs[i]

            # Notes that appeared in the current beat but not the previous one
            new_notes = [n for n in instr if not n in prev_instr]
            # Notes that appeared in the previous beat but not the current one
            old_notes = [n for n in prev_instr if not n in instr]

            for n in new_notes:
                # If the note is a rest or an invalid character
                if n == "~" or ord(n) > 127:
                    continue
                mid.instruments[i].notes.append(pretty_midi.Note(127, ord(n), b * time_increment, b * time_increment))
            
            for n in old_notes:
                if n == "~" or ord(n) > 127:
                    continue
                possible_notes: list[pretty_midi.Note] = mid.instruments[i].notes
                possible_notes = [note for note in possible_notes if note.start == note.end and note.pitch == ord(n)]
                if len(possible_notes) > 0:
                    possible_notes[0].end = b * time_increment


    if saveTo:
        mid.write(saveTo)

    return mid