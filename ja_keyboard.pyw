import keyboard
from threading import Timer

class gv:
    running = True
    hirigana_mode = True  # Which language to translate
    katakana_mode = False  # Which language to translate
    translate_bool = True  # Whether or not to translate
    processed_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '/', '-', '~', '[', ']', ',', '.', 'space', 'shift', 'ctrl', 'alt', 'enter', 'backspace', 'left', 'right', 'up', 'down', 'tab', 'delete']
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
        '~a': ['ァ'],
        '~i': ['ィ'],
        '~u': ['ゥ'],
        '~e': ['ェ'],
        '~o': ['ォ'],
        
        '~~': ['っ', 'ッ'],
        
        '<DOUBLES>': {
            'bb': ['っ', 'ッ'],
            'cc': ['っ', 'ッ'],
            'dd': ['っ', 'ッ'],
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
            
            'nb': ['ん', 'ン'],
            'nc': ['ん', 'ン'],
            'nd': ['ん', 'ン'],
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
        keyboard.add_hotkey(switch_hotkey, lambda: TranslationAPI.switch()) # Trigger the hirigana/katakana switch
        keyboard.add_hotkey(toggle_hotkey, lambda: TranslationAPI.enable_disable()) # Enable/disable translation while still running the script
    def reset_latin():
        _Language.typed_latin = ''
        _Language.latin_to_type = ''
    def start_reveal_timer(delay):
        _Helpers.timer_thread = Timer(delay, function=lambda: _Helpers.timer_trigger(delay))
        _Helpers.timer_thread.start()
    def timer_trigger(delay): 
        for c in _Language.latin_to_type:
            keyboard.send(c)
        _Language.typed_latin += _Language.latin_to_type 
        _Language.latin_to_type = ''
    def reset_timer(delay):
        if _Helpers.timer_thread != None and _Language.input_modifiers == []:
            _Helpers.timer_thread.cancel()
        _Helpers.start_reveal_timer(delay)


class _Language():
    active_kanji_keys = []
    input_modifiers = [] 

    kanji_index = 0
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
                if len(jp_symbols) == 1 or gv.hirigana_mode == True:
                    for c in jp_symbols[0]:
                        keyboard._os_keyboard.type_unicode(c)
                elif gv.katakana_mode == True: 
                    for c in jp_symbols[1]:
                        keyboard._os_keyboard.type_unicode(c)


    def handle_kanji_cycle(event):
        if event.name != 'space': _Language.reset_kanji() ; return False
        elif event.name == 'space' and len(_Language.active_kanji_keys) > 1: _Language.cycle_valid_kanji() ; return True

    def handle_hotkeys(event):
        if event.modified == gv.switch_hotkey: 
            TranslationAPI.switch()
            return True
        elif event.modified == gv.toggle_hotkey: 
            TranslationAPI.enable_disable()  
            return True
        else: return False

    def handle_enter(event):
        if event.name == 'enter':
            if _Language.latin_to_type == '': keyboard.send(event.modified) ; _Language.set_working_string('', True) ; _Helpers.reset_latin()
            else: keyboard.write(_Language.latin_to_type) ; _Language.typed_latin = _Language.latin_to_type ; _Language.latin_to_type = ''
            return True
        else: return False

    def handle_backspace(event): 
        if event.name == 'backspace':
            if _Language.typed_latin != '': _Helpers.reset_latin() ; _Language.working_string = ''
            if _Language.working_string != '': _Language.working_string = _Language.working_string[:-1]; _Language.latin_to_type = _Language.latin_to_type[:-1]
            elif _Language.working_string == '': keyboard.send(event.modified) ;  return True
            return True
        else: return False
        
    def handle_modded_event(event):
        if event.name != event.modified: 
            if 'ctrl' not in event.modified and 'shift' in event.modified and len(event.modified.removeprefix('shift+')) == 1:
                _Language.handle_translation(event)
                return True
            else: 
                _Language.working_string = ''
                keyboard.send(event.modified)
                _Helpers.reset_latin()
                return True
        
    def handle_translation(event): 
        if len(event.name) == 1:
            _Language.working_string += event.name
            _Language.latin_to_type += event.name 

            if _Language.working_string in const.TRANSLATION_DICT.keys(): # Is there a match in the main dictionary
                _Helpers.reset_timer(gv.reveal_delay + 1) 
                _Language.execute_translation(const.TRANSLATION_DICT[_Language.working_string])
                _Language.set_working_string('', True)

            elif _Language.working_string in const.TRANSLATION_DICT['<DOUBLES>'].keys(): # Is there a match in the doubles dictionary
                _Helpers.reset_timer(gv.reveal_delay + 1) 
                _Language.execute_translation( const.TRANSLATION_DICT['<DOUBLES>'][_Language.working_string])
                _Language.working_string = _Language.working_string[-1]
                _Language.latin_to_type = _Language.working_string
            return True
        else: return False 
        
    def handle_space(event):
        if event.modified == 'space' or event.modified == 'ctrl+backspace':
            if _Language.working_string == '': keyboard.send(event.modified)
            else: _Language.set_working_string('', True) ; _Helpers.reset_latin() 
            return True

    def handle_kanji_match(event):
        if event.name == 'space' and _Language.working_string in const.TRANSLATION_DICT['<KANJI>'].keys(): # Is there a match in the Kanji dictionary
            _Language.get_valid_kanji()
            _Language.execute_translation(const.TRANSLATION_DICT['<KANJI>'][_Language.working_string])
            _Language.set_working_string('', True) 
            return True

    def handle_overflow(event):
        if len(event.name) > 1: keyboard.send(event.name) ; _Language.set_working_string('', True) ; _Helpers.reset_latin()  ; return True
        else: return False

    def pre_process_event(event):
        event.input_modifiers = []
        if keyboard.is_modifier(event.name) == True:
            if event.event_type == 'down': keyboard.send(event.name, True, False) 
            elif event.event_type == 'up': keyboard.send(event.name, False, True)
            return True  
        else: 
            if keyboard.is_pressed('ctrl') or keyboard.is_pressed('right ctrl'): event.input_modifiers.append('ctrl+') 
            else: keyboard.send('ctrl', False, True) ; 
            if keyboard.is_pressed('shift') or keyboard.is_pressed('right shift'): event.input_modifiers.append('shift+') 
            else: keyboard.send('shift', False, True) ; 
            if keyboard.is_pressed('alt') or keyboard.is_pressed('right alt'): event.input_modifiers.append('alt+') 
            else: keyboard.send('alt', False, True) ; 
            event.modified = ''.join(event.input_modifiers) + event.name
            return event.modified 

    def process_input(event): # The event is keyboard's 'KeyboardEvent'
        event.modified = _Language.pre_process_event(event)  
        if event.modified == True: return 
        if event.event_type == 'down':
            _Helpers.reset_timer(gv.reveal_delay)
            if _Language.handle_kanji_cycle(event) == True: return 
            if _Language.handle_hotkeys(event) == True: return
            if _Language.handle_modded_event(event) == True: return
            if _Language.handle_kanji_match(event) == True: return
            if _Language.handle_enter(event) == True: return
            if _Language.handle_backspace(event) == True: return 
            if _Language.handle_space(event) == True: return 
            if _Language.handle_translation(event) == True: return   
            if _Language.handle_overflow(event) == True: return 
            raise Exception('Unhandled Key: "' + event.name + '"')
        elif event.event_type == 'up': 
            return 

class TranslationAPI(): 
    def __init__(self, switch_hotkey:str=gv.switch_hotkey,toggle_hotkey:str=gv.toggle_hotkey, exit_hotkey:str=gv.exit_hotkey,reveal_delay=gv.reveal_delay) -> None:
        if reveal_delay <= .05: gv.reveal_delay = .05
        else: gv.reveal_delay = reveal_delay
        _Helpers.add_hotkeys(switch_hotkey=switch_hotkey, toggle_hotkey=toggle_hotkey, exit_hotkey=exit_hotkey)
        _Helpers.add_hooks()
        keyboard.wait(gv.exit_hotkey)
        try: _Helpers.timer_thread.cancel()
        except: pass
        
    def switch():  # Switch between hirigana and katakana translation modes. 
        if gv.hirigana_mode == True: gv.hirigana_mode = False; gv.katakana_mode = True
        elif gv.katakana_mode == True: gv.katakana_mode = False; gv.hirigana_mode = True

    def enable_disable():  # Enable/disable the translation function
        if gv.translate_bool == True: gv.translate_bool = False ; _Helpers.remove_hooks()
        elif gv.translate_bool == False: gv.translate_bool = True ; _Helpers.add_hooks()
        _Language.set_working_string('', True)
        _Helpers.reset_latin()

main = TranslationAPI(reveal_delay=1)
