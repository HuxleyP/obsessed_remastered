init -500 python:
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

    class Obs_Continue(Action):
        """
        Function for Action
        """
        def __call__(self):
            Function(renpy.load, renpy.newest_slot("obs_FilePage_"))()
        def get_sensitive(self):
            if renpy.newest_slot("obs_FilePage_"):
                return True
            else:
                return False

    class Obs_Call(Action):
        """
        Function for Action
        """
        def __init__(self, label):
            self.label = label
        def __call__(self):
            if "." in self.label:
                SetVariable("obs_label", self.label.split(".")[0])()
                SetField(self, "label", self.label.split(".")[1])()
            SetVariable("obs_return", obs_label + ".loop")()
            Jump(obs_label + "." + self.label)()

    class Obs_JumpFunction(Action, DictEquality):
        """
        Function for Action
        """
        def __init__(self, _func):
            self.func = [store, _func]
        def __call__(self):
            SetVariable("func", self.func)()
            Function(renpy.load_string("$ getattr(store, self.func)()"))()

    class Obs_JumpClass(Action, DictEquality):
        """
        Function for Action
        """
        def __init__(self, object, func):
            self.object = object
            self.func = func
        def __call__(self):
            SetVariable("func", self.func)()
            Function(renpy.load_string("$ getattr(self.object, self.func)()"))()

    class Obs_StartMainMenu(Action):
        """
        Function for Action
        """
        def __call__(self):
            Show("obs_yesno_prompt", message=layout.MAIN_MENU,
                  yes_action=[SetVariable("obs_before_main_menu", True),
                              Function(Obs.Settings.ReloadNames, False),
                              Start(obs_config_label)],
                  no_action=Hide("obs_yesno_prompt"))()

    class Obs_SelectedSlot(Action, DictEquality):
        """
        Function for Action
        """
        def __init__(self, name):
            self.name = name
        def __call__(self):
            SetVariable("obs_hover_slot", Obs.SelectedSlot(self.name))()
        def get_sensitive(self):
            if obs_hover_slot != Obs.SelectedSlot(self.name):
                return True
            else:
                return False

    class Obs_QuitItemsMenu(Action):
        """
        Function for Action
        """
        def __call__(self):
            SetVariable("obs_show_items_window", False)()
            SetVariable("obs_hover_slot", {"slot":None, "name":"empty", "stats":None})()

    class Obs_QuitOutOfMod(Action):
        """
        Function for Action
        """
        def __call__(self):
            Function(Obs.Settings.ScreensReactivate)()
            if obs_game_menu:
                Start("obs_default_start")()
            else:
                Jump("obs_default_start")()

    class Obs_ShowItem(Action, DictEquality):
        """
        Function for Action
        """
        def __init__(self, number, items, stats, slot):
            self.number = number
            self.items = items
            self.stats = stats
            self.slot = slot
        def __call__(self):
            Play("sound", store.Obs.PathMain() + "sound/buttons/obs_" + self.items[self.slot]["name"] + ".ogg")()
            Function(store.Obs.Show.Item, self.items[self.slot]["name"], self.stats)()
            Function(store.Obs.Set.ItemEmpty, self.number, self.slot)()

    class Obs_ApplyItem(Action, DictEquality):
        """
        Function for Action
        """
        def __init__(self, item, type):
            self.item = item
            self.type = type
        def __call__(self):
            if obs_hover_slot["name"] == self.item or obs_hover_slot["name"] in obs_ordinary_items_list:
                Hide("obs_inventory_message")()
                if self.item not in obs_reusable_items_list:
                    Function(Obs.Show.Item, obs_hover_slot["name"], obs_hover_slot["stats"], "remove", "Использовано:")()
            else:
                Hide("obs_inventory_message")()
                Show("obs_inventory_message")()
                if obs_hover_slot["name"] in obs_weapons_list and obs_weapon == "lock":
                    SetVariable("obs_inventory_message", "Оружие в настоящее время нет необходимости использовать.")()
                else:
                    SetVariable("obs_inventory_message", "Этот предмет нельзя здесь применить.")()
                Play("sound", Obs.PathMain() + "sound/buttons/obs_lock.ogg")()

    class Obs_ThrowItem(Action):
        """
        Function for Action
        """
        def __call__(self):
            if obs_hover_slot["name"] in obs_ordinary_items_list:
                Hide("obs_inventory_message")()
                Function(Obs.Show.Item, obs_hover_slot["name"], obs_hover_slot["stats"], "remove", "Выброшено:")()
            else:
                Hide("obs_inventory_message")()
                Show("obs_inventory_message")()
                SetVariable("obs_inventory_message", "Сюжетные предметы нельзя выбросить.")()
                Play("sound", Obs.PathMain() + "sound/buttons/obs_lock.ogg")()

    class Obs_TakeoffItem(Action):
        """
        Function for Action
        """
        def __call__(self):
            Function(Obs.Show.Item, obs_weapon["name"], obs_weapon["stats"], "add", None)()
            SetVariable("obs_weapon", "empty")

    class Obs_Message(Action):
        """
        Function for Action
        """
        def __init__(self, text):
            self.text = text
        def __call__(self):
            Hide("obs_inventory_message")()
            Show("obs_inventory_message")()
            SetVariable("obs_inventory_message", self.text)()
            Play("sound", Obs.PathMain() + "sound/buttons/obs_lock.ogg")()

    class Obs_FunctionCallback(Action):
        """
        Function for Action
        """
        def __init__(self, function, *arguments):
            self.function = function
            self.arguments = arguments
        def __call__(self):
            return self.function(self.arguments)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
