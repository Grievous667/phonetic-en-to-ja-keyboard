import keyboard
import time


class var:
    hirigana_mode = True  # Which language to translate
    katakana_mode = False  # Which language to translate
    translate_bool = True  # Whether or not to translate
    keystroke_queue = []
    working_string = ''

    translation_dict = {
        # Monographs 
        'a': ['あ', 'ア'],
        'i': ['い', 'イ'],
        'u': ['う', 'ウ'],
        'e': ['え', 'エ'],
        'o': ['お', 'オ'],
        'ka': ['か', 'カ'],
        'ki': ['き', 'キ'],
        'ku': ['く', 'ク'],
        'ke': ['け', 'ケ'],
        'ko': ['こ', 'コ'],
        'sa': ['さ', 'サ'],
        'si': ['し', 'シ'],
        'shi': ['し', 'シ'],
        'su': ['す', 'ス'],
        'se': ['せ', 'セ'],
        'so': ['そ', 'ソ'],
        'ta': ['た', 'タ'],
        'ti': ['ち', 'チ'],
        'chi': ['ち', 'チ'],
        'tu': ['つ', 'ツ'],
        'tsu': ['つ', 'ツ'],
        'te': ['て', 'テ'],
        'to': ['と', 'ト'],
        'na': ['な', 'ナ'],
        'ni': ['に', 'ニ'],
        'nu': ['ぬ', 'ヌ'],
        'ne': ['ね', 'ネ'],
        'no': ['の', 'ノ'],
        'ha': ['は', 'ハ'],
        'hi': ['ひ', 'ヒ'],
        'hu': ['ふ', 'フ'],
        'fu': ['ふ', 'フ'],
        'he': ['へ', 'ヘ'],
        'ho': ['ほ', 'ホ'],
        'ma': ['ま', 'マ'],
        'mi': ['み', 'ミ'],
        'mu': ['む', 'ム'],
        'me': ['め', 'メ'],
        'mo': ['も', 'モ'],
        'ya': ['や', 'ヤ'],
        'yu': ['ゆ', 'ユ'],
        'yo': ['よ', 'ヨ'],
        'ra': ['ら', 'ラ'],
        'ri': ['り', 'リ'],
        'ru': ['る', 'ル'],
        're': ['れ', 'レ'],
        'ro': ['ろ', 'ロ'],
        'wa': ['わ', 'ワ'],
        'wi': ['ゐ', 'ヰ'],
        'we': ['ゑ', 'ヱ'],
        'wo': ['を', 'ヲ'],
        'nn': ['ん', 'ン'],
        
        # Monographs with diacratics
        'ga': ['が', 'ガ'],
        'gi': ['ぎ', 'ギ'],
        'gu': ['ぐ', 'グ'],
        'ge': ['げ', 'ゲ'],
        'go': ['ご', 'ゴ'],
        'za': ['ざ', 'ザ'],
        'zi': ['じ', 'ジ'],
        'zu': ['ず', 'ズ'],
        'ze': ['ぜ', 'ゼ'],
        'zo': ['ぞ', 'ゾ'],
        'da': ['だ', 'ダ'],
        'di': ['ぢ', 'ヂ'],
        'dji': ['ぢ', 'ヂ'],
        'ji': ['じ', 'ジ'],
        'du': ['づ', 'ヅ'],
        'dzu': ['づ', 'ヅ'],
        'de': ['で', 'デ'],
        'do': ['ど', 'ド'],
        'ba': ['ば', 'バ'],
        'bi': ['び', 'ビ'],
        'bu': ['ぶ', 'ブ'],
        'be': ['べ', 'ベ'],
        'bo': ['ぼ', 'ボ'],
        'pa': ['ぱ', 'パ'],
        'pi': ['ぴ', 'ピ'],
        'pu': ['ぷ', 'プ'],
        'pe': ['ぺ', 'ペ'],
        'po': ['ぽ', 'ポ'],
        
        # Digraphs
        'kya': ['きゃ', 'キャ'],
        'kyu': ['きゅ', 'キュ'],
        'kyo': ['きょ', 'キョ'],
        'sha': ['しゃ', 'シャ'],
        'shu': ['しゅ', 'シュ'],
        'sho': ['しょ', 'ショ'],
        'cha': ['ちゃ', 'チャ'],
        'chu': ['ちゅ', 'チュ'],
        'cho': ['ちょ', 'チョ'],
        'nya': ['にゃ', 'ニャ'],
        'nyu': ['にゅ', 'ニュ'],
        'nyo': ['にょ', 'ニョ'],
        'hya': ['ひゃ', 'ヒャ'],
        'hyu': ['ひゅ', 'ヒュ'],
        'hyo': ['ひょ', 'ヒョ'],
        'mya': ['みゃ', 'ミャ'],
        'myu': ['みゅ', 'ミュ'],
        'myo': ['みょ', 'ミョ'],
        'rya': ['りゃ', 'リャ'],
        'ryu': ['りゅ', 'リュ'],
        'ryo': ['りょ', 'リョ'],
        
        # Digraphs with diacratics
        'gya': ['ぎゃ', 'ギャ'],
        'gyu': ['ぎゅ', 'ギュ'],
        'gyo': ['ぎょ', 'ギョ'],
        'shya': ['じゃ', 'ジャ'],
        'shyu': ['じゅ', 'ジュ'],
        'shyo': ['じょ', 'ジョ'],
        'chya': ['ぢゃ', 'ヂャ'],
        'chyu': ['ぢゅ', 'ヂュ'],
        'chyo': ['ぢょ', 'ヂョ'],
        'ja': ['じゃ', 'ジャ'],
        'ju': ['じゅ', 'ジュ'],
        'jo': ['じょ', 'ジョ'],
        'bya': ['びゃ', 'ビャ'],
        'byu': ['びゅ', 'ビュ'],
        'byo': ['びょ', 'ビョ'],
        'pya': ['ぴゃ', 'ピャ'],
        'pyu': ['ぴゅ', 'ピュ'],
        'pyo': ['ぴょ', 'ピョ'],
        
        # Punctuation
        '.': ['。', '。'],
        ',': ['、', '、'],
        '-': ['ー', 'ー'],
        '[': ['「', '「'],
        ']': ['」', '」'],
        '[]': ['「」'],

        # Diacratic symbols (yoon)
        '~ya': ['ゃ', 'ャ'],
        '~yu': ['ゅ', 'ュ'],
        '~yo': ['ょ', 'ョ'],
        '~': ['っ', 'ッ'],
        
        '<DOUBLE_CONSONANTS>': {
            'bb': ['っb', 'ッb'],
            'cc': ['っc', 'ッc'],
            'ff': ['っf', 'ッf'],
            'gg': ['っg', 'ッg'],
            'hh': ['っh', 'ッh'],
            'jj': ['っj', 'ッj'],
            'kk': ['っk', 'ッk'],
            'mm': ['っm', 'ッm'],
            'pp': ['っp', 'ッp'],
            'rr': ['っr', 'ッr'],
            'ss': ['っs', 'ッs'],
            'tt': ['っt', 'ッt'],
            'ww': ['っw', 'ッw'],
            'yy': ['っy', 'ッy'],
            'zz': ['っz', 'ッz'],
        },
        '<KANJI>': { # Kanji
            # Numbers
            '/ichi': ['一'],
            '/ni': ['二'],
            '/san': ['三'],
            '/yon': ['四'],
            '/go': ['五'],
            '/roku': ['六'],
            '/nana': ['七'], '/shichi': ['七'], 
            '/hachi': ['八'],
            '/ku': ['九'], '/kyu': ['九'],
            '/juu': ['十'],

            '/han': ['半'],
            '/hyaku': ['百'],
            '/sen': ['千'],
            
            # Common 
            '/hito': ['人'],
            '/ten': ['天'],
            '/dai': ['大'], '/oo': ['大'],
            '/hon': ['本'],
            '/sai': ['才'],
            '/chii': ['小'],
            '/watashi': ['私'],
            '/imouto': ['妹'],
            '/haha': ['母'],
            '/chichi': ['父'],
            '/mi': ['見'],
            '/ai': ['愛'],
            '/toshi': ['歳'],
            '/yo': ['読'], '/satoru': ['読'],    
            '/ji': ['時'], '/toki': ['時'],
            '//go': ['語'],
            
            '/manabu': ['学'],

            # Full words
            '/atarashi': ['新しい'],
            '/furui':['古い'],
            '/uta':['歌'],
            '/okiniiri':['お気に入り'],
            '/subarashii': ['素晴らしい'],
            '/nihongo': ['日本語'],

            # Cities / places
            '/nihon': ['日本'],
            '/tokyo': ['東京'],
            '/kyoto': ['京都'],

            # Misc
            '/yama': ['山'],
            '/guchi': ['口'],
        },
    }

def execute_queue(): # Perform queued keystrokes
    time.sleep(.005)
    for key in var.keystroke_queue:
        if key == 'backspace' or key == 'space': keyboard.send(key)
        else: keyboard.write(key)
    var.keystroke_queue = []

def analyze(wking_string, key_event):
    if wking_string in var.translation_dict.keys():
        mora_to_jp_character(wking_string, var.translation_dict[wking_string])
        return ''
    elif wking_string in var.translation_dict['<DOUBLE_CONSONANTS>'].keys():
        mora_to_jp_character(wking_string, var.translation_dict['<DOUBLE_CONSONANTS>'][wking_string])
        return wking_string[-1]
    elif wking_string in var.translation_dict['<KANJI>'].keys():
        if key_event == 'space':
            var.keystroke_queue.append('backspace')
            mora_to_jp_character(wking_string, var.translation_dict['<KANJI>'][wking_string])
            return ''
        else: return wking_string
    elif wking_string != '' and key_event == 'space': var.keystroke_queue.append('backspace'); execute_queue(); return ''
    else: return wking_string

def mora_to_jp_character(mora, jp_symbols): # Given a mora and its translation, add the appropriate actions to the queue.
    if var.translate_bool == True:
        if type(jp_symbols) == list:
            for i in range(len(mora)): var.keystroke_queue.append('backspace')
            if len(jp_symbols) == 1 or var.hirigana_mode == True: var.keystroke_queue.append(jp_symbols[0])
            elif var.katakana_mode == True: var.keystroke_queue.append(jp_symbols[1])
        execute_queue()
        

def switch():  # Switch between hirigana and katakana translation modes. 
    if var.hirigana_mode == True: var.hirigana_mode = False; var.katakana_mode = True
    elif var.katakana_mode == True: var.katakana_mode = False; var.hirigana_mode = True
    keyboard.call_later(lambda: keyboard.send('backspace'),delay=.01)

def enable_disable():  # Enable/disable the translation function
    if var.translate_bool == True: var.translate_bool = False
    elif var.translate_bool == False: var.translate_bool = True
    var.working_string = ''
    var.keystroke_queue = []

def run(switch_hotkey:str='shift+space',enable_disable_hotkey:str='ctrl+space'): 
    var.working_string = ''
    keyboard.add_hotkey(switch_hotkey, lambda: switch()) # Trigger the hirigana/katakana switch
    keyboard.add_hotkey(enable_disable_hotkey, lambda: enable_disable()) # Enable/disable translation while still running the script
    mainloop()

def mainloop():
    while True:
        key_event = keyboard.read_event()
        if key_event.event_type == 'down':
            if key_event.name == 'esc': break
            if var.translate_bool == True and keyboard.is_pressed('ctrl') == False:
                if len(key_event.name) == 1:
                    var.working_string += key_event.name
                    var.working_string = analyze(var.working_string, key_event)
                elif key_event.name == 'backspace': var.working_string = var.working_string[:-1]
                elif key_event.name == 'space': analyze(var.working_string, key_event.name); var.working_string = ''
                else: var.working_string = ''
run()
