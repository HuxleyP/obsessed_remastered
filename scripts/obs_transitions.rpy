init -450 python:
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

init 9999 python:
    obs_dissolve_fast = Dissolve(0.1, alpha=True)
    obs_flash_hard = Fade(0.1, 0.0, 1.0, color="#fff")
    obs_mosaic_slow = Obs.ImageDissolve("mosaic", 5.0)
    obs_mosaic_slow_alt = Obs.ImageDissolve("mosaic_alt", 5.0)
    obs_mosaic_scene_fast = Obs.MultipleTransition("mosaic", 0.5, 0.5)
    obs_blinds_scene = Obs.MultipleTransition(blinds, 0.5, 1.0)
    obs_squares2_scene = Obs.MultipleTransition(squares, 0.5, 1.0)
    obs_in_x_move_fast = list(["in", "x", 0.5])
    obs_in_y_move_fast = list(["in", "y", 0.5])
    obs_out_x_move_fast = list(["out", "x", 0.5])
    obs_out_y_move_fast = list(["out", "y", 0.5])
    obs_in_x_move = list(["in", "x", 1.0])
    obs_in_y_move = list(["in", "y", 1.0])
    obs_out_x_move = list(["out", "x", 1.0])
    obs_out_y_move = list(["out", "y", 1.0])

    for i in range(1, 51):
        setattr(store, "obs_dissolve" + (str(i) if i != 1 else ""), Dissolve(0.25*i, alpha=True))
    for i in range(1, 11):
        setattr(store, "obs_flash" + (str(i) if i != 1 else ""), Fade(0.15*i, 0, 0.37*i, color="#FFFFFF"))
        setattr(store, "obs_flash_red" + (str(i) if i != 1 else ""), Fade(0.1*i, 0, 0.15*i, color="#FF0000"))
    for i in [["fast", 0.5], ["veryfast", 0.25]]:
        setattr(store, "obs_pushright" + i[0], PushMove(i[1], "pushright"))
        setattr(store, "obs_pushleft" + i[0], PushMove(i[1], "pushleft"))
        setattr(store, "obs_pushup" + i[0], PushMove(i[1], "pushup"))
        setattr(store, "obs_pushdown" + i[0], PushMove(i[1], "pushdown"))
    for i in obs_transitions_list:
        if "wipe" in i:
            setattr(store, i, Obs.ImageDissolve(i[4:], 1.0, 25))
            setattr(store, i + "_scene", Obs.MultipleTransition(i[4:], 0.5, 0.25, 25, False))
            setattr(store, i.replace("wipe", "bounce") + "_scene", Obs.MultipleTransition(i[4:], 0.5, 0.25, 25))
        else:
            setattr(store, i, Obs.ImageDissolve(i[4:], 1.0))
            setattr(store, i + "_alt", Obs.ImageDissolve(i[4:] + "_alt", 1.0, 5))
            setattr(store, i + "_scene", Obs.MultipleTransition(i[4:], 0.5, 1.0, 5))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
