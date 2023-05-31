import keyboard

class var:
    translate_bool = True  # Whether or not to translate
    translation_dict = {
        '/a': ['á'],
        '/e': ['é'],
        '/i': ['í'],
        '/n': ['ñ'],
        '/o': ['ó'],
        '/u': ['ú'],
        '//u': ['ü'],
        '/A': ['Á'],
        '/E': ['É'],
        '/I': ['Í'],
        '/N': ['Ñ'],
        '/O': ['Ó'],
        '/U': ['Ú'],
        '//U': ['Ü'],
        '/?': ['¿'],
        '/!': ['¡'],
        '/<': ['«'],
        '/>': ['»'],
    }

def generate_local_functions(): # Generate Local Functions
    return [(i, "lambda: key_to_es_character('" + i + "', " + str(var.translation_dict[i]) + ")") for i in var.translation_dict]

def key_to_es_character(key, es_symbols): # Given a key and its translation, delete the key characters and add the translation
    if var.translate_bool == True:
        for i in range(len(key)+1): keyboard.send('backspace')
        if len(es_symbols) == 1: keyboard.write(es_symbols[0])
        elif var.hirigana_mode == True: keyboard.write(es_symbols[0])
        elif var.katakana_mode == True: keyboard.write(es_symbols[1])
    
def enable_disable():  # Enable/disable the translation function
    if var.translate_bool == True: var.translate_bool = False
    elif var.translate_bool == False: var.translate_bool = True
        
def run():
    translations = generate_local_functions()
    for i in translations: keyboard.add_word_listener(i[0], eval(i[1]), timeout=10, allow_backspace=True, match_suffix=True) # Initialize the listener dictionary
    keyboard.add_hotkey('shift+space', lambda: enable_disable()) # Enable/disable translation while still running the script
    keyboard.wait('esc') # Receiving this input ends the program 
    exit()

run()

