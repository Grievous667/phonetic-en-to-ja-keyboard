# phonetic-en-to-ja-keyboard
Translate English/Latin syllables to equivalent Japanese Hiragana or Katakana characters

INSTALLATION

1. Download the repository and extract it to a unique folder.
2. Install the keyboard module. If you have pip, simply enter `pip install keyboard` into the terminal. If you need an in-depth explanation on installing python libraries, you can refer to this webpage: https://docs.python.org/3/installing/index.html
3. In the keyboard module's main folder, replace the file named `__init__.py` with the file of the same name in this repository. The file location will be relative to your Python install location, so find that and navigate as follows (keeping in mind 'Python310' will be replaced with whatever Python version you're running): `Python\Python310\Lib\site-packages\keyboard`.
4. That's the installation done. To use the script, run it with python or from the terminal.


DESCRIPTION
 
This program uses the keyboard module (with modifications) to identify when a typed string matches to a Japanese character based on a dictionary of corresponding phonetic moras or syllables. When a match is identified, the typed string will be replaced with the Japanese character. E.g., typing 'ka' while the program is running will type 'か' instead of the Latin characters. The program can be switched between Hiragana and Katakana via the default hotkey 'shift+space', or can be toggled on/off entirely with 'ctrl+space'. Pressing 'esc' at any time will terminate the program. 

Note that for some duplicate phonetic equivalents, what to input for a desired output may not be perfectly intuitive. Looking through the translation dictionary is recommended. 

Kanji translations can be supported - even multiple phonetic equivalents, if the dictionary is configured correctly. To add Kanji keys, either:

1. Manually add an entry in `ja_translation_dict.py`. Entries should be prefixed with '/', and should (but are not required to) be phonetically equivalent to the Kanji. Equivalent translations in the dictionary suffixed by '-' and any other character will be cycled through on subsequent space presses. The example format is as follows:
 KANJI_DICT: {
   '/go': ['五'],
   '/go-1': ['語'],
   }
   Typing '/go' and pressing space with this configuration will first translate, then cycle through each translation key listed. 

2. Copy the Kanji you're adding a translation for to the clipboard, then press the default hotkey 'shift+f2'. The GUI will then prompt you to add a key for the clipboard data.

Note that for both of the options listed, restarting the script is required for the new translations to be registered.

This branch suppresses physical keystrokes, and includes a GUI to display what you are currently typing. The GUI can be enabled/disabled with the default hotkey 'shift+f1'. Queued keystrokes will be sent after a configurable delay (default 10 seconds), whereafter the script will call an appropriate number of backspace keystrokes for a matched translation key.
