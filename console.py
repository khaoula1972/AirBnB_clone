#!/usr/bin/python3
"""
This contains the console
"""
import cmd
import models
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
                "BaseModel": BaseModel, "User": User,
                "State": State, "City": City, "Amenity": Amenity,
                "Place": Place, "Review": Review
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
        classes = [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
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
        classes = [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
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
        classes = [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]
        args = arg.split()
        objects = storage.all()
        everyting = []

        if not arg:
            for obj in objects.values():
                everyting.append(str(obj))
            print(everyting)
        elif args[0] not in classes:
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
        classes = [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        if args[0] not in classes:
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

        attr_name = args[2]
        attr_value = args[3]

        setattr(objects[key], attr_name, attr_value)
        objects[key].save()

    def default(self, line):
        """Override default to handle class.all() syntax"""
        if not line:
            return

        parts = line.split(".")
        classes = [
                "BaseModel", "User", "State", "City",
                "Amenity", "Place", "Review"
                ]
        if len(parts) == 2:
            class_name = parts[0]
            if parts[1] == "all()":
                if class_name in classes:
                    self.do_all(class_name)
                else:
                    print("** class doesn't exist **")
            elif parts[1] == "count()":
                if class_name in classes:
                    instances = models.storage.all()
                    counter = sum(
                            1 for instance in
                            instances.values()
                            if instance.__class__.__name__ == class_name
                            )
                    print(counter)
                    return
                else:
                    print("** class doesn't exist **")
            elif parts[1].startswith("show(") and parts[1].endswith(")"):
                if class_name in classes:
                    cmd_parts = parts[1].strip('show("")').split()
                    if len(cmd_parts) == 1:
                        instance_id = cmd_parts[0]
                        show_command = "show {} {}".format(
                                class_name, instance_id
                                )
                        self.onecmd(show_command)
                    else:
                        print("*** Unknown syntax: {}".format(line))
                else:
                    print("** class doesn't exist **")
            elif parts[1].startswith("destroy(") and parts[1].endswith(")"):
                if class_name in classes:
                    cmd_parts = parts[1].strip('destroy("")').split()
                    if len(cmd_parts) == 1:
                        instance_id = cmd_parts[0]
                        destroy_command = "destroy {} {}".format(
                                class_name, instance_id
                                )
                        self.onecmd(destroy_command)
                    else:
                        print("*** Unknown syntax: {}".format(line))
                else:
                    print("** class doesn't exist **")
            elif parts[1].startswith("update(") and parts[1].endswith(")"):
                if class_name in classes:
                    update_args = parts[1][7:-1].split(", ")
                    if len(update_args) == 3:
                        obj_id = update_args[0][1:-1]
                        attr_name = update_args[1][1:-1]
                        attr_value = update_args[2]
                        if attr_value.startswith('"'):
                            if attr_value.endswith('"'):
                                attr_value = update_args[2][1:-1]
                        show_cmd = "update {} {} {} {}".format(
                                    class_name, obj_id,
                                    attr_name, attr_value
                                    )
                        self.onecmd(show_cmd)
                    else:
                        print("*** Unknown syntax: {}".format(line))
                else:
                    print("** class doesn't exist **")
            else:
                print("*** Unknown syntax: {}".format(line))
        else:
            print("*** Unknown syntax: {}".format(line))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
