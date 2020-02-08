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

init python:
    def obs_splashscreen():
        Obs.Scene.Image("black", _with=obs_dissolve4)
        Obs.Pause(1)
        Obs.Master(obs_bg_zoom_e(1.0, 1.7, 4.0))
        Obs.Play.Music("obs_careless_whisper", 1, start=16.2)
        for num in range(1, 68):
            if config.skipping:
                break
            Obs.Show.Image("logo", at=[obs_image("misc/logo/" + str(num) + ".png"), obs_align(0.5, 0.5)])
            Obs.Pause(0.005)
            Obs.Hide.Image("logo")
        Obs.Show.Image("logo", at=[obs_image("misc/logo/68.png"), obs_align(0.5, 0.5)])
        Obs.Pause(2)
        Obs.Play.Sound2("obs_glass_breaking")
        Obs.Show.Image("obs_broken_glass", sound="obs_shoot", layer="mapoverlay", expr="obs_redscale", _with=vpunch)
        Obs.Pause(2.5)
        Obs.Master(obs_bg_zoom_e(1.7, 1.0, 4.0))
        Obs.Stop.Music(4)
        Obs.Hide.Image("obs_broken_glass", layer="mapoverlay")
        Obs.Scene.Image("black", _with=obs_dissolve12)
        Obs.Pause(1, hard=False)
        Obs.Play.Music("obs_detroit", 3)
        Obs.Scene.Image("bg obs_old_building_corridor_red")
        Obs.Show.Image("obs_interference_anim")
        Obs.Show.Image("obs_loading_icon", at=obs_full_rotate_repeat(1.0, 0.5, 1.0, 1.0), _with=obs_dissolve8)
        Obs.Show.Text("В моде присутствует система автосохранения.\nНе отключайте игру, пока виден этот значок.", 40, color="#FF0000", type="normal", pause=False)
        Obs.Show.Image("obs_loading_icon", tag="icon2", at=obs_full_rotate_repeat(1.0, 0.5, 0.5, 0.62), _with=obs_dissolve8)
        Obs.Pause(3, hard=False)
        Obs.Hide.Text()
        Obs.Hide.Image("icon2", _with=obs_dissolve8)
        Obs.Pause(1, hard=False)
        Obs.Show.Text("Также во фразах второго главного героя\n может проскакивать нецензурная речь.\nВ настройках можно включить фильтр мата, дабы тот убрать.", 40, color="#FF0000", type="normal", pause=False, _with=obs_dissolve8)
        Obs.Pause(3, hard=False)
        Obs.Hide.Text(obs_dissolve8)
        Obs.Pause(1, hard=False)
        Obs.Show.Text("В моде могут присутствовать сцены жестокости и кровопролития.\nНе рекомендуется играть слабонервным или людям, страдающим\n от беспокойства или депрессии.", 40, color="#FF0000", type="normal", pause=False, _with=obs_dissolve8)
        Obs.Pause(3, hard=False)
        Obs.Hide.Text(obs_dissolve8)
        Obs.Stop.Music(3)
        Obs.Scene.Image("black", _with=obs_dissolve8)
        Obs.Pause(1, hard=False)

    def obs_girls_attack(yoffset, time):
        Obs.Master(obs_bg_zoom_e2(1.0, 1.2, 0.3, y=1.0, yy=1.0, tt=0.3, yyy=1.0))
        Obs.Show.Image("obs_girls_attack_layer", at=obs_xoffset_linear(0, 200, 0.1))
        Obs.Play.Sound("obs_attack")
        Obs.With.Statement(hpunch)
        Obs.Pause(0.1)
        Obs.Master(obs_bg_zoom_e2(1.0, 1.2, 0.3, y=1.0, yy=1.0, tt=0.3, yyy=1.0))
        Obs.Show.Image("obs_girls_attack_layer", at=obs_xoffset_linear(200, -200, 0.1))
        Obs.Play.Sound("obs_attack")
        Obs.With.Statement(hpunch)
        Obs.Pause(0.1)
        Obs.Master(obs_bg_zoom_e2(1.0, 1.2, 0.3, y=1.0, yy=1.0, tt=0.3, yyy=1.0))
        Obs.Show.Image("obs_girls_attack_layer", at=obs_offset_linear(0, 0, 0, yoffset, 0.1))
        if yoffset == 400:
            Obs.Play.Sound2("obs_comedy_shake")
            Obs.Screens(obs_screen_shake(0.01))
        Obs.Play.Sound("obs_attack")
        Obs.With.Statement(vpunch)
        Obs.Pause(time)
        Obs.Show.Image("obs_girls_attack_layer", at=obs_yoffset_linear(yoffset, 0, 0.5))

    def obs_dinner_art_cg(number, time, emotion, x, s):
        Obs.Global("zoom_time", [1.2, 1.0] if number != 3 else [1.7, 3.0])
        Obs.Screens(obs_circular_dizziness)
        Obs.Scene.Image("cg obs_d1_art_dining" + str(number), at=obs_bg_zoom_e(1.0, zoom_time[0], zoom_time[1], y=0.4, yy=0.4))
        Obs.With.Statement(Dissolve(0.25))
        Obs.Pause(time)
        Obs.Scene.Image("bg obs_int_dining_table_sunset")
        Obs.Show.Image("mi " + emotion, at=[obs_normal(1050), obs_offset(x, -150), obs_rotate(0)])
        Obs.Show.Image("obs_int_dining_table_layer_sunset", zorder=2)
        Obs.Master(obs_shake(7, 1.25, 0.1))
        Obs.Screens(obs_shake_motion(s))
        Obs.With.Statement(Dissolve(0.25))
        Obs.Delete("zoom_time")

    def obs_msk_and_us_square_zoom():
        Obs.Hide.Screens()
        Obs.Show.BlockDissmiss()
        Obs.GlobalField(config, "skipping", False)
        Obs.Play.Music("obs_bad_apple")
        Obs.Pause(3)
        Obs.Master(obs_bg_zoom_rotate_e(1.0, 1.1, 0.5))
        Obs.Pause(0.8)
        Obs.Master(obs_bg_zoom_rotate_e(1.1, 1.2, 0.5))
        Obs.Pause(0.8)
        Obs.Master(obs_bg_zoom_rotate_e(1.2, 1.3, 0.5))
        Obs.Pause(0.6)
        Obs.Master(obs_bg_zoom_rotate_e(1.3, 1.4, 0.5))
        Obs.Pause(0.6)
        Obs.Master(obs_bg_zoom_rotate_e(1.4, 1.5, 0.5))
        Obs.Pause(0.6)
        Obs.Master(obs_bg_zoom_rotate_e(1.5, 1.6, 0.5))
        Obs.Pause(0.6)
        Obs.Master(obs_bg_zoom_rotate_e(1.6, 2.8, 0.5))
        Obs.Pause(0.6)
        Obs.Master(obs_bg_zoom_rotate_e(2.8, 2.0, 0.5))
        Obs.Show.Image("us grin far", at=obs_lf11)
        Obs.Show.Image("us smile far", _with=None)
        Obs.Show.Screens()

    def obs_msk_and_us_square_dialogs(name, time=0, time2=0, start="", end=""):
        if name == "msk":
            Obs.Show.Image("us grin far", sound="obs_run", end_sound=0.8, at=getattr(store, "obs_" + start + "fhide"))
            Obs.Master(obs_bg_zoom_rotate_e(2.0, 1.2, 1.0))
            Obs.Pause(time)
            Obs.Show.Image("msk sad far", sound="obs_run", end_sound=0.8, at=getattr(store, "obs_" + end + "f11"))
            Obs.Master(obs_bg_zoom_rotate_e(1.2, 1.7, 1.0, yy=0.4))
            Obs.Pause(time2)
        elif name == "us":
            Obs.Show.Image("msk sad far", sound="obs_run", end_sound=0.8, at=getattr(store, "obs_" + start + "fhide"))
            Obs.Master(obs_bg_zoom_rotate_e(1.7, 1.2, 1.0, y=0.4, yy=0.5))
            Obs.Pause(time)
            Obs.Show.Image("us grin far", sound="obs_run", end_sound=0.8, at=getattr(store, "obs_" + end + "f11"))
            Obs.Master(obs_bg_zoom_rotate_e(1.2, 2.0, 1.0))
        else:
            Obs.Show.Image("us grin far", sound="obs_run", end_sound=0.8, at=obs_lfhide)
            Obs.Master(obs_bg_zoom_rotate_e(2.0, 1.2, 1.0))
            Obs.Pause(1.0)
            Obs.Screens(obs_circular_dizziness)
            Obs.Play.Sound2("obs_run", end=0.8)
            Obs.Show.Image("msk sad far", at=obs_rf11)
            Obs.Master(obs_bg_zoom_rotate_e(1.2, 1.7, 1.0, yy=0.4))

    def obs_msk_and_us_square_running():
        Obs.Global("pos", ["l", "r"])
        Obs.Master(obs_bg_zoom_rotate_e(1.7, 1.7, 0.5, y=0.4, yy=0.5, r=360))
        Obs.Pause(0.5)
        Obs.Master(obs_bg_zoom_rotate_e(1.7, 1.2, 0.5, y=0.5, yy=0.5, r=-360))
        Obs.Pause(0.5)
        Obs.Master(obs_bg_zoom_rotate_e(1.7, 1.2, 0.5, y=0.5, yy=0.5))
        Obs.Play.SoundLoop("obs_run")
        Obs.Show.Image("msk sad far", at=obs_lfhide)
        Obs.Hide.Screens()
        for emotion in ["grin", "laugh", "smile", "surp1", "laugh"]:
            Obs.Show.Image("us " + emotion + " far", at=getattr(store, "obs_" + pos[0] + "f11"))
            Obs.Pause(0.5)
            Obs.Show.Image("us " + emotion + " far", at=getattr(store, "obs_" + pos[1] + "fhide"))
            Obs.Pause(0.5)
            Obs.Show.Image("msk sad far", at=getattr(store, "obs_" + pos[0] + "f11"))
            Obs.Pause(0.5)
            Obs.Show.Image("msk sad far", at=getattr(store, "obs_" + pos[1] + "fhide"))
            Obs.Pause(0.5)
            Obs.Global("pos", ["l", "r"] if pos == ["r", "l"] else ["r", "l"])
        Obs.Stop.SoundLoop(1)
        Obs.Show.Screens()
        Obs.Delete("pos")

    def obs_sound_repeat(audio, time, rep):
        for repeat in range(0, rep):
            Obs.Play.Sound(audio)
            Obs.Pause(time)

    def obs_cards_sprites(un="normal", aln="normal", mi="normal", msk="smile", trans=True, nomi=False, _with=""):
        if trans:
            Obs.Show.Image("black")
            Obs.With.Statement(obs_blinds_up)
            Obs.Pause(0.5)
        Obs.Global("xpos", 800 if mi != "happy" else 720)
        Obs.Scene.Image("bg obs_int_house_of_aln_rain_anim")
        Obs.Show.Image("obs_chair", tag="c1", at=[obs_i41, obs_yoffset(-100)])
        Obs.Show.Image("obs_chair", tag="c2", at=[obs_i42, obs_yoffset(-100)])
        Obs.Show.Image("obs_chair", tag="c3", at=[obs_i43, obs_yoffset(-100)])
        Obs.Show.Image("obs_chair", tag="c4", at=[obs_i44, obs_yoffset(-100)])
        Obs.Show.Image("un " + un, at=[obs_sit, obs_i41, obs_yoffset(-100)])
        Obs.Show.Image("aln " + aln, at=[obs_sit, obs_i43, obs_yoffset(-100)])
        if nomi == False:
            Obs.Show.Image("mi " + mi, at=[obs_sit, obs_normal(xpos), obs_yoffset(-100)])
        Obs.Show.Image("msk " + msk, at=[obs_sit, obs_normal(1650), obs_yoffset(-100)])
        Obs.Show.Image("obs_int_house_of_aln_rain_layer")
        if nomi == None:
            Obs.Show.Image("mi normal", at=obs_bg_zoom_e(zz=1.7, xx=-0.05, yy=0.25))
        Obs.With.Statement(_with if _with != "" else obs_blinds_up_alt)
        Obs.Delete("xpos")

    def obs_flashlight_on_of(rep, time):
        for repeat in range(0, rep):
            Obs.Pause(time)
            Obs.Play.Sound("obs_flashlight_on")
            Obs.Pause(time)
            Obs.Play.Sound("obs_flashlight_off")

    def obs_mi_greedy_kissing(rep):
        for repeat in range(0, rep):
            Obs.Play.Sound("obs_kiss2")
            Obs.With.Statement(flash)
            Obs.Pause(0.1)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
