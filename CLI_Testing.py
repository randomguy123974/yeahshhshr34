import cmd
import avMain
import os
import sys
import subprocess
import math
class AVMacro(cmd.Cmd):
    
    intro = "Welcome to Loxer's Automation (Ver: 0.01, Anime Vanguards), use n to navigate. .\n"
    prompt = ">"
    def __init__(self):
        super().__init__()
        self.Menu = 0
        self.Task = ""
        self.cmd_menu = {
            "Main_Menu":  {
                "pos_rblx" : [avMain.start_bot, None, None],
                "s_tasks": [self.change_menu, 1, None],
                "stg": [self.change_menu, 2, None],
                "help": [self.change_menu, 11, True]
                },
            "Settings": {
                "Config": [self.change_menu, 10]
            },
            "Tasks": {
                "Dungeon": self.change_menu,
                "Raid" : self.change_menu,
                "Story": self.change_menu,
                "L_stage": self.change_menu,
                "Challenge": self.change_menu,
                "Odyssey": self.change_menu,
                "Rift": self.change_menu
                },
            "help": {
                "Navigate": "Use n (arg) to navigate, n b to go backwards",
                "Change Value": "Use c (arg) to change value",
                "Restart": "restart to restart the program",
                
            }
        }
        self.num_to_string_keys = {
                0: "Main_Menu",
                1: "Tasks",
                2: "Settings",
                3: "Dungeon",
                4: "Raid",
                5: "Story",
                6: "L_stage",
                7: "Challenge",
                8: "Oddyssey",
                9: "Rift",
                10: "Config",
                11: "help"
            }
    def change_menu(self,arg):
        try:
            self.Menu = arg
        except Exception as e:
            print(f"{e}")
    
    def print_menu(self, args, print_val: bool | None = None):
        try:

            pos = args
            menu_name = self.num_to_string_keys.get(pos)
            print(menu_name)
            print("================================")
            print("|", end="")
            for i in range(0,(30-len(menu_name))//2,1):
                print("_", end="")
            print(menu_name, end="")
            for i in range(0,(30-len(menu_name))//2,1):
                print("_", end="")

            if ((30-len(menu_name))/2)>math.floor((30-len(menu_name))/2):
                print("_", end="")
            print("|")
            # len = 32, -2 -len(i) 
            for i in self.cmd_menu.get(menu_name):
                print(f"| {i}: {self.cmd_menu.get(menu_name).get(i) if print_val else ""}",end = " ")
                for j in range(26-len(self.cmd_menu.get(menu_name).get(i)) if print_val else 26-len(i)):
                    print(" ", end = "")
                if len(i)+len(self.cmd_menu.get(menu_name).get(i)) < 26:
                    print("|")
                else:
                    print("")
            print("================================")

        except Exception as e:
            print(f"Error loading menu: {e}")
        
    def do_task(self, arg):
        task = arg.strip().lower()
        print(task)
    
    def do_n(self,arg):
        '''Navigate'''
        a = arg.strip()
        try:
            if a == "b":
                if self.Menu == 1 or self.Menu == 2 or self.Menu == 11:
                    self.Menu = 0
                else:
                    self.Menu-=1
                self.do_menu("")
            else:
                instruct = self.cmd_menu.get(self.num_to_string_keys.get(self.Menu)).get(a)
                if instruct[1] is not None:
                    instruct[0](instruct[1])
                else:
                    instruct[0]()
                self.do_menu(instruct[2])
                return 0
        except Exception as e:
            print(f"error: {e}")
    

    def do_menu(self, arg):
         # 1 - Tasks menu, 2 - Settings Menu, 3 - Dungeon Menu, 4 - Raid Menu, 5 - Story Menu, 6 - Legendstage Menu,7 - Challenge Menu, 8 - Oddyssey Menu, 9 - Rift Menu
        try:
            os.system('cls')
            if arg is True:
                self.print_menu(self.Menu, print_val=True)
            else:
                self.print_menu(self.Menu, print_val=False)
        except Exception as e:
            print(f"Menu not found: {e}")
        
    def do_exit(self, arg): 
        print("off")
        return True
    def do_restart(self,arg):
        os.system('cls')
        subprocess.run([sys.executable, os.path.abspath(__file__)])
        sys.exit()
        
    def default(self, line):
        print(f"Uknown command: {line}")

if __name__ == "__main__":
    AVMacro().cmdloop()
