#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand inherits from cmd.Cmd"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Creates a new instance of BaseModel

        Prints '** class name missing **' if no class name is given
        Prints '** class doesn't exist **' if class name doesn't exist
        """
        if not arg:
            print('** class name missing **')
            return
        if arg == "BaseModel":
            new_model = BaseModel()
            new_model.save()
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print string representation of instance based on the class name and id

        Usage: $ show BaseModel 1234-1234-1234
        """
        pass

    def do_destroy(self, arg):
        """Deletes an instance based on a class name and id
        and save changes to a JSON file"""
        pass

    def do_all(self, arg):
        """Prints all instances based on a class name or not"""
        objs = storage.all()
        ins = []
        if not arg:
            for o in objs:
                ins.append(objs[o])
        if arg == "BaseModel":
            for o in objs:
                if o.__name__ == arg:
                    ins.append(objs[o])
        else:
            print("** class doesn't exist **")
        print(ins)
    
    def do_update(self, arg):
        """ Updates an instance based on the class name and id
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        pass

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
