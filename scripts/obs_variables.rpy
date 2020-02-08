init -550 python:
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

init -15 python:
    import datetime

    obs_swear_dict = {"блять":"блин", "ёпта":"ё-моё", "бля":"блин", "мля":"блин", "ни хуя":"ничего",
        "ни хуя се":"ничего се", "ни хрена":"ничего", "на хуя":"на фига", "на хуй":"на фиг", "на хрен":"на фиг",
        "пошлют на хрен":"пошлют на три буквы", "хуйня":"фигня", "нах":"зачем", "ебать":"блин", "ёпте":"блин",
        "пиздец":"капец", "какого хрена":"какого чёрта", "твою мать":"твою дивизию", "заебись":"шикардос",
        "ахуенно":"супер", "ахуе":"недоумении", "ахуеть":"вот это да", "заебумба":"зашибись", "ни фига":"ничего",
        "нафига":"зачем", "хреново":"так себе", "хуявила":"шмалива", "тоби пизда":"кому-то трындец",
        "бляяяяяяяяяяяя":"блиииииииииииин", "хренасе-хуясе":"шыры-мыры", "пиздеть":"брехать", "пиздел":"брехал",
        "съебись":"свали"}

    obs_music_dict = {
        "obs_a_pashtun_story":"He Named Me Malala — A Pashtun Story (Main Theme) - Thomas Newman",
        "obs_ame_iro_rondo":"Cat Trumpet — Ame Iro Rondo (Piano Version)",
        "obs_anglegrinder":"Josh Powell — Anglegrinder (Instrumental)",
        "obs_arbitz":"\"Nature\" — Album Intro Arbitz",
        "obs_autumn_song":"God is An Astronaut — Autumn Song",
        "obs_bad_apple":"Touhou — Bad Apple (Receptor Cover)",
        "obs_been_to_hell":"Hollywood Undead — Been to Hell (Instrumental)",
        "obs_bit":"Мекка-Ватикан — Бит v2",
        "obs_blitzkrieg_death_mix":"Audiomachine — Blitzkrieg Death Mix (Deus Ex Machina OST)",
        "obs_bridge_over_stars":"Keiko Matsui — Bridge Over Stars (Instrumental)",
        "obs_cant_not":"Alanis Morissette — Can't Not",
        "obs_careless_whisper":"Seether — Careless Whisper (Instrumental, SuperRage Editing, Loop Version)",
        "obs_chance":"Chance",
        "obs_comatose":"Piano Tribute Players — Comatose",
        "obs_company":"Disasterpeace — Company (Саундтрек из фильма \"Оно следует за тобой\", Calm Version)",
        "obs_complete_silence":"Complete Silence",
        "obs_creeping_up":"Josh Powell — Creeping Up",
        "obs_cryin_light":"Rock'n'Rollerz — Crying Lightning (Instrumental)",
        "obs_curb_your_enthusiasm":"Theme — Curb Your Enthusiasm",
        "obs_cut_and_dry_electronic_hard":"Kevin MacLeod — Cut and Dry - Electronic Hard",
        "obs_dead_silence":"Charlie Clouser — Dead Silence (Calm Version)",
        "obs_deadman_on_vacation":"April Rain — Deadman on Vacation",
        "obs_death_note_ost":"Yotsuba Koroshi no Kaigi Shitsu — Death Note OST (Саундтрек из аниме \"Тетрадь Смерти\")",
        "obs_demilitarized_zone":"Ethan Meixsell — Demilitarized Zone",
        "obs_depression":"Витюша Бондарев — 17DEPRESSION (Instrumental)",
        "obs_detroit":"Disasterpeace — Detroit (Саундтрек из фильма \"Оно следует за тобой\")",
        "obs_emptiness":"Владимир Зеленцов — Emptiness (Calm Version)",
        "obs_ending":"Ранетки — Окончание",
        "obs_ending_our_reign":"Kvoid — Ending Our Reign",
        "obs_escape_from_yourself":"Escape from Yourself",
        "obs_fighting_johnny_vincent":"Shawn Lee — Fighting Johnny Vincent: Boss Fight (Bully OST)",
        "obs_final_showdown":"Shawn Lee — Final Showdown (Bully OST)",
        "obs_gonna_be_ok":"DeepCosmo — Gonna Be Ok (Calm Version)",
        "obs_hawaii_budapest":"Bye Horus — Hawaii Budapest",
        "obs_hopelessness":"Hopelessness",
        "obs_ingaritsu_daiseidou":"Tatsuya Katou — Ingaritsu Daiseidou (Саундтрек из аниме \"Дневник Будущего\", Symphonic Metal, Piano, Violin)",
        "obs_inquiry":"Disasterpeace — Inquiry (Саундтрек из фильма \"Оно следует за тобой\", Calm Version)",
        "obs_inquiry2":"Disasterpeace — Inquiry (Саундтрек из фильма \"Оно следует за тобой\", Calm Version)",
        "obs_i_am_sending_a_code_remix":"Катя Чехова — Я посылаю код (Russian House Remix, SuperRage Instrumental)",
        "obs_i_ll_find_it_anyway":"Дима Билан — Всё Равно Найду (Instrumental)",
        "obs_i_ll_find_it_anyway_with_vocal":"Дима Билан — Всё Равно Найду",
        "obs_konran_culture":"Tatsuya Katou — Konran Culture (Саундтрек из аниме \"Дневник Будущего\")",
        "obs_laborious_work":"Laborious Work",
        "obs_lakeward":"Disasterpeace — Lakeward (Саундтрек из фильма \"Оно следует за тобой\")",
        "obs_leafs_falling":"Dead By Aplil — Leafs Falling",
        "obs_lights_go_out":"I Am Waiting for You Last Summer — Lights Go Out (SuperRage Editing)",
        "obs_lunar_anguish":"Л. ван Бетховен — Лунная Соната (Remix)",
        "obs_madness":"Madness",
        "obs_mafia":"Mafia",
        "obs_main_theme":"Rik Schaffer — Main Theme (Vampire: The Masquerade – Bloodlines 2 OST)",
        "obs_medicating":"David Wingo — Medicating",
        "obs_memory":"Аревик Аветисян — Воспоминание",
        "obs_miniskirt":"AOA — Miniskirt Japanese Version (Instrumental)",
        "obs_mirage_go_summer":"MIRAGE — Уходящее Лето",
        "obs_mudda_sunrise":"Muddasheep — Sunrise",
        "obs_mystery_after_mystery":"Mystery After Mystery",
        "obs_never_forgive_me":"Akira Yamaoka — Never Forgive Me, Never Forget Me (Саундтрек из фильма \"Сайлент Хилл 2\")",
        "obs_niles_blues":"Kevin MacLeod — Niles Blues",
        "obs_no_tresspassing_hunx":"Sergey Eybog — No Tresspassing (Hunx)",
        "obs_no_tresspassing_remix":"Sergey Eybog — No Tresspassing (Remix)",
        "obs_no_tresspassing_remix2":"Sergey Eybog — No Tresspassing (Remix, Glitch Version)",
        "obs_norikoeru_beki_wa_satsugai_kyoufu":"Tatsuya Katou — Norikoeru Beki wa Satsugai Kyoufu (Саундтрек из аниме \"Дневник Будущего\")",
        "obs_obiymy":"BACKSPACE x VCIDMIND — ОБIЙМИ (Instrumental)",
        "obs_orchid_remix":"Between August and December — Orchid (Remix)",
        "obs_patriots":"Дионис — Патриоты (Instrumental)",
        "obs_poligon":"Oxxymiron — Poligon (Instrumental)",
        "obs_poligon_grimly":"Oxxymiron — Poligon (Instrumental, Grimly Version)",
        "obs_psicose":"R3ckzet — Psicose (Original Mix)",
        "obs_rethinking":"Rethinking",
        "obs_salvation":"Salvation (SuperRage Editing)",
        "obs_second_season":"Алексей Шелыгин — 2-ой сезон (Саундтрек из Т/с \"Карпов\")",
        "obs_senritsu":"Yotsuba Koroshi no Kaigi Shitsu — Senritsu (Саундтрек из аниме \"Тетрадь Смерти\", SuperRage Editing)",
        "obs_sheer_terror":"Harry Manfredini — Sheer Terror (Friday the 13th: The Game OST)",
        "obs_sirius":"Ben Chatwin — Sirius",
        "obs_soma":"Project Hypoxia — Soma",
        "obs_son_of_the_monolith":"Project Hypoxia — Son of The Monolith",
        "obs_son_of_torture":"Soul Psycho — Son of Torture",
        "obs_sound_of_madness2":"Shinedown — Sound of Madness 2",
        "obs_spirit":"Marcus D — Kindred Spirit Feat. Emancipator",
        "obs_suiri":"Taniuchi Hideki — Suiri (Саундтрек из аниме \"Тетрадь Смерти\")",
        "obs_surrender":"I Am Waiting for You Last Summer — Surrender (SuperRage Editing, Loop Version)",
        "obs_sweater_weather":"The Karaoke Universe — Sweater Weather (Instumental)",
        "obs_taking_a_beating":"Ethan Meixsell — Taking a Beating",
        "obs_tearsges":"Tearsges",
        "obs_that_man":"Caro Emerald — That Man (Instrumental)",
        "obs_the_game_of_life":"Hatsune Miku — The Game of Life (Instrumental)",
        "obs_the_loneliness_of_the_capercaillie":"Алексей Шелыгин — Одиночество Глухаря (Саундтрек из Т/с \"Глухарь\")",
        "obs_the_nothing":"Creep Crawl Flash — The Nothing",
        "obs_the_town_that_does_not_exist":"Игорь Корнелюк — Город, которого нет (Instrumental)",
        "obs_the_ways":"НИККИ — Комета",
        "obs_theme_from_the_ocean":"Digital Elvis & Zero — Theme From The Ocean",
        "obs_title":"Disasterpeace — Title (Саундтрек из фильма \"Оно следует за тобой\")",
        "obs_ukyo_melody":"OST Amnesia — Ukyo's Melody (Calm Version)",
        "obs_violence_of_the_moonlight":"Veturheim — Violence of the Moonlight (SuperRage Editing)",
        "obs_waking_up_in_florence":"Dayda Banks, Filth the Enabler — Waking up in Florence (Instrumental)",
        "obs_weekdays":"Weekdays",
        "obs_where_are_you":"Walkaway — Where Are You?",
        "obs_white_roses_piano":"Юра Шатунов — Белые Розы (Instrumental, Piano Version)",
        "obs_white_roses_remix":"Юра Шатунов — Белые Розы (Instrumental, Remix)",
        "obs_wood":"Dom!No — Wood (Instrumental)"}

    obs_names_list = []
    obs_items_list = ["phone", "matches", "flashlight", "key13"]
    obs_weapons_list = ["knife"]
    obs_backpacks_list = ["easy"]
    obs_reusable_items_list = ["key13"]
    obs_ordinary_items_list = []
    obs_key_i_list = ["i", "I", "ш", "Ш"]
    obs_transitions_list = ["obs_blinds_up", "obs_circle", "obs_darkness", "obs_love", "obs_mosaic", "obs_paint", "obs_pattern", "obs_pixel", "obs_pixels", "obs_scratches", "obs_squares", "obs_stained", "obs_time_circle", "obs_wipedown", "obs_wipeleft", "obs_wiperight", "obs_wipeup"]
    obs_key_dismiss_list = ["K_MENU", "K_ESCAPE", "dismiss", "button_select", "input_enter", "bar_activate", "bar_deactivate", "mouseup_1", "mouseup_3", "K_SPACE"]
    obs_tint_dict = {"s":im.matrix.tint(0.94, 0.82, 1.0), "n":im.matrix.tint(0.63, 0.78, 0.82), "r":im.matrix.tint(0.32, 0.54, 0.24)}
    obs_items_dict = {"phone":"Старый телефон", "matches":"Спички", "flashlight":"Фонарик", "knife":"Кухонный нож", "easy":"Лёгкий рюкзак", "key13":"Ключ от 13-го домика"}
    obs_effects_dict = {"bleeding":"кровотечение"}
    obs_fail_end_credits = "Конец.\n\nВот так и заканчивается моя история..."

    obs_black_color = "#000000"
    obs_white_color = "#FFFFFF"
    obs_red_color = "#DB0000"
    obs_red_light_color = "#FF0000"
    obs_red_dark_color = "#690000"
    obs_blue_color = "#00FFFF"
    obs_blue_dark_color = "#0042FF"
    obs_orange_color = "#DF5500"
    obs_orange_light_color = "#FAAC58"
    obs_orange_dark_color = "#853300"
    obs_gray_color = "#848484"
    obs_gray_light_color = "#BDBDBD"
    obs_gray_dark_color = "#323232"
    obs_gray_dark_color2 = "#4E4E4E"
    obs_yellow_color = "#E4CE13"
    obs_green_color = "#31BE00"
    obs_green_dark_color = "#00CB22"

    obs_hover_sound = Obs.PathMain() + "sound/buttons/obs_hover.ogg"
    obs_hover_interface_sound = Obs.PathMain() + "sound/buttons/obs_interface_hover.ogg"
    obs_hover_item_sound = Obs.PathMain() + "sound/buttons/obs_item_hover.ogg"
    obs_activate_sound = Obs.PathMain() + "sound/buttons/obs_activate.ogg"
    obs_activate_interface_sound = Obs.PathMain() + "sound/buttons/obs_interface_activate.ogg"
    obs_activate_menu_sound = Obs.PathMain() + "sound/buttons/obs_menu_activate.ogg"
    obs_lock_sound = Obs.PathMain() + "sound/buttons/obs_lock.ogg"

    obs_normal_font = Obs.PathImg() + "gui/font/normal.ttf"
    obs_gloomy_font = Obs.PathImg() + "gui/font/gloomy.ttf"
    obs_big_font = Obs.PathImg() + "gui/font/big.ttf"

    obs_outlines = [(1, "#000000", 0, 0)]
    obs_down_left_align = (0.985, 0.985)
    obs_normal_xsize = 600
    obs_right_xanchor = 1.0
    obs_center_xanchor = 0.5
    obs_center_text_align = 0.5
    obs_load_maximum = (650, 54) 
    obs_normal_size = 50
    obs_medium_size = 42
    obs_small_size = 30
    obs_little_size = 23
    obs_thumb_offset = 0
    obs_kerning = 3

    persistent.obs_game_last_time = datetime.datetime.now()
    persistent.obs_session_last_time = datetime.datetime.now()
    persistent.obs_session_time = 0

default obs_screens_check = False
default persistent.obs_autosaves = True
default persistent.obs_effects = True
default persistent.obs_swear_filter = False
default persistent.obs_cards_win = {"aln":False}
default persistent.obs_cards_fail = {"msk":False, "un":False, "aln":False}
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
