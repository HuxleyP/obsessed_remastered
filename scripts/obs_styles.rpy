init -350 python:
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

init python:
    style.obs_imagemap                                            = Style(style.default)
    style.obs_imagemap.hover_sound                                = obs_hover_item_sound

    style.obs_version_text                                        = Style(style.default)
    style.obs_version_text.color                                  = obs_red_color
    style.obs_version_text.align                                  = obs_down_left_align
    style.obs_version_text.xanchor                                = obs_right_xanchor
    style.obs_version_text.font                                   = obs_normal_font
    style.obs_version_text.outlines                               = obs_outlines

    style.obs_quest_name_day                                      = Style(style.default)
    style.obs_quest_name_day.font                                 = obs_normal_font
    style.obs_quest_name_day.color                                = obs_red_color
    style.obs_quest_name_day.size                                 = obs_normal_size
    style.obs_quest_name_day.outlines                             = obs_outlines

    style.obs_quest_name_sunset                                   = Style(style.default)
    style.obs_quest_name_sunset.font                              = obs_normal_font
    style.obs_quest_name_sunset.color                             = obs_orange_light_color
    style.obs_quest_name_sunset.size                              = obs_normal_size
    style.obs_quest_name_sunset.outlines                          = obs_outlines

    style.obs_quest_name_prologue                                 = Style(style.default)
    style.obs_quest_name_prologue.font                            = obs_normal_font
    style.obs_quest_name_prologue.color                           = obs_gray_light_color
    style.obs_quest_name_prologue.size                            = obs_normal_size
    style.obs_quest_name_prologue.outlines                        = obs_outlines

    style.obs_quest_objectives_day                                = Style(style.default)
    style.obs_quest_objectives_day.font                           = obs_normal_font
    style.obs_quest_objectives_day.color                          = obs_red_dark_color
    style.obs_quest_objectives_day.size                           = obs_small_size
    style.obs_quest_objectives_day.outlines                       = obs_outlines

    style.obs_quest_objectives_sunset                             = Style(style.default)
    style.obs_quest_objectives_sunset.font                        = obs_normal_font
    style.obs_quest_objectives_sunset.color                       = obs_orange_color
    style.obs_quest_objectives_sunset.size                        = obs_small_size
    style.obs_quest_objectives_sunset.outlines                    = obs_outlines

    style.obs_quest_objectives_prologue                           = Style(style.default)
    style.obs_quest_objectives_prologue.font                      = obs_normal_font
    style.obs_quest_objectives_prologue.color                     = obs_gray_color
    style.obs_quest_objectives_prologue.size                      = obs_small_size
    style.obs_quest_objectives_prologue.outlines                  = obs_outlines

    style.obs_settings_text                                       = Style(style.default)
    style.obs_settings_text.font                                  = obs_normal_font
    style.obs_settings_text.size                                  = obs_small_size
    style.obs_settings_text.kerning                               = obs_kerning
    style.obs_settings_text.color                                 = obs_red_light_color
    style.obs_settings_text.hover_color                           = obs_blue_color
    style.obs_settings_text.outlines                              = obs_outlines

    style.obs_text_quit_day                                       = Style(style.default)
    style.obs_text_quit_day.font                                  = obs_normal_font
    style.obs_text_quit_day.size                                  = obs_normal_size
    style.obs_text_quit_day.color                                 = obs_red_color
    style.obs_text_quit_day.hover_color                           = obs_blue_color
    style.obs_text_quit_day.selected_color                        = obs_red_color
    style.obs_text_quit_day.selected_idle_color                   = obs_red_color
    style.obs_text_quit_day.selected_hover_color                  = obs_blue_color
    style.obs_text_quit_day.insensitive_color                     = obs_red_color

    style.obs_text_quit_sunset                                    = Style(style.default)
    style.obs_text_quit_sunset.font                               = obs_normal_font
    style.obs_text_quit_sunset.size                               = obs_normal_size
    style.obs_text_quit_sunset.color                              = obs_orange_color
    style.obs_text_quit_sunset.hover_color                        = obs_orange_light_color
    style.obs_text_quit_sunset.selected_color                     = obs_orange_color
    style.obs_text_quit_sunset.selected_idle_color                = obs_orange_color
    style.obs_text_quit_sunset.selected_hover_color               = obs_orange_light_color
    style.obs_text_quit_sunset.insensitive_color                  = obs_orange_color

    style.obs_text_quit_prologue                                  = Style(style.default)
    style.obs_text_quit_prologue.font                             = obs_normal_font
    style.obs_text_quit_prologue.size                             = obs_normal_size
    style.obs_text_quit_prologue.color                            = obs_gray_color
    style.obs_text_quit_prologue.hover_color                      = obs_gray_light_color
    style.obs_text_quit_prologue.selected_color                   = obs_gray_color
    style.obs_text_quit_prologue.selected_idle_color              = obs_gray_color
    style.obs_text_quit_prologue.selected_hover_color             = obs_gray_light_color
    style.obs_text_quit_prologue.insensitive_color                = obs_gray_color

    style.obs_button_quit                                         = Style(style.button)
    style.obs_button_quit.background                              = None
    style.obs_button_quit.hover_background                        = None
    style.obs_button_quit.selected_background                     = None
    style.obs_button_quit.selected_hover_background               = None
    style.obs_button_quit.selected_idle_background                = None

    style.obs_history_button_text_day                             = Style(style.default)
    style.obs_history_button_text_day.selected_color              = obs_red_color
    style.obs_history_button_text_day.hover_color                 = obs_blue_color

    style.obs_history_button_text_sunset                          = Style(style.default)
    style.obs_history_button_text_sunset.selected_color           = obs_orange_color
    style.obs_history_button_text_sunset.hover_color              = obs_orange_light_color

    style.obs_history_button_text_prologue                        = Style(style.default)
    style.obs_history_button_text_prologue.selected_color         = obs_gray_color
    style.obs_history_button_text_prologue.hover_color            = obs_gray_light_color

    style.obs_button_none                                         = Style(style.button)
    style.obs_button_none.background                              = None
    style.obs_button_none.hover_background                        = None
    style.obs_button_none.selected_background                     = None
    style.obs_button_none.selected_hover_background               = None
    style.obs_button_none.selected_idle_background                = None

    style.obs_text_setting_day                                    = Style(style.default)
    style.obs_text_setting_day.font                               = obs_normal_font
    style.obs_text_setting_day.size                               = obs_normal_size
    style.obs_text_setting_day.color                              = obs_red_color
    style.obs_text_setting_day.hover_color                        = obs_blue_color
    style.obs_text_setting_day.selected_color                     = obs_red_color
    style.obs_text_setting_day.outlines                           = obs_outlines

    style.obs_text_setting_sunset                                 = Style(style.default)
    style.obs_text_setting_sunset.font                            = obs_normal_font
    style.obs_text_setting_sunset.size                            = obs_normal_size
    style.obs_text_setting_sunset.color                           = obs_orange_color
    style.obs_text_setting_sunset.hover_color                     = obs_orange_light_color
    style.obs_text_setting_sunset.selected_color                  = obs_orange_color
    style.obs_text_setting_sunset.outlines                        = obs_outlines

    style.obs_text_setting_prologue                               = Style(style.default)
    style.obs_text_setting_prologue.font                          = obs_normal_font
    style.obs_text_setting_prologue.size                          = obs_normal_size
    style.obs_text_setting_prologue.color                         = obs_gray_color
    style.obs_text_setting_prologue.hover_color                   = obs_gray_light_color
    style.obs_text_setting_prologue.selected_color                = obs_gray_color
    style.obs_text_setting_prologue.outlines                      = obs_outlines

    style.obs_text_small_setting_day                              = Style(style.default)
    style.obs_text_small_setting_day.font                         = obs_normal_font
    style.obs_text_small_setting_day.size                         = obs_normal_size
    style.obs_text_small_setting_day.color                        = obs_gray_color
    style.obs_text_small_setting_day.hover_color                  = obs_blue_color
    style.obs_text_small_setting_day.selected_color               = obs_red_color
    style.obs_text_small_setting_day.outlines                     = obs_outlines

    style.obs_text_small_setting_sunset                           = Style(style.default)
    style.obs_text_small_setting_sunset.font                      = obs_normal_font
    style.obs_text_small_setting_sunset.size                      = obs_normal_size
    style.obs_text_small_setting_sunset.color                     = obs_gray_color
    style.obs_text_small_setting_sunset.hover_color               = obs_orange_light_color
    style.obs_text_small_setting_sunset.selected_color            = obs_orange_color
    style.obs_text_small_setting_sunset.outlines                  = obs_outlines

    style.obs_text_small_setting_prologue                         = Style(style.default)
    style.obs_text_small_setting_prologue.font                    = obs_normal_font
    style.obs_text_small_setting_prologue.size                    = obs_normal_size
    style.obs_text_small_setting_prologue.color                   = obs_gray_dark_color
    style.obs_text_small_setting_prologue.hover_color             = obs_gray_light_color
    style.obs_text_small_setting_prologue.selected_color          = obs_gray_color
    style.obs_text_small_setting_prologue.outlines                = obs_outlines

    style.obs_text_big_setting_day                                = Style(style.default)
    style.obs_text_big_setting_day.font                           = obs_normal_font
    style.obs_text_big_setting_day.size                           = obs_normal_size
    style.obs_text_big_setting_day.color                          = obs_red_color
    style.obs_text_big_setting_day.hover_color                    = obs_blue_color
    style.obs_text_big_setting_day.selected_color                 = obs_red_color
    style.obs_text_big_setting_day.insensitive_color              = obs_red_color
    style.obs_text_big_setting_day.outlines                       = obs_outlines

    style.obs_text_big_setting_sunset                             = Style(style.default)
    style.obs_text_big_setting_sunset.font                        = obs_normal_font
    style.obs_text_big_setting_sunset.size                        = obs_normal_size
    style.obs_text_big_setting_sunset.color                       = obs_orange_color
    style.obs_text_big_setting_sunset.hover_color                 = obs_orange_light_color
    style.obs_text_big_setting_sunset.selected_color              = obs_orange_color
    style.obs_text_big_setting_sunset.insensitive_color           = obs_orange_color
    style.obs_text_big_setting_sunset.outlines                    = obs_outlines

    style.obs_text_big_setting_prologue                           = Style(style.default)
    style.obs_text_big_setting_prologue.font                      = obs_normal_font
    style.obs_text_big_setting_prologue.size                      = obs_normal_size
    style.obs_text_big_setting_prologue.color                     = obs_gray_color
    style.obs_text_big_setting_prologue.hover_color               = obs_gray_light_color
    style.obs_text_big_setting_prologue.selected_color            = obs_gray_color
    style.obs_text_big_setting_prologue.insensitive_color         = obs_gray_color
    style.obs_text_big_setting_prologue.outlines                  = obs_outlines

    style.obs_text_small_invers_setting_day                       = Style(style.default)
    style.obs_text_small_invers_setting_day.font                  = obs_normal_font
    style.obs_text_small_invers_setting_day.size                  = obs_normal_size
    style.obs_text_small_invers_setting_day.color                 = obs_red_color
    style.obs_text_small_invers_setting_day.hover_color           = obs_blue_color
    style.obs_text_small_invers_setting_day.selected_color        = obs_red_color
    style.obs_text_small_invers_setting_day.outlines              = obs_outlines

    style.obs_text_small_invers_setting_sunset                    = Style(style.default)
    style.obs_text_small_invers_setting_sunset.font               = obs_normal_font
    style.obs_text_small_invers_setting_sunset.size               = obs_normal_size
    style.obs_text_small_invers_setting_sunset.color              = obs_orange_color
    style.obs_text_small_invers_setting_sunset.hover_color        = obs_orange_light_color
    style.obs_text_small_invers_setting_sunset.selected_color     = obs_orange_color
    style.obs_text_small_invers_setting_sunset.outlines           = obs_outlines

    style.obs_text_small_invers_setting_prologue                  = Style(style.default)
    style.obs_text_small_invers_setting_prologue.font             = obs_normal_font
    style.obs_text_small_invers_setting_prologue.size             = obs_normal_size
    style.obs_text_small_invers_setting_prologue.color            = obs_gray_color
    style.obs_text_small_invers_setting_prologue.hover_color      = obs_gray_light_color
    style.obs_text_small_invers_setting_prologue.selected_color   = obs_gray_color
    style.obs_text_small_invers_setting_prologue.outlines         = obs_outlines

    style.obs_text_item_label_day                                 = Style(style.default)
    style.obs_text_item_label_day.font                            = obs_normal_font
    style.obs_text_item_label_day.size                            = obs_medium_size
    style.obs_text_item_label_day.xanchor                         = obs_center_xanchor
    style.obs_text_item_label_day.insensitive_color               = obs_red_dark_color
    style.obs_text_item_label_day.outlines                        = obs_outlines

    style.obs_text_item_label_sunset                              = Style(style.default)
    style.obs_text_item_label_sunset.font                         = obs_normal_font
    style.obs_text_item_label_sunset.size                         = obs_medium_size
    style.obs_text_item_label_sunset.xanchor                      = obs_center_xanchor
    style.obs_text_item_label_sunset.insensitive_color            = obs_orange_dark_color
    style.obs_text_item_label_sunset.outlines                     = obs_outlines

    style.obs_text_item_label_prologue                            = Style(style.default)
    style.obs_text_item_label_prologue.font                       = obs_normal_font
    style.obs_text_item_label_prologue.size                       = obs_medium_size
    style.obs_text_item_label_prologue.xanchor                    = obs_center_xanchor
    style.obs_text_item_label_prologue.insensitive_color          = obs_gray_dark_color2
    style.obs_text_item_label_prologue.outlines                   = obs_outlines

    style.obs_text_item_description_day                           = Style(style.default)
    style.obs_text_item_description_day.font                      = obs_normal_font
    style.obs_text_item_description_day.size                      = obs_little_size
    style.obs_text_item_description_day.xsize                     = obs_normal_xsize
    style.obs_text_item_description_day.text_align                = obs_center_text_align
    style.obs_text_item_description_day.insensitive_color         = obs_red_color
    style.obs_text_item_description_day.outlines                  = obs_outlines

    style.obs_text_item_description_sunset                        = Style(style.default)
    style.obs_text_item_description_sunset.font                   = obs_normal_font
    style.obs_text_item_description_sunset.size                   = obs_little_size
    style.obs_text_item_description_sunset.xsize                  = obs_normal_xsize
    style.obs_text_item_description_sunset.text_align             = obs_center_text_align
    style.obs_text_item_description_sunset.insensitive_color      = obs_orange_color
    style.obs_text_item_description_sunset.outlines               = obs_outlines

    style.obs_text_item_description_prologue                      = Style(style.default)
    style.obs_text_item_description_prologue.font                 = obs_normal_font
    style.obs_text_item_description_prologue.size                 = obs_little_size
    style.obs_text_item_description_prologue.xsize                = obs_normal_xsize
    style.obs_text_item_description_prologue.text_align           = obs_center_text_align
    style.obs_text_item_description_prologue.insensitive_color    = obs_gray_color
    style.obs_text_item_description_prologue.outlines             = obs_outlines

    style.obs_text_label_day                                      = Style(style.default)
    style.obs_text_label_day.font                                 = obs_normal_font
    style.obs_text_label_day.size                                 = obs_normal_size
    style.obs_text_label_day.insensitive_color                    = obs_red_color
    style.obs_text_label_day.outlines                             = obs_outlines

    style.obs_text_label_sunset                                   = Style(style.default)
    style.obs_text_label_sunset.font                              = obs_normal_font
    style.obs_text_label_sunset.size                              = obs_normal_size
    style.obs_text_label_sunset.insensitive_color                 = obs_orange_color
    style.obs_text_label_sunset.outlines                          = obs_outlines

    style.obs_text_label_prologue                                 = Style(style.default)
    style.obs_text_label_prologue.font                            = obs_normal_font
    style.obs_text_label_prologue.size                            = obs_normal_size
    style.obs_text_label_prologue.insensitive_color               = obs_gray_color
    style.obs_text_label_prologue.outlines                        = obs_outlines

    style.obs_text_extra_day                                      = Style(style.default)
    style.obs_text_extra_day.font                                 = obs_normal_font
    style.obs_text_extra_day.size                                 = obs_normal_size
    style.obs_text_extra_day.insensitive_color                    = obs_red_light_color
    style.obs_text_extra_day.outlines                             = obs_outlines

    style.obs_text_extra_sunset                                   = Style(style.default)
    style.obs_text_extra_sunset.font                              = obs_normal_font
    style.obs_text_extra_sunset.size                              = obs_normal_size
    style.obs_text_extra_sunset.insensitive_color                 = obs_orange_color
    style.obs_text_extra_sunset.outlines                          = obs_outlines

    style.obs_text_extra_prologue                                 = Style(style.default)
    style.obs_text_extra_prologue.font                            = obs_normal_font
    style.obs_text_extra_prologue.size                            = obs_normal_size
    style.obs_text_extra_prologue.insensitive_color               = obs_gray_color
    style.obs_text_extra_prologue.outlines                        = obs_outlines

    style.obs_text_big_save_load_day                              = Style(style.default)
    style.obs_text_big_save_load_day.font                         = obs_normal_font
    style.obs_text_big_save_load_day.size                         = obs_normal_size
    style.obs_text_big_save_load_day.color                        = obs_red_color
    style.obs_text_big_save_load_day.hover_color                  = obs_blue_color
    style.obs_text_big_save_load_day.selected_color               = obs_red_dark_color
    style.obs_text_big_save_load_day.selected_idle_color          = obs_red_dark_color
    style.obs_text_big_save_load_day.selected_hover_color         = obs_red_dark_color
    style.obs_text_big_save_load_day.insensitive_color            = obs_red_dark_color
    style.obs_text_big_save_load_day.outlines                     = obs_outlines

    style.obs_text_big_save_load_sunset                           = Style(style.default)
    style.obs_text_big_save_load_sunset.font                      = obs_normal_font
    style.obs_text_big_save_load_sunset.size                      = obs_normal_size
    style.obs_text_big_save_load_sunset.color                     = obs_orange_color
    style.obs_text_big_save_load_sunset.hover_color               = obs_orange_light_color
    style.obs_text_big_save_load_sunset.selected_color            = obs_orange_dark_color
    style.obs_text_big_save_load_sunset.selected_idle_color       = obs_orange_dark_color
    style.obs_text_big_save_load_sunset.selected_hover_color      = obs_orange_dark_color
    style.obs_text_big_save_load_sunset.insensitive_color         = obs_orange_dark_color
    style.obs_text_big_save_load_sunset.outlines                  = obs_outlines

    style.obs_text_big_save_load_prologue                         = Style(style.default)
    style.obs_text_big_save_load_prologue.font                    = obs_normal_font
    style.obs_text_big_save_load_prologue.size                    = obs_normal_size
    style.obs_text_big_save_load_prologue.color                   = obs_gray_color
    style.obs_text_big_save_load_prologue.hover_color             = obs_gray_light_color
    style.obs_text_big_save_load_prologue.selected_color          = obs_gray_dark_color
    style.obs_text_big_save_load_prologue.selected_idle_color     = obs_gray_dark_color
    style.obs_text_big_save_load_prologue.selected_hover_color    = obs_gray_dark_color
    style.obs_text_big_save_load_prologue.insensitive_color       = obs_gray_dark_color
    style.obs_text_big_save_load_prologue.outlines                = obs_outlines

    style.obs_text_big_inventory_day                              = Style(style.default)
    style.obs_text_big_inventory_day.font                         = obs_normal_font
    style.obs_text_big_inventory_day.size                         = obs_normal_size
    style.obs_text_big_inventory_day.color                        = obs_red_color
    style.obs_text_big_inventory_day.hover_color                  = obs_blue_color
    style.obs_text_big_inventory_day.selected_color               = obs_red_color
    style.obs_text_big_inventory_day.selected_idle_color          = obs_red_color
    style.obs_text_big_inventory_day.selected_hover_color         = obs_blue_color
    style.obs_text_big_inventory_day.insensitive_color            = obs_red_color
    style.obs_text_big_inventory_day.outlines                     = obs_outlines

    style.obs_text_big_inventory_sunset                           = Style(style.default)
    style.obs_text_big_inventory_sunset.font                      = obs_normal_font
    style.obs_text_big_inventory_sunset.size                      = obs_normal_size
    style.obs_text_big_inventory_sunset.color                     = obs_orange_color
    style.obs_text_big_inventory_sunset.hover_color               = obs_orange_light_color
    style.obs_text_big_inventory_sunset.selected_color            = obs_orange_color
    style.obs_text_big_inventory_sunset.selected_idle_color       = obs_orange_color
    style.obs_text_big_inventory_sunset.selected_hover_color      = obs_orange_light_color
    style.obs_text_big_inventory_sunset.insensitive_color         = obs_orange_color
    style.obs_text_big_inventory_sunset.outlines                  = obs_outlines

    style.obs_text_big_inventory_prologue                         = Style(style.default)
    style.obs_text_big_inventory_prologue.font                    = obs_normal_font
    style.obs_text_big_inventory_prologue.size                    = obs_normal_size
    style.obs_text_big_inventory_prologue.color                   = obs_gray_color
    style.obs_text_big_inventory_prologue.hover_color             = obs_gray_light_color
    style.obs_text_big_inventory_prologue.selected_color          = obs_gray_color
    style.obs_text_big_inventory_prologue.selected_idle_color     = obs_gray_color
    style.obs_text_big_inventory_prologue.selected_hover_color    = obs_gray_light_color
    style.obs_text_big_inventory_prologue.insensitive_color       = obs_gray_color
    style.obs_text_big_inventory_prologue.outlines                = obs_outlines

    style.obs_text_small_save_load_day                            = Style(style.default)
    style.obs_text_small_save_load_day.font                       = obs_normal_font
    style.obs_text_small_save_load_day.size                       = obs_normal_size
    style.obs_text_small_save_load_day.color                      = obs_red_color
    style.obs_text_small_save_load_day.hover_color                = obs_blue_color
    style.obs_text_small_save_load_day.selected_color             = obs_red_color
    style.obs_text_small_save_load_day.selected_idle_color        = obs_red_color
    style.obs_text_small_save_load_day.selected_hover_color       = obs_blue_color
    style.obs_text_small_save_load_day.insensitive_color          = obs_red_color
    style.obs_text_small_save_load_day.outlines                   = obs_outlines

    style.obs_text_small_save_load_sunset                         = Style(style.default)
    style.obs_text_small_save_load_sunset.font                    = obs_normal_font
    style.obs_text_small_save_load_sunset.size                    = obs_normal_size
    style.obs_text_small_save_load_sunset.color                   = obs_orange_color
    style.obs_text_small_save_load_sunset.hover_color             = obs_orange_light_color
    style.obs_text_small_save_load_sunset.selected_color          = obs_orange_color
    style.obs_text_small_save_load_sunset.selected_idle_color     = obs_orange_color
    style.obs_text_small_save_load_sunset.selected_hover_color    = obs_orange_light_color
    style.obs_text_small_save_load_sunset.insensitive_color       = obs_orange_color
    style.obs_text_small_save_load_sunset.outlines                = obs_outlines

    style.obs_text_small_save_load_prologue                       = Style(style.default)
    style.obs_text_small_save_load_prologue.font                  = obs_normal_font
    style.obs_text_small_save_load_prologue.size                  = obs_normal_size
    style.obs_text_small_save_load_prologue.color                 = obs_gray_color
    style.obs_text_small_save_load_prologue.hover_color           = obs_gray_light_color
    style.obs_text_small_save_load_prologue.selected_color        = obs_gray_color
    style.obs_text_small_save_load_prologue.selected_idle_color   = obs_gray_color
    style.obs_text_small_save_load_prologue.selected_hover_color  = obs_gray_light_color
    style.obs_text_small_save_load_prologue.insensitive_color     = obs_gray_color
    style.obs_text_small_save_load_prologue.outlines              = obs_outlines

    style.obs_save_load_button_day                                = Style(style.button)
    style.obs_save_load_button_day.font                           = obs_normal_font
    style.obs_save_load_button_day.color                          = obs_red_color
    style.obs_save_load_button_day.background                     = Obs.PathImg() + "gui/save/day/save_load_button_idle.png"
    style.obs_save_load_button_day.hover_background               = Obs.PathImg() + "gui/save/day/save_load_button_hover.png"
    style.obs_save_load_button_day.selected_background            = Obs.PathImg() + "gui/save/day/save_load_button_selected.png"
    style.obs_save_load_button_day.selected_hover_background      = Obs.PathImg() + "gui/save/day/save_load_button_selected.png"
    style.obs_save_load_button_day.selected_idle_background       = Obs.PathImg() + "gui/save/day/save_load_button_selected.png"
    style.obs_save_load_button_day.outlines                       = obs_outlines

    style.obs_save_load_button_sunset                             = Style(style.button)
    style.obs_save_load_button_sunset.font                        = obs_normal_font
    style.obs_save_load_button_sunset.color                       = obs_orange_color
    style.obs_save_load_button_sunset.background                  = Obs.PathImg() + "gui/save/sunset/save_load_button_idle.png"
    style.obs_save_load_button_sunset.hover_background            = Obs.PathImg() + "gui/save/sunset/save_load_button_hover.png"
    style.obs_save_load_button_sunset.selected_background         = Obs.PathImg() + "gui/save/sunset/save_load_button_selected.png"
    style.obs_save_load_button_sunset.selected_hover_background   = Obs.PathImg() + "gui/save/sunset/save_load_button_selected.png"
    style.obs_save_load_button_sunset.selected_idle_background    = Obs.PathImg() + "gui/save/sunset/save_load_button_selected.png"
    style.obs_save_load_button_sunset.outlines                    = obs_outlines

    style.obs_save_load_button_prologue                           = Style(style.button)
    style.obs_save_load_button_prologue.font                      = obs_normal_font
    style.obs_save_load_button_prologue.color                     = obs_gray_color
    style.obs_save_load_button_prologue.background                = Obs.PathImg() + "gui/save/prologue/save_load_button_idle.png"
    style.obs_save_load_button_prologue.hover_background          = Obs.PathImg() + "gui/save/prologue/save_load_button_hover.png"
    style.obs_save_load_button_prologue.selected_background       = Obs.PathImg() + "gui/save/prologue/save_load_button_selected.png"
    style.obs_save_load_button_prologue.selected_hover_background = Obs.PathImg() + "gui/save/prologue/save_load_button_selected.png"
    style.obs_save_load_button_prologue.selected_idle_background  = Obs.PathImg() + "gui/save/prologue/save_load_button_selected.png"
    style.obs_save_load_button_prologue.outlines                  = obs_outlines

    style.obs_loading_bar                                         = Style(style.default)
    style.obs_loading_bar.left_bar                                = Frame(Obs.PathImg() + "gui/loading/bar_full.png")
    style.obs_loading_bar.right_bar                               = Frame(Obs.PathImg() + "gui/loading/bar_null.png")
    style.obs_loading_bar.thumb                                   = None
    style.obs_loading_bar.thumb_offset                            = obs_thumb_offset 
    style.obs_loading_bar.maximum                                 = obs_load_maximum
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
