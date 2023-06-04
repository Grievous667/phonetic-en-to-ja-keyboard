# phonetic-en-to-ja-keyboard
Translate English/Latin syllables to equivelant Japanese Hirigana or Katakana characters


This program uses the keyboard module to identify when a typed string matches to a Japanese character based on a dictionary of corrosponding phonetic moras or syllables. When a match is identified, the typed string will be replaced with the Japanese character. E.g., typing 'ka' while the program is running will call two backspace keystrokes and then type 'か'. The program can be switched between Hirigana and Katakana via the default hotkey 'shift+space', or can be toggled on/off entirely with 'ctrl+space'. Pressing 'esc' at any time will terminate the program. 

Note that for some duplicate phonetic equivalents, what to input for a desired output may not be perfectly intuitive. Looking through the the translation dictionary is reccommended. 

The dictionary can be easily extended for common words, and by adding keys, specific Kanji translations can be supported.

This branch does away with the word listeners and instead keeps track of a working string according to what is typed. This has the advantage of translating immediately after a mora is matched. Kanji is still supported with mostly the same process as the original branch. 

There is an issue where very quick or simultaneous inputs are not processed correctly, which I tried to alleviate a bit by using time's sleep function, so there is another import. This band-aid is mostly optional, as this issue isn't really present when typing normally, but holding down keys, for example, fails to translate properly. 
