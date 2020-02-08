init -800 python:
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

screen obs_items(number, name, items, check, stats) tag menu zorder 100 modal True:
    if check != True:
        $ check = Obs.InventoryIf(check, stats)

    fixed at obs_menu_move:
        frame background Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/background2.png"
        imagebutton offset (1423, 184):
            if check:
                hover_sound obs_hover_interface_sound activate_sound obs_activate_menu_sound
                auto Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/exit2_%s.png"
                action [Obs_QuitItemsMenu(), Return()]
            else:
                idle Obs.Brightness(Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/exit2_idle.png", -0.2)
        text name style "obs_text_item_label_" + Obs.Rename(obs_timeofday) offset (793, 172)

        vbox pos (0.309, 0.242) spacing 6:
            use obs_items_slots(number, items, stats)
        vbox pos (0.526, 0.242) spacing 6:
            use obs_inventory_slots

screen obs_inventory(type=None, item=None) tag menu zorder 100 modal True:
    if type == None:
        for key_i in obs_key_i_list:
            key key_i action Return()

    fixed offset (27, -4) at obs_menu_move:
        frame background Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/icons/" + obs_hover_slot["name"] + ".png"
        frame background Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/background.png"

        imagebutton offset (1378, 279):
            idle Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + obs_backpack["name"] + "_idle.png"
            if obs_backpack["name"] != "empty":
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                hover Obs.Brightness(Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + obs_backpack["name"] + "_hover.png", 0.1)
                insensitive Obs.Brightness(Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + obs_backpack["name"] + "_idle.png", 0.5)
                action Obs_SelectedSlot("BPK")

        imagebutton offset (1378, 363):
            idle Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + obs_weapon + "_idle.png"
            if obs_weapon != "empty" and obs_weapon != "lock":
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                hover Obs.Brightness(Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + obs_weapon + "_idle.png", 0.1)
                insensitive Obs.Brightness(Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + obs_weapon + "_idle.png", 0.5)
                action Obs_SelectedSlot("WPG")

        if obs_hover_slot["slot"] != "BPK" and obs_hover_slot["name"] != "empty":
            if obs_hover_slot["slot"] == "WPG":
                textbutton ["Снять"] action Obs_TakeoffItem()
            else:
                textbutton ["Экипировать" if obs_hover_slot["name"] in obs_weapons_list else "Применить"]:
                    style "obs_button_none" offset (970, 837) text_size 30
                    text_style "obs_text_small_save_load_" + Obs.Rename(obs_timeofday)
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                    action [Obs_ApplyItem(item, type), If(obs_hover_slot["name"] == item, true=Return(), false=Hide("none"))]
            textbutton ["Выбросить"]:
                style "obs_button_none" offset (1155, 837) text_size 30
                text_style "obs_text_small_save_load_" + Obs.Rename(obs_timeofday)
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                action Obs_ThrowItem()

        if obs_hover_slot["name"] != "empty":
            text obs_items_dict[obs_hover_slot["name"]] style "obs_text_label_" + Obs.Rename(obs_timeofday) size 40 pos (0.594, 0.53) xanchor 0.5
            vbox pos (0.439, 0.58):
                if obs_hover_slot["name"] in obs_weapons_list:
                    text "Урон: " + str(obs_hover_slot["stats"]["d"]) style "obs_text_label_" + Obs.Rename(obs_timeofday) size 20 xpos 0.5 xanchor 0.5
                    text "Тяжесть: " + str(obs_hover_slot["stats"]["h"]) style "obs_text_label_" + Obs.Rename(obs_timeofday) size 20 xpos 0.5 xanchor 0.5
                    text "Скорость атаки: " + str(obs_hover_slot["stats"]["s"]) style "obs_text_label_" + Obs.Rename(obs_timeofday) size 20 xpos 0.5 xanchor 0.5
                    if obs_hover_slot["stats"]["e"]:
                        text "Шанс вызвать " + obs_effects_dict[obs_hover_slot["stats"]["e"][0]] + " : " + str(obs_hover_slot["stats"]["e"][1]) style "obs_text_label_" + Obs.Rename(obs_timeofday) size 20 xpos 0.5 xanchor 0.5
                    text "" size 5
                elif obs_hover_slot["name"] in obs_backpacks_list:
                    text "Качество: " + obs_hover_slot["stats"]["q"] style "obs_text_label_" + Obs.Rename(obs_timeofday) size 20 xpos 0.5 xanchor 0.5
                    text "Доп. ячейки: " + str(obs_hover_slot["stats"]["c"]) style "obs_text_label_" + Obs.Rename(obs_timeofday) size 20 xpos 0.5 xanchor 0.5
                    text "" size 5
                text Obs.Settings.ItemDescription(obs_hover_slot["name"]) style "obs_text_item_description_" + Obs.Rename(obs_timeofday)

        vbox pos (0.187, 0.242) spacing 6:
            use obs_inventory_slots

    fixed at obs_menu_move:
        imagebutton offset (1573, 174):
            hover_sound obs_hover_interface_sound activate_sound obs_activate_menu_sound
            auto Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/exit_%s.png"
            action If(type, true=Obs_Message("Вам необходимо использовать нужный предмет."), false=Return())

    fixed align (0.5, 0.5) anchor (0.5, 0.5) at obs_menu_move(0.7):
        text "Инвентарь":
            style "obs_text_label_" + Obs.Rename(obs_timeofday)
            size 70 text_align 0.5 align (0.5, 0.005) antialias True kerning 2
        if type == None:
            textbutton "<":
                text_style "obs_text_setting_" + Obs.Rename(obs_timeofday)
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                style "obs_button_none" text_size 60 align (0.34, 0.01)
                action ShowMenu("obs_preferences")
            textbutton ">":
                text_style "obs_text_setting_" + Obs.Rename(obs_timeofday)
                hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                style "obs_button_none" text_size 60 align (0.65, 0.01)
                action ShowMenu("obs_load")

screen obs_inventory_message:
    text obs_inventory_message style "obs_text_label_" + Obs.Rename(obs_timeofday) size 40 at obs_message_move
    timer 3.4 action [SetVariable("obs_inventory_message", ""), Hide("obs_inventory_message")]

screen obs_items_slots(number, items, stats):
    grid 4 2 spacing 7:
        for slot in range(0, 8):
            imagebutton:
                idle Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + items[slot]["name"] + "_idle.png"
                if items[slot]["name"] != "empty":
                    hover_sound obs_hover_interface_sound
                    hover Obs.Brightness(Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + items[slot]["name"] + "_hover.png", 0.1)
                    action Obs_ShowItem(number, items, stats, slot)

screen obs_inventory_slots:
    grid 4 8 spacing 7:
        for slot in range(0, 32):
            imagebutton:
                idle Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + obs_inventory[slot]["name"] + "_idle.png"
                if obs_inventory[slot]["name"] not in ["empty", "lock"] and not obs_show_items_window:
                    hover_sound obs_hover_interface_sound activate_sound obs_activate_interface_sound
                    hover Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + obs_inventory[slot]["name"] + "_hover.png"
                    insensitive Obs.Brightness(Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/" + obs_inventory[slot]["name"] + "_idle.png", 0.5)
                    action Obs_SelectedSlot(slot)
                if obs_inventory[slot]["name"] != "lock" and slot > 3:
                    foreground Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/plus_idle.png"
                    hover_foreground Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/plus_hover.png"
                    if obs_inventory[slot]["name"] != "empty":
                        insensitive_foreground Obs.Brightness(Obs.PathImg() + "gui/inventory/" + obs_timeofday + "/slots/plus_idle.png", 0.5)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
