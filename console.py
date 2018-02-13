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
        Prints '** instance id missing **' if instance id missing
        Prints '** no instance found **' if instance of class does not exist 
        """
        if not arg:
            print('** class name missing **')
            return
        args = arg.split(" ")
        objs = storage.all()
        if args[0] == "BaseModel":
            if len(args) != 2:
                print("** instance id missing **")
            elif ("BaseModel." + args[1]) not in objs:
                print("** no instance found **")
            else:
                print(objs["BaseModel." + args[1]])

    def do_destroy(self, arg):
        """Destroy command to delete an instance based on a class name and id
        and save changes to a JSON file

        Usage:
            $ destroy BaseModel 1234-1234-1234

        Prints '** class name missing **' if no class name is given
        Prints '** class doesn't exist **' if class name doesn't exist
        Prints '** instance id missing **' if instance id missing
        Prints '** no instance found **' if instance of class does not exist 
        """
        if not arg:
            print('** class name missing **')
            return
        args = arg.split(" ")
        objs = storage.all()
        if args[0] == "BaseModel":
            if len(args) != 2:
                print("** instance id missing **")
            if ("BaseModel." + args[1]) not in objs:
                print("** no instance found **")
            else:
                del objs["BaseModel." + args[1]]
                storage.save()

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
        args = arg.split(" ")
        if args[0] == "BaseModel":
            for o in objs:
                if o[0:len("BaseModel")] == args[0]:
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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
