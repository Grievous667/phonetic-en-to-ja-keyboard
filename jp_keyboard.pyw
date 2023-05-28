import keyboard


class var:
    hirigana_mode = True  # Which language to translate
    katakana_mode = False  # Which language to translate
    translate_bool = True  # Whether or not to translate

    translation_dict = {
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
        'n': ['ん', 'ン'],
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
        'ji': ['じ', 'ジ'],
        'Ji': ['ぢ', 'ヂ'],
        'du': ['づ', 'ヅ'],
        'tzu': ['づ', 'ヅ'],
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
        '[]': ['「」', '「」'],
        '[': ['「', '「'],
        ']': ['」', '」'],

        # Diacratic symbols
        '~ya': ['ゃ', 'ャ'],
        '~yu': ['ゅ', 'ュ'],
        '~yo': ['ょ', 'ョ'],
        '~': ['っ', 'ッ'],

        # Common words (over 2 character)
        'iie': ['いいえ'],
        
        # Kanji
        # Numbers
        '/ichi': ['一'],
        '/ni': ['二'],
        '/san': ['三'],
        '/yon': ['四'],
        '/go': ['五'],
        '/roku': ['六'],
        '/nana': ['七'], '/shichi': ['七'], 

        # Common 
        '/ai': ['愛'],
        '/hito': ['人'],
        '/hon': ['本'],
        '/watashi': ['私'],
        '/imouto': ['妹'],
        '/haha': ['母'],
        '/chichi': ['父'],
        '/mi': ['見'],
        '/yo': ['読'], '/satoru': ['読'],    
        '/ji': ['時'], '/toki': ['時'],

        # Cities
        '/nihon': ['日本'],
        '/tokyo': ['東京'],
        '/kyoto': ['京都'],

        # Misc
        '/yama': ['山'],
        '/guchi': ['口'],
    }





# Add combo translations to the main set of word listeners
combo_translations = {i + a: [var.translation_dict[i][0] + var.translation_dict[a][0], var.translation_dict[i][1] + var.translation_dict[a][1]] for i in var.translation_dict if len(var.translation_dict[i]) > 1 for a in var.translation_dict if len(var.translation_dict[a]) > 1}
var.translation_dict = dict(combo_translations, **var.translation_dict)
# Generate Local Functions
translations = [(i, "lambda: mora_to_jp_character('" + i + "', " + str(var.translation_dict[i]) + ")") for i in var.translation_dict]

# Given a mora and its translation, delete the mora characters and add the translation
def mora_to_jp_character(mora, jp_symbols):
    if var.translate_bool == True:
        for i in range(len(mora)+1): keyboard.send('backspace')
        if len(jp_symbols) == 1: keyboard.write(jp_symbols[0])
        elif var.hirigana_mode == True: keyboard.write(jp_symbols[0])
        elif var.katakana_mode == True: keyboard.write(jp_symbols[1])

def switch():  # Switch between hirigana and katakana translation modes. 
    if var.hirigana_mode == True:
        var.hirigana_mode = False
        var.katakana_mode = True
    elif var.katakana_mode == True:
        var.katakana_mode = False
        var.hirigana_mode = True
    keyboard.call_later(lambda: keyboard.send('backspace'),delay=.01)
    

def enable_disable():  # Enable/disable the translation function by emptying the listener dictionaties
    if var.translate_bool == True:
        var.translate_bool = False
    elif var.translate_bool == False: 
        var.translate_bool = True
            

if var.translate_bool == True:
    for i in translations:  # Initialize the listener dictionary
        keyboard.add_word_listener(i[0], eval(i[1]))
keyboard.add_hotkey(  # Trigger the hirigana/katakana switch
    'shift+space', lambda: switch())
keyboard.add_hotkey(  # Enable/disable translation while still running the script
    'ctrl+space', lambda: enable_disable())
keyboard.wait('esc')  # Receiving this input ends the program 
