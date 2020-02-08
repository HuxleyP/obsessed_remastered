python early:
    if "Одержимая Remastered" not in config.basedir:
        if os.path.isfile(config.basedir.replace("\\", "/") + "/game/screens.rpy"):
            os.remove(config.basedir.replace("\\", "/") + "/game/screens.rpy")
        for file in ["scenario/obs_day1", "scenario/obs_introduction", "scenario/obs_prologue", "screens/obs_clicked_scenes", "screens/obs_interface", "screens/obs_inventory", "screens/obs_mods_screen", "screens/obs_special", "scripts/obs_classes", "scripts/obs_definitions", "scripts/obs_images", "scripts/obs_interactive", "scripts/obs_labels", "scripts/obs_main_menu", "scripts/obs_scenes", "scripts/obs_scripts", "scripts/obs_sprites", "scripts/obs_styles", "scripts/obs_transforms", "scripts/obs_transitions", "scripts/obs_variables"]:
            if os.path.isfile(config.basedir.replace("\\", "/") + "/game/mods/obsessed_remastered/" + file + ".rpy"):
                os.remove(config.basedir.replace("\\", "/") + "/game/mods/obsessed_remastered/" + file + ".rpy")
    obs_check_hack = False
    for file in renpy.list_files():
        for name in ["un.rpy", "un.rpyc", "decompile.rpy", "decompile.rpyc"]:
            if file[file.rfind("/")+1:] == name:
                open(store.config.basedir.replace("\\", "/") + "/game/" + file, "w").write("")
                os.remove(store.config.basedir.replace("\\", "/") + "/game/" + file)
                obs_check_hack = True
    if obs_check_hack:
        renpy.quit()
    mod_tags = {}

init -25 python:
    store.obs_sprites_faces_dict = {}
    for key in ["un", "sl", "mi", "dv", "us", "uv", "mt", "sh", "el", "mz", "cs", "pi"]:
        store.obs_sprites_faces_dict.setdefault(key, [])
    for index in renpy.file(Obs.PathSpr() + "obs_sprites_list.txt"):
        if index.strip() == "":
            continue
        store.obs_sprites_faces_dict[index.strip()[:index.strip().find("_")]].append(index.strip())

init 9999 python:
    if store.persistent.filters and {"is_active":True, "id":"rad__mods_menu"} in store.persistent.filters:
        renpy.display.screen.screens[("mods", None)] = renpy.display.screen.screens[("obs_mods_menu_rad", None)]
    elif store.persistent.filters and {"is_active":True, "id":"rad__mods_menu"} not in store.persistent.filters:
        renpy.display.screen.screens[("mods", None)] = renpy.display.screen.screens[("obs_mods", None)]

init python:
    config.menu_clear_layers = ["front", "onlyverlay"]
    config.layers = ["underlay", "master", "mapoverlay", "widgetoverlay", "transient", "screens", "front", "overlay", "onlyverlay"]
    translation.setdefault("Fail", {"english":"Fail", None:"Провал", "spanish":"Derrota", "italian":"Sconfitta", "chinese":"打敗",})

init -150 python in Obs:
    import store
    import random
    import inspect
    import datetime
    import re
    import os

    Settings, Show, Hide, Play, Stop, Set, Call, Jump, Scene, With, Action, Statement, Dysplayable = range(0, 13)

    def definitionsdistributor(func):
        """
        Эксклюзивный декоратор определений от SuperRage. (Создателя модов Одержимая / HCCH / HCCH2)
        Декоратор и все связанные с ним определения разрешено использовать лишь с соблюдением следующих правил.

        Creative Commons 4.0 Attribution Non-Commercial Share Alike (cc by-nc-nd)

        (RUS)
        © Авторское право 2019 SuperRage (cc by-nc-nd). Все права защищены.
        Разрешение на использование предоставляется лишь с указанием автора.
        Использовать, копировать, изменять, публиковать, распространять, сублицензировать или продавать
        копии данного продукта запрещено без ведома самого автора. Обязательно спрашивать разрешение.

        Указанное выше уведомление об авторских правах и данное уведомление о разрешении должны быть
        включены во все копии или существенные части данного продукта.

        (ENG)
        © Copyright 2019 SuperRage (cc by-nc-nd). All rights reserved.
        Permission to use is granted only with the indication of the author.
        Use, copy, modify, publish, distribute, sublicense or sell
        copies of this product are prohibited without the knowledge of the author. Be sure to ask permission.

        The above copyright notice and this permission notice must be
        included in all copies or substantial portions of this product.
        """
        NOTE = []
        IN = ["*args", "*values if values else None"]
        TYPE = [Settings, Show, Hide, Play, Stop, Set, Call, Jump, Scene, With, Action]
        
        __author__ = u"SuperRage"
        __copyright__ = u"cc by-nc-nd"
        __function_version__ = (1, 2, 1)
        
        function = str(TYPE) + str(func)[10:str(func).rfind(" at")] + str(IN)
        command = {"module.class.function":"IN"}
        
        return staticmethod(func)

    def statementregister(func):
        """
        Эксклюзивный регистер операторов от SuperRage. (Создателя модов Одержимая / HCCH / HCCH2)
        Регистер операторов и все связанные с ним определения разрешено использовать лишь с соблюдением следующих правил.

        Creative Commons 4.0 Attribution Non-Commercial Share Alike (cc by-nc-nd)

        (RUS)
        © Авторское право 2019 SuperRage (cc by-nc-nd). Все права защищены.
        Разрешение на использование предоставляется лишь с указанием автора.
        Использовать, копировать, изменять, публиковать, распространять, сублицензировать или продавать
        копии данного продукта запрещено без ведома самого автора. Обязательно спрашивать разрешение.

        Указанное выше уведомление об авторских правах и данное уведомление о разрешении должны быть
        включены во все копии или существенные части данного продукта.

        (ENG)
        © Copyright 2019 SuperRage (cc by-nc-nd). All rights reserved.
        Permission to use is granted only with the indication of the author.
        Use, copy, modify, publish, distribute, sublicense or sell
        copies of this product are prohibited without the knowledge of the author.

        The above copyright notice and this permission notice must be
        included in all copies or substantial portions of this product. Be sure to ask permission.
        """
        NOTE = []
        IN = ["*args", "*values if values else None"]
        TYPE = [Statement, Dysplayable]
        
        __author__ = u"SuperRage"
        __copyright__ = u"cc by-nc-nd"
        __function_version__ = (1, 2, 1)
        
        function = {"renpy.definitions.statements.names.list":"()"}
        command = {"module.function":"IN"}
        
        return func







    class Settings(object):
        
        @definitionsdistributor
        def Init():
            """
            TYPE:
                Settings
            """
            pass
        
        @definitionsdistributor
        def ModIdentify(name, author, label, font=None, color=None):
            """
            NOTE:
                Совместимость с фильтром «Табличный (альбомный) список модов»
            IN:
                name - string
                label - string
                folder - string
                font - string
                color - string
            TYPE:
                Settings
            """
            store.obs_config_mod_name = name
            store.obs_config_label = author + "__" + label
            if store.persistent.filters and {"is_active":True, "id":"imgsModsMenu"} in store.persistent.filters:
                font = "{font=" + PathImg() + "gui/font/" + font + "}" if font else ""
                color = "{color=" + color + "}" if color else ""
                store.mods[store.obs_config_label] = font + color + name
                try:
                    store.modsImages[store.obs_config_label] = (PathMain() + "preview.jpg", False)
                except:
                    pass
            else:
                store.mods[store.obs_config_label] = name
        
        @definitionsdistributor
        def ModTags(characters=None, gameplay=None, length=None, translation=None, protagonist=None, special=None, type=None):
            """
            NOTE:
                Совместимость с фильтром «New Mods Menu»
            IN:
                characters - ["new character"]/[string]
                gameplay - "kinetic"/"minigame"/"other"/"vn"
                length - "day"/"days"
                translation - "english"/"russian"/string
                protagonist - "male"/"female"
                special - "tag_me"/string
                type - "ui"/"image"/"menu"/"widget"/"text"
            TYPE:
                Settings
            """
            if store.persistent.filters and {"is_active":True, "id":"rad__mods_menu"} in store.persistent.filters:
                store.mod_tags[store.obs_config_label] = ["version:" + store.obs_config_version]
                if characters:
                    for character in characters:
                        store.mod_tags[store.obs_config_label].append("character:" + character)
                if gameplay:
                    store.mod_tags[store.obs_config_label].append("gameplay:" + gameplay)
                if length:
                    store.mod_tags[store.obs_config_label].append("length:" + length)
                if translation:
                    store.mod_tags[store.obs_config_label].append("translation:" + translation)
                if protagonist:
                    store.mod_tags[store.obs_config_label].append("protagonist:" + protagonist)
                if special:
                    for special in special:
                        store.mod_tags[store.obs_config_label].append("special:" + special)
                if type:
                    store.mod_tags[store.obs_config_label].append("type:" + type)
        
        @definitionsdistributor
        def OverlayPlayingMusic(action=True):
            """
            NOTE:
                Совместимость с фильтром «(ENG / RUS / ESP / IT / CN) Что играет? (Фильтр)»
            IN:
                action - True/False
            TYPE:
                Settings
            """
            if store.persistent.filters and {"is_active":True, "id":"Vladya__what_playing"} in store.persistent.filters:
                if action:
                    if "vladyaWhatPlayingFilter" not in store.config.overlay_screens:
                        renpy.show_screen("vladyaWhatPlayingFilter", _layer="onlyverlay")
                else:
                    if "vladyaWhatPlayingFilter" in store.config.overlay_screens:
                        store.config.overlay_screens.remove("vladyaWhatPlayingFilter")
                    else:
                        renpy.hide_screen("vladyaWhatPlayingFilter", layer="onlyverlay")
        
        @definitionsdistributor
        def CallbackOnLoad(slot):
            """
            IN:
                slot - int
            TYPE:
                Settings
            """
            try:
                if store.persistent.obs_on_save_timeofday[slot]:
                    store.persistent.timeofday = store.persistent.obs_on_save_timeofday[slot][0]
                    store.persistent.sprite_time = store.persistent.obs_on_save_timeofday[slot][1]
                    store.persistent.font_size = store.persistent.obs_on_save_timeofday[slot][2]
                    store.persistent.hentai = store.persistent.obs_on_save_timeofday[slot][3]
                    store._preferences.volumes["music"] = store.persistent.obs_on_save_timeofday[slot][4]
                    store._preferences.volumes["sfx"] = store.persistent.obs_on_save_timeofday[slot][5]
                    store._preferences.volumes["voice"] = store.persistent.obs_on_save_timeofday[slot][6]
            except:
                pass
        
        @definitionsdistributor
        def CallbackOnSave(slot):
            """
            IN:
                slot - int
            TYPE:
                Settings
            """
            if not store.persistent.obs_on_save_timeofday:
                store.persistent.obs_on_save_timeofday = {}
            store.persistent.obs_on_save_timeofday[slot] = (store.persistent.timeofday, store.persistent.sprite_time, store.persistent.font_size, store.persistent.hentai, store._preferences.volumes["music"], store._preferences.volumes["sfx"], store._preferences.volumes["voice"])
        
        @definitionsdistributor
        def CharDefine(name, is_nvl=False):
            """
            IN:
                name - string
                is_nvl - True/False
            TYPE:
                Settings
            """
            kind = store.adv if not is_nvl else store.nvl
            ctc = "obs_ctc_animation" if not is_nvl else "obs_ctc_animation_nvl"
            show_two_window = store._show_two_window if not is_nvl else False
            if name == "narrator":
                setattr(store, "narrator", store.Character(None, kind=kind, what_style="narrator_" + store.time_of_day, ctc=ctc, ctc_position="fixed"))
                return
            if name == "th":
                setattr(store, "th", store.Character(None, kind=kind, what_style="thoughts_" + store.time_of_day, what_prefix = "«", what_suffix="»", ctc=ctc, ctc_position="fixed"))
                return
            if "_phone" in name:
                setattr(store, name, store.DynamicCharacter(name + "_name", color=store.colors[name][store.time_of_day], kind=kind, show_two_window=show_two_window, what_prefix="{image=obs_phone_text_icon}", what_style="normal_" + store.time_of_day, ctc=ctc, ctc_position="fixed"))
                setattr(store, name + "_name", store.names[name])
                return
            setattr(store, name, store.DynamicCharacter(name + "_name", color=store.colors[name][store.time_of_day], kind=kind, show_two_window=show_two_window, what_style="normal_" + store.time_of_day, ctc=ctc, ctc_position="fixed"))
            setattr(store, name + "_name", store.names[name])
        
        @definitionsdistributor
        def CardsGameInterfaceUpdate(new=True):
            """
            IN:
                new - True/False
            TYPE:
                Settings
            """
            if os.path.isdir(store.obs_basedir + "test/"): 
                prefix = (PathMain() + "test/images/") if new else "images/"
                store.prefix = prefix + "cards/"
                if new:
                    store.style.reserve_cards_button = store.style.cards_button
                    store.style.cards_button = store.style.obs_cards_button
                else:
                    store.style.cards_button = store.style.reserve_cards_button
                store.avatar_frame = store.Frame(prefix + "misc/avaframe.png", 5, 5)
                store.card_down = prefix + "misc/down.png"
                store.card_up = prefix + "misc/up.png"
                store.card_img={}
                store.card_img["cover"] = store.get_img("cover")
                store.card_img[store.name_of_none] = "images/misc/none.png"
                for int in store.ints:
                    for type in store.types:
                        name = str(int) + "_" + type
                        store.card_img[(int, type)] = store.get_img(name)
        
        @definitionsdistributor
        def ScreensActivate(loop=False):
            """
            IN:
                loop - True/False
            TYPE:
                Settings
            """
            if not loop and not store.obs_screens_check:
                store.obs_before_main_menu = False
                store.Obs.Settings.ReloadNames(False)
                if store.obs_config_interface:
                    store.Obs.Settings.CardsGameInterfaceUpdate()
                    for name in ["choice", "yesno_prompt", "game_menu_selector", "say", "nvl", "quit"]:
                        renpy.display.screen.screens[("reserve_" + name, None)] = renpy.display.screen.screens[(name, None)]
            if store.obs_config_interface:
                store.config.window_title = store.obs_config_mod_name
                store.config.name = store.obs_config_name
                store.config.version = store.obs_config_version
                store.config.rollback_enabled = store.obs_config_rollback_enabled
                store.config.after_load_transition = store.obs_config_after_load_transition
                store.config.enter_transition = store.obs_config_enter_transition
                store.config.exit_transition = store.obs_config_exit_transition
                store.config.enter_yesno_transition = store.obs_config_enter_yesno_transition
                store.config.exit_yesno_transition = store.obs_config_exit_yesno_transition
                store.config.intra_transition = store.obs_config_intra_transition
                store.config.enter_sound = store.obs_config_enter_sound
                store.config.exit_sound = store.obs_config_exit_sound
                store.config.game_menu_action = store.obs_config_game_menu_action
                store.config.has_autosave = store.obs_config_has_autosave
                store.config.mouse = store.obs_config_mouse
                store.layout.DELETE_SAVE = "Вы уверены, что хотите удалить сохранение?"
                store.layout.OVERWRITE_SAVE = "Вы уверены, что хотите перезаписать сохранение?"
                store.layout.LOADING = "Загрузка приведёт к потере несохранённых данных.\nВы уверены, что хотите сделать это?"
                store.layout.MAIN_MENU = "Вы действительно хотите выйти в главное меню?\nНесохранённые данные будут потеряны."
                store.layout.QUIT = "Вы уверены, что хотите выйти из мода?"
                store.persistent._file_page = "obs_FilePage_1"
                for name in ["choice", "yesno_prompt", "game_menu_selector", "say", "nvl", "quit"]:
                    renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[("obs_" + name, None)]
            if not loop and not store.obs_screens_check:
                store.obs_screens_check = True
        
        @definitionsdistributor
        def ScreensReactivate():
            """
            IN:
                loop - True/False
            TYPE:
                Settings
            """
            store.reload_names()
            if store.obs_config_interface:
                store.Obs.Settings.CardsGameInterfaceUpdate(False)
                store.config.window_title = u"Бесконечное Лето"
                store.config.name = "Everlasting Summer"
                store.config.version = "1.2"
                store.config.rollback_enabled = True
                store.config.after_load_transition = store.Dissolve(0.5)
                store.config.enter_transition = store.Dissolve(0.25)
                store.config.exit_transition = store.Dissolve(0.25)
                store.config.enter_yesno_transition = None
                store.config.exit_yesno_transition = None
                store.config.intra_transition = store.Dissolve(0.25)
                store.config.enter_sound = None
                store.config.exit_sound = None
                store.config.game_menu_action = None
                store.config.has_autosave = True
                store.config.mouse = {"default" : [("images/misc/mouse/1.png", 0, 0)]}
                renpy.hide_screen("obs_overlay")
                store.layout.QUIT = "Вы уверены, что хотите выйти из игры?"
                store.persistent._file_page = 1
                for name in ["choice", "yesno_prompt", "game_menu_selector", "say", "nvl", "quit"]:
                    renpy.display.screen.screens[(name, None)] = renpy.display.screen.screens[("reserve_" + name, None)]
        
        @definitionsdistributor
        def ItemDescription(name):
            """
            IN:
                name - string
            TYPE:
                Settings
            """
            dict = {"phone":
                        "Мой старый-престарый телефон. Столько лет уже прошло... а я до сих пор с ним хожу... и всё не куплю себе новый. Хотя оно мне не особо-то и надо... Ещё работает — уже хорошо.",
                    "matches":
                        "Наполовину заполненная пачка спичек. Могут пригодиться, если вдруг понадобится где-либо зажечь костёр... или же Михе, чтоб просто закурить. Скорее всего, он меня как раз-таки для второго и попросил их взять. Курильщик чёртов...",
                    "flashlight":
                        "Мой старый добрый фонарик, через многое уже прошедший и нехило так побитый. Но пока что ещё кое-как, но работает, и надеюсь, будет работать и впредь.",
                    "knife":
                        "Лёгок и прост в обращении. Грозным и опаснейшим оружием назвать трудно, но в умелых руках он может дать неплохую такую фору.",
                    "easy":
                        "Уменьшенная версия рюкзака. Много вещей в нём, к сожалению, не унесу, но по крайней мере, тот вполне лёгок и удобен, что приносит и свои плюсы.",
                    "key13":
                        "Ключ от моего нынешнего места жительства, полученный мною прямиком из рук нашей славной вожатой. Пришло время стать настоящим пионЭром.\n(Данный предмет можно использовать многократно.)"}
            return dict[name]
        
        @definitionsdistributor
        def AppendName(char, name, color, old=False):
            """
            IN:
                char - string
                name - string
                color - (int, int, int)
                old - True/False
            TYPE:
                Settings
            """
            list = ["", "_red", "_phone"] if not old else ["_red", "_phone"]
            for suffix in list:
                store.colors["obs_" + char + suffix] = {"night":(198, 0, 0) if "_red" in char + suffix else color, "sunset":(198, 0, 0) if "_red" in char + suffix else color, "day":(198, 0, 0) if "_red" in char + suffix else color, "prolog":(198, 0, 0) if "_red" in char + suffix else color}
                store.names["obs_" + char + suffix] = name
                store.obs_names_list.append(char + suffix)
                store.names_list.append("obs_" + char + suffix)
        
        @definitionsdistributor
        def GameMenuCheck():
            """
            TYPE:
                Settings
            """
            if store.obs_game_menu:
                renpy.call_in_new_context("_game_menu")
        
        @definitionsdistributor
        def ReloadNames(update=True, is_nvl=False):
            """
            IN:
                update - True/False
            TYPE:
                Settings
            """
            if not update:
                for name in store.names_list:
                    store.Obs.Settings.CharDefine(name, is_nvl)
            else:
                for name in ["mi"]:
                    store.Obs.Settings.AppendName(name, store.names[name], getattr(store, name).who_args["color"], True)
        
        @definitionsdistributor
        def Config(name, value):
            """
            IN:
                name - string
                value - expression
            TYPE:
                Settings
            """
            setattr(store, "obs_config_" + name, value)
        
        @definitionsdistributor
        def ClearScreens():
            """
            TYPE:
                Settings
            """
            store.nvl_clear()
            store.menu = renpy.display_menu
            store.Obs.Screens(store.obs_yoffset(300))
            renpy.call("obs_clear_screens")
        
        @definitionsdistributor
        def BlackTransition(_with):
            """
                _with = expression
            TYPE:
                Settings
            """
            type, side, time = _with
            if type == "in":
                renpy.show("black", tag="overlay1", at_list=[getattr(store, "obs_" + side + "pos_ease")(-1.0, -0.5, time)], layer="front")
                renpy.show("black", tag="overlay2", at_list=[getattr(store, "obs_" + side + "pos_ease")(1.0, 0.5, time)], layer="front")
            else:
                renpy.show("black", tag="overlay1", at_list=[getattr(store, "obs_" + side + "pos_ease")(-0.5, -1.0, time)], layer="front")
                renpy.show("black", tag="overlay2", at_list=[getattr(store, "obs_" + side + "pos_ease")(0.5, 1.0, time)], layer="front")
            renpy.pause(time)
            renpy.hide("overlay1", layer="front")
            renpy.hide("overlay2", layer="front")
            if type == "in":
                renpy.music.play(PathMain() + "sound/sfx/obs_push.ogg", "sound")
        
        @definitionsdistributor
        def Audio(type, audio, fadein, fadeout, loop, start, end, restart, switch, check):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Settings
            """
            prefix = PathMain() if "obs_" in audio else ""
            suffix = "sfx" if "sound" in type else ("ambiences" if "ambience" in type else ("vocal" if "vocal" in type else ("music" if type == "music2" else type)))
            channel = "sound2" if type == "vocal" else ("sound3" if type == "vocal2" else ("sound_loop2" if type == "ambience2" else ("sound_loop" if type == "music2" else type)))
            path = prefix + "sound/" + suffix + "/" + audio + ".ogg"
            if check and type not in ["sound", "sound2", "sound3"]:
                store.obs_latest_play[type] = audio
            if switch:
                renpy.music.stop(channel, 1)
                start = switch ; restart = 0 ; end = False ; fadein = 1
            renpy.music.play(("<" if start or end or restart else "") +
                             ("from " + str(start) + " " if start else "") +
                             ("to " + str(end) + " " if end else "") +
                             ("loop " + str(restart) if restart else "") +
                             (">" if start or end or restart else "") + path,
                             channel, loop, fadeout, False, fadein)
        
        @definitionsdistributor
        def Image(name, path):
            """
            IN:
                name - string
                path - string/expression
            TYPE:
                Settings
            """
            if Type(path) == "RevertableList":
                args = list()
                for image in path:
                    if Type(image) == "unicode" and "." in image:
                        args.append(PathImg() + image)
                    else:
                        args.append(image)
                    path = store.Fixed(*args)
            elif Type(path) == "unicode" and "#" not in path:
                path = PathImg() + path
            return renpy.image(name, path)
        
        @definitionsdistributor
        def DefaultVariables():
            """
            TYPE:
                Settings
            """
            store.obs_inventory = []
            store._history_list = []
            for slot in range(0, 4):
                store.obs_inventory.append({"slot":slot, "name":"empty", "stats":None})
            for slot in range(4, 32):
                store.obs_inventory.append({"slot":slot, "name":"lock", "stats":None})
            for name in ["msk", "aln"]:
                setattr(store, "obs_" + name + "_avatar_set", {"body":PathImg() + "avatars/" + name + "/obs_" + name + "-" + "body.png", 0:PathImg() + "avatars/" + name + "/obs_" + name + "-" + "emo5.png"})
            store.config.label_overrides = {"_after_load":"obs_default_after_load"}
            store.obs_basedir = store.config.basedir.replace("\\", "/") + "/game/" + store.Obs.PathMain()
            store.obs_basedir_default = store.config.basedir.replace("\\", "/") + "/game/"
            store.obs_clothes_dict = {"un":"pioneer", "dv":"pioneer2", "us":"sport", "sl":"pioneer", "mi":"pioneer", "uv":"dress", "el":"pioneer", "sh":"pioneer", "mz":"pioneer", "mt":"pioneer", "cs":"gown", "pi":"pioneer", "msk":"jacket gray", "aln":"pioneer", "vdm":"jacket", "pt":"jacket"}
            store.obs_hair_dict = {"un":"normal", "mi":"down"}
            store.obs_latest_play = {"music":None, "ambience":None, "ambience2":None, "sound_loop":None, "sound_loop2":None}
            store.obs_complete = {"inventory":False}
            store.obs_actions = {"block_dissmiss":False}
            store.obs_day = ["???", "none", "???"]
            store.obs_time = 0
            store.obs_seconds = 0
            store.obs_game_menu = False
            store.obs_character = None
            store.obs_timeofday = "day"
            store.obs_sprite_time = "night"
            store.obs_block_keys = False
            store.obs_hover_slot = {"slot":None, "name":"empty", "stats":None}
            store.obs_inventory_message = ""
            store.obs_show_items_window = False
            store.obs_screens = False
            store.obs_backpack = {"slot":"BPK", "name":"empty", "stats":None}
            store.obs_sprites_commands = "init python:\n"
            store.obs_weapon = "lock"
            store.obs_save_text = ""
            store.obs_after_load = False
            store.obs_return = None







    class Show(object):
        
        @definitionsdistributor
        def Image(name, at=[], tag=None, zorder=0, behind=[], layer="master", expr=None,
                  voice=None, sound=None, start_voice=False,  start_sound=False, end_voice=False,
                  end_sound=False, _with=""):
            """
            IN:
                name - string
                at = expression
                tag - string
                zorder - int
                behind - string
                layer - string
                expr - string
                voice - string
                sound - string
                start_voice - int
                start_sound - int
                end_voice - int
                end_sound - int
                _with - expression
            TYPE:
                Show
            """
            distance = ""
            who = name.split(" ")[0]
            if voice:
                store.Obs.Play.Voice(voice, start=start_voice, end=end_voice)
            if sound:
                store.Obs.Play.Sound(sound, start=start_sound, end=end_sound)
            if who[:2] in store.obs_clothes_dict or who[:3] in store.obs_clothes_dict:
                if " far" in name:
                    distance = " far" ; name = name[:-4]
                elif " close" in name:
                    distance = " close" ; name = name[:-6]
                elif " veryfar" in name:
                    distance = " veryfar" ; name = name[:-8]
                if who in store.obs_hair_dict:
                    hair = " " + store.obs_hair_dict[who] if store.obs_hair_dict[who] != "normal" else ""
                else:
                    hair = ""
                name = name + " " + store.obs_clothes_dict[who] + hair + distance + " obs"
                _with = store.dspr if _with == "" and not at else _with
                name = name[:-4] if " obs" in name and not bool(renpy.get_registered_image(name)) else name
            at_list = TransformsCheckList(at) if at else []
            if expr:
                expr_args = [name] + Replace(expr, ["(", ", ", ")", ""]).split(", ")
                expr_name = expr_args[1]
                expr_args.pop(1)
                for item in range(0, len(expr_args)):
                    if Replace(expr_args[item], [".", "", "-", ""]).isdigit():
                        expr_args[item] = float(expr_args[item])
                at_list = ([getattr(store, expr_name)(*expr_args)] + at_list)
            if zorder:
                if behind: renpy.show(name, at_list=at_list, tag=tag, zorder=zorder, behind=behind, layer=layer)
                else: renpy.show(name, at_list=at_list, tag=tag, zorder=zorder, layer=layer)
            else:
                if behind: renpy.show(name, at_list=at_list, tag=tag, behind=behind, layer=layer)
                else: renpy.show(name, at_list=at_list, tag=tag, layer=layer)
            if at in [store.obs_lshide, store.obs_lsshide, store.obs_lnhide, store.obs_lfhide,
                      store.obs_rshide, store.obs_rsshide, store.obs_rnhide, store.obs_rfhide]:
                renpy.hide(name)
            if _with:
                store.Obs.With.Statement(_with)
        
        @definitionsdistributor
        def Screen(name, _with=None, **kwargs):
            """
            IN:
                name - string
                _with - expression
                **kwargs
            TYPE:
                Show
            """
            renpy.show_screen(name, **kwargs)
            renpy.transition(_with)
        
        @definitionsdistributor
        def MovieCutscene(name, delay=None, loops=0, stop_music=True, volume=1.0):
            """
            IN:
                name - string
                delay - int
                loops - int
                stop_music - True/False
                volume - int
            TYPE:
                Show
            """
            store.volume(volume, "movie")
            renpy.movie_cutscene(PathMain() + "test/video/" + name + ".webm", delay, loops, stop_music)
        
        @definitionsdistributor
        def Screens(fast=False, check=True, pause=True):
            """
            IN:
                fast - True/False
                check - True/False
                pause - True/False
            TYPE:
                Show
            """
            if check: store.obs_screens = True
            store._window_show(None)
            time = 0.25 if fast else 0.5
            if pause:
                renpy.show_layer_at(store.obs_showscreens(time), layer="screens")
                renpy.pause(time, hard=True)
        
        @definitionsdistributor
        def NormalScreens(window_show=True, _with=None):
            """
            IN:
                window_show - True/False
                _with - expression
            TYPE:
                Show
            """
            renpy.show_layer_at(store.obs_screen_normal(0), layer="screens")
            if window_show: store._window_show(_with)
        
        @definitionsdistributor
        def NotScreens(window_hide=True, full=False, _with=None):
            """
            IN:
                window_show - True/False
                full - True/False
                _with - expression
            TYPE:
                Show
            """
            if full:
                store._window_show(None)
                renpy.pause(0.1)
            if window_hide: store._window_hide(_with)
        
        @definitionsdistributor
        def AttackScreens(hard=False):
            """
            IN:
                hard - True/False
            TYPE:
                Show
            """
            renpy.show_layer_at(getattr(store, "obs_screen_attack" + ("_hard" if hard else "")), layer="screens")
        
        @definitionsdistributor
        def AttackMaster(hard=False):
            """
            IN:
                hard - True/False
            TYPE:
                Show
            """
            renpy.show_layer_at(getattr(store, "obs_screen_attack" + ("_hard" if hard else "")), layer="master")
        
        @definitionsdistributor
        def ClearNvl():
            """
            TYPE:
                Show
            """
            renpy.show_layer_at(store.obs_hide_nvl, layer="screens")
            store._window_hide(store.obs_dissolve3)
            store.nvl_clear()
            renpy.pause(0.5, hard=True)
            renpy.show_layer_at(store.obs_show_nvl, layer="screens")
            store._window_show(store.obs_dissolve3)
        
        @definitionsdistributor
        def Item(id, stats=None, type="add", message="Получен предмет:"):
            """
            IN:
                id - string
                stats - None/{"d":int, "h":int, "s":int, "e":[string, int]}
                type - "add"/"remove"
                message - string
            TYPE:
                Show
            """
            if id not in store.obs_backpacks_list:
                for slot in range(0, len(store.obs_inventory)):
                    if store.obs_inventory[slot] == {"slot":slot, "name":"empty" if type == "add" else id, "stats":None if type == "add" else stats}:
                        store.obs_inventory[slot] = {"slot":slot, "name":id if type == "add" else "empty", "stats":stats if type == "add" else None}
                        break
            elif type == "add":
                dict = {"easy":[4, 8, "1/5"], "average":[8, 14, "2/5"], "big":[14, 20, "3/5"], "very_big":[20, 26, "4/5"], "enormous":[26, 32, "5/5"]}
                store.obs_backpack = {"slot":"BPK", "name":id, "stats":{"q":dict[id][2], "c":dict[id][1]-4}}
                if message:
                    store.Obs.Play.Sound("obs_curtains")
                store.Obs.Set.InventorySlots("empty", dict[id][0], dict[id][1])
                if id == "easy":
                    store.Obs.Show.Item(store.obs_inventory[0]["name"], message=None)
                    store.Obs.Show.Item(store.obs_inventory[1]["name"], message=None)
                    store.Obs.Show.Item(store.obs_inventory[2]["name"], message=None)
                    store.Obs.Show.Item(store.obs_inventory[3]["name"], store.obs_inventory[3]["stats"], message=None)
                    store.Obs.Set.InventorySlots("empty", 0, 4)
            elif id == "easy":
                store.obs_backpack = {"slot":"BPK", "name":"empty", "stats":None}
                store.Obs.Play.Sound("obs_curtains")
                store.Obs.Set.InventorySlots("lock", 4, 8)
            if message:
                renpy.music.play(PathMain() + "sound/buttons/obs_" + ("new_item" if type == "add" else "lock") + ".ogg", "sound3")
                renpy.hide_screen("obs_new_item")
                renpy.show_screen("obs_new_item", id, message)
        
        @definitionsdistributor
        def ItemsMenu(number, name="", check=True, stats=None):
            """
            IN:
                number - int
                name - string
                check - expression
                stats - None/{"d":int, "h":int, "s":int, "e":[string, int]}
            TYPE:
                Show
            """
            store.Obs.Show.NormalScreens(False)
            store.obs_show_items_window = True
            items = getattr(store, "obs_items_reserve" + str(number))
            renpy.call_screen("obs_items", number, name, items, check, stats)
        
        @definitionsdistributor
        def Inventory(item, type="apply"):
            """
            IN:
                item - string
                type - "apply"
            TYPE:
                Show
            """
            store.Obs.Show.NormalScreens(False)
            store.obs_hover_slot = {"slot":None, "name":"empty", "stats":None}
            renpy.call_screen("obs_inventory", type, item)
        
        @definitionsdistributor
        def Message(name):
            """
            IN:
                name - string
            TYPE:
                Show
            """
            dict = {
                "inventory": [
                    "Теперь вам доступен инвентарь!",
                    "Инвентарь мы сможете пополнять по ходу игры различными вещами, которые могут понадобиться вам по сюжету. Ячейки для предметов ограничены, так что иногда сами предметы нужно будет выбирать с умом."],
                "backpack": [
                    "Вы получили рюкзак!",
                    "Рюкзаки позволяют вам носить гораздо больше вещей с собой. В моде существует несколько разновидностей рюкзаков, и каждый из них в зависимости от качества, будет открывать разное количество ячеек в инвентаре."]}
            store.Obs.Show.NormalScreens(False)
            store.Obs.Play.Sound("obs_lock")
            renpy.call_screen("obs_message", name, dict[name][0], dict[name][1])
        
        @definitionsdistributor
        def Effects(img, alpha=1.0, zorder=100, layer="master", voice=None, sound=None, start_voice=False,  start_sound=False, end_voice=False, end_sound=False, _with=None):
            """
            IN:
                img - string
                alpha - int
                zorder - int
                layer - "master"/"mapoverlay"
                voice - string
                sound - string
                start_voice - int
                start_sound - int
                end_voice - int
                end_sound - int
                _with - expression
            TYPE:
                Show
            """
            if voice:
                store.Obs.Play.Voice(voice, start=start_voice, end=end_voice)
            if sound:
                store.Obs.Play.Sound(sound, start=start_sound, end=end_sound)
            if store.persistent.obs_effects:
                renpy.show(img, at_list=[store.obs_alpha(alpha)], zorder=zorder, layer=layer)
            if _with:
                store.Obs.With.Statement(_with)
        
        @definitionsdistributor
        def Blink():
            """
            TYPE:
                Show
            """
            renpy.hide("unblink", layer="mapoverlay")
            renpy.show("blink", layer="mapoverlay")
        
        @definitionsdistributor
        def Unblink():
            """
            TYPE:
                Show
            """
            renpy.hide("blink", layer="mapoverlay")
            renpy.show("unblink", layer="mapoverlay")
        
        @definitionsdistributor
        def Blinking():
            """
            TYPE:
                Show
            """
            renpy.show("blinking", layer="mapoverlay")
        
        @definitionsdistributor
        def HeadAttack(img=None):
            """
            IN:
                img - string
            TYPE:
                Show
            """
            if img:
                renpy.music.play(PathMain() + "sound/sfx/obs_squeak.ogg", "sound")
                renpy.show(img, at_list=[store.obs_alpha_linear_return(0.0, 1.0, 2.25, 0.5)], layer="mapoverlay")
                renpy.show("obs_rage_anim", at_list=[store.obs_alpha_linear_return(0.0, 1.0, 2.25, 0.5)], layer="mapoverlay")
                renpy.pause(5, hard=True)
                renpy.hide("obs_int_dining_table_sunset_miku_blur", layer="mapoverlay")
                renpy.hide("obs_rage_anim", layer="mapoverlay")
                renpy.hide(img, layer="mapoverlay")
            else:
                renpy.show("obs_rage_anim", at_list=[store.obs_alpha_linear(0.0, 1.0, 1.0)])
                store.Obs.With.Shake(1.0, 20)
                store.Obs.Play.Sound("obs_head_heartbeat", 1, start=1.0, end=3.0)
                renpy.with_statement(store.flash_red)
                renpy.show("obs_rage_anim", at_list=[store.obs_alpha_linear(1.0, 0.0, 1.5)])
        
        @definitionsdistributor
        def CardsGame(label, name):
            """
            IN:
                label - string
                name - string
            TYPE:
                Show
            """
            renpy.scene()
            renpy.show("black")
            renpy.with_statement(store.obs_blinds_up)
            renpy.pause(0.5, hard=True)
            store.VISIBLE = True
            store.INVISIBLE = False
            replace = {"msk":"Dv", "un":"Un", "aln":"Us"}
            prefix = "obs_" if name in ["msk", "aln"] else ""
            dialogs = {(0, "win","jump"):label + "." + name + "_win",
                       (0, "fail","jump"):label + "." + name + "_fail",
                       (0, "draw","jump"):label + "." + name + "_draw"}
            store.generate_cards("bg obs_int_house_of_aln_cards_desk", dialogs)
            store.rival = getattr(store, "CardGameRival" + replace[name])(getattr(store, prefix + name + "_avatar_set"), Rename(name))
            renpy.jump("cards_gameloop")
        
        @definitionsdistributor
        def Timer(time):
            """
            IN:
                time - int
            TYPE:
                Show
            """
            renpy.hide_screen("obs_timer")
            renpy.show_screen("obs_timer", time)
        
        @definitionsdistributor
        def BlockDissmiss():
            """
            TYPE:
                Show
            """
            store.obs_game_menu = False
            store.obs_actions["block_dissmiss"] = True
        
        @definitionsdistributor
        def Text(text, size, linear=0, time=0, x=0.5, y=0.5, color="#FFFFFF", type="alpha", number=1, font=None, pause=True, _with=None):
            """
            IN:
                text - string
                color - string
                size - int
                at - transform
                time - int
                xal - int
                yal - int
                type - "alpha"/"normal"
                number - int
                pause - True/False
                _with - expression
            TYPE:
                Show
            """
            if not font:
                font = store.obs_normal_font
            if type != "normal":
                at = store.obs_text_alpha_in(linear)
            else:
                at = []
            renpy.show_screen("obs_normal_text_anim" + str(number), text, color, size, at, x, y, font)
            if type != "normal" and pause:
                renpy.pause(time, hard=True)
            if type == "alpha":
                at = store.obs_text_alpha_out(linear)
                renpy.show_screen("obs_normal_text_anim" + str(number), text, color, size, at, x, y, font)
            if type != "normal" and pause:
                renpy.pause(time, hard=True)
            if type == "alpha" and pause:
                renpy.hide_screen("obs_normal_text_anim" + str(number))
            if _with:
                renpy.with_statement(_with)
        
        @definitionsdistributor
        def Clicked(name, *args):
            """
            IN:
                name - string
                *args
            TYPE:
                Show
            """
            renpy.show_screen("obs_clicked_text")
            renpy.call_screen("obs_clicked", name, *args)
            renpy.hide_screen("obs_clicked_text")







    class Hide(object):
        
        @definitionsdistributor
        def Image(name, layer="master", _with=None):
            """
            IN:
                name - string
                layer - string
                _with - expression
            TYPE:
                Hide
            """
            renpy.hide(name, layer=layer)
            if _with:
                store.Obs.With.Statement(_with)
        
        @definitionsdistributor
        def Screen(name, _with=None):
            """
            IN:
                name - string
                _with - expression
            TYPE:
                Hide
            """
            renpy.hide_screen(name)
            renpy.transition(_with)
        
        @definitionsdistributor
        def Screens(fast=False, check=True, pause=True):
            """
            IN:
                fast - True/False
                check - True/False
                pause - True/False
            TYPE:
                Hide
            """
            if check: store.obs_screens = False
            time = 0.25 if fast else 0.5
            renpy.show_layer_at(store.obs_hidescreens(time), layer="screens")
            if pause: renpy.pause(time, hard=True)
            renpy.show_layer_at(store.obs_screen_normal(0), layer="screens")
            store._window_hide(None)
        
        @definitionsdistributor
        def Effects(img, layer="master", _with=None):
            """
            IN:
                img - string
                layer - "master"/"mapoverlay"
                _with - expression
            TYPE:
                Hide
            """
            renpy.hide(img, layer=layer)
            if _with:
                store.Obs.With.Statement(_with)
        
        @definitionsdistributor
        def Blink():
            """
            TYPE:
                Hide
            """
            renpy.hide("blink", layer="mapoverlay")
        
        @definitionsdistributor
        def Unblink():
            """
            TYPE:
                Hide
            """
            renpy.hide("unblink", layer="mapoverlay")
        
        @definitionsdistributor
        def Blinking():
            """
            TYPE:
                Hide
            """
            renpy.hide("blinking", layer="mapoverlay")
        
        @definitionsdistributor
        def BlockDissmiss():
            """
            TYPE:
                Hide
            """
            store.obs_game_menu = True
            store.obs_actions["block_dissmiss"] = False
        
        @definitionsdistributor
        def Text(_with=None):
            """
            IN:
                _with - expression
            TYPE:
                Hide
            """
            renpy.hide_screen("obs_normal_text_anim1")
            if _with:
                renpy.with_statement(_with)







    class Play(object):
        
        @definitionsdistributor
        def Sound(audio, fadein=False, fadeout=False, loop=False, start=False, end=False, restart=False, switch=False, check=True):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Play
            """
            store.Obs.Settings.Audio("sound", audio, fadein, fadeout, loop, start, end, restart, switch, check)
        
        @definitionsdistributor
        def Sound2(audio, fadein=False, fadeout=False, loop=False, start=False, end=False, restart=False, switch=False, check=True):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Play
            """
            store.Obs.Settings.Audio("sound2", audio, fadein, fadeout, loop, start, end, restart, switch, check)
        
        @definitionsdistributor
        def Sound3(audio, fadein=False, fadeout=False, loop=False, start=False, end=False, restart=False, switch=False, check=True):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Play
            """
            store.Obs.Settings.Audio("sound3", audio, fadein, fadeout, loop, start, end, restart, switch, check)
        
        @definitionsdistributor
        def Voice(audio, fadein=False, fadeout=False, loop=False, start=False, end=False, restart=False, switch=False, check=True):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Play
            """
            store.Obs.Settings.Audio("vocal", audio, fadein, fadeout, loop, start, end, restart, switch, check)
        
        @definitionsdistributor
        def Voice2(audio, fadein=False, fadeout=False, loop=False, start=False, end=False, restart=False, switch=False, check=True):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Play
            """
            store.Obs.Settings.Audio("vocal2", audio, fadein, fadeout, loop, start, end, restart, switch, check)
        
        @definitionsdistributor
        def SoundLoop(audio, fadein=False, fadeout=False, loop=True, start=False, end=False, restart=False, switch=False, check=True):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Play
            """
            store.Obs.Settings.Audio("sound_loop", audio, fadein, fadeout, loop, start, end, restart, switch, check)
        
        @definitionsdistributor
        def SoundLoop2(audio, fadein=False, fadeout=False, loop=True, start=False, end=False, restart=False, switch=False, check=True):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Play
            """
            store.Obs.Settings.Audio("sound_loop2", audio, fadein, fadeout, loop, start, end, restart, switch, check)
        
        @definitionsdistributor
        def Music(audio, fadein=False, fadeout=False, loop=True, start=False, end=False, restart=False, switch=False, check=True):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Play
            """
            store.Obs.Settings.Audio("music", audio, fadein, fadeout, loop, start, end, restart, switch, check)
        
        @definitionsdistributor
        def Music2(audio, fadein=False, fadeout=False, loop=True, start=False, end=False, restart=False, switch=False, check=True):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Play
            """
            store.Obs.Settings.Audio("music2", audio, fadein, fadeout, loop, start, end, restart, switch, check)
        
        @definitionsdistributor
        def Ambience(audio, fadein=False, fadeout=False, loop=True, start=False, end=False, restart=False, switch=False, check=True):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Play
            """
            store.Obs.Settings.Audio("ambience", audio, fadein, fadeout, loop, start, end, restart, switch, check)
        
        @definitionsdistributor
        def Ambience2(audio, fadein=False, fadeout=False, loop=True, start=False, end=False, restart=False, switch=False, check=True):
            """
            IN:
                audio - audio
                fadein - True/False
                fadeout - True/False
                loop - True/False
                start - int
                end - int
                restart - int
                switch - int
                check - True/False
            TYPE:
                Play
            """
            store.Obs.Settings.Audio("ambience2", audio, fadein, fadeout, loop, start, end, restart, switch, check)







    class Stop(object):
        
        @definitionsdistributor
        def Sound(fadeout=False):
            """
            IN:
                fadeout - int
            TYPE:
                Stop
            """
            renpy.music.stop("sound", fadeout)
        
        @definitionsdistributor
        def Sound2(fadeout=False):
            """
            IN:
                fadeout - int
            TYPE:
                Stop
            """
            renpy.music.stop("sound2", fadeout)
        
        @definitionsdistributor
        def Sound3(fadeout=False):
            """
            IN:
                fadeout - int
            TYPE:
                Stop
            """
            renpy.music.stop("sound3", fadeout)
        
        @definitionsdistributor
        def Voice(fadeout=False):
            """
            IN:
                fadeout - int
            TYPE:
                Stop
            """
            renpy.music.stop("sound2", fadeout)
        
        @definitionsdistributor
        def Voice2(fadeout=False):
            """
            IN:
                fadeout - int
            TYPE:
                Stop
            """
            renpy.music.stop("sound3", fadeout)
        
        @definitionsdistributor
        def SoundLoop(fadeout=False, check=True):
            """
            IN:
                fadeout - int
                check - True/False
            TYPE:
                Stop
            """
            if check: store.obs_latest_play["sound_loop"] = None
            renpy.music.stop("sound_loop", fadeout)
        
        @definitionsdistributor
        def SoundLoop2(fadeout=False, check=True):
            """
            IN:
                fadeout - int
                check - True/False
            TYPE:
                Stop
            """
            if check: store.obs_latest_play["sound_loop2"] = None
            renpy.music.stop("sound_loop2", fadeout)
        
        @definitionsdistributor
        def Music(fadeout=False, check=True):
            """
            IN:
                fadeout - int
                check - True/False
            TYPE:
                Stop
            """
            if check: store.obs_latest_play["music"] = None
            renpy.music.stop("music", fadeout)
        
        @definitionsdistributor
        def Music2(fadeout=False, check=True):
            """
            IN:
                fadeout - int
                check - True/False
            TYPE:
                Stop
            """
            if check: store.obs_latest_play["music"] = None
            renpy.music.stop("sound_loop", fadeout)
        
        @definitionsdistributor
        def Ambience(fadeout=False, check=True):
            """
            IN:
                fadeout - int
                check - True/False
            TYPE:
                Stop
            """
            if check: store.obs_latest_play["ambience"] = None
            renpy.music.stop("ambience", fadeout)
        
        @definitionsdistributor
        def Ambience2(fadeout=False, check=True):
            """
            IN:
                fadeout - int
                check - True/False
            TYPE:
                Stop
            """
            if check: store.obs_latest_play["ambience2"] = None
            renpy.music.stop("sound_loop2", fadeout)
        
        @definitionsdistributor
        def All(fadeout=False, check=True):
            """
            IN:
                fadeout - int
                check - True/False
            TYPE:
                Stop
            """
            if check:
                for channel in ["sound_loop", "sound_loop2", "music", "ambience", "ambience2"]:
                    store.obs_latest_play[channel] = None
            for channel in ["sound", "sound2", "sound3", "sound_loop", "sound_loop2", "music", "ambience"]:
                renpy.music.stop(channel, fadeout)







    class Set(object):
        
        @definitionsdistributor
        def Day(name):
            """
            IN:
                name - string
            TYPE:
                Set
            """
            ground = Replace(name, ["День ", "day", "Пролог", "prologue", "???", "none", "Вступление", "none"])
            label = {"Вступление":".",
                     "Пролог":"С чего всё начиналось.",
                     "День 1":"Знакомство с лагерем.",
                     "День 2":"Ещё больше загадок.",
                     "День 3":"Затишье перед бурей."}[name]
            store.obs_day = [name, ground, name + (": " if label != "." else "") + label]
        
        @definitionsdistributor
        def DayTime(type, day=True, sprites=True):
            """
            IN:
                type - "day"/"sunset"/"night"/"prologue"/"rain"
                day - True/False
                sprites - True/False
            TYPE:
                Set
            """
            if day:
                store.obs_timeofday = type
            if type == "prologue":
                type == "day"
            if sprites:
                store.obs_sprite_time = type
            store.persistent.sprite_time = store.obs_sprite_time
            store.config.mouse = {"default" : [(PathImg() + "gui/mouse/" + store.obs_timeofday + ".png", 0, 0)]}
            store.obs_config_mouse = store.config.mouse
        
        @definitionsdistributor
        def Clothes(name, type):
            """
            IN:
                name - string
                type - string
            TYPE:
                Set
            """
            store.obs_clothes_dict[name] = type
        
        @definitionsdistributor
        def Hair(name, type):
            """
            IN:
                name - string
                type - string
            TYPE:
                Set
            """
            store.obs_hair_dict[name] = type
        
        @definitionsdistributor
        def Volume(number, channel):
            """
            IN:
                number - int
                channel - string
            TYPE:
                Set
            """
            store.volume(number, channel)
        
        @definitionsdistributor
        def ModeNvl(window=False, pause=True):
            """
            IN:
                window - True/False
                pause - True/False
            TYPE:
                Set
            """
            if window:
                store.Obs.Hide.Screens(pause=pause)
            else:
                store.Obs.Show.NotScreens()
            renpy.pause(0.4, hard=True)
            store.Obs.Screens(store.obs_show_nvl)
            store.nvl_clear()
            store.menu = store.nvl_menu
            store.narrator_nvl = store.narrator
            store.th_nvl = store.th
            store.Obs.Settings.ReloadNames(False, True)
        
        @definitionsdistributor
        def ModeAdv(window=False, pause=True):
            """
            IN:
                window - True/False
                pause - True/False
            TYPE:
                Set
            """
            if pause:
                store.Obs.Screens(store.obs_hide_nvl)
            store._window_hide(store.obs_dissolve4 if pause else None)
            store.nvl_clear()
            store.menu = store.renpy.display_menu
            store.Obs.Settings.ReloadNames(False)
            if window:
                store.Obs.Show.Screens(pause=pause)
        
        @definitionsdistributor
        def InventorySlots(name, is_from, is_to):
            """
            IN:
                name = "empty"/"lock"
                is_from - int
                is_to - int
            TYPE:
                Set
            """
            for slot in range(is_from, is_to):
                store.obs_inventory[slot] = {"slot":slot, "name":name, "stats":None}
        
        @definitionsdistributor
        def ItemEmpty(number, item):
            """
            IN:
                number - int
                item - int
            TYPE:
                Set
            """
            name = getattr(store, "obs_items_reserve" + str(number))
            name[item] = {"slot":name[item]["slot"], "name":"empty"}
        
        @definitionsdistributor
        def ItemsList(*args):
            """
            IN:
                *args
            TYPE:
                Set
            """
            store.obs_items_seen = {}
            for key in range(1, 17):
                store.obs_items_seen.setdefault(str(key), False)
            for num in range(0, len(args)+1):
                setattr(store, "obs_items_reserve" + str(num+1), [])
                for n in range(0, 9):
                    getattr(store, "obs_items_reserve" + str(num+1)).append({"slot":n, "name":"empty"})
            for item in range(0, len(args)):
                getattr(store, "obs_items_reserve" + str(item+1))[args[item][0]] = {"slot":args[item][0], "name":args[item][1], "stats":args[item][2] if len(args[item]) == 3 else None}
        
        @definitionsdistributor
        def MusicChange(audio, type="normal"):
            """
            IN:
                audio - audio
                type - "normal"/"changed"
            TYPE:
                Set
            """
            path = store.music_list[audio] if "obs_" not in audio else PathMain() + "sound/music/" + audio + ".ogg"
            pos = renpy.music.get_pos(channel="music" if type == "changed" else "sound_loop2")
            pos = 0 if not pos else pos
            currentpos = Settings.MusicPos()
            name = "<from " + str(currentpos) + " loop 4.444>" + path
            if type == "changed":
                renpy.music.stop("music", 1.0)
                renpy.music.play(name, "sound_loop2", fadein=1.0, tight=True)
            else:
                renpy.music.stop("sound_loop2", 1.0)
                renpy.music.play(name, fadein=1.0)
        
        @definitionsdistributor
        def Quest(name, type=None):
            """
            IN:
                name - None/string
                type - "start"/"end"/True/False/string
            TYPE:
                Set
            """
            if type == "start":
                store.obs_quest = {"name":[name, False if type == "start" else True], "objectives":[], "move":[]}
                renpy.show_screen("obs_quest", _layer="front")
                renpy.pause(1.0, hard=True)
            elif type == "end":
                store.obs_quest["name"][1] = True
            elif type in [True, False]:
                if type:
                    for item in range(0, len(store.obs_quest["objectives"])):
                        if store.obs_quest["objectives"][item][0] == name:
                            store.obs_quest["objectives"][item][1] = True
                    renpy.music.play(PathMain() + "sound/sfx/obs_wink.ogg", "sound2")
                else:
                    store.obs_quest["objectives"].append([name, type])
                    store.obs_quest["move"].append(False)
            else:
                renpy.show_layer_at(store.obs_xoffset_ease(0, -500, 1.0), layer="front")
                renpy.pause(1.0, hard=True)
                renpy.hide_screen("obs_quest", layer="front")
                renpy.show_layer_at(store.obs_xoffset(0), layer="front")
        
        @definitionsdistributor
        def NewChapter(name):
            """
            IN:
                name - string
            TYPE:
                Set
            """
            renpy.scene()
            renpy.show("obs_intro_" + name)
            renpy.show("obs_intro_" + name.replace("1", "") + "_layer", zorder=10)
            renpy.music.play(PathMain() + "sound/music/obs_lunar_anguish.ogg", "music", fadein=5)
            renpy.with_statement(store.fade3)
            renpy.show("obs_intro_" + name + "_day", at_list=[store.obs_name_move(1.0, -0.11, 0.35)])
            renpy.show("obs_intro_" + name + "_name", at_list=[store.obs_name_move2(1.0, 0.11, -0.35)])
            renpy.pause(8, hard=True)
            renpy.scene()
            renpy.show("black")
            renpy.music.stop("music", 5)
            renpy.with_statement(store.fade3)
            renpy.pause(3, hard=True)







    class Call(object):
        
        @definitionsdistributor
        def Screen(name, layer="screens", _with=None, with_return=True, **kwargs):
            """
            IN:
                name - string
                layer - string
                _with - expression
                with_return - True/False
                **kwargs
            TYPE:
                Call
            """
            _exceptions = (renpy.game.JumpException, renpy.game.CallException)
            renpy.mode("screen")
            renpy.show_screen(name, _layer=layer, **kwargs)
            renpy.transition(_with)
            try:
                result = renpy.ui.interact(
                    mouse="screen",
                    type="screen",
                    roll_forward=renpy.roll_forward_info()
                )
            except _exceptions as exc:
                result = exc
            renpy.hide_screen(name, layer=layer)
            if with_return:
                renpy.transition(_with)
            renpy.exports.checkpoint(result)
            if isinstance(result, _exceptions):
                raise result
            return result
        
        @definitionsdistributor
        def Label(label, *args, **kwargs):
            """
            IN:
                label - string
                *args
                **kwargs
            TYPE:
                Call
            """
            renpy.call(label, *args, **kwargs)







    class Jump(object):
        
        @definitionsdistributor
        def Label(label, check=False):
            """
            IN:
                label - string
                check - True/False
            TYPE:
                Jump
            """
            if "items_start" in label and check and store.config.developer and "Одержимая Remastered" in store.config.basedir:
                store.obs_label = label
                renpy.jump("obs_interactive_choice")
            renpy.jump(label)
        
        @definitionsdistributor
        def LabelOutOfContext(label):
            """
            IN:
                label - string
            TYPE:
                Jump
            """
            renpy.jump_out_of_context(label)







    class Scene(object):
        
        @definitionsdistributor
        def Image(name, at=[], expr=None, voice=None, sound=None, start_voice=False, start_sound=False,
                  end_voice=False, end_sound=False, _with=None):
            """
            IN:
                name - string
                at = expression
                expr - string
                voice - string
                sound - string
                start_voice - int
                start_sound - int
                end_voice - int
                end_sound - int
                _with - expression
            TYPE:
                Scene
            """
            renpy.scene()
            store.Obs.Show.Image(name=name, at=at, expr=expr, voice=voice, sound=sound, start_voice=start_voice, start_sound=start_sound, end_voice=end_voice, end_sound=end_sound, _with=_with)
        
        @definitionsdistributor
        def Clear():
            """
            TYPE:
                Scene
            """
            for layer in ["underlay", "master", "screens", "mapoverlay", "front"]:
                renpy.scene(layer)
        
        @definitionsdistributor
        def Function(func, *args, **kwargs):
            """
            IN:
                func - expression
                *args
                **kwargs
            TYPE:
                Scene
            """
            func(*args, **kwargs)







    class With(object):
        
        @definitionsdistributor
        def Shake(time=4.0, dist=100):
            """
            IN:
                time - int
                dist - int
            TYPE:
                Show
            """
            renpy.with_statement(store.Shake((0, 0, 0, 0), time, None, dist))
        
        @definitionsdistributor
        def Statement(trans, always=False):
            """
            IN:
                trans - expression
                always - True/False
            TYPE:
                With
            """
            if Type(trans) != "RevertableList":
                renpy.with_statement(trans, always)
            else:
                store.Obs.Settings.BlackTransition(trans)







    class Action(object):
        
        @definitionsdistributor
        def NewContext():
            """
            TYPE:
                Action
            """
            renpy.hide_screen("obs_timer")
            renpy.call("obs_new_context")







    @statementregister
    def Say(who, image="", what="", voice=None, sound=None, start_voice=False, start_sound=False,
            end_voice=False, end_sound=False, at=[], behind=[], zorder=0, master=None, screens=None,
            interact=True, cps=None, bold=False, font=None, timer=None, veiled=False, extend=None,
            dis=False, trans="", show_effect=None, hide_effect=None, _with=None):
        """
        IN:
            who - <character> / <text>
            image - <emotion> <extra> <distance> / <text>
            what - <text>
            voice - string
            sound - string
            start_voice - int
            start_sound - int
            end_voice - int
            end_sound - int
            at - expression
            behind - string
            zorder - int
            master - expression
            screens - expression
            interact - True/False
            cps - int
            bold - int
            font - expression
            timer - int
            extend - "save"/True
            dis - True/False
            trans - expression
            show_effect - string
            hide_effect - string
            _with - expression
        TYPE:
            Statement
        """
        if voice:
            store.Obs.Play.Voice(voice, start=start_voice, end=end_voice)
        if sound:
            store.Obs.Play.Sound(sound, start=start_sound, end=end_sound)
        if who not in store.names_list and who not in store.obs_names_list:
            what = who ; who = store.narrator
        else:
            prefix = who.replace("_red", "")
            if not IsOnlyAlpha(image, "eng"):
                what = image ; image = ""
            who = getattr(store, ("obs_" if who in store.obs_names_list else "") + who)
        behind = behind if behind != [] else []
        zorder = zorder if zorder != 0 else 0
        if image:
            store.Obs.Show.Image(prefix + " " + image, behind=behind, zorder=zorder, at=at, _with=False)
        if master:
            if master in [store.obs_screen_attack, store.obs_screen_attack_hard]:
                store.Obs.Master()
            store.Obs.Master(master, False)
        if screens:
            store.Obs.Screens(screens, True)
        if trans != None and image and not _with and (not at or (at and trans)):
            trans = store.dspr if trans == "" else trans
            renpy.with_statement(trans)
        what = "{font=" + getattr(store, "obs_" + font + "_font") + "}" + what + "{/font}" if font else what
        what = "{cps=" + str(cps) + "}" + what + "{/cps}" if cps else what
        what = "{b}" + what + "{/b}" if bold else what
        what = TextTags(TextSwear(what, veiled))
        if timer:
            renpy.hide_screen("obs_timer")
            renpy.show_screen("obs_timer", timer)
        if extend == "save":
            store.obs_save_text = Replace(what, ["{fast}", "", "{nw}", "", "{w}", ""])
        elif extend == True:
            what = store.obs_save_text + "{fast}" + what
            store.obs_save_text = Replace(what, ["{fast}", "", "{nw}", "", "{w}", ""])
        if dis:
            renpy.pause(0.1, hard=True)
            _with = store.obs_dissolve8
        elif show_effect:
            store.Obs.Show.Image("obs_" + show_effect, layer="mapoverlay", at=store.obs_alpha_linear(0.0, 1.0, 1.0))
        elif hide_effect:
            store.Obs.Show.Image("obs_" + hide_effect, layer="mapoverlay", at=store.obs_alpha_linear(1.0, 0.0, 1.0))
        if _with or store.menu == store.nvl_menu:
            renpy.call("obs_say", who, what, _with)
        else:
            renpy.say(who, what, interact)

    @statementregister
    def AutoSave(name="", auto=True, text=True, force=False):
        """
        IN:
            name - string
            auto - True/False
            text - True/False
            force - True/False
        TYPE:
            Statement
        """
        if text:
            prefix = (". " + store.obs_day[0]) if store.obs_day[0] else ""
            store.save_name = "{size=-5}" + store.obs_config_mod_name + prefix + ".\n" + name + "{/size}"
        if (auto and store.persistent.obs_autosaves and not store.obs_after_load) or force:
            renpy.loadsave.cycle_saves("obs_FilePage_auto-", 12)
            if not force:
                renpy.take_screenshot()
                renpy.hide_screen("obs_autosave")
                renpy.show_screen("obs_autosave")
            renpy.save("obs_FilePage_auto-1", store.save_name)
            if not force:
                renpy.pause(0.1, hard=True)

    @statementregister
    def Load(time):
        """
        IN:
            time - int
        TYPE:
            Statement
        """
        dict = {"Пролог":"obs_depression", "День 1":"obs_wood", "???":"obs_title"}
        store.Obs.Stop.All(check=False)
        store.Obs.Front(store.obs_alpha(0.0))
        store.Obs.Show.BlockDissmiss()
        if store.obs_screens:
            store._window_hide()
        reserve = store.obs_timeofday
        store.Obs.Set.DayTime("day")
        renpy.show("black", tag="extra", zorder=100, layer="mapoverlay")
        renpy.with_statement(store.dissolve2)
        store.Obs.Pause(1)
        store.load_value = 0
        store.Obs.Play.Music(dict[store.obs_day[0].replace("Вступление", "???")], 2, check=False)
        renpy.show_layer_at(store.obs_showscreens(0.5), layer="screens")
        renpy.call_screen("obs_loading", time=time) 
        store.Obs.Pause(2)
        renpy.hide("extra", layer="mapoverlay")
        renpy.with_statement(store.config.after_load_transition)
        for name in ["music", "ambience", "ambience2", "sound_loop", "sound_loop2"]:
            if store.obs_latest_play[name]:
                getattr(store.Obs.Play, name.title().replace("_", ""))(store.obs_latest_play[name], 1)
        store.Obs.Front(store.obs_alpha(1.0))
        store.Obs.Hide.BlockDissmiss()
        store.Obs.Set.DayTime(reserve)
        if store.obs_screens:
            store.Obs.Show.Screens()

    @statementregister
    def Pause(delay=None, music=None, with_none=None, hard=True, checkpoint=None):
        """
        IN:
            delay - int
            music - True/False
            with_none - True/False
            hard - True/False
            checkpoint - True/False
        TYPE:
            Statement
        """
        if not delay:
            renpy.ui.saybehavior(afm=" ")
            renpy.ui.interact(mouse="pause", type="pause", roll_forward=None)
            return
        if delay <= 0:
            return
        renpy.pause(delay, music, with_none, hard, checkpoint)

    @statementregister
    def Return(restart=False, check=True):
        """
        IN:
            restart - True/False
            check - True/False
        TYPE:
            Statement
        """
        if restart:
            store.obs_before_main_menu = True
            renpy.jump(store.obs_config_label)
        elif store.obs_return and check:
            renpy.jump(store.obs_return)
        renpy.return_statement()

    @statementregister
    def Pass():
        """
        TYPE:
            Statement
        """
        pass

    @statementregister
    def Local(name, value):
        """
        IN:
            name - string
            value - string/expression/int
        TYPE:
            Statement
        """
        renpy.dynamic(name)
        setattr(store, name, value)

    @statementregister
    def Global(name, value):
        """
        IN:
            name - string
            value - string/expression/int
        TYPE:
            Statement
        """
        setattr(store, name, value)

    @statementregister
    def GlobalDict(name, key, value):
        """
        IN:
            name - string
            key - string
            value - string/expression/int
        TYPE:
            Statement
        """
        getattr(store, name)[key] = value

    @statementregister
    def GlobalDictList(name, key, item, value):
        """
        IN:
            name - string
            key - string
            item - string
            value - string/expression/int
        TYPE:
            Statement
        """
        getattr(store, name)[key][item] = value

    @statementregister
    def GlobalField(object, name, value):
        """
        IN:
            object - expression
            name - string
            value - string/expression/int
        TYPE:
            Statement
        """
        setattr(object, name, value)

    @statementregister
    def GlobalFieldDict(object, name, key, value):
        """
        IN:
            object - expression
            name - string
            key - string
            value - string/expression/int
        TYPE:
            Statement
        """
        getattr(object, name)[key] = value

    @statementregister
    def GlobalFieldDictList(object, name, key, item, value):
        """
        IN:
            object - expression
            name - string
            key - string
            item - string
            value - string/expression/int
        TYPE:
            Statement
        """
        getattr(object, name)[key][item] = value

    @statementregister
    def Default(name, value):
        """
        IN:
            name - string
            value - string/expression/int
        TYPE:
            Statement
        """
        try:
            getattr(store, name)
        except:
            setattr(store, name, value)

    @statementregister
    def DefaultField(object, name, value):
        """
        IN:
            object - expression
            name - string
            value - string/expression/int
        TYPE:
            Statement
        """
        if not getattr(object, name):
            setattr(object, name, value)

    @statementregister
    def Delete(*args):
        """
        IN:
            *args
        TYPE:
            Statement
        """
        try:
            for name in args:
                delattr(store, name)
        except:
            pass

    @statementregister
    def Underlay(at=None, reset=True):
        """
        IN:
            at - expression
            reset - True/False
        TYPE:
            Statement
        """
        at = store.obs_screen_normal(0) if not at else TransformsCheckList(at)
        renpy.show_layer_at(at, "underlay", reset)

    @statementregister
    def Master(at=None, reset=True, voice=None, sound=None, start_voice=False,  start_sound=False, end_voice=False, end_sound=False, _with=None):
        """
        IN:
            at - expression
            reset - True/False
            voice - string
            sound - string
            start_voice - int
            start_sound - int
            end_voice - int
            end_sound - int
            _with - expression
        TYPE:
            Statement
        """
        at = store.obs_screen_normal(0) if not at else TransformsCheckList(at)
        renpy.show_layer_at(at, "master", reset)
        if voice:
            store.Obs.Play.Voice(voice, start=start_voice, end=end_voice)
        if sound:
            store.Obs.Play.Sound(sound, start=start_sound, end=end_sound)
        if _with:
            store.Obs.With.Statement(_with)

    @statementregister
    def Mapoverlay(at=None, reset=True):
        """
        IN:
            at - expression
            reset - True/False
        TYPE:
            Statement
        """
        at = store.obs_screen_normal(0) if not at else TransformsCheckList(at)
        renpy.show_layer_at(at, "mapoverlay", reset)

    @statementregister
    def Widgetoverlay(at=None, reset=True):
        """
        IN:
            at - expression
            reset - True/False
        TYPE:
            Statement
        """
        at = store.obs_screen_normal(0) if not at else TransformsCheckList(at)
        renpy.show_layer_at(at, "widgetoverlay", reset)

    @statementregister
    def Transient(at=None, reset=True):
        """
        IN:
            at - expression
            reset - True/False
        TYPE:
            Statement
        """
        at = store.obs_screen_normal(0) if not at else TransformsCheckList(at)
        renpy.show_layer_at(at, "transient", reset)

    @statementregister
    def Screens(at=None, reset=True):
        """
        IN:
            at - expression
            reset - True/False
        TYPE:
            Statement
        """
        at = store.obs_screen_normal(0) if not at else TransformsCheckList(at)
        renpy.show_layer_at(at, "screens", reset)

    @statementregister
    def Front(at=None, reset=True):
        """
        IN:
            at - expression
            reset - True/False
        TYPE:
            Statement
        """
        at = store.obs_screen_normal(0) if not at else TransformsCheckList(at)
        renpy.show_layer_at(at, "front", reset)

    @statementregister
    def Overlay(at=None, reset=True):
        """
        IN:
            at - expression
            reset - True/False
        TYPE:
            Statement
        """
        if not at:
            at=store.obs_screen_normal(0)
        else:
            at = TransformsCheckList(at)
        renpy.show_layer_at(at, "overlay", reset)

    @statementregister
    def Onlyoverlay(at=None, reset=True):
        """
        IN:
            at - expression
            reset - True/False
        TYPE:
            Statement
        """
        at = store.obs_screen_normal(0) if not at else TransformsCheckList(at)
        renpy.show_layer_at(at, "onlyoverlay", reset)







    @statementregister
    def PathMain():
        """
        TYPE:
            Dysplayable
        """
        return store.obs_config_folder

    @statementregister
    def PathImg():
        """
        TYPE:
            Dysplayable
        """
        return store.obs_config_folder + "images/"

    @statementregister
    def PathSpr():
        """
        TYPE:
            Dysplayable
        """
        return store.obs_config_folder + "images/sprites/"

    @statementregister
    def PathDef():
        """
        TYPE:
            Dysplayable
        """
        return "/images/sprites/"

    @statementregister
    def IsModActive():
        """
        TYPE:
            Dysplayable
        """
        return store.save_name.find(store.obs_config_mod_name) != -1

    @statementregister
    def IsPresentAlpha(name, type):
        """
        IN:
            name - string
            type - "rus"/"eng"
        TYPE:
            Dysplayable
        """
        letters = "[а-яА-Я]+" if type == "rus" else "[a-zA-Z]+"
        return bool(re.compile(letters).findall(name))

    @statementregister
    def IsOnlyAlpha(name, type):
        """
        IN:
            name - string
            type - "rus"/"eng"
        TYPE:
            Dysplayable
        """
        dict = {"rus":"eng", "eng":"rus"}
        symbols = bool(re.compile("[{}\"..]").findall(name))
        return IsPresentAlpha(name, type) and not IsPresentAlpha(name, dict[type]) and not symbols

    @statementregister
    def ImageDissolve(name, time, rabmlen=0):
        """
        IN:
            name - string
            time - int
            rabmlen - int
        TYPE:
            Dysplayable
        """
        reverse = False if "_alt" not in name else True
        name = Replace(name, ["_alt", ""])
        return store.ImageDissolve(PathImg() + "transitions/obs_" + name + ".png", time, ramplen=rabmlen, reverse=reverse)

    @statementregister
    def MultipleTransition(name, time, pause, rabmlen=0, alt=True):
        """
        IN:
            name - string
            time - int
            pause - int
            rabmlen - int
            alt - True/False
        TYPE:
            Dysplayable
        """
        return store.MultipleTransition([
            False, ImageDissolve(name, time, rabmlen) if Type(name) == "unicode" else name,
            store.Solid("#000"), store.Pause(pause),
            store.Solid("#000"), ImageDissolve(name + ("_alt" if alt else ""),
            time, rabmlen) if Type(name) == "unicode" else name,
            True])

    @statementregister
    def Rename(name):
        """
        IN:
            name - string
        TYPE:
            Dysplayable
        """
        dict = {"night":"day", "rain":"prologue", "msk":"Мишка", "un":"Лена", "aln":"Алёна"}
        if name in dict:
            return dict[name]
        else:
            return name

    @statementregister
    def Replace(name, args=[]):
        """
        IN:
            name - string
            args - [string, string]
        TYPE:
            Dysplayable
        """
        for item in range(0, len(args), 2):
            name = name.replace(args[item], args[item+1])
        return name

    @statementregister
    def Type(name):
        """
        IN:
            name - expression
        TYPE:
            Dysplayable
        """
        if "renpy" in str(type(name)):
            return str(type(name))[str(type(name)).rfind(".")+1:-2]
        elif "NVLCharacter" in str(type(name)):
            return "NVLCharacter"
        elif "class" in str(type(name)):
            return "class"
        elif "RevertableDict" in str(type(name)):
            return "RevertableDict"
        else:
            return str(type(name))[7:-2]

    @statementregister
    def SecondsCounter(name, visible="seconds", add_type="minutes", add_time=False):
        """
        IN:
            name - int
            visible - "seconds"/"minutes"/"hours"
            add_type - "seconds"/"minutes"/"hours"
            add_time - int
        TYPE:
            Dysplayable
        """
        if add_time:
            if add_type == "hours":
                add_time = (add_time * 3600)
            elif add_type == "minutes":
                add_time = (add_time * 60)
            name = name + add_time
            store.obs_time = store.obs_time + add_time
        minutes, seconds = divmod(int(float(name)), 60)
        hours, minutes = divmod(minutes, 60)
        hours = str(hours)
        if len(str(hours)) == 1:
            hours = "0" + str(hours)
        else:
            hours = str(hours)
        if len(str(minutes)) == 1:
            minutes = "0" + str(minutes)
        else:
            minutes = str(minutes)
        if len(str(seconds)) == 1:
            seconds = "0" + str(seconds)
        else:
            seconds = str(seconds)
        if visible == "seconds":
            return hours + ":" + minutes + ":" + seconds
        elif visible == "minutes":
            return hours + ":" + minutes
        else:
            return hours

    @statementregister
    def GameTime(st, at):
        """
        IN:
            st - int
            at - int
        TYPE:
            Dysplayable
        """
        t = datetime.datetime.now()
        dt = t - store.persistent.obs_game_last_time
        store.persistent.obs_game_last_time = t
        store.obs_game_time += dt.total_seconds()
        minutes, seconds = divmod(int(store.obs_game_time), 60)
        hours, minutes = divmod(minutes, 60)
        image = store.Text("%0*d:%0*d:%0*d" % (2, hours, 2, minutes, 2, seconds),
            style="obs_text_extra_" + Rename(store.obs_timeofday), xanchor=0.5, yalign=0.97,
            xalign=0.5, font=store.obs_normal_font, size=35)
        return (image, .1)

    @statementregister
    def SessionTime(st, at):
        """
        IN:
            st - int
            at - int
        TYPE:
            Dysplayable
        """
        t = datetime.datetime.now()
        dt = t - store.persistent.obs_session_last_time
        store.persistent.obs_session_last_time = t
        store.persistent.obs_session_time += dt.total_seconds()
        minutes, seconds = divmod(int(store.persistent.obs_session_time), 60)
        hours, minutes = divmod(minutes, 60)
        image = store.Text("%0*d:%0*d:%0*d" % (2, hours, 2, minutes, 2, seconds),
            style="obs_text_extra_" + Rename(store.obs_timeofday), xanchor=0.5, yalign=0.97,
            xalign=0.5, font=store.obs_normal_font, size=35)
        return (image, .1)

    @statementregister
    def TextSwear(name, veiled):
        """
        IN:
            name - string
            veiled - True/False
        TYPE:
            Dysplayable
        """
        if "<" in name:
            if store.persistent.obs_swear_filter:
                for item in range(0, len(re.findall("<", name))):
                    item = name[name.find("<")+1:name.find(">")].lower()
                    if item in store.obs_swear_dict:
                        if not veiled:
                            if name[name.find("<")+1:name.find(">")].replace(" ", "").istitle():
                                name = name[:name.find("<")] + store.obs_swear_dict[item].title() + name[name.find(">")+1:]
                            elif name[name.find("<")+1:name.find(">")].isupper():
                                name = name[:name.find("<")] + store.obs_swear_dict[item].upper() + name[name.find(">")+1:]
                            else:
                                name = name[:name.find("<")] + store.obs_swear_dict[item] + name[name.find(">")+1:]
                        else:
                            word = name[name.find("<")+1:name.find(">")]
                            if " " in word:
                                name = name[:name.find("<")] + "*" * len(word[:word.find(" ")]) + " " + "*" * len(word[word.find(" ")+1:]) + name[name.find(">")+1:]
                            else:
                                name = name[:name.find("<")] + "*" * len(word) + name[name.find(">")+1:]
            else:
                name = Replace(name, ["<", "", ">", ""])
        return name

    @statementregister
    def TextTags(name):
        """
        IN:
            name - string
        TYPE:
            Dysplayable
        """
        return Replace(name, ["{-}", "{font=" + PathImg() + "gui/font/big.ttf}—{/font}",
                              "{el}", "{w=0.3}.{w=0.3}.{w=0.3}.{w=0.3}",
                              "{el2}", "{w=0.6}.{w=0.6}.{w=0.6}.{w=0.6}",
                              "{break}", "—{w=0.5}{nw}",
                              "{break2}", "—{w=1.0}{nw}",
                              "{ww}", "-{w=0.3}",
                              "{www}", "-{w=0.6}"])

    @statementregister
    def TextSizeFind(name, point, size):
        """
        IN:
            name - string
            point - string
            size - int
        TYPE:
            Dysplayable
        """
        if point in name:
            return "{size=" + str(size) + "}" + name[:name.find(point)+len(point)] + "{/size}" + name[name.find(point)+len(point):]
        else:
            return "{size=" + str(size) + "}" + name + "{/size}"

    @statementregister
    def Random(min=0, max=None):
        """
        IN:
            min - int
            max - int
        TYPE:
            Dysplayable
        """
        if not max:
            max = min ; min = 0
        return store.random.randint(int(min), int(max))

    @statementregister
    def SelectedSlot(name):
        """
        IN:
            name - string/int
        TYPE:
            Dysplayable
        """
        dict = {"BPK":store.obs_backpack, "WPG":store.obs_weapon}
        name = {"slot":name, "name":dict[name]["name"], "stats":dict[name]["stats"]} if name in dict else store.obs_inventory[name]
        return name

    @statementregister
    def ImageNameComponent(l):
        """
        IN:
            l - lexer
        TYPE:
            Dysplayable
        """
        points = [l.checkpoint()]
        rv = [l.require(l.image_name_component)]
        while True:
            points.append(l.checkpoint())
            n = l.image_name_component()
            if not n:
                points.pop()
                break
            rv.append(n.strip())
        points.append(l.checkpoint())
        s = l.simple_expression()
        if s is not None:
            rv.append(unicode(s))
        else:
            points.pop()
        return tuple(rv)

    @statementregister
    def SimpleExpressionList(l):
        """
        IN:
            l - lexer
        TYPE:
            Dysplayable
        """
        rv = [l.require(l.simple_expression)]
        while True:
            if not l.match(","):
                break
            e = l.simple_expression()
            if not e:
                break
            rv.append(e)
        return rv

    @statementregister
    def TransformsCheckList(at):
        """
        IN:
            at - expression
        TYPE:
            Dysplayable
        """
        list = []
        if "," not in str(at).replace("rpy\',", ""):
            list.append(at)
        elif len(at) >= 1:
            for item in range(0, len(at)):
                list.append(at[item])
        return list

    @statementregister
    def ListDir(path, replace="", ignore=[], default=False):
        """
        IN:
            path - string
            replace - string
            ignore - [string]
            default - True/False
        TYPE:
            Dysplayable
        """
        path = getattr(store, "obs_basedir" + ("_default" if default else "")) + path
        if "Steam" in store.obs_basedir and not default:
            if os.path.exists(path[:path.find("common")] + "workshop/content/331470/1985425431/" + path[path.find("mods"):]):
                path = path[:path.find("common")] + "workshop/content/331470/1985425431/" + path[path.find("mods"):]
        if not os.path.isdir(path):
            return None
        list, list2 = os.listdir(path), []
        if ignore:
            ignore = [] + ignore
            for exception in ignore:
                for repeat in range(0, 5):
                    for item in list:
                        if exception in item:
                            list.remove(item)
        if replace:
            for item in list:
                list2.append(item.replace(replace, ""))
            list = list2
        return list

    @statementregister
    def SpriteSize(name):
        """
        IN:
            name - string
        TYPE:
            Dysplayable
        """
        dict = {"normal":900, "far":630, "close":1050, "veryfar":500}
        return dict[name.split("-")[1]]

    @statementregister
    def SpritePath(name, argument):
        """
        IN:
            name - string
            argument - string
        TYPE:
            Dysplayable
        """
        if argument:
            name = name.split("-")
            argument = argument.split("-")
            extra = "obsessed/" if "obs" in argument[1] else ("blue/" if "blue" in argument[1] else "")
            return (getattr(store.Obs, "Path" + argument[0].title())() + name[1] + "/" + name[0] + "/" +
                    extra + name[0] + "_" + name[2] + "_" + argument[1] + ".png")
        return "obs_none"

    @statementregister
    def SpriteBlinking(name, check, time=None):
        """
        IN:
            name - string
            check - [string, string]
            time - string
        TYPE:
            Dysplayable
        """
        list_un = ["clos_normal", "clos_sad", "clos_sad2", "clos_shy", "clos_smile", "clos_smile2", "grin", "laugh"]
        if name.split("-")[0] == "un" and check[1].split("-")[1] == "body_down_hair":
            eyes = "spr-close_eyes_down_hair"
        else:
            eyes = "spr-close_eyes"
        if name.split("-")[0] == "un" and check[0].split("-")[1] not in list_un:
            if name.split("-")[0] == "un":
                return store.ConditionSwitch("store.persistent.obs_Live2D_sprites_animation",
                    store.Animation(LiveColor("obs_none", time), Float(Random(25, 30))/10,
                        LiveColor(SpritePath(name, eyes), time), 0.1), True, "obs_none")
        return "obs_none"

    @statementregister
    def LiveColor(image, time):
        """
        IN:
            image - string
            time - string
        TYPE:
            Dysplayable
        """
        if image != "obs_none":
            return store.im.MatrixColor(image, obs_tint_dict[time]) if time else image
        return image

    @statementregister
    def Int(name):
        """
        IN:
            name - string
        TYPE:
            Dysplayable
        """
        name = name[:name.find(".")] if "." in name else name
        return int(re.sub("[^0-9]", "", name)) if Type(name) == "unicode" else int(name)

    @statementregister
    def Float(name):
        """
        IN:
            name - string
        TYPE:
            Dysplayable
        """
        return float(re.sub("[^0-9]", "", name)) if Type(name) == "unicode" else float(name)

    @statementregister
    def Num(name):
        """
        IN:
            name - string
        TYPE:
            Dysplayable
        """
        return str(re.sub("[^0-9^..]", "", name))

    @statementregister
    def Str(name, type="value"):
        """
        IN:
            name - expression
            type - "value"/"unicode"/"name"/"class"/"module"/"function"/"IN"/"NOTE"/"TYPE"
        TYPE:
            Dysplayable
        """
        if type not in ["value", "unicode"]:
            if Type(name) == "NoneType":
                return "None"
            elif Type(name) == "class":
                return str(type(name))[8:-2].replace("store.", "")
            elif Type(name) in ["ADVCharacter", "NVLCharacter"]:
                dict = {store.narrator:"narrator", store.th:"th"}
                if name in dict:
                    return dict[name]
                return str(name.name).replace("_name", "").replace("None", "''")
            elif Type(name) == "function":
                doc = name.__doc__ ; dict = {}
                module_ = (name.__module__.replace("store.", "") + ".")
                class_ = (doc[doc.find("TYPE:")+5:].strip() + ".").replace("[].", "")
                function_ = (name.__name__)
                if type == "IN":
                    for item in re.sub("[ ]", "", doc[doc.find("IN:")+3:doc.find("TYPE:")])[1:-1].split("\n"):
                        dict.setdefault(item.split("-")[0], item.split("-")[1])
                    return dict
                elif type == "NOTE":
                    return doc[doc.find("NOTE:")+5:doc.find("IN:")][17:-12]
                elif type == "TYPE":
                    return class_[:-1] if class_[:-1] else "[]"
                elif type == "class":
                    return class_[:-1]
                elif type == "function":
                    return function_
                elif type == "module":
                    return module_[:-1]
                else:
                    return module_ + class_ + function_
            else:
                vars = inspect.currentframe().f_back.f_locals.items()
                return [k for k, v in vars if v is name][0]
        else:
            return str(name)

    @statementregister
    def ListInVar(list, var):
        """
        IN:
            list - string
            var - string
        TYPE:
            Dysplayable
        """
        for item in list:
            if item in var:
                return True
        return False

    @statementregister
    def VarInList(var, list):
        """
        IN:
            var - string
            list - string
        TYPE:
            Dysplayable
        """
        for item in list:
            if item in list:
                return True
        return False

    @statementregister
    def ListInList(list1, list2):
        """
        IN:
            list1 - string
            list2 - string
        TYPE:
            Dysplayable
        """
        for item in list1:
            if item in list2:
                return True
        return False

    @statementregister
    def Space(num):
        """
        IN:
            num - string
        TYPE:
            Dysplayable
        """
        text = ""
        for repeat in range(0, num):
            text += " "
        return text

    @statementregister
    def ObjectivesIconIf(name):
        """
        IN:
            name - string
        TYPE:
            Dysplayable
        """
        if name:
            return "{image=" + PathImg() + "misc/else/obs_icon_" + ("yes" if name[1] else ("no_" + Rename(store.obs_timeofday))) + ".png} " + name[0]
        else:
            return "{image=" + PathImg() + "misc/else/obs_icon_empty" + ".png}" + Space(150) + "{image=" + PathImg() + "misc/else/obs_icon_empty" + ".png}"

    @statementregister
    def QuestObjectiveMoveIf(name):
        """
        IN:
            name - string
        TYPE:
            Dysplayable
        """
        for item in range(0, len(store.obs_quest["objectives"])):
            if store.obs_quest["objectives"][item][0] == name[0]:
                if not store.obs_quest["move"][item]:
                    return True
                else:
                    return False

    @statementregister
    def InventoryIf(name, stats=None):
        """
        IN:
            name - string
            stats - None/{"d":int, "h":int, "s":int, "e":[string, int]}
        TYPE:
            Dysplayable
        """
        for item in range(0, len(store.obs_inventory)):
            if store.obs_inventory[item]["name"] == name and stats == store.obs_inventory[item]["stats"]:
                return True
        return False

    @statementregister
    def Brightness(img, b):
        """
        IN:
            img - string
            b - int
        TYPE:
            Dysplayable
        """
        return store.im.MatrixColor(img, store.im.matrix.brightness(b))

    @statementregister
    def SpriteCondition(name, *args):
        """
        IN:
            name - <character> <distance> <pose>
            *args
        TYPE:
            Dysplayable
        """
        subargs = [(SpriteSize(name), 1080)]
        for object in args:
            if object:
                subargs.append((0, 0),)
                subargs.append(SpritePath(name, object))
        return store.ConditionSwitch(
            "store.obs_sprite_time == 'sunset'", store.im.MatrixColor(
                store.im.Composite(*subargs), store.obs_tint_dict["s"]),
            "store.obs_sprite_time == 'night'", store.im.MatrixColor(
                store.im.Composite(*subargs), store.obs_tint_dict["n"]),
            "store.obs_sprite_time == 'rain'", store.im.MatrixColor(
                store.im.Composite(*subargs), store.obs_tint_dict["r"]),
            True, store.im.Composite(*subargs))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
