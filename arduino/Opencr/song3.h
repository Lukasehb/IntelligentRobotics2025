#include "pitches.h"

// Imperial March melody:
int melody[] = {
  NOTE_A4, NOTE_A4, NOTE_A4, NOTE_F4, NOTE_C5,
  NOTE_A4, NOTE_F4, NOTE_C5, NOTE_A4,
  NOTE_E5, NOTE_E5, NOTE_E5, NOTE_F5, NOTE_C5,
  NOTE_GS4, NOTE_F4, NOTE_C5, NOTE_A4
};

// Note durations: 4 = quarter note, 8 = eighth note, etc.
// A 2 = half note.
int noteDurations[] = {
  4, 4, 4, 8, 8,
  4, 8, 8, 2,
  4, 4, 4, 8, 8,
  4, 8, 8, 2
};

void setup() {
  // Calculate the number of notes
  int melodySize = sizeof(melody) / sizeof(melody[0]);

  for (int thisNote = 0; thisNote < melodySize; thisNote++) {
    // Determine the note duration
    int noteDuration = 1000 / noteDurations[thisNote];
    
    tone(BDPIN_BUZZER, melody[thisNote], noteDuration);

    // Pause between notes
    int pauseBetweenNotes = noteDuration * 1.30;
    delay(pauseBetweenNotes);
    
    // Stop the tone
    noTone(BDPIN_BUZZER);
  }
}

void loop() {
  // No repeat
}