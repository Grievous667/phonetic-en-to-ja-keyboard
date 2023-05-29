# phonetic-en-to-jp-keyboard
Translate English/Latin syllables to equivelant Japanese Hirigana or Katakana characters


This program uses the keyboard module to identify when a typed string matches to a Japanese character based on a dictionary of corrosponding phonetic moras or syllables. When a match is identified, the typed string will be replaced with the Japanese character. E.g., typing 'ka' and pressing space while the program is running will call two backspace keystrokes and then type 'か'. The program can be switched between Hirigana and Katakana via the default hotkey 'shift+space', or can be toggled on/off entirely with 'ctrl+space'. Pressing 'esc' at any time will terminate the program. 

Note that for some duplicate phonetic equivalents, what to input for a desired output may not be perfectly intuitive. Looking through the the translation dictionary is reccommended. 

The dictionary can be easily extended for common words, and by adding keys, specific Kanji translations can be supported.
