#!/usr/bin/python3
"""
This contains the console
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.review import Review
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place


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
        classes = {
                "BaseModel":BaseModel, "User":User,
                "State":State, "City":City, "Amenity":Amenity,
                "Place":Place, "Review":Review
                }
        if not arg:
            print("** class name missing **")
            return
        elif arg not in classes:
            print("** class doesn't exist **")
            return
        new_instance = classes[arg]()
        new_instance.save()
        print(new_instance.id)
        storage.save()
        """
        try:
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        except ImportError:
            print("** class doesn't exist **")
        """

    def do_show(self, arg):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key in objects:
            print(objects[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on class name and id
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        objects = storage.all()
        everyting = []

        if not arg:
            for obj in objects.values():
                everyting.append(str(obj))
            print(everyting)
        elif args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
        else:
            for key in objects:
                if key.split(".")[0] == args[0]:
                    everyting.append(str(objects[key]))
            print(everyting)

    def do_update(self, arg):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute
        """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(objects[key], args[2], args[3])
        objects[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
