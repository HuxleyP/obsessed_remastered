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

label obs_say(who, what, _with):
    who "[what]" with _with
    return

label obs_new_context:
    return

label obs_clear_screens:
    "" nointeract
    pause 0.1
    window hide
    show layer screens at obs_screen_normal(0)
    return

label obs_default_start:
    $ Obs.Scene.Clear()
    $ Obs.Scene.Image("black")
    $ Obs.Stop.All(1)
    $ obs_screens_check = False
    $ _init_window()
    $ _history_list = []
    $ renpy.show("black")
    $ renpy.call("_start_store")
    $ renpy.start_predict_screen("main_menu")
    $ renpy.block_rollback()
    $ renpy.hide_screen("obs_overlay")
    $ Obs.Settings.ClearScreens()
    $ renpy.display.interface.with_none(overlay=False)
    $ renpy.music.play(config.main_menu_music, if_changed=True)
    $ renpy.music.stop(channel="movie")
    $ renpy.stop_predict_screen("main_menu")
    $ renpy.transition(config.end_splash_transition)
    $ renpy.call_in_new_context("_main_menu")
    $ renpy.game.context().force_checkpoint = True
    $ renpy.jump("start")

label obs_default_after_load:
    python:
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None
        renpy.execute_default_statement(False)
        _init_language()
    python hide:
        for i in config.after_load_callbacks:
            i()
        if config.after_load_transition and not Obs.IsModActive():
            renpy.transition(config.after_load_transition, force=True)
        if "_reload_time" in renpy.session:
            start = renpy.session.pop("_reload_time")
            import time
            if config.profile_reload:
                print("Reloading took:", time.time() - start, "seconds" )
        menu = renpy.session.pop("_reload_screen", None)
        if config.reload_menu and (menu is not None):
            renpy.run(ShowMenu(menu, *renpy.session.pop("_reload_screen_args", tuple()), **renpy.session.pop("_reload_screen_kwargs", { })))
    if Obs.IsModActive():
        $ Obs.Load(0.6 if persistent.obs_game_menu else 0.2)
        $ Obs.Settings.ScreensActivate(True)
        $ persistent._file_page = "obs_FilePage_1"
        $ persistent.sprite_time = obs_sprite_time
        $ persistent.obs_game_menu = True
        $ obs_after_load = True
    elif renpy.has_label("after_load"):
        $ renpy.jump("after_load")
    $ renpy.return_statement()
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
