#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand inherits from cmd.Cmd"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        quit()

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        quit()

    def do_help(self, arg):
        """Help command to get info on command
        If no parameter given, list all commands
        """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Empty line should do nothing"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
