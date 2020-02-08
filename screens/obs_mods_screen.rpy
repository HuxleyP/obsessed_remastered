init -700 python:
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

screen obs_mods tag menu modal True:
    $ bar_null = Frame(get_image("gui/settings/bar_null.png"),12,12)
    $ bar_full = Frame(get_image("gui/settings/bar_full.png"),12,12)
    window:
        background get_image("gui/settings/preferences_bg.jpg")
        hbox:
            align (0.5, 0.08)
            add get_image("gui/settings/star.png") yalign 0.65
            text " "+translation["mods"][_preferences.language]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("gui/settings/star.png") yalign 0.65
        textbutton translation["Back"][_preferences.language] style "log_button" text_style "settings_link":
            align (0.015, 0.92) action ShowMenu("preferences")
        if mods:
            side "c b r" area (0.27, 0.24, 0.47, 0.70):
                viewport id "mods" draggable True mousewheel True scrollbars None yinitial 0.0:
                    has grid 1 len(mods)
                    for lbl, name in sorted(mods.iteritems()):
                        textbutton name style "log_button":
                            if name == obs_config_mod_name:
                                text_style "obs_settings_text" ypos -0.12
                                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                            else:
                                text_style "settings_text"
                            action (SetField(persistent, "jump_to", lbl), SetVariable(backdrop, "prologue"), Start())
                bar value XScrollValue("mods"):
                    left_bar "images/misc/none.png" right_bar "images/misc/none.png"
                    thumb "images/misc/none.png" hover_thumb "images/misc/none.png"
                vbar value YScrollValue("mods"):
                    bottom_bar "images/misc/none.png" top_bar "images/misc/none.png"
                    thumb "images/gui/settings/vthumb.png" thumb_offset -12

if not persistent.filters or {"is_active":True, "id":"rad__mods_menu"} not in persistent.filters:
    screen rad_preferences_header

    screen scrollbars


screen obs_mods_menu_rad tag menu modal True:
    if persistent.filters and {"is_active":True, "id":"rad__mods_menu"} in persistent.filters:
        python:
            what_tag_filters = [(k, len(filter_mods_lst(v))) for k, v in tag_mods.iteritems() if k not in mods_filter["+"] and len(filter_mods_lst(v))]
            what_items = [(k, "%s %s" %( "" if k.find("__") == -1 else "{color=#117743}[[" + k.split("__")[0] + "]{/color}", __(mods[k]) )) for k in filter_mods_lst(mods.keys())]
            what_tag_filter_groups = sorted(list(set([i.split(":")[0] for i, n in what_tag_filters if i.find(":") != -1])))
            basic = {"current_menu": "mods", "prev_link": "preferences", "left_link": "filters",
                     "right_link": "mods_menu_settings_rad", "right_args": {"prev_menu": 'mods'}}
        frame:
            background get_image("gui/settings/preferences_bg.jpg")
            if store.persistent.filters and {"is_active":True, "id":"rad__mods_menu"} in store.persistent.filters:
                use rad_preferences_header(**basic)
            add Image("mods_rad/side_menu.png") alpha 0.9 align (-0.08, 0.61)
            side "c b r" area (0.006, 0.24, 0.234, 0.605):
                viewport id "left" draggable True mousewheel True scrollbars None yinitial 0.0:
                    has hbox
                    null width 5
                    vbox xfill True:
                        hbox:
                            if persistent.mods_filter != mods_filter:
                                textbutton "★" style "log_button" text_style "fav_icon":
                                    action (Function(mods_to_persistent), Show("notify_prompt",message="Текущий набор фильтров тэгов сохранён."))
                            text __("Фильтров тэгов: %d")%len(sum(mods_filter.values(), [])) style "settings_text"
                        for t in mods_filter:
                            for name in sorted(mods_filter[t]):
                                hbox xpos 35:
                                    textbutton "X" style "log_button" text_style "settings_text_small":
                                        action (Function(filter_mods_del, t, name), ShowMenu("mods"))
                                    text "%s %s: %s"%(t, (tag_groups_translate[name.split(":")[0]][_preferences.language] if name.split(":")[0] in tag_groups_translate else name.split(":")[0]),(tags_translate[name.split(":")[0]][name.split(":")[-1]][_preferences.language] if name.split(":")[0] in tag_groups_translate and name.split(":")[0] in tags_translate and name.split(":")[-1] in tags_translate[name.split(":")[0]] else name.split(":")[-1])):
                                        style "settings_text_small"
                        text __("Модов: %d")%len(what_items) style "settings_text"
                        for g in what_tag_filter_groups:
                            if g == "author" and not persistent.filter_settings["rad__mods_menu"]["author_tags"]:
                                pass
                            else:
                                text "%s:" % (tag_groups_translate[g][_preferences.language] if g in tag_groups_translate else g):
                                    style "settings_text" xpos 35
                                for name, n in sorted(what_tag_filters):
                                    if name.startswith(g + ":"):
                                        hbox xpos 70:
                                            textbutton "-" style "log_button" text_style "settings_text_small":
                                                action (Function(filter_mods_add, "-", name), ShowMenu("mods"))
                                            textbutton "+" style "log_button" text_style "settings_text_small":
                                                action (Function(filter_mods_add, "+", name), ShowMenu("mods"))
                                            textbutton "%s (%d)"%((tags_translate[g][name.split(":")[-1]][_preferences.language] if g in tag_groups_translate and g in tags_translate and name.split(":")[-1] in tags_translate[g] else name.split(":")[-1]),n):
                                                xfill True right_margin 100 style "log_button"
                                                text_style "settings_text_small"
                    null width 5
                use scrollbars("left")
            if mods:
                side "c b r" area (0.27, 0.24, 0.47, 0.70):
                    viewport id "center" draggable True mousewheel True scrollbars None yinitial 0.0:
                        has vbox
                        for lbl, name in sorted(what_items,key=lambda (i,j):(j,i)):
                            hbox:
                                null width 5
                                if persistent.filter_settings["rad__mods_menu"]["quick_launch"]:
                                    if persistent.filter_settings["rad__mods_menu"]["swap_button_actions"]:
                                        imagebutton ypos 10:
                                            idle im.MatrixColor(im.Flip("images/gui/settings/vthumb.png", horizontal=True), im.matrix.opacity(0.6))
                                            hover im.Flip("images/gui/settings/vthumb.png", horizontal=True)
                                            action (Function(mod_select, lbl), ShowMenu("mods"))
                                    else:
                                        imagebutton ypos 10:
                                            idle im.MatrixColor(im.Flip("images/gui/settings/vthumb.png", horizontal=True), im.matrix.opacity(0.6))
                                            hover im.Flip("images/gui/settings/vthumb.png", horizontal=True)
                                            action (SetField(persistent, "jump_to", lbl), SetVariable(backdrop, 'prologue'), Start())
                                if persistent.filter_settings["rad__mods_menu"]["swap_button_actions"]:
                                    textbutton name style "log_button":
                                        if obs_config_mod_name in name:
                                            text_style "obs_settings_text" ypos -0.12
                                            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                                        else:
                                            text_style "settings_text"
                                        action (SetField(persistent, "jump_to", lbl), SetVariable(backdrop, 'prologue'), Start())
                                else:
                                    textbutton name style "log_button":
                                        if obs_config_mod_name in name:
                                            text_style "obs_settings_text" ypos -0.12
                                            hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                                        else:
                                            text_style "settings_text"
                                        action (Function(mod_select, lbl), ShowMenu("mods"))
                    use scrollbars("center")
            if mod_selected:
                add Image("mods_rad/side_menu.png") alpha 0.9 align (1.07, 0.61)
                side "c b r" area (0.761, 0.24, 0.234, 0.605):
                    viewport id "right" draggable True mousewheel True scrollbars None yinitial 0.0:
                        has hbox
                        null width 5
                        vbox xfill True:
                            text mods[mod_selected] style "settings_text"
                            for g in sorted(mod_tags_grouped[mod_selected]):
                                text "{color=#117743}%s:{/color} %s" % ( (tag_groups_translate[g][_preferences.language] if g in tag_groups_translate else g), (", ".join(mod_tags_grouped[mod_selected][g]))):
                                    style "settings_text_small"
                            vbox xalign 0.5:
                                textbutton __("Запустить") style "log_button" text_style "settings_text":
                                    action (SetField(persistent, "jump_to", mod_selected), SetVariable(backdrop, 'prologue'), Start())
                                for link, options in mod_links[mod_selected].iteritems():
                                    if options["type"] == "screen":
                                        textbutton options["name"][_preferences.language] xalign 0.5:
                                            style "log_button" text_style "settings_text"
                                            action ShowMenu(options["label"], **options["args"])
                                    elif options["type"] == "label":
                                        textbutton options["name"][_preferences.language] xalign 0.5:
                                            style "log_button" text_style "settings_text"
                                            action (SetField(persistent, "jump_to", options["label"]), SetVariable(backdrop, 'prologue'), Start())
                        null width 5
                    use scrollbars("right")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
