import keyboard


class var:
    hirigana_mode = True  # Which language to translate
    katakana_mode = False  # Which language to translate
    translate_bool = True  # Whether or not to translate

    hirigana_dict = {
        # Monographs
        'a': 'あ',
        'i': 'い',
        'u': 'う',
        'e': 'え',
        'o': 'お',
        'ka': 'か',
        'ki': 'き',
        'ku': 'く',
        'ke': 'け',
        'ko': 'こ',
        'sa': 'さ',
        'si': 'し',
        'shi': 'し',
        'su': 'す',
        'se': 'せ',
        'so': 'そ',
        'ta': 'た',
        'ti': 'ち',
        'chi': 'ち',
        'tu': 'つ',
        'tsu': 'つ',
        'te': 'て',
        'to': 'と',
        'na': 'な',
        'ni': 'に',
        'nu': 'ぬ',
        'ne': 'ね',
        'no': 'の',
        'ha': 'は',
        'hi': 'ひ',
        'hu': 'ふ',
        'fu': 'ふ',
        'he': 'へ',
        'ho': 'ほ',
        'ma': 'ま',
        'mi': 'み',
        'mu': 'む',
        'me': 'め',
        'mo': 'も',
        'ya': 'や',
        'yu': 'ゆ',
        'yo': 'よ',
        'ra': 'ら',
        'ri': 'り',
        'ru': 'る',
        're': 'れ',
        'ro': 'ろ',
        'wa': 'わ',
        'wi': 'ゐ',
        'we': 'ゑ',
        'wo': 'を',
        'n': 'ん',

        # Monographs with Diacratics
        'ga': 'が',
        'gi': 'ぎ',
        'gu': 'ぐ',
        'ge': 'げ',
        'go': 'ご',
        'za': 'ざ',
        'zi': 'じ',
        'zu': 'ず',
        'ze': 'ぜ',
        'zo': 'ぞ',
        'da': 'だ',
        'di': 'ぢ',
        'ji': 'じ',
        'Ji': 'ぢ',
        'du': 'づ',
        'zu': 'づ',
        'de': 'で',
        'do': 'ど',
        'ba': 'ば',
        'bi': 'び',
        'bu': 'ぶ',
        'be': 'べ',
        'bo': 'ぼ',
        'pa': 'ぱ',
        'pi': 'ぴ',
        'pu': 'ぷ',
        'pe': 'ぺ',
        'po': 'ぽ',

        # Digraphs
        'kya': 'きゃ',
        'kyu': 'きゅ',
        'kyo': 'きょ',
        'sha': 'しゃ',
        'shu': 'しゅ',
        'sho': 'しょ',
        'cha': 'ちゃ',
        'chu': 'ちゅ',
        'cho': 'ちょ',
        'nya': 'にゃ',
        'nyu': 'にゅ',
        'nyo': 'にょ',
        'hya': 'ひゃ',
        'hyu': 'ひゅ',
        'hyo': 'ひょ',
        'mya': 'みゃ',
        'myu': 'みゅ',
        'myo': 'みょ',
        'rya': 'りゃ',
        'ryu': 'りゅ',
        'ryo': 'りょ',
        'gya': 'ぎゃ',

        # Digraphs with Diacratics
        'gyu': 'ぎゅ',
        'gyo': 'ぎょ',
        'shya': 'じゃ',
        'shyu': 'じゅ',
        'shyo': 'じょ',
        'chya': 'ぢゃ',
        'chyu': 'ぢゅ',
        'chyo': 'ぢょ',
        'ja': 'じゃ',
        'ju': 'じゅ',
        'jo': 'じょ',
        'Ja': 'ぢゃ',
        'Ju': 'ぢゅ',
        'Jo': 'ぢょ',
        'bya': 'びゃ',
        'byu': 'びゅ',
        'byo': 'びょ',
        'pya': 'ぴゃ',
        'pyu': 'ぴゅ',
        'pyo': 'ぴょ',

        # Punctuation
        '.': '。',
        ',': '、',
        '-': 'ー',

        # Diacratic Marks
        '~ya': 'ゃ',
        '~yu': 'ゅ',
        '~yo': 'ょ',
        'yA': 'ゃ',
        'yU': 'ゅ',
        'yO': 'ょ',

        # Common words
        'Wa': 'は',
        'desu': 'です',
        'hai': 'はい',
        'iie': 'いいえ',
        'nani': 'なに',
        'koko': 'ここ',
        'soko': 'そこ',
        'doko': 'どこ',
        'sore': 'それ',
        'kore': 'これ',
        'sono': 'その',
        'kono': 'この',
        'san': 'さん',
        'kun': 'くん',

    }

    katakana_dict = {
        # Monographs
        'a': 'ア',
        'i': 'イ',
        'u': 'ウ',
        'e': 'エ',
        'o': 'オ',
        'ka': 'カ',
        'ki': 'キ',
        'ku': 'ク',
        'ke': 'ケ',
        'ko': 'コ',
        'sa': 'サ',
        'si': 'シ',
        'shi': 'シ',
        'su': 'ス',
        'se': 'セ',
        'so': 'ソ',
        'ta': 'タ',
        'ti': 'チ',
        'chi': 'チ',
        'tu': 'ツ',
        'tsu': 'ツ',
        'te': 'テ',
        'to': 'ト',
        'na': 'ナ',
        'ni': 'ニ',
        'nu': 'ヌ',
        'ne': 'ネ',
        'no': 'ノ',
        'ha': 'ハ',
        'hi': 'ヒ',
        'hu': 'フ',
        'fu': 'フ',
        'he': 'ヘ',
        'ho': 'ホ',
        'ma': 'マ',
        'mi': 'ミ',
        'mu': 'ム',
        'me': 'メ',
        'mo': 'モ',
        'ya': 'ヤ',
        'yu': 'ユ',
        'yo': 'ヨ',
        'ra': 'ラ',
        'ri': 'リ',
        'ru': 'ル',
        're': 'レ',
        'ro': 'ロ',
        'wa': 'ワ',
        'wi': 'ヰ',
        'we': 'ヱ',
        'wo': 'ヲ',
        'n': 'ン',

        # Monographs with Diacratics
        'ga': 'ガ',
        'gi': 'ギ',
        'gu': 'グ',
        'ge': 'ゲ',
        'go': 'ゴ',
        'za': 'ザ',
        'zi': 'ジ',
        'zu': 'ズ',
        'ze': 'ゼ',
        'zo': 'ゾ',
        'da': 'ダ',
        'di': 'ヂ',
        'ji': 'ジ',
        'Ji': 'ヂ',
        'du': 'ヅ',
        'zu': 'ヅ',
        'de': 'デ',
        'do': 'ド',
        'ba': 'バ',
        'bi': 'ビ',
        'bu': 'ブ',
        'be': 'ベ',
        'bo': 'ボ',
        'pa': 'パ',
        'pi': 'ピ',
        'pu': 'プ',
        'pe': 'ペ',
        'po': 'ポ',

        # Digraphs
        'kya': 'キャ',
        'kyu': 'キュ',
        'kyo': 'キョ',
        'sha': 'シャ',
        'shu': 'シュ',
        'sho': 'ショ',
        'cha': 'チャ',
        'chu': 'チュ',
        'cho': 'チョ',
        'nya': 'ニャ',
        'nyu': 'ニュ',
        'nyo': 'ニョ',
        'hya': 'ヒャ',
        'hyu': 'ヒュ',
        'hyo': 'ヒョ',
        'mya': 'ミャ',
        'myu': 'ミュ',
        'myo': 'ミョ',
        'rya': 'リャ',
        'ryu': 'リュ',
        'ryo': 'リョ',

        # Digraphs with Diacratics
        'gya': 'ギャ',
        'gyu': 'ギュ',
        'gyo': 'ギョ',
        'shya': 'ジャ',
        'shyu': 'ジュ',
        'shyo': 'ジョ',
        'chya': 'ヂャ',
        'chyu': 'ヂュ',
        'chyo': 'ヂョ',
        'ja': 'ジャ',
        'ju': 'ジュ',
        'jo': 'ジョ',
        'Ja': 'ヂャ',
        'Ju': 'ヂュ',
        'Jo': 'ヂョ',
        'bya': 'ビャ',
        'byu': 'ビュ',
        'byo': 'ビョ',
        'pya': 'ピャ',
        'pyu': 'ピュ',
        'pyo': 'ピョ',

        # Punctuation
        '.': '。',
        ',': '、',
        '-': 'ー',

        # Diacratic Marks
        '~ya': 'ャ',
        '~yu': 'ュ',
        '~yo': 'ョ',
        'yA': 'ャ',
        'yU': 'ュ',
        'yO': 'ョ',
    }


# Generate Local Functions
hirigana = [(i, "lambda: mora_to_jp_character('" + i + "', '" + var.hirigana_dict[i] + "')") for i in var.hirigana_dict]
katakana = [(i, "lambda: mora_to_jp_character('" + i + "', '" + var.katakana_dict[i] + "')") for i in var.katakana_dict]



def mora_to_jp_character(mora, jp_character): # Given a mora and its translation, delete the mora characters and add the translation
    for i in range(len(mora)+1):
        keyboard.send('backspace')
    keyboard.write(jp_character)


def switch():  # Switch between hirigana and katakana translation modes. KeyError is ignored because the listener dictionary can be emptied by the enable/disable function
    if var.hirigana_mode == True:
        try:
            var.hirigana_mode = False
            var.katakana_mode = True
            for i in hirigana:
                keyboard.remove_word_listener(i[0])
            for i in katakana:
                keyboard.add_word_listener(i[0], eval(i[1]))
        except KeyError:
            pass
    elif var.katakana_mode == True:
        try:
            var.katakana_mode = False
            var.hirigana_mode = True
            for i in katakana:
                keyboard.remove_word_listener(i[0])
            for i in hirigana:
                keyboard.add_word_listener(i[0], eval(i[1]))
        except KeyError:
            pass
    keyboard.send('backspace')


def enable_disable():  # Enable/disable the translation function by emptying the listener dictionaties
    if var.translate_bool == True:
        try:
            var.translate_bool = False
            if var.hirigana_mode == True:
                for i in hirigana:
                    keyboard.remove_word_listener(i[0])
            elif var.katakana_mode == True:
                for i in katakana:
                    keyboard.remove_word_listener(i[0])
            return
        except KeyError:
            pass
    elif var.translate_bool == False:
        try:
            var.translate_bool = True
            if var.hirigana_mode == True:
                for i in hirigana:
                    keyboard.add_word_listener(i[0], eval(i[1]))
            elif var.katakana_mode == True:
                for i in katakana:
                    keyboard.add_word_listener(i[0], eval(i[1]))
            return
        except KeyError:
            pass


if var.translate_bool == True:
    for i in hirigana:  # Initial listener dictionary
        keyboard.add_word_listener(i[0], eval(i[1]))
keyboard.add_hotkey(  # Trigger the hirigana/katakana switch
    'shift+space', lambda: switch())
keyboard.add_hotkey(  # Enable/disable translation while still running the script
    'ctrl+space', lambda: enable_disable())
keyboard.wait('esc')  # Receiving this input ends the program
