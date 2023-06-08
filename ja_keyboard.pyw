import keyboard
import winTip as tt
from threading import Timer

class gv:
    running = True
    hirigana_mode = True  # Which language to translate
    katakana_mode = False  # Which language to translate
    translate_bool = True  # Whether or not to translate
    tool_tip = tt.ToolTip('')
    processed_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '/', '-', '~', '[', ']', ',', '.', 'space', 'enter', 'backspace', 'ctrl', 'shift', 'left', 'right', 'up', 'down', 'tab', 'delete']
    hooked_keys = []
    reveal_delay = 1

    switch_hotkey = 'shift+space'
    toggle_hotkey = 'ctrl+space'
    exit_hotkey = 'esc'

class const:
    TRANSLATION_DICT = {
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
        
        '<DOUBLES>': {
            'bb': ['っ', 'ッ'],
            'cc': ['っ', 'ッ'],
            'ff': ['っ', 'ッ'],
            'gg': ['っ', 'ッ'],
            'hh': ['っ', 'ッ'],
            'jj': ['っ', 'ッ'],
            'kk': ['っ', 'ッ'],
            'mm': ['っ', 'ッ'],
            'pp': ['っ', 'ッ'],
            'rr': ['っ', 'ッ'],
            'ss': ['っ', 'ッ'],
            'tt': ['っ', 'ッ'],
            'ww': ['っ', 'ッ'],
            'zz': ['っ', 'ッ'],
            'yy': ['っ', 'ッ'],
            
            'nc': ['ん', 'ン'],
            'nb': ['ん', 'ン'],
            'nf': ['ん', 'ン'],
            'ng': ['ん', 'ン'],
            'nh': ['ん', 'ン'],
            'nj': ['ん', 'ン'],
            'nk': ['ん', 'ン'],
            'nm': ['ん', 'ン'],
            'np': ['ん', 'ン'],
            'nr': ['ん', 'ン'],
            'ns': ['ん', 'ン'],
            'nt': ['ん', 'ン'],
            'nw': ['ん', 'ン'],
            'nz': ['ん', 'ン'], 
            'ny': ['ん', 'ン'],
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
            '/go-1': ['語'],
            '/sama': ['様'],
            '/ko': ['子'],
            
            
            '/manabu': ['学'],

            # Full words
            '/atarashii': ['新しい'],
            '/furui':['古い'],
            '/uta':['歌'],
            '/okiniiri':['お気に入り'],
            '/subarashii': ['素晴らしい'],
            '/nihongo': ['日本語'],
            '/daigakusei': ['大学生'],
            '/chiisai': ['小さい'],
            '/kaimasu': ['買います'],
            '/doyoubi': ['土曜日'],

            # Cities / places
            '/nihon': ['日本'],
            '/tokyo': ['東京'],
            '/kyoto': ['京都'],

            # Misc
            '/yama': ['山'],
            '/guchi': ['口'],
            '/ta': ['田'],
            '/naka': ['中'],
        },
    }


class _Helpers():
    timer_thread = None
    def add_hooks():
        for k in gv.processed_keys: keyboard.hook_key(k, callback=lambda e: _Language.process_input(e), suppress=True)
    def remove_hooks():
        keyboard._listener.start_if_necessary()
        keyboard._listener.blocking_keys.clear()
        keyboard._listener.nonblocking_keys.clear()
        del keyboard._listener.blocking_hooks[:]
        del keyboard._listener.handlers[:]
    def add_hotkeys(switch_hotkey=gv.switch_hotkey, toggle_hotkey=gv.toggle_hotkey, exit_hotkey=gv.exit_hotkey):
        gv.switch_hotkey = switch_hotkey
        gv.toggle_hotkey = toggle_hotkey
        gv.exit_hotkey = exit_hotkey
        keyboard.add_hotkey(switch_hotkey, lambda: switch()) # Trigger the hirigana/katakana switch
        keyboard.add_hotkey(toggle_hotkey, lambda: enable_disable()) # Enable/disable translation while still running the script
    def start_reveal_timer(delay):
        _Helpers.timer_thread = Timer(delay, function=lambda: _Helpers.timer_trigger(delay))
        _Helpers.timer_thread.start()
    def timer_trigger(delay): 
        for c in _Language.latin_to_type:
            keyboard.send(c, True, False)
        _Language.typed_latin += _Language.latin_to_type
        _Language.latin_to_type = ''
        

class _Language():
    active_kanji_keys = []
    kanji_index = 0
    input_modifiers = []
    sent_modified = []
    modified_index = 0
    liminal_index = 0
    liminal_keyups = []
    working_string = ''
    latin_to_type = ''
    typed_latin = ''

    def get_valid_kanji():
        _Language.reset_kanji()
        _Language.active_kanji_keys.append(_Language.working_string)
        for key in const.TRANSLATION_DICT['<KANJI>']:
            if _Language.working_string + '-' in key and key != _Language.working_string:
                _Language.active_kanji_keys.append(key)

    def cycle_valid_kanji():
        for c in range(len(const.TRANSLATION_DICT['<KANJI>'][_Language.active_kanji_keys[_Language.kanji_index]][0])):
            keyboard.send('backspace')
        try: 
            _Language.kanji_index += 1
            keyboard.write(const.TRANSLATION_DICT['<KANJI>'][_Language.active_kanji_keys[_Language.kanji_index]][0])
        except IndexError: 
            _Language.kanji_index = 0
            keyboard.write(const.TRANSLATION_DICT['<KANJI>'][_Language.active_kanji_keys[_Language.kanji_index]][0])
    
    def reset_kanji():
        _Language.active_kanji_keys = []
        _Language.kanji_index = 0

    def set_working_string(text, include_latin_str=True):
        _Language.working_string = text
        if include_latin_str == True:
            _Language.typed_latin = text
        
    def execute_translation(jp_symbols): # Execute a translation based on the translation mode
        if gv.translate_bool == True:
            if type(jp_symbols) == list:
                for c in _Language.typed_latin:
                    keyboard.send('backspace')
                _Language.typed_latin = ''
                _Language.latin_to_type = ''
                if len(jp_symbols) == 1 or gv.hirigana_mode == True: keyboard.write(jp_symbols[0])
                elif gv.katakana_mode == True: keyboard.write(jp_symbols[1])
                gv.tool_tip.destroy()
            
    
    
    def process_input(event): 
        if keyboard.is_modifier(event.name): modified_event = event.name 
        else: modified_event = ''.join(_Language.input_modifiers) + event.name 
        if event.event_type == 'down':
            if event.name != 'space':
                _Language.reset_kanji()
            elif len(_Language.active_kanji_keys) > 1 and event.name == 'space':
                _Language.cycle_valid_kanji()
                return 

            if keyboard.is_modifier(event.name):
                _Language.input_modifiers.append(event.name + '+')
                return

            elif len(event.name) == 1 and 'ctrl+' not in _Language.input_modifiers: 
                _Language.working_string += event.name
                _Language.latin_to_type += event.name

                if _Language.working_string in const.TRANSLATION_DICT.keys():
                    _Language.execute_translation(const.TRANSLATION_DICT[_Language.working_string])
                    _Language.set_working_string('', True)

                elif _Language.working_string in const.TRANSLATION_DICT['<DOUBLES>'].keys():
                    _Language.execute_translation( const.TRANSLATION_DICT['<DOUBLES>'][_Language.working_string])
                    _Language.working_string = _Language.working_string[-1]
                    _Language.latin_to_type = _Language.working_string
                    

            elif event.name == 'space' and _Language.working_string in const.TRANSLATION_DICT['<KANJI>'].keys():
                _Language.get_valid_kanji()
                _Language.execute_translation(const.TRANSLATION_DICT['<KANJI>'][_Language.working_string])
                _Language.set_working_string('', True)

            else:
                _Language.typed_latin = ''
                _Language.latin_to_type = ''
                if modified_event == gv.switch_hotkey: 
                    switch()
                elif modified_event == gv.toggle_hotkey:   
                    enable_disable()
                elif modified_event == 'enter':
                    if _Language.working_string == '': keyboard.send(modified_event, True, False)
                    else: keyboard.write(_Language.working_string) ; _Language.set_working_string('', True)
                elif modified_event == 'backspace':
                    if _Language.working_string == '': keyboard.send(modified_event)
                    else: _Language.working_string = _Language.working_string[:-1]; _Language.latin_to_type = _Language.latin_to_type[:-1]
                elif modified_event == 'space' or modified_event == 'ctrl+backspace':
                    if _Language.working_string == '': keyboard.send(modified_event)
                    else: _Language.set_working_string('', True)
                else: 
                    keyboard.send(modified_event)
            gv.tool_tip.destroy()
            gv.tool_tip = tt.ToolTip(_Language.working_string)
            
        
        elif event.event_type == 'up':
            if keyboard.is_modifier(event.name):
                try: _Language.input_modifiers.remove(modified_event + '+')
                except ValueError: _Language.input_modifiers = []
            if _Helpers.timer_thread != None and _Language.input_modifiers == []:
                _Helpers.timer_thread.cancel()
            _Helpers.start_reveal_timer(gv.reveal_delay) 


def switch():  # Switch between hirigana and katakana translation modes. 
    if gv.hirigana_mode == True: gv.hirigana_mode = False; gv.katakana_mode = True
    elif gv.katakana_mode == True: gv.katakana_mode = False; gv.hirigana_mode = True


def enable_disable():  # Enable/disable the translation function
    if gv.translate_bool == True: gv.translate_bool = False ; _Helpers.remove_hooks()
    elif gv.translate_bool == False: gv.translate_bool = True ; _Helpers.add_hooks()
    _Language.set_working_string('', True)

def start(switch_hotkey:str=gv.switch_hotkey,toggle_hotkey:str=gv.toggle_hotkey, exit_hotkey:str=gv.exit_hotkey,reveal_delay=gv.reveal_delay): 
    if reveal_delay <= .001: gv.reveal_delay = .001 
    else: gv.reveal_delay = reveal_delay
    _Helpers.add_hotkeys(switch_hotkey=switch_hotkey, toggle_hotkey=toggle_hotkey, exit_hotkey=exit_hotkey)
    _Helpers.add_hooks()
    keyboard.wait(gv.exit_hotkey)
start(reveal_delay=1)


