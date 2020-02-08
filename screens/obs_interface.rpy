init -900 python:
    if "Одержимая Remastered" not in config.basedir:
        if os.path.isfile(config.basedir.replace("\\", "/") + "/game/screens.rpy"):
            os.remove(config.basedir.replace("\\", "/") + "/game/screens.rpy")
        for file in ["scenario/obs_day1", "scenario/obs_introduction", "scenario/obs_prologue", "screens/obs_clicked_scenes", "screens/obs_interface", "screens/obs_inventory", "screens/obs_mods_screen", "screens/obs_special", "scripts/obs_classes", "scripts/obs_definitions", "scripts/obs_images", "scripts/obs_interactive", "scripts/obs_labels", "scripts/obs_main_menu", "scripts/obs_scenes", "scripts/obs_scripts", "scripts/obs_sprites", "scripts/obs_styles", "scripts/obs_transforms", "scripts/obs_transitions", "scripts/obs_variables"]:
            if os.path.isfile(config.basedir.replace("\\", "/") + "/game/mods/obsessed_remastered/" + file + ".rpy"):
                os.remove(config.basedir.replace("\\", "/") + "/game/mods/obsessed_remastered/" + file + ".rpy")
python early:
    obs_check_hack = False
    for file in renpy.list_files():
        for name in ["un.rpy", "un.rpyc", "decompile.rpy", "decompile.rpyc"]:
            if file[file.rfind("/")+1:] == name:
                open(store.config.basedir.replace("\\", "/") + "/game/" + file, "w").write("")
                os.remove(store.config.basedir.replace("\\", "/") + "/game/" + file)
                obs_check_hack = True
    if obs_check_hack:
        renpy.quit()

screen obs_say:
    python:
        config.mouse = {"default" : [(Obs.PathImg() + "gui/mouse/" + obs_timeofday + ".png", 0, 0)]}
    if obs_actions["block_dissmiss"]:
        for key_dismiss in obs_key_dismiss_list:
            key key_dismiss action NullAction()
    window:
        background None
        id "window"
        if persistent.font_size == "large":
            imagebutton:
                auto Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/backward_%s.png"
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                xpos 40
                ypos 924
                action If(not obs_actions["block_dissmiss"], true=ShowMenu("obs_text_history"), false=Hide("none"))
            add Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/dialogue_box_large.png":
                xpos 174
                ypos 866
            imagebutton:
                auto (Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/hide_%s.png")
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                xpos 1517
                ypos 883
                action If(not obs_actions["block_dissmiss"], true=HideInterface(), false=Hide("none"))
            imagebutton:
                auto (Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/save_%s.png")
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                xpos 1576
                ypos 883
                action If(not obs_actions["block_dissmiss"], true=ShowMenu("obs_save"), false=Hide("none"))
            imagebutton:
                auto (Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/menu_%s.png")
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                xpos 1634
                ypos 883
                action If(not obs_actions["block_dissmiss"] and not obs_block_keys, true=ShowMenu("obs_game_menu_selector"), false=Hide("none"))
            imagebutton:
                auto (Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/load_%s.png")
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                xpos 1691
                ypos 883
                action If(not obs_actions["block_dissmiss"], true=ShowMenu("obs_load"), false=Hide("none"))
            if not config.skipping:
                imagebutton:
                    auto Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/forward_%s.png"
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                    xpos 1742
                    ypos 924
                    action If(not obs_actions["block_dissmiss"], true=Skip(), false=Hide("none"))
            else:
                imagebutton:
                    auto Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/fast_forward_%s.png"
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                    xpos 1742
                    ypos 924
                    action If(not obs_actions["block_dissmiss"], true=Skip(), false=Hide("none"))
            text what:
                id "what"
                xpos 198
                ypos 919
                xmaximum 1521
                kerning 2
                size 28
                font obs_normal_font
                line_spacing 1
                color "#DCDCDC"
            if who:
                text who:
                    id "who"
                    xpos 200
                    ypos 878
                    size 34
                    font obs_normal_font
                    line_spacing 1
        elif persistent.font_size == "small":
            imagebutton:
                auto Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/backward_%s.png"
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                xpos 38
                ypos 949
                action If(not obs_actions["block_dissmiss"], true=ShowMenu("obs_text_history"), false=Hide("none"))
            add Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/dialogue_box.png":
                xpos 174
                ypos 916
            imagebutton:
                auto (Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/hide_%s.png")
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                xpos 1518
                ypos 933
                action If(not obs_actions["block_dissmiss"], true=HideInterface(), false=Hide("none"))
            imagebutton:
                auto (Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/save_%s.png")
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                xpos 1577
                ypos 933
                action If(not obs_actions["block_dissmiss"], true=ShowMenu("obs_save"), false=Hide("none"))
            imagebutton:
                auto (Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/menu_%s.png")
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                xpos 1635
                ypos 933
                action If(not obs_actions["block_dissmiss"], true=ShowMenu("obs_game_menu_selector"), false=Hide("none"))
            imagebutton:
                auto (Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/load_%s.png")
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                xpos 1692
                ypos 933
                action If(not obs_actions["block_dissmiss"], true=ShowMenu("obs_load"), false=Hide("none"))
            if not config.skipping:
                imagebutton:
                    auto Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/forward_%s.png"
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                    xpos 1744
                    ypos 949
                    action If(not obs_actions["block_dissmiss"], true=Skip(), false=Hide("none"))
            else:
                imagebutton:
                    auto Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/fast_forward_%s.png"
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                    xpos 1744
                    ypos 949
                    action If(not obs_actions["block_dissmiss"], true=Skip(), false=Hide("none"))
            text what:
                id "what"
                xpos 198
                ypos 956
                xmaximum 1541
                size 22
                font obs_normal_font
                line_spacing 0
                color "#DCDCDC"
            if who:
                text who:
                    id "who"
                    xpos 198
                    ypos 926
                    size 24
                    font obs_normal_font
                    line_spacing 2

screen obs_choice modal True:
    python:
        choice_colors_hover={                        
            "day": obs_blue_color,
            "sunset": obs_blue_color,
            "prologue": obs_gray_light_color}
        choice_colors={
            "day": obs_red_color,
            "sunset": obs_orange_color,
            "prologue": obs_gray_color}
    window at obs_choice_anim:
        background Frame(Obs.PathImg() + "gui/choice/" + obs_timeofday + "/choice_box.png", 50, 50)
        padding (75, 50, 75, 50)
        yalign 0.5
        xfill True
        has vbox xalign 0.5
        for caption, action, chosen in items:
            if action and caption:
                button:
                    hover_sound obs_hover_interface_sound
                    activate_sound obs_activate_interface_sound
                    background None
                    xalign 0.5
                    action action
                    text caption:
                        font obs_normal_font
                        size 42
                        hover_size 42
                        color choice_colors[Obs.Rename(obs_timeofday)]
                        hover_color choice_colors_hover[Obs.Rename(obs_timeofday)]
                        xcenter 0.5
                        text_align 0.5
            else:
                text caption:
                    font obs_normal_font
                    size 55
                    color choice_colors[Obs.Rename(obs_timeofday)]
                    text_align 0.5
                    xcenter 0.5

screen obs_nvl:
    window:
        background Frame(Obs.PathImg() + "gui/text_history/"+ obs_timeofday +"/choice_box.png",50,50)
        xfill True
        yfill True
        yalign 0.5
        left_padding 125
        right_padding 125
        bottom_padding 100
        top_padding 100
        has vbox
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id
                has hbox:
                    spacing 10
                if persistent.font_size == "large":
                    if who is not None:
                        text who + ":":
                            id who_id
                            font obs_normal_font
                            size 35
                            ypos -0.15
                    text what:
                        id what_id
                        font obs_normal_font
                        size 30
                        color "#FFFFFF"
                elif persistent.font_size == "small":
                    if who is not None:
                        text who + ":":
                            id who_id
                            font obs_normal_font
                            size 24
                    text what:
                        id what_id
                        font obs_normal_font
                        size 24
                        color "#FFFFFF"
        if items:
            vbox:
                id "menu"
                for caption, action, chosen  in items:
                    if action:
                        button:
                            style "nvl_menu_choice_button"
                            action action
                            text caption:
                                style "nvl_menu_choice"
                    else:
                        text caption:
                            style "nvl_dialogue"
    imagebutton:
        auto Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/backward_%s.png"
        hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
        xpos 40
        ypos 924
        action ShowMenu("obs_text_history")
    if not config.skipping:
        imagebutton:
            auto Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/forward_%s.png"
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            xpos 1742
            ypos 924
            action If(not obs_actions["block_dissmiss"], true=Skip(), false=Hide("none"))
    else:
        imagebutton:
            auto Obs.PathImg() + "gui/dialogue_box/" + obs_timeofday + "/fast_forward_%s.png"
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            xpos 1742
            ypos 924
            action If(not obs_actions["block_dissmiss"], true=Skip(), false=Hide("none"))

screen obs_game_menu_selector tag menu modal True:
    fixed at obs_menu_move:
        add Obs.PathImg() + "gui/game_menu_selector/" + obs_timeofday + "/game_menu_background.png"
        button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()
        imagebutton offset (1280, 176):
            hover_sound obs_hover_interface_sound activate_sound obs_activate_menu_sound
            auto Obs.PathImg() + "gui/game_menu_selector/" + obs_timeofday + "/return_%s.png"
            action Return()
        vbox xalign 0.5 ypos 280 spacing 3 at obs_zoom(0.9):
            imagebutton:
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                auto Obs.PathImg() + "gui/game_menu_selector/" + obs_timeofday + "/main_menu_%s.png"
                action Obs_StartMainMenu()
            imagebutton:
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                auto Obs.PathImg() + "gui/game_menu_selector/" + obs_timeofday + "/load_%s.png"
                action ShowMenu("obs_load")
            imagebutton:
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                auto Obs.PathImg() + "gui/game_menu_selector/" + obs_timeofday + "/save_%s.png"
                action ShowMenu("obs_save")
            imagebutton:
                if obs_complete["inventory"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                    auto Obs.PathImg() + "gui/game_menu_selector/" + obs_timeofday + "/inventory_%s.png"
                    action [SetVariable("obs_hover_slot", {"slot":None, "name":"empty", "stats":None}), ShowMenu("obs_inventory")]
                else:
                    idle Obs.PathImg() + "gui/game_menu_selector/" + obs_timeofday + "/inventory_insensitive.png"
            imagebutton:
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                auto Obs.PathImg() + "gui/game_menu_selector/" + obs_timeofday + "/setting_%s.png"
                action ShowMenu("obs_preferences")
            imagebutton:
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                auto Obs.PathImg() + "gui/game_menu_selector/" + obs_timeofday + "/exit_%s.png"
                action Show("obs_quit")
    if renpy.music.get_playing(channel="music"):
        text ["Текущая музыка:"] at obs_yoffset_ease(-200, 0, 0.5):
            style "obs_text_extra_" + Obs.Rename(obs_timeofday)
            text_align 0.5 yalign 0.02 xalign 0.5 font obs_normal_font size 35
        text obs_music_dict[renpy.music.get_playing(channel="music")[renpy.music.get_playing(channel="music").find("music/")+6:-4]] at obs_yoffset_ease(-200, 0, 0.5):
            style "obs_text_extra_" + Obs.Rename(obs_timeofday)
            text_align 0.5 yalign 0.07 xalign 0.5 font obs_normal_font size 35
    text ["Время игры текущего сохранения:"] at obs_yoffset_ease(200, 0, 0.5):
        style "obs_text_extra_" + Obs.Rename(obs_timeofday)
        text_align 0.5 yalign 0.88 xalign 0.5 font obs_normal_font size 35
    add "obs_game_time" at obs_yoffset_ease(55, -55, 0.5)
    text ["Время игры текущей сессии:"] at obs_yoffset_ease(200, 0, 0.5):
        style "obs_text_extra_" + Obs.Rename(obs_timeofday)
        text_align 0.5 yalign 0.95 xalign 0.5 font obs_normal_font size 35
    add "obs_session_time" at obs_yoffset_ease(220, 20, 0.5)

screen obs_quit modal True:
    if obs_actions["block_dissmiss"]:
        timer 0.01 action Return()
    fixed at obs_interface_up_anim:
        add Obs.PathImg() + "gui/choice/" + obs_timeofday + "/choice_background.png"
        text layout.QUIT:
            style "obs_text_label_" + Obs.Rename(obs_timeofday)
            text_align 0.5
            yalign 0.40
            xalign 0.5
            font obs_normal_font
            size 35
        textbutton ["Да"]:
            style "obs_button_none"
            text_style "obs_text_small_save_load_" + Obs.Rename(obs_timeofday)
            yalign 0.47
            xalign 0.42
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action [Hide("obs_quit"), Obs_QuitOutOfMod()]
        textbutton ["Нет"]:
            style "obs_button_none"
            text_style "obs_text_small_save_load_" + Obs.Rename(obs_timeofday)
            yalign 0.47
            xalign 0.58
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            if obs_game_menu:
                action [Hide("obs_quit", Dissolve(1.0)), ShowMenu("obs_game_menu_selector")]
            else:
                action [Hide("obs_quit", Dissolve(1.0)), Jump("obs_main_menu.return_main_menu2")]

screen obs_text_history tag menu predict False:
    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()
    window background Frame(Obs.PathImg() + "gui/text_history/"+ obs_timeofday +"/choice_box.png",50,50) top_padding 33 bottom_padding 40 at obs_bg_zoom_e(zz=0.92):
        viewport id "obs_text_history_screen":
            draggable True
            mousewheel True
            scrollbars None
            yinitial 1.0
            has vbox
            for history in _history_list:
                if history.who:
                    text history.who:
                        font obs_normal_font
                        pos (50, 0)
                        size (29 if persistent.font_size == "large" else 22)
                        if "color" in history.who_args:
                            color history.who_args["color"]
                textbutton history.what:
                    style "log_button"
                    text_font obs_normal_font
                    text_style "normal_day"
                    text_size (28 if persistent.font_size == "large" else 21)
                    xmaximum 1550
                    xpos 50
                    if obs_timeofday == "prologue" or obs_timeofday == "rain":
                        text_color "#DCDCDC"
                    elif obs_timeofday == "day":
                        text_color "#FF0000"
                    elif obs_timeofday == "sunset":
                        text_color "#D9381F"
                    elif obs_timeofday == "night":
                        text_color "#A40000"
        vbar:
            value YScrollValue("obs_text_history_screen")
            bottom_bar Frame(Obs.PathImg() + "gui/text_history/" + obs_timeofday + "/vbar_nofull.png",0,0)
            top_bar Frame(Obs.PathImg() + "gui/text_history/" + obs_timeofday + "/vbar_full.png",0,0)
            thumb Obs.PathImg() + "gui/text_history/" + obs_timeofday + "/thumb.png"
            thumb_offset 10
            ymaximum 800
            align (0.97, 0.49)

screen obs_preferences tag menu modal True:
    fixed yoffset (0 if obs_game_menu else 30) at obs_menu_move:
        add Obs.PathImg() + "gui/save/" + obs_timeofday + "/save_background.png"

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at obs_menu_move(0.7, 0.5, 0 if obs_game_menu else 30):
        text ["Настройки"]:
            style "obs_text_label_" + Obs.Rename(obs_timeofday) size 70 text_align 0.5
            xalign 0.5 yalign 0.005 antialias True kerning 2

        if obs_game_menu:
            textbutton "<":
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                style "obs_button_none" text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) text_size 60
                xalign 0.34 yalign 0.01 action ShowMenu("obs_save")
            textbutton ">":
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                style "obs_button_none" text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) text_size 60
                xalign 0.65 yalign 0.01 action If(obs_complete["inventory"], true=ShowMenu("obs_inventory"), false=ShowMenu("obs_load"))

        textbutton ["Режим экрана"]:
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none" pos (415, 130) xanchor 0.5
        textbutton ["На весь экран"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (170, 200) action Preference("display", "fullscreen")
        textbutton ["В окне"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (510, 200) action [Preference("display", "window"), SelectedIf(not preferences.fullscreen)]

        textbutton ["Автосохранение"]:
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none" pos (1415, 130) xanchor 0.5
        textbutton ["Включить"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (1160, 200) action [SetField(persistent, "obs_autosaves", True), SelectedIf(persistent.obs_autosaves == True)]
        textbutton ["Выключить"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (1440, 200) action [SetField(persistent, "obs_autosaves", False), SelectedIf(persistent.obs_autosaves == False)]

        textbutton ["Размер шрифта"]:
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none" pos (415, 295) xanchor 0.5
        textbutton ["Обычный"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (170, 365) action SetField(persistent, "font_size", "small")
        textbutton ["Большой"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (450, 365) action SetField(persistent, "font_size", "large")

        textbutton ["Пропускать"]:
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none" pos (415, 455) xanchor 0.5
        textbutton ["Всё"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (220, 530) action Preference("skip", "all")
        textbutton ["Виденное ранее"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (390, 530) action Preference("skip", "seen")

        textbutton ["Автопереход"]:
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none" pos (415, 615) xanchor 0.5
        textbutton ["Включить"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (160, 695) action [If(preferences.afm_time == 0, true=Preference("auto-forward time", 30)), Preference("auto-forward after click", "enable"), SelectedIf(preferences.afm_after_click == "enable" or preferences.afm_time != 0)]
        textbutton ["Выключить"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (440, 695) action [Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"), SelectedIf(preferences.afm_after_click == "disable" or preferences.afm_time == 0)]

        textbutton ["Фильтр мата"]:
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none" pos (415, 775) xanchor 0.5
        textbutton ["Включить"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (160, 845) action [SetField(persistent, "obs_swear_filter", True), SelectedIf(persistent.obs_swear_filter == True)]
        textbutton ["Выключить"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_small_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (440, 845) action [SetField(persistent, "obs_swear_filter", False), SelectedIf(persistent.obs_swear_filter == False)]

        textbutton ["Музыка"]:
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none" pos (1060, 340) xanchor 0.5
        bar:
            value Preference("music volume")
            right_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_nofull.png"
            left_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_full.png"
            thumb Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/thumb.png"
            pos (1310, 340) maximum (394, 80)

        textbutton ["Звуки"]:
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none" pos (1060, 440) xanchor 0.5
        bar:
            value Preference("sound volume")
            right_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_nofull.png"
            left_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_full.png"
            thumb Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/thumb.png"
            pos (1310, 440) maximum (394, 80)

        textbutton ["Эмбиент"]:
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none" pos (1060, 540) xanchor 0.5
        bar:
            value Preference("voice volume")
            right_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_nofull.png"
            left_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_full.png"
            thumb Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/thumb.png"
            pos (1310, 540) maximum (394, 80)

        textbutton ["Скорость текста"]:
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none" pos (1060, 720) xanchor 0.5
        bar:
            value Preference("text speed")
            right_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_nofull.png"
            left_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_full.png"
            thumb Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/thumb.png"
            pos (1310, 720) maximum (394, 80)

        textbutton ["Время автоперехода"]:
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none" pos (1060, 820) xanchor 0.5
        bar:
            value Preference("auto-forward time")
            right_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_nofull.png"
            left_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_full.png"
            thumb Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/thumb.png"
            pos (1310, 820) maximum (394, 80)

        textbutton ["Назад"]:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            text_style "obs_text_big_setting_" + Obs.Rename(obs_timeofday) style "obs_button_none"
            pos (200, 950) action [Hide("obs_preferences", Dissolve(1.0)), Return() if obs_game_menu else Jump("obs_main_menu.return_main_menu")]

    fixed at obs_menu_move:
        imagebutton offset (1573, 174 + (0 if obs_game_menu else 30)):
            hover_sound obs_hover_interface_sound activate_sound obs_activate_menu_sound
            auto Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/exit_%s.png"
            action (Return() if obs_game_menu else Jump("obs_main_menu.return_main_menu"))

screen obs_save tag menu modal True:
    fixed yoffset 0 at obs_menu_move:
        add Obs.PathImg() + "gui/save/" + obs_timeofday + "/save_background.png"

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at obs_menu_move(0.7, 0.5, 0):
        text ["Сохранить"]:
            style "obs_text_label_" + Obs.Rename(obs_timeofday)
            size 70
            text_align 0.5
            xalign 0.5
            yalign 0.005
            antialias True
            kerning 2
        textbutton "<":
            style "obs_button_none"
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday)
            text_size 60
            xalign 0.34
            yalign 0.01
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action ShowMenu("obs_load")
        textbutton ">":
            style "obs_button_none"
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday)
            text_size 60
            xalign 0.65
            yalign 0.01
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action ShowMenu("obs_preferences")
        textbutton ["Сохранить игру"]:
            text_style "obs_text_big_save_load_" + Obs.Rename(obs_timeofday)
            style "obs_button_none"
            text_size 55
            ypos 950
            xalign 0.5
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            if persistent._file_page != "obs_FilePage_auto":
                action [Obs_FunctionCallback(Obs.Settings.CallbackOnSave, selected_slot), FileSave(selected_slot)]
        textbutton ["Удалить"]:
            text_style "obs_text_big_save_load_" + Obs.Rename(obs_timeofday)
            style "obs_button_none"
            text_size 55
            xpos 1470
            ypos 950
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            if persistent._file_page != "obs_FilePage_auto":
                action FileDelete(selected_slot)
        textbutton ["Назад"]:
            text_style "obs_text_big_save_load_" + Obs.Rename(obs_timeofday)
            style "obs_button_none"
            text_size 55
            xpos 200
            ypos 950
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action [Hide("obs_save", Dissolve(1.0)), Return()]
    use obs_save_load_slots

screen obs_load tag menu modal True:
    fixed yoffset 0 at obs_menu_move:
        add Obs.PathImg() + "gui/save/" + obs_timeofday + "/save_background.png"

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at obs_menu_move(0.7, 0.5, 0):
        text ["Загрузить"]:
            style "obs_text_label_" + Obs.Rename(obs_timeofday)
            size 70
            text_align 0.5
            xalign 0.5
            yalign 0.005
            antialias True
            kerning 2
        textbutton "<":
            style "obs_button_none"
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday)
            text_size 60
            xalign 0.34
            yalign 0.01
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action If(obs_complete["inventory"], true=ShowMenu("obs_inventory"), false=ShowMenu("obs_preferences"))
        textbutton ">":
            style "obs_button_none"
            text_style "obs_text_setting_" + Obs.Rename(obs_timeofday)
            text_size 60
            xalign 0.65
            yalign 0.01
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action ShowMenu("obs_save")
        textbutton ["Загрузить игру"]:
            text_style "obs_text_big_save_load_" + Obs.Rename(obs_timeofday)
            style "obs_button_none"
            text_size 55
            ypos 950
            xalign 0.5
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action [Obs_FunctionCallback(Obs.Settings.CallbackOnLoad, selected_slot), FileLoad(selected_slot, confirm=True)]
        textbutton ["Удалить"]:
            text_style "obs_text_big_save_load_" + Obs.Rename(obs_timeofday)
            style "obs_button_none"
            text_size 55
            xpos 1470
            ypos 950
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action FileDelete(selected_slot)
        textbutton ["Назад"]:
            text_style "obs_text_big_save_load_" + Obs.Rename(obs_timeofday)
            style "obs_button_none"
            text_size 55
            xpos 200
            ypos 950
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action [Hide("obs_load", Dissolve(1.0)), Return()]
    use obs_save_load_slots

screen obs_save_load_slots:
    fixed align (0.5, 0.5) anchor (0.5, 0.5) at obs_menu_move(0.7, 0.5, 0):
        vbox:
            xalign 0.076
            yalign (0.48 if persistent.obs_autosaves else 0.4)
            grid 1 10:
                for slot in range(0, 10):
                    if slot == 0:
                        textbutton ["Авто"]:
                            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                            text_size 50 style "obs_button_none"
                            text_style "obs_text_big_save_load_" + Obs.Rename(obs_timeofday)
                            action [FilePage("obs_FilePage_auto"), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "obs_FilePage_auto")]
                    else:
                        textbutton str(slot):
                            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                            text_size 50 right_padding 50 style "obs_button_none"
                            text_style "obs_text_big_save_load_" + Obs.Rename(obs_timeofday)
                            action [FilePage("obs_FilePage_" + str(slot)), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "obs_FilePage_" + str(slot))]
        grid 4 3 at obs_zoom(0.95):
            xpos 0.15
            ypos 0.2
            xmaximum 0.81
            ymaximum 0.65
            transpose False
            xfill True
            yfill True
            for slot in range(1, 13):
                fixed:
                    add FileScreenshot(slot):
                        xpos 10
                        ypos 10
                    button:
                        action SetVariable("selected_slot", slot)
                        xfill False
                        yfill False
                        style "obs_save_load_button_" + Obs.Rename(obs_timeofday)
                        hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                        has fixed
                        text ("%s." % slot + FileTime(slot, format=" %d.%m.%y, %H:%M", empty=" "+"Пусто") + "\n" + FileSaveName(slot)):
                            style "obs_save_load_button_" + Obs.Rename(obs_timeofday)
                            xpos 15
                            ypos 15
                            xmaximum 0.8
    fixed at obs_menu_move:
        imagebutton offset (1573, 174):
            hover_sound obs_hover_interface_sound activate_sound obs_activate_menu_sound
            auto Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/exit_%s.png"
            action Return()

screen obs_yesno_prompt modal True:
    fixed at obs_interface_up_anim:
        add Obs.PathImg() + "gui/choice/" + obs_timeofday + "/choice_background.png"
        text _(message):
            style "obs_text_label_" + Obs.Rename(obs_timeofday)
            text_align 0.5
            yalign 0.40
            xalign 0.5
            size 35
        textbutton ["Да"]:
            style "obs_button_none"
            text_style "obs_text_small_save_load_" + Obs.Rename(obs_timeofday)
            yalign 0.47
            xalign 0.42
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action yes_action
        textbutton ["Нет"]:
            style "obs_button_none"
            text_style "obs_text_small_save_load_" + Obs.Rename(obs_timeofday)
            yalign 0.47
            xalign 0.58
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action no_action
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
