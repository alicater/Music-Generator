import random
from music21 import stream, note, chord


def gen_music(length):
    composition = stream.Stream()
    pitches = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
    total_duration = 0

    while total_duration < length:
        num_notes = random.randint(1,4) # determins how many notes in chord (between 1 and 4)
        chord_notes = [note.Note(random.choice(pitches)) for i in range(num_notes)] # selects pitches to create chord

        new_chord = chord.Chord(chord_notes) # creates the chord 
        
        chord_duration = random.uniform(1,4) # selects random duration for chord between 1 and 3 secs
        total_duration += chord_duration # adds to the "clock" of composition

        new_chord.quarterLength = chord_duration # sets the chord's duration
        composition.append(new_chord) # adds chord to composition

    return composition

def music_to_midi(composition, midi_file="new_composition.mid"):
    # turns composition into midi file
    midi_file = composition.write("midi", fp=midi_file)
    return midi_file


length = input("Enter the length of the composition (eg 2 minutes, or 120 seconds): ")
if 'minute' in length.lower():
    length_sec = int(length.split()[0]) * 60
elif 'second' in length.lower():
    length_sec = int(length.split()[0])
else:
    length_sec = int(length)

if length_sec <= 0:
    print("Must be longer than 0 and a positive number")
else:
    composition = gen_music(length_sec)

    midi_file_path = music_to_midi(composition)
    print(f"composition saved as a midi file as {midi_file_path}")
