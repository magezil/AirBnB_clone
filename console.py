#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd
from datetime import datetime
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Class HBNBCommand inherits from cmd.Cmd"""
    prompt = '(hbnb) '

    def do_create(self, arg):
        """Create command to create a new instance of BaseModel

        Usage:
            $ create BaseModel

        Prints:
            '** class name missing **' if no class name is given
            '** class doesn't exist **' if class name doesn't exist
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

        Prints:
            '** class name missing **' if no class name is given
            '** class doesn't exist **' if class name doesn't exist
            '** instance id missing **' if instance id missing
            '** no instance found **' if instance of class does not exist 
        """
        obj = self.find_obj(arg)
        if obj:
            print(obj)

    def do_destroy(self, arg):
        """Destroy command to delete an instance based on a class name and id
        and save changes to a JSON file

        Usage:
            $ destroy BaseModel 1234-1234-1234

        Prints:
            '** class name missing **' if no class name is given
            '** class doesn't exist **' if class name doesn't exist
            '** instance id missing **' if instance id missing
            '** no instance found **' if instance of class does not exist 
        """
        obj = self.find_obj(arg)
        if obj:
            objs = storage.all()
            del objs["{}.{}".format(type(obj).__name__, obj.id)]
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

        Prints:
            '** class name missing **' if no class name is given
            '** class doesn't exist **' if class name doesn't exist
            '** instance id missing **' if instance id missing
            '** no instance found **' if instance of class does not exist 
            '** attribute name missing **' if attribute name is missing
            '** value missing **' if value for attribute name is missing
        """
        obj = self.find_obj(arg)
        if obj:
            args = arg.split(" ")
            objs = storage.all()
            if len(args) < 3:
                print('** attribute name missing **')
            elif len(args) < 4:
                print('** value missing **')
            elif args[2] != "id" and args[2] != "created_at" and args[2] != "updated_at":
                # args[2] = attribute, args[3] = value
                print(args[3])
    #            if args[2] in obj:
                obj.__dict__[args[2]] = args[3]
                obj.updated_at = datetime.now()
                storage.save()

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

    def find_obj(self, arg):
        """Finds specified object instance based on given arguments"""
        if not arg:
            print('** class name missing **')
            return
        args = arg.split(" ")
        objs = storage.all()
        if args[0] == "BaseModel":
            if len(args) < 2:
                print("** instance id missing **")
            elif ("BaseModel." + args[1]) not in objs:
                print("** no instance found **")
            else:
                return objs["BaseModel." + args[1]]
        else:
            print("** class doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
