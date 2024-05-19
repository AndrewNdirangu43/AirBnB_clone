#!/usr/bin/python3
"""
This is a module to start the Airbnb Clone Console.
The module compiles necessary functions to interprete and execute commands.
"""
import cmd


class HBNB(cmd.Cmd):
    """ This is a class inherited by the different subclasses """

    prompt = "(hbnb) "


if __name__ == '__main__':
    HBNB().cmdloop()

