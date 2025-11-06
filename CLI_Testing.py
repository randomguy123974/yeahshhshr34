import cmd
import avMain


class AVMacro(cmd.Cmd):
    
    intro = "Welcome to Loxer's Automation (Ver: 0.01, Anime Vanguards) .\n"
    prompt = "(AV)"
    def __init__(self):
        super().__init__()
        self.Menu = 0
        self.Task = ""
    def change_menu(self,arg):
        try:
            self.Menu = arg
        except Exception as e:
            print(f"{e}")

    

    def do_menu(self,arg):
        cmd_menu = {
        "Main Menu":  {
            "Position Roblox" : avMain.start_bot,
            "Select Tasks": self.change_menu,
            "Settings": self.change_menu,
            },
        "Settings": {
            "Config": True
        },
        "Tasks": {
            "Dungeon": self.change_menu,
            "Raid" : self.change_menu,
            "Story": self.change_menu,
            "Legend Stage": self.change_menu,
            "Challenge": self.change_menu,
            "Odyssey": self.change_menu,
            "Rift": self.change_menu
            },

        }
         # 1 - Tasks menu, 2 - Settings Menu, 3 - Dungeon Menu, 4 - Raid Menu, 5 - Story Menu, 6 - Legendstage Menu,7 - Challenge Menu, 8 - Oddyssey Menu, 9 - Rift Menu
   
        num_to_string_keys = {
            0: "Main Menu",
            1: "Tasks",
            2: "Settings",
            3: "Dungeon",
            4: "Raid",
            5: "Story",
            6: "Legend Stage",
            7: "Challenge",
            8: "Oddyssey",
            9: "Rift"
        }
        pos = int(arg.strip().lower())
        print(cmd_menu.get(num_to_string_keys.get(pos)))
        
    def do_exit(self, arg):
        "exit program" 
        print("off")
        return True
    def default(self, line):
        print(f"Uknown command: {line}")

if __name__ == "__main__":
    AVMacro().cmdloop()
