from midiutil import MIDIFile


notes = [60, 62, 64, 65, 67, 69, 71, 72]
track = 0
channel = 0
time = 0
duration = 1
tempo = 60 #beats per minute
volume = 100 #0-127

myMIDI = MIDIFile(1)
myMIDI.addTempo(track,time,tempo)
i=0
while i <len(notes):
    myMIDI.addNote(track,channel, notes[i], time, duration, volume)
    time += duration
    i += 1 

with open("myMIDINotes.mid","wb") as out_file:
    myMIDI.writeFile(out_file)