# -*- coding: utf-8 -*-
import keyboard
import ja_translation_dict
import lang_gui as tt
import win32clipboard
from threading import Timer

class gv:
    running = True
    hirigana_mode = True  # Which language to translate
    katakana_mode = False  # Which language to translate
    translate_bool = True  # Whether or not to translate 
    adding_kanji = False
    translation_gui = tt.TranslationGUI()
    processed_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '/', '-', '~', '[', ']', ',', '.', 'space', 'shift', 'ctrl', 'alt', 'enter', 'backspace', 'left', 'right', 'up', 'down', 'tab', 'delete']
    hooked_keys = []
    reveal_delay = 1

    toggle_gui_hotkey = 'shift+f1'
    add_kanji_hotkey = 'shift+f2'
    switch_hotkey = 'shift+space'
    toggle_hotkey = 'ctrl+space'
    exit_hotkey = 'esc'

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
    def add_hotkeys(switch_hotkey=gv.switch_hotkey, toggle_hotkey=gv.toggle_hotkey, exit_hotkey=gv.exit_hotkey, add_kanji_hotkey=gv.add_kanji_hotkey, toggle_gui_hotkey=gv.toggle_gui_hotkey):
        gv.switch_hotkey = switch_hotkey
        gv.toggle_hotkey = toggle_hotkey
        gv.toggle_gui_hotkey = toggle_gui_hotkey
        gv.exit_hotkey = exit_hotkey
        gv.add_kanji_hotkey = add_kanji_hotkey
        keyboard.add_hotkey(switch_hotkey, lambda: TranslationAPI.switch()) # Trigger the hirigana/katakana switch
        keyboard.add_hotkey(toggle_hotkey, lambda: TranslationAPI.enable_disable()) # Enable/disable translation while still running the script
        keyboard.add_hotkey(add_kanji_hotkey, lambda: TranslationAPI.add_kanji_key())
        keyboard.add_hotkey(toggle_gui_hotkey, lambda: _Helpers.toggle_gui())
    def toggle_gui():
        if gv.translate_bool == True: gv.translation_gui.hide()
    def reset_latin():
        _Language.typed_latin = ''
        _Language.latin_to_type = ''
        _Language.displayed_string = ''
        gv.translation_gui.update_text(_Language.displayed_string)
    def start_reveal_timer(delay):
        _Helpers.timer_thread = Timer(delay, function=lambda: _Helpers.timer_trigger(delay))
        _Helpers.timer_thread.start() 
    def timer_trigger(delay): 
        for c in _Language.latin_to_type:
            try: keyboard._os_keyboard.type_unicode(c)
            except: keyboard.send(c)
            _Language.typed_latin += c 
        _Language.latin_to_type = ''
        _Language.working_string = _Language.typed_latin
    def reset_timer(delay):
        if _Helpers.timer_thread != None and _Language.input_modifiers == []:
            _Helpers.timer_thread.cancel()
        _Helpers.start_reveal_timer(delay)
    def update_displayed_text():
        # gv.tool_tip.destroy() 
        # gv.tool_tip = tt.ToolTip(_Language.working_string)  
        if _Language.working_string != '':
            _Language.displayed_string = _Language.working_string 
            gv.translation_gui.update_text(_Language.displayed_string)


class _Language():
    active_kanji_keys = []
    input_modifiers = [] 
    kanji_index = 0
    working_string = ''
    latin_to_type = ''
    typed_latin = ''
    displayed_string = ''
    new_kanji_key = ''
    new_kanji_translation = ''


    def get_valid_kanji():
        _Language.reset_kanji()
        _Language.active_kanji_keys.append(_Language.working_string)
        for key in ja_translation_dict.LatinToJapanese.TRANSLATION_DICT['<KANJI>']:
            if _Language.working_string + '-' in key and key != _Language.working_string:
                _Language.active_kanji_keys.append(key)

    def cycle_valid_kanji():
        for c in range(len(ja_translation_dict.LatinToJapanese.TRANSLATION_DICT['<KANJI>'][_Language.active_kanji_keys[_Language.kanji_index]][0])):
            keyboard.send('backspace')
        try: 
            _Language.kanji_index += 1
            keyboard.write(ja_translation_dict.LatinToJapanese.TRANSLATION_DICT['<KANJI>'][_Language.active_kanji_keys[_Language.kanji_index]][0])
        except IndexError: 
            _Language.kanji_index = 0
            keyboard.write(ja_translation_dict.LatinToJapanese.TRANSLATION_DICT['<KANJI>'][_Language.active_kanji_keys[_Language.kanji_index]][0])
        _Language.displayed_string = ja_translation_dict.LatinToJapanese.TRANSLATION_DICT['<KANJI>'][_Language.active_kanji_keys[_Language.kanji_index]][0]
        gv.translation_gui.update_text(_Language.displayed_string)
        gv.translation_gui.flash([180,220,220]) 
    
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
                    _Language.displayed_string = jp_symbols[0]
                elif gv.katakana_mode == True: 
                    for c in jp_symbols[1]:
                        keyboard._os_keyboard.type_unicode(c)
                    _Language.displayed_string = jp_symbols[1]
                # gv.tool_tip.destroy() 
                gv.translation_gui.update_text(_Language.displayed_string)
                gv.translation_gui.flash([180,220,220])

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
            _Helpers.update_displayed_text()
            return True
        else: return False

    def handle_backspace(event): 
        if event.name == 'backspace':
            if _Language.displayed_string != _Language.working_string: _Language.displayed_string = '' ; gv.translation_gui.update_text(_Language.displayed_string)
            if _Language.typed_latin != '' and _Language.working_string != '': _Language.typed_latin = _Language.typed_latin[:-1] ; _Language.working_string = _Language.working_string[:-1] ; keyboard.send(event.modified)
            elif _Language.working_string != '': _Language.working_string = _Language.working_string[:-1]; _Language.latin_to_type = _Language.latin_to_type[:-1]
            else: keyboard.send(event.modified) ; _Helpers.update_displayed_text() ; _Language.displayed_string = _Language.displayed_string[:-1] ; return True 
            _Helpers.update_displayed_text()
            if _Language.displayed_string != _Language.working_string: _Language.displayed_string = '' ; gv.translation_gui.update_text(_Language.displayed_string)
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
                _Helpers.update_displayed_text()    
                return True
        
    def handle_translation(event):
        if len(event.name) == 1:
            _Language.working_string += event.name
            _Language.latin_to_type += event.name 

            if _Language.working_string in ja_translation_dict.LatinToJapanese.TRANSLATION_DICT.keys(): # Is there a match in the main dictionary
                _Helpers.reset_timer(gv.reveal_delay + 1) 
                _Language.execute_translation(ja_translation_dict.LatinToJapanese.TRANSLATION_DICT[_Language.working_string])
                _Language.set_working_string('', True)

            elif _Language.working_string in ja_translation_dict.LatinToJapanese.TRANSLATION_DICT['<DOUBLES>'].keys(): # Is there a match in the doubles dictionary
                _Helpers.reset_timer(gv.reveal_delay + 1) 
                _Language.displayed_string = ja_translation_dict.LatinToJapanese.TRANSLATION_DICT['<DOUBLES>'][_Language.working_string]
                _Language.execute_translation( ja_translation_dict.LatinToJapanese.TRANSLATION_DICT['<DOUBLES>'][_Language.working_string])
                _Language.working_string = _Language.working_string[-1]
                _Language.latin_to_type = _Language.working_string
                _Language.displayed_string += _Language.working_string
                gv.translation_gui.update_text(_Language.displayed_string)
            else:
                _Helpers.update_displayed_text()
            return True
        else: return False 
        
    def handle_space(event):
        if event.modified == 'space' or event.modified == 'ctrl+backspace':
            if _Language.working_string == '': keyboard.send(event.modified)
            else: _Language.set_working_string('', True) ; _Helpers.reset_latin() ; 
            _Helpers.update_displayed_text()  
            return True

    def handle_kanji_match(event):
        if event.name == 'space' and _Language.working_string in ja_translation_dict.LatinToJapanese.TRANSLATION_DICT['<KANJI>'].keys(): # Is there a match in the Kanji dictionary
            _Language.get_valid_kanji()
            _Language.execute_translation(ja_translation_dict.LatinToJapanese.TRANSLATION_DICT['<KANJI>'][_Language.working_string])
            _Language.set_working_string('', True) 
            _Helpers.update_displayed_text()
            return True

    def handle_overflow(event):
        if len(event.name) > 1: keyboard.send(event.name) ; _Language.set_working_string('', True) ; _Helpers.reset_latin() ; _Helpers.update_displayed_text() ; return True
        else: return False

    def handle_kanji_addition(event):
        if gv.adding_kanji == True:
            if len(event.name) == 1:
                _Language.new_kanji_key += event.name
                gv.translation_gui.update_text('/' + _Language.new_kanji_key + ': ' + _Language.new_kanji_translation) 
            elif event.name == 'backspace':
                _Language.new_kanji_key = _Language.new_kanji_key[:-1]
                gv.translation_gui.update_text('/' + _Language.new_kanji_key + ': ' + _Language.new_kanji_translation) 
            elif event.name == 'enter':
                with open('ja_translation_dict.py', 'r', encoding='utf-8') as file:
                    lines = file.readlines() 
                    has_key = 0
                    for line in lines:
                        if "'/" + _Language.new_kanji_key + "':" in line or "'/" + _Language.new_kanji_key + "-" in line: has_key += 1 
                    for line in lines:
                        if '<KANJI>' in line:
                            if has_key == 0:
                                lines.insert(lines.index(line)+1, '\n\t\t\t' + "'/" + _Language.new_kanji_key + "':" +  "['" + _Language.new_kanji_translation + "'],") 
                            else: lines.insert(lines.index(line)+1, '\n\t\t\t' + "'/" + _Language.new_kanji_key + "-" + str(has_key) + "':" +  "['" + _Language.new_kanji_translation + "'],") 

                with open('ja_translation_dict.py', 'w', encoding='utf-8') as file:
                    for line in lines: 
                        file.writelines(line) 
                

                _Language.new_kanji_key = '' 
                _Language.new_kanji_translation = '' 
                gv.adding_kanji = False
                gv.translation_gui.update_text('Kanji Added')
                gv.translation_gui.flash([200,255,200])

            return True
            
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
            if _Language.handle_kanji_addition(event) == True: return
            if _Language.handle_kanji_cycle(event) == True: return 
            if _Language.handle_hotkeys(event) == True: return
            if _Language.handle_modded_event(event) == True: return
            if _Language.handle_kanji_match(event) == True: return
            if _Language.handle_enter(event) == True: return
            if _Language.handle_backspace(event) == True: return 
            if _Language.handle_space(event) == True: return 
            if _Language.handle_translation(event) == True: return   
            if _Language.handle_overflow(event) == True: return 
            raise ValueError('Unhandled Key: "' + event.name + '"')
        elif event.event_type == 'up': 
            _Helpers.reset_timer(gv.reveal_delay) 
            return

class TranslationAPI():
    def __init__(self, switch_hotkey:str=gv.switch_hotkey,toggle_hotkey:str=gv.toggle_hotkey, exit_hotkey:str=gv.exit_hotkey,reveal_delay=gv.reveal_delay) -> None:
        self.running = True
        if reveal_delay <= .05: gv.reveal_delay = .05
        else: gv.reveal_delay = reveal_delay
        _Helpers.add_hotkeys(switch_hotkey=switch_hotkey, toggle_hotkey=toggle_hotkey, exit_hotkey=exit_hotkey)
        _Helpers.add_hooks()
        keyboard.add_hotkey(gv.exit_hotkey, lambda: self.exit())
        while self.running == True:
            gv.translation_gui.mainloop()
        gv.translation_gui.exit()
        exit()

    def exit(self):
        self.running = False
    def add_kanji_key():
        if gv.adding_kanji == False:
            try:
                win32clipboard.OpenClipboard()
                _Language.new_kanji_translation = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                if "'" not in _Language.new_kanji_translation:
                    gv.adding_kanji = True 
                    gv.translation_gui.update_text("Adding key for: " + _Language.new_kanji_translation) 
                else:
                    _Language.new_kanji_translation = ''
                    gv.translation_gui.update_text('Clipboard Data Incompatable') 
                    gv.translation_gui.flash([255,200,200])
            except:
                gv.translation_gui.update_text('Clipboard Data Incompatable')
                gv.translation_gui.flash([255,200,200])
        elif gv.adding_kanji == True: 
            _Language.new_kanji_key = ''
            _Language.new_kanji_translation = '' 
            gv.translation_gui.update_text('Process Aborted')
            gv.translation_gui.flash([255,200,200])
            gv.adding_kanji = False

    def switch():  # Switch between hirigana and katakana translation modes. 
        if gv.hirigana_mode == True: gv.hirigana_mode = False ; gv.katakana_mode = True ; _Language.displayed_string = 'カタカナ'
        elif gv.katakana_mode == True: gv.katakana_mode = False ; gv.hirigana_mode = True ; _Language.displayed_string = '平仮名'
        gv.translation_gui.update_text(_Language.displayed_string)
    def enable_disable():  # Enable/disable the translation function
        if gv.translate_bool == True: gv.translate_bool = False ; _Helpers.remove_hooks()
        elif gv.translate_bool == False: gv.translate_bool = True ; _Helpers.add_hooks()
        _Language.set_working_string('', True)
        _Helpers.reset_latin()
        if gv.translation_gui.hidden == False:
            gv.translation_gui.hide()

main = TranslationAPI(reveal_delay=10)



