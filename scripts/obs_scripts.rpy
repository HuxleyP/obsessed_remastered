init -150 python:
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

init -50 python:
    Obs.Settings.Config("folder", "mods/obsessed_remastered/")
    Obs.Settings.ModIdentify("Одержимая Remastered", "SuperRage", "obs_start", "normal.ttf", "#FF0000")

    Obs.Settings.Config("name", "Obsessed")
    Obs.Settings.Config("version", "0.1.0.6")

    Obs.Settings.ModTags(gameplay="kinetic", length="days", protagonist="male", characters=["new character", "Артём", "Мишка", "Алёна", "Вадим", "Петя", "Внутренний голос", "Алиса", "Виола", "Женя", "Лена", "Мику", "Ольга Дмитриевна", "Славя", "Ульяна", "Шурик", "Электроник", "Юля"])
    Obs.Settings.DefaultVariables()

    Obs.Settings.Config("interface", True)
    Obs.Settings.Config("rollback_enabled", True)
    Obs.Settings.Config("after_load_transition", Obs.MultipleTransition("mosaic", 0.5, 0.5))
    Obs.Settings.Config("enter_transition", Obs.ImageDissolve("pattern", 0.7))
    Obs.Settings.Config("exit_transition", Obs.ImageDissolve("pattern_alt", 0.7))
    Obs.Settings.Config("enter_yesno_transition", store.Dissolve(0.25))
    Obs.Settings.Config("exit_yesno_transition", store.Dissolve(0.25))
    Obs.Settings.Config("intra_transition", Obs.ImageDissolve("pattern", 0.7))
    Obs.Settings.Config("enter_sound", Obs.PathMain() + "sound/buttons/obs_menu.ogg")
    Obs.Settings.Config("exit_sound", Obs.PathMain() + "sound/buttons/obs_menu.ogg")
    Obs.Settings.Config("game_menu_action", Obs.Settings.GameMenuCheck)
    Obs.Settings.Config("has_autosave", False)
    Obs.Settings.Config("mouse", {"default" : [(Obs.PathImg() + "gui/mouse/" + obs_timeofday + ".png", 0, 0)]})

init python:
    Obs.Settings.ReloadNames()

    Obs.Settings.AppendName("art", "Артём",             (0, 255, 0))
    Obs.Settings.AppendName("msk", "Мишка",             (255, 140, 0))
    Obs.Settings.AppendName("cop", "Мент",              (0, 130, 181))
    Obs.Settings.AppendName("dgs", "Собаки",            (255, 255, 255))
    Obs.Settings.AppendName("grl", "Девушка",           (255, 255, 255))
    Obs.Settings.AppendName("kvl", "...",               (255, 255, 255))
    Obs.Settings.AppendName("gls", "Голоса",            (198, 0, 0))
    Obs.Settings.AppendName("gl",  "Голос",             (255, 255, 255))
    Obs.Settings.AppendName("aln", "Алёна",             (65, 105, 225))
    Obs.Settings.AppendName("vdm", "Вадим",             (173, 255, 47))
    Obs.Settings.AppendName("pt",  "Петя",              (0, 130, 181))
    Obs.Settings.AppendName("dnc", "Внутренний танцор", (255, 255, 255))
    Obs.Settings.AppendName("unk1", "Неизвестный 1",    (255, 255, 255))
    Obs.Settings.AppendName("unk2", "Неизвестный 2",    (255, 255, 255))
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
