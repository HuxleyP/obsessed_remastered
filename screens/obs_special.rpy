init -600 python:
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

screen obs_quest:
    text obs_quest["name"][0] pos (0.02, 0.03) at obs_quest_name_move:
        style "obs_quest_name_" + Obs.Rename(obs_timeofday)
        if obs_quest["name"][1]:
            color obs_green_dark_color
    if obs_quest["objectives"]:
        vbox xanchor 0.0 ypos 0.055:
            text Obs.ObjectivesIconIf("") style "obs_quest_objectives_" + Obs.Rename(obs_timeofday)
            for item in obs_quest["objectives"]:
                text Obs.ObjectivesIconIf(item):
                    if item[1]:
                        color obs_green_dark_color
                    style "obs_quest_objectives_" + Obs.Rename(obs_timeofday)
                    if Obs.QuestObjectiveMoveIf(item):
                        at obs_quest_objectives_move_in
                    else:
                        at obs_quest_objectives_move_out
    if obs_quest["move"] != [] and not obs_quest["move"][len(obs_quest["objectives"])-1]:
        timer 2.0 repeat True action Function(Obs.GlobalDictList, "obs_quest", "move", len(obs_quest["objectives"])-1, True)

screen obs_new_item(name, message):
    layer "front"
    fixed at obs_new_item_move:
        add Obs.PathImg() + "gui/overlays/obs_new_item_frame_" + obs_timeofday + ".png" pos (-0.012, -0.01)
        add Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + name + "_idle.png"
        text message style "obs_text_label_" + Obs.Rename(obs_timeofday) size 20 pos (0.05, 0.005) xanchor 0.0
        text obs_items_dict[name] style "obs_text_label_" + Obs.Rename(obs_timeofday) size 30 pos (0.05, 0.025) xanchor 0.0
    timer 5.0 action Hide("obs_new_item")

screen obs_message(name, label, text):
    fixed at obs_menu_move:
        add Obs.PathImg() + "gui/overlays/obs_message_ground_" + obs_timeofday + ".png"
        add Obs.PathImg() + "gui/overlays/obs_message_icon_" + name + ".png"
        add Obs.PathImg() + "gui/overlays/obs_message_layer_" + obs_timeofday + ".png"
        text label style "obs_text_label_" + Obs.Rename(obs_timeofday) size 35 pos (0.51, 0.34) xanchor 0.5
        text text style "obs_text_item_description_" + Obs.Rename(obs_timeofday) pos (0.35, 0.39)
        imagebutton offset (1255, 365):
            hover_sound obs_hover_interface_sound activate_sound obs_activate_menu_sound
            auto Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/exit2_%s.png"
            action Return()

screen obs_loading(time) tag menu modal True:
    for key_dismiss in obs_key_dismiss_list:
        key key_dismiss action NullAction()
    add Obs.PathImg() + "gui/loading/" + obs_day[1] + ".png" at obs_loading_bg_move
    add "obs_interference_anim" at obs_alpha(0.5)
    timer 0.01 repeat True action If(load_value < 100, 
        true=SetVariable("load_value", load_value + time), 
        false=[Stop("music", fadeout=3), Hide("obs_loading", transition=Dissolve(2.0, alpha=True)), Return()])
    vbox xalign 0.5 ypos 0.8:
        text "Загрузка..." xalign 0.5 xanchor 0.5 style "obs_text_setting_day"
        bar range 100 value load_value style "obs_loading_bar"
        text str(int(load_value)) + "%" xalign 0.5 xanchor 0.5 style "obs_text_setting_day"
    add "obs_loading_icon" yoffset 160 at obs_full_rotate_repeat(1.0, 0.5, 1.0, 0.8)
    text Obs.TextSizeFind(obs_day[2], ":", 80):
        xalign 0.05 ypos 0.05 style "obs_text_setting_day" size 60 at obs_xoffset_ease(-1000, 0, 1.0)

screen obs_autosave:
    layer "front"
    fixed at obs_show_hide_alpha(1.0):
        text "Автосохранение..." pos (0.785, 0.72) size 37:
            style "obs_text_label_" + Obs.Rename(obs_timeofday)
            at obs_alpha_ease_repeat(0.4, 1.0, 1.0)
        add Obs.PathMain() + "images/gui/overlays/autosave_icon_" + Obs.Rename(obs_timeofday) + ".png":
            at obs_alpha_ease_repeat(0.8, 1.0, 1.0), obs_full_rotate_repeat(2.0, 0.45, 1.0, 0.8)
    timer 6.0 action Hide("obs_autosave")

screen obs_overlay:
    python:
        obs_after_load = False
    if obs_complete["inventory"]:
        for key_i in obs_key_i_list:
            key key_i action If(renpy.get_screen("obs_inventory") == None,
                true=[SetVariable("obs_hover_slot", {"slot":None, "name":"empty", "stats":None}), ShowMenu("obs_inventory")],
                false=Return())
    if obs_actions["block_dissmiss"]:
        for key_dismiss in obs_key_dismiss_list:
            key key_dismiss action NullAction()

screen obs_clicked(name, *args) layer "master" zorder 1:
    imagemap alpha True:
        ground "bg " + name
        hover Obs.PathImg() + "objects/" + ("obs_" if "obs_" not in name else "") + name + "_clicked.png"
        hotspot (args) clicked Return() style "obs_imagemap"

screen obs_clicked_text:
    text "Наведите курсор на объект, чтобы его использовать." pos (0.02, 0.03) style "obs_quest_name_" + Obs.Rename(obs_timeofday) at obs_clicked_text_move

screen obs_timer(time):
    timer time action Function(Obs.Action.NewContext)

screen obs_normal_text_anim1(ui_text, ui_color, ui_size, ui_at, ui_x, ui_y, ui_font):
    text ui_text color ui_color size ui_size xalign ui_x ypos ui_y at ui_at font ui_font outlines obs_outlines yalign 0.5 text_align 0.5

screen obs_normal_text_anim2(ui_text, ui_color, ui_size, ui_at, ui_x, ui_y, ui_font):
    text ui_text color ui_color size ui_size xalign ui_x ypos ui_y at ui_at font ui_font outlines obs_outlines yalign 0.5 text_align 0.5
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
