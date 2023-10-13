#!/usr/bin/python3
"""
This contains the console
"""
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This is the console
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        To exist the program
        """
        return True

    def do_EOF(self, arg):
        """
        EOF
        """
        return True

    def emptyline(self):
        """
        for an empty line we do nothing
        """
        pass

    def do_create(self, arg):
        """
        To create a new instance
        """
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except ImportError:
            print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
