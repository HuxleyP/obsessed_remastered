init -999 python:
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

screen obs_prologue_room_clicked:
    imagemap:
        ground Obs.PathImg() + "objects/obs_art_room_layer_gray.png"
        hover Obs.PathImg() + "objects/obs_art_room_layer_clicked_gray.png"
        alpha True

        if not obs_items_seen["1"]:
            hotspot (247, 838, 196, 243) clicked Obs_Call("check1") style "obs_imagemap"
        if not obs_items_seen["2"]:
            hotspot (604, 642, 118, 166) clicked Obs_Call("check2") style "obs_imagemap"
        if not obs_items_seen["3"]:
            hotspot (792, 492, 116, 83) clicked Obs_Call("check3") style "obs_imagemap"
        if not obs_items_seen["4"]:
            hotspot (782, 896, 392, 104) clicked Obs_Call("check4") style "obs_imagemap"
        if not obs_items_seen["5"]:
            hotspot (1011, 656, 116, 37) clicked Obs_Call("check5") style "obs_imagemap"
        if not Obs.InventoryIf("matches"):
            hotspot (1011, 695, 116, 37) clicked Obs_Call("check6") style "obs_imagemap"
        if not obs_items_seen["7"]:
            hotspot (1150, 786, 162, 82) clicked Obs_Call("check7") style "obs_imagemap"
        if not obs_items_seen["8"]:
            hotspot (1376, 518, 60, 171) clicked Obs_Call("check8") style "obs_imagemap"
        if not obs_items_seen["9"]:
            hotspot (1444, 936, 228, 93) clicked Obs_Call("check9") style "obs_imagemap"
        if not obs_items_seen["10"] and not Obs.InventoryIf("flashlight"):
            hotspot (1760, 890, 175, 96) clicked Obs_Call("check10") style "obs_imagemap"

    imagebutton style "obs_imagemap":
        idle Obs.PathImg() + "misc/arrows/kitchen.png"
        hover Obs.Brightness(Obs.PathImg() + "misc/arrows/kitchen.png", 0.3)
        align (1.0, 0.4) at obs_arrow_right_anim action Obs_Call("obs_prologue_kitchen_items.move")

screen obs_prologue_kitchen_clicked:
    imagemap:
        ground Obs.PathImg() + "objects/obs_art_kitchen2_gray.png"
        hover Obs.PathImg() + "objects/obs_art_kitchen_clicked_gray.png"
        alpha True

        if not obs_items_seen["11"] and not Obs.InventoryIf("knife", {"d":5, "h":7, "s":20, "e":["bleeding", 5]}):
            hotspot (404, 462, 185, 262) clicked Obs_Call("check1") style "obs_imagemap"
        if not obs_items_seen["12"] and not Obs.InventoryIf("knife", {"d":5, "h":7, "s":20, "e":["bleeding", 5]}):
            hotspot (957, 699, 144, 370) clicked Obs_Call("check2") style "obs_imagemap"
        if Obs.InventoryIf("matches") and Obs.InventoryIf("flashlight") and not Obs.InventoryIf("knife", {"d":5, "h":7, "s":20, "e":["bleeding", 5]}):
            hotspot (1254, 796, 150, 294) clicked Obs_Call("check3") style "obs_imagemap"
        if not obs_items_seen["14"] and not Obs.InventoryIf("knife", {"d":5, "h":7, "s":20, "e":["bleeding", 5]}):
            hotspot (1059, 210, 192, 273) clicked Obs_Call("check4") style "obs_imagemap"
        if not obs_items_seen["15"] and not Obs.InventoryIf("knife", {"d":5, "h":7, "s":20, "e":["bleeding", 5]}):
            hotspot (1414, 70, 173, 372) clicked Obs_Call("check5") style "obs_imagemap"
        if not Obs.InventoryIf("flashlight") and not Obs.InventoryIf("knife", {"d":5, "h":7, "s":20, "e":["bleeding", 5]}):
            hotspot (1587, 0, 356, 452) clicked Obs_Call("check6") style "obs_imagemap"

    add "obs_art_kitchen_backpack_gray" at obs_align(0.157, 1.0)

    imagebutton align (0.157, 1.0):
        idle Obs.PathImg() + "objects/obs_art_kitchen_backpack_gray.png"
        if Obs.InventoryIf("knife", {"d":5, "h":7, "s":20, "e":["bleeding", 5]}):
            style "obs_imagemap"
            hover Obs.Brightness(Obs.PathImg() + "objects/obs_art_kitchen_backpack_gray.png", 0.5)
            action Obs_Call("obs_prologue_kitchen_items.end")

    if not Obs.InventoryIf("knife", {"d":5, "h":7, "s":20, "e":["bleeding", 5]}):
        imagebutton align (0.0, 0.4) at obs_arrow_left_anim:
            style "obs_imagemap"
            idle Obs.PathImg() + "misc/arrows/room.png"
            hover Obs.Brightness(Obs.PathImg() + "misc/arrows/room.png", 0.3)
            action Obs_Call("obs_prologue_room_items.move")
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
