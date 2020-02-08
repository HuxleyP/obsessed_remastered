init -100 python:
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

label SuperRage__obs_start:
    $ Obs.Scene.Function(renpy.block_rollback)
    $ Obs.GlobalField(renpy.game.context(), "force_checkpoint", True)
    $ Obs.Settings.ScreensActivate()
    $ Obs.AutoSave("", False)
    $ Obs.Stop.All(1)
    $ Obs.Show.NotScreens()
    $ Obs.Settings.DefaultVariables()
    $ Obs.Set.DayTime("day")
    $ Obs.Show.BlockDissmiss()
    if not obs_before_main_menu:
        $ Obs.Scene.Function(obs_splashscreen)
        $ Obs.Hide.BlockDissmiss()

label obs_main_menu:
    $ Obs.Global("obs_game_menu", False)
    $ Obs.Global("obs_config_version_text", "Открытая Бета v" + obs_config_version)
    $ Obs.GlobalField(persistent, "obs_game_menu", False)
    $ Obs.Settings.OverlayPlayingMusic(False)
    $ Obs.Scene.Clear()
    $ Obs.Scene.Image("black")
    $ Obs.Show.Screen("obs_overlay")
    if obs_before_main_menu:
        $ Obs.Settings.ClearScreens()
    $ Obs.With.Statement(dissolve)
    $ Obs.Play.Ambience("obs_bizzard_outside", 1)
    $ Obs.Play.Music("obs_senritsu", 2)
    $ Obs.Scene.Image("obs_main_menu_background")
    $ Obs.Show.Image("obs_main_menu_eye", at=obs_bg_zoom_e(xx=1.345, yy=0.38))
    $ Obs.Show.Image("obs_prologue_dream_red", at=obs_bg_zoom_e(zz=0.15, xx=1.35, yy=0.38))
    $ Obs.Show.Image("obs_main_menu_layer", at=obs_align(1.62, 0.0))
    $ Obs.Show.Image("obs_main_menu_bus", at=obs_xalign(-4.0))
    $ Obs.Show.Image("obs_main_menu_hand", at=obs_main_menu_hand_anim)
    $ Obs.Show.Image("obs_main_menu_layer2", zorder=1, at=obs_xalign(-4.0))
    $ Obs.Show.Image("obs_main_menu_mi")
    $ Obs.Show.Image("obs_main_menu_art_and_msk")
    $ Obs.Show.Image("obs_snow right_red", layer="mapoverlay", at=obs_alpha(0.6))
    if not obs_before_main_menu:
        $ Obs.Master(obs_bg_zoom_e(3.0, 3.0, 3.0, 0.25, 0.4, 0.0, 0.0))
        $ Obs.With.Statement(obs_dissolve12)
        $ Obs.Master(obs_bg_zoom_e(3.0, 3.0, 3.0, 0.4, 0.62, 0.0, 0.55))
        $ Obs.Pause(3)
    else:
        $ Obs.Master(obs_bg_zoom_e(3.0, 3.0, 2.0, 0.62, 0.62, 0.0, 0.55))
        $ Obs.With.Statement(obs_dissolve4)
    $ Obs.Show.Image("obs_version_text [obs_config_version_text]", layer="mapoverlay", at=[obs_zoom(1.2), obs_yoffset_ease(400, 0, 1.0)])
    $ Obs.Show.Image("obs_main_menu_logo", layer="mapoverlay", at=obs_xoffset_ease(800, 0, 1.0))
    $ Obs.Pause(1.0)
    $ Obs.Show.Image("obs_main_menu_ground", layer="mapoverlay", at=obs_xoffset_ease(-800, 0, 1.0))
    $ Obs.Pause(0.5)
    $ Obs.Call.Screen("obs_main_menu")

    label obs_main_menu.new_game:

        $ Obs.Show.Image("obs_main_menu_ground", layer="mapoverlay", at=obs_xoffset_ease(0, -800, 1.0))
        $ Obs.Pause(0.5)
        $ Obs.Jump.Label("obs_main_menu.start")
















    label obs_main_menu.start:
        $ Obs.Stop.Ambience(7)
        $ Obs.Stop.Music(7)
        $ Obs.Pause(0.5)
        $ Obs.Show.Image("obs_version_text [obs_config_version_text]", layer="mapoverlay", at=[obs_zoom(1.2), obs_yoffset_ease(0, 400, 1.0)])
        $ Obs.Show.Image("obs_main_menu_logo", layer="mapoverlay", at=obs_xoffset_ease(0, 800, 1.0))
        $ Obs.Pause(1.0)
        $ Obs.Master(obs_bg_zoom_to_e(3.0, 4.0, 0.62, 0.0), False)
        $ Obs.Pause(3.0)
        $ Obs.Hide.Image("obs_snow right_red", layer="mapoverlay")
        $ Obs.Hide.Image("obs_main_menu_ground", layer="mapoverlay")
        $ Obs.Hide.Image("obs_version_text", layer="mapoverlay")
        $ Obs.Hide.Image("obs_main_menu_logo", layer="mapoverlay")
        $ Obs.Scene.Image("obs_gray2_color")
        $ Obs.With.Statement(dissolve2)
        $ Obs.Pause(1.0)
        $ Obs.Scene.Image("black", _with=dissolve2)
        $ Obs.Settings.OverlayPlayingMusic()
        $ Obs.Delete("pos")
        $ Obs.Global("obs_game_time", 0)
        $ Obs.GlobalField(persistent, "obs_game_menu", True)
        $ Obs.Hide.BlockDissmiss()
        $ Obs.Jump.Label("obs_introduction")

    label obs_main_menu.load:
        $ Obs.Show.Image("obs_main_menu_ground", layer="mapoverlay", at=obs_xoffset_ease(0, -800, 1.0))
        $ Obs.Pause(1.0)
        $ Obs.Show.Image("obs_main_menu_hand", at=obs_main_menu_hand_anim)
        $ Obs.Master(obs_bg_zoom_to_e(2.3, 2.0, -1.255, 1.0), False)
        $ Obs.Play.SoundLoop("obs_knife_loop", 2)
        $ Obs.Pause(1.5)
        $ Obs.Hide.Image("obs_main_menu_ground", layer="mapoverlay")
        $ Obs.Call.Screen("obs_main_menu_load")

    label obs_main_menu.preferences:
        $ Obs.Show.Image("obs_main_menu_ground", layer="mapoverlay", at=obs_xoffset_ease(0, -800, 1.0))
        $ Obs.Pause(1.0)
        $ Obs.Master(obs_bg_zoom_to_e(3.2, 1.0, 1.47, 0.35), False)
        $ Obs.Pause(1.0)
        $ Obs.Hide.Image("obs_main_menu_ground", layer="mapoverlay")
        $ Obs.Play.SoundLoop("obs_tv_noise")
        $ Obs.Call.Screen("obs_main_menu_preferences")

    label obs_main_menu.quit:
        $ Obs.Show.Image("obs_main_menu_ground", layer="mapoverlay", at=obs_xoffset_ease(0, -800, 1.0))
        $ Obs.Show.Screen("obs_quit")






    label obs_main_menu.return_main_menu:
        $ Obs.Pause(1.0)
        $ Obs.Stop.SoundLoop(1)
        $ Obs.Master(obs_bg_zoom_to_e(3.0, 1.0, 0.62, 0.55), False)
        $ Obs.Pause(1.0)
        $ Obs.Show.Image("obs_main_menu_ground", layer="mapoverlay", at=obs_xoffset_ease(-800, 0, 1.0))
        $ Obs.Pause(0.5)
        $ Obs.Call.Screen("obs_main_menu")

    label obs_main_menu.return_main_menu2:
        $ Obs.Show.Image("obs_main_menu_ground", layer="mapoverlay", at=obs_xoffset_ease(-800, 0, 1.0))
        $ Obs.Call.Screen("obs_main_menu")


























screen obs_main_menu tag menu modal True:
    vbox xalign 0.025 ypos 100 spacing 3 at obs_main_menu_buttons_move:
        imagebutton:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            auto Obs.PathImg() + "gui/main_menu/continue_%s.png"
            insensitive Obs.PathImg() + "gui/main_menu/continue_insensitive.png"
            action Obs_Continue()
        imagebutton:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            auto Obs.PathImg() + "gui/main_menu/new_game_%s.png"
            action Jump("obs_main_menu.new_game")
        imagebutton:
            idle Obs.PathImg() + "gui/main_menu/days_insensitive.png"
        imagebutton:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            auto Obs.PathImg() + "gui/main_menu/load_%s.png"
            action Jump("obs_main_menu.load")
        imagebutton:
            idle Obs.PathImg() + "gui/main_menu/dlc_insensitive.png"
        imagebutton:
            idle Obs.PathImg() + "gui/main_menu/achievements_insensitive.png"
        imagebutton:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            auto Obs.PathImg() + "gui/main_menu/preferences_%s.png"
            action Jump("obs_main_menu.preferences")
        imagebutton:
            idle Obs.PathImg() + "gui/main_menu/gallery_insensitive.png"
        imagebutton:
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            auto Obs.PathImg() + "gui/main_menu/exit_%s.png"
            action Jump("obs_main_menu.quit")
    imagebutton at obs_main_menu_load_move(0.0, 500, 1.1, 0.99, 0.9):
        hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
        auto Obs.PathImg() + "gui/main_menu/vk_%s.png"
        action OpenURL("https://vk.com/obsessed_everlasting_summer")

screen obs_main_menu_load tag menu modal True:
    fixed at obs_main_menu_load_move(0.0, 1500, 0.85, 2.25, 1.05):
        add Obs.PathImg() + "gui/save/day/save_background.png"
    fixed anchor (0.5, 0.5) at obs_main_menu_load_move(0.0, 1500, 0.6, 1.15, 0.68):
        text ["Загрузить"]:
            style "obs_text_label_day" size 70 text_align 0.5
            xalign 0.5 yalign 0.025 antialias True kerning 2
        textbutton ["Загрузить игру"]:
            text_style "obs_text_big_save_load_day"
            style "obs_button_none" text_size 55 ypos 950 xalign 0.5
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action [Obs_FunctionCallback(Obs.Settings.CallbackOnLoad, selected_slot), FileLoad(selected_slot, confirm=False)]
        textbutton ["Удалить"]:
            text_style "obs_text_big_save_load_day"
            style "obs_button_none" text_size 55 pos (1470, 950)
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action FileDelete(selected_slot)
        textbutton ["Назад"]:
            text_style "obs_text_big_save_load_day"
            style "obs_button_none" text_size 55 pos (200, 950)
            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
            action [Hide("obs_main_menu_load", Dissolve(1.0)), Jump("obs_main_menu.return_main_menu")]
    fixed anchor (0.5, 0.5) at obs_main_menu_load_move(0.5, 1500, 0.55, 1.07, 0.69):
        vbox:
            align (0.076, 0.48 if persistent.obs_autosaves else 0.4)
            grid 1 10:
                for slot in range(0, 10):
                    if slot == 0:
                        textbutton ["Авто"]:
                            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                            text_size 50 style "obs_button_none"
                            text_style "obs_text_big_save_load_day"
                            action [FilePage("obs_FilePage_auto"), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "obs_FilePage_auto")]
                    else:
                        textbutton str(slot):
                            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                            text_size 50 right_padding 50 style "obs_button_none"
                            text_style "obs_text_big_save_load_day"
                            action [FilePage("obs_FilePage_" + str(slot)), SetVariable("selected_slot", False), SelectedIf(persistent._file_page == "obs_FilePage_" + str(slot))]
        grid 4 3 pos (0.15, 0.2) maximum (0.81, 0.65) at obs_zoom(0.95):
            transpose False xfill True yfill True
            for slot in range(1, 13):
                fixed:
                    add FileScreenshot(slot) pos (10, 10)
                    button xfill False yfill False:
                        action SetVariable("selected_slot", slot)
                        style "obs_save_load_button_day"
                        hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                        has fixed
                        text ("%s." % slot + FileTime(slot, format=" %d.%m.%y, %H:%M", empty=" "+"Пусто") + "\n" + FileSaveName(slot)):
                            style "obs_save_load_button_day"
                            pos (15, 15) xmaximum 0.8

screen obs_main_menu_preferences tag menu modal True:
    window background Obs.PathImg() + "gui/main_menu/ground2.png" at obs_main_menu_preferences_move(0, -800, -800, 0, 0)
    window background None at obs_main_menu_preferences_move(0.5, -800, -800, 0, 0):
        top_padding 110 bottom_padding -500
        has viewport id "obs_main_menu_preferences_screen":
            draggable True mousewheel True scrollbars None yinitial 0.0
        vbox spacing 2:

            null height 25

            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Режим экрана:"]:
                    text_style "obs_text_setting_day" style "obs_button_none" text_size 40
            hbox xanchor 0.5 xalign 0.65:
                textbutton ["На весь экран"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action Preference("display", "fullscreen")
                textbutton ["В окне"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action [Preference("display", "window"), SelectedIf(not preferences.fullscreen)]

            null height 20

            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Размер шрифта:"]:
                    text_style "obs_text_setting_day" style "obs_button_none" text_size 40
            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Обычный"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action SetField(persistent, "font_size", "small")
                textbutton ["Большой"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action SetField(persistent, "font_size", "large")

            null height 20

            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Пропускать:"]:
                    text_style "obs_text_setting_day" style "obs_button_none" text_size 40
            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Всё"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action Preference("skip", "all")
                textbutton ["Виденное ранее"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action Preference("skip", "seen")

            null height 20

            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Автопереход:"]:
                    text_style "obs_text_setting_day" style "obs_button_none" text_size 40
            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Включить"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action [If(preferences.afm_time == 0, true=Preference("auto-forward time", 30)), Preference("auto-forward after click", "enable"), SelectedIf(preferences.afm_after_click == "enable" or preferences.afm_time != 0)]
                textbutton ["Выключить"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action [Preference("auto-forward time", 0), Preference("auto-forward after click", "disable"), SelectedIf(preferences.afm_after_click == "disable" or preferences.afm_time == 0)]

            null height 20

            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Фильтр мата:"]:
                    text_style "obs_text_setting_day" style "obs_button_none" text_size 40
            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Включить"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action [SetField(persistent, "obs_swear_filter", True), SelectedIf(persistent.obs_swear_filter == True)]
                textbutton ["Выключить"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action [SetField(persistent, "obs_swear_filter", False), SelectedIf(persistent.obs_swear_filter == False)]

            null height 20

            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Автосохранение:"]:
                    text_style "obs_text_setting_day" style "obs_button_none" text_size 40
            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Включить"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action [SetField(persistent, "obs_autosaves", True), SelectedIf(persistent.obs_autosaves == True)]
                textbutton ["Выключить"]:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound text_size 40
                    text_style "obs_text_small_setting_day" style "obs_button_none"
                    action [SetField(persistent, "obs_autosaves", False), SelectedIf(persistent.obs_autosaves == False)]

            null height 20

            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Музыка"]:
                    text_style "obs_text_setting_day" style "obs_button_none" text_size 40
            hbox xanchor 0.5 xalign 0.65 ypos -0.2 at obs_zoom(0.8):
                bar value Preference("music volume") maximum (394, 80):
                    right_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_nofull.png"
                    left_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_full.png"
                    thumb Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/thumb.png"

            null height 1

            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Звуки"]:
                    text_style "obs_text_setting_day" style "obs_button_none" text_size 40
            hbox xanchor 0.5 xalign 0.65 ypos -0.2 at obs_zoom(0.8):
                bar value Preference("sound volume") maximum (394, 80):
                    right_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_nofull.png"
                    left_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_full.png"
                    thumb Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/thumb.png"

            null height 1

            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Эмбиент"]:
                    text_style "obs_text_setting_day" style "obs_button_none" text_size 40
            hbox xanchor 0.5 xalign 0.65 ypos -0.2 at obs_zoom(0.8):
                bar value Preference("voice volume") maximum (394, 80):
                    right_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_nofull.png"
                    left_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_full.png"
                    thumb Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/thumb.png"

            null height 1

            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Скорость текста"]:
                    text_style "obs_text_setting_day" style "obs_button_none" text_size 40
            hbox xanchor 0.5 xalign 0.65 ypos -0.2 at obs_zoom(0.8):
                bar value Preference("text speed") maximum (394, 80):
                    right_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_nofull.png"
                    left_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_full.png"
                    thumb Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/thumb.png"

            null height 1

            hbox xanchor 0.5 xalign 0.65:
                textbutton ["Время автоперехода"]:
                    text_style "obs_text_setting_day" style "obs_button_none" text_size 40
            hbox xanchor 0.5 xalign 0.65 ypos -0.2 at obs_zoom(0.8):
                bar value Preference("auto-forward time") maximum (394, 80):
                    right_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_nofull.png"
                    left_bar Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/bar_full.png"
                    thumb Obs.PathImg() + "gui/preferences/" + obs_timeofday + "/thumb.png"

            null height 510

    window background None at obs_main_menu_preferences_move(0.5, 0, -800, 1200, 0):
        vbar value YScrollValue("obs_main_menu_preferences_screen"):
            bottom_bar Frame(Obs.PathImg() + "gui/text_history/" + obs_timeofday + "/vbar_nofull.png", 0, 0)
            top_bar Frame(Obs.PathImg() + "gui/text_history/" + obs_timeofday + "/vbar_full.png", 0, 0)
            thumb Obs.PathImg() + "gui/text_history/" + obs_timeofday + "/thumb.png"
            thumb_offset 10 ymaximum 800 xalign (0.285) ypos -0.15

    text ["Настройки"] at obs_main_menu_preferences_move(0.5, -800, -800, 0, 0):
        style "obs_text_label_day" color obs_red_color size 65 text_align 0.5
        antialias True kerning 2 xanchor 0.5 align (0.136, 0.01)

    textbutton ["Назад"] at obs_main_menu_preferences_move(0.5, 0, 0, 400, 400):
        hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound pos (590, 1000)
        text_style "obs_text_big_setting_day" style "obs_button_none"
        action [Hide("obs_main_menu_preferences", Dissolve(1.0)), Jump("obs_main_menu.return_main_menu")]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
