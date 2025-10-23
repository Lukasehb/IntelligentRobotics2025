#include "pitches.h"

// Imperial March melody:
int DarthVader[] = {
  NOTE_A4, NOTE_A4, NOTE_A4, NOTE_F4, NOTE_C5,
  NOTE_A4, NOTE_F4, NOTE_C5, NOTE_A4,
  NOTE_E5, NOTE_E5, NOTE_E5, NOTE_F5, NOTE_C5,
  NOTE_GS4, NOTE_F4, NOTE_C5, NOTE_A4
};

// Note durations: 4 = quarter note, 8 = eighth note, etc.
// A 2 = half note.
int noteDurations_DarthVader[] = {
  4, 4, 4, 8, 8,
  4, 8, 8, 2,
  4, 4, 4, 8, 8,
  4, 8, 8, 2
};

void playSequence(int melody[], int noteDurations[]) {
  // Calculate the number of notes
  for (int thisNote = 0; thisNote < 25; thisNote++) {

    // to calculate the note duration, take one second
    // divided by the note type.
    //e.g. quarter note = 1000 / 4, eighth note = 1000/8, etc.
    int noteDuration = 1000 / noteDurations[thisNote];
    tone(BDPIN_BUZZER, melody[thisNote], noteDuration);

    // to distinguish the notes, set a minimum time between them.
    // the note's duration + 30% seems to work well:
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    // stop the tone playing:
    noTone(BDPIN_BUZZER);
  }
}
