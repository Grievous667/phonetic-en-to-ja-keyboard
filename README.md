# phonetic-en-to-ja-keyboard
Translate English/Latin syllables to equivalent Japanese Hiragana or Katakana characters


This program uses the keyboard module (with modifications) to identify when a typed string matches to a Japanese character based on a dictionary of corresponding phonetic moras or syllables. When a match is identified, the typed string will be replaced with the Japanese character. E.g., typing 'ka' while the program is running will call two backspace keystrokes and then type 'か'. The program can be switched between Hiragana and Katakana via the default hotkey 'shift+space', or can be toggled on/off entirely with 'ctrl+space'. Pressing 'esc' at any time will terminate the program. 

Note that for some duplicate phonetic equivalents, what to input for a desired output may not be perfectly intuitive. Looking through the translation dictionary is recommended. 

Kanji translations can be supported - even multiple phonetic equivalents, if the dictionary is configured correctly. To add Kanji keys, prefix the key with '/'. Equivalent translations in the dictionary suffixed by '-' and any other character will be cycled through on subsequent space presses. E.g.:

KANJI_DICT: {
  '/go': ['五'],
  '/go-1': ['語'],
  }
  
Typing '/go' and pressing space with this configuration will first translate, then cycle through each translation key listed. 

This branch works by recording suppressed physical keystrokes, and matching the recorded bit to the translation dictionary. This means that Latin characters will not be typed at all except after a configurable delay (default 1 second - you can set it to zero if typing blind is scary), when any Latin characters left hanging will be typed for convenience/typo identification. In order to accomplish this, I had to edit the keyboard module, so for installation, replace the '__init__.py' file in the keyboard module with the one provided in this repository.
