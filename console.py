#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand inherits from cmd.Cmd"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel

        Usage:
            $ create BaseModel

        Prints '** class name missing **' if no class name is given
        Prints '** class doesn't exist **' if class name doesn't exist
        """
        if not arg:
            print('** class name missing **')
            return
        if arg == "BaseModel":
            new_model = BaseModel()
            new_model.save()
            print("{}".format(new_model.id))
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show command to print string representation of instance
        based on the class name and id

        Usage:
            $ show BaseModel 1234-1234-1234

        Prints '** class name missing **' if no class name is given
        Prints '** class doesn't exist **' if class name doesn't exist
        """
        if not arg:
            print('** class name missing **')
            return
        objs = storage.all()

    def do_destroy(self, arg):
        """Destroy command to delete an instance based on a class name and id
        and save changes to a JSON file

        Usage:
            $ destroy BaseModel 1234-1234-1234
        """
        pass

    def do_all(self, arg):
        """All command to print all instances based on a class name or
        all classes

        Usage:
            $ all BaseModel
            $ all
        """
        objs = storage.all()
        ins = []
        if not arg:
            for o in objs:
                ins.append(objs[o])
            print(ins)
            return
        if arg == "BaseModel":
            for o in objs:
                if o.__name__ == arg:
                    ins.append(objs[o])
            print(ins)
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Update command to update an instance based on the class name and id

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        """
        pass

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        quit()

    def do_EOF(self, arg):
        """EOF command to exit the program\n"""
        quit()

    def do_help(self, arg):
        """Help command to get info on specified command
        If no parameter given, list all commands
        """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Empty line should do nothing"""
        return


def parse(arg):
    """Convert a series of arguments into argument tuple"""
    return tuple(map(int, arg.split()))

if __name__ == "__main__":
    HBNBCommand().cmdloop()
