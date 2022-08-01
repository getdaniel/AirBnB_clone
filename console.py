#!/usr/bin/python3
""" Defines entry point of the command interpreter."""
import cmd
import re


class HBNBCommand(cmd.Cmd):
    """
    Implements the class HBNBCommand.

    Attributes:
        prompt (str): The command prompt.
    """
    prompt = "(hbnb) "

    def default(self, arg):
        """ Improves the default cmd. """
        argdict = {
                "EOF": self.do_EOF,
                "help": self.cmd.help,
                "quit": self.do_quit
                }
        match = re.search(r"\.", arg)
        if match != None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])

            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]

                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)

    def do_quit(self, args):
        """ Quit command to exit. """
        return True

    def do_EOF(self, arg):
        """ EOF signal to exit the program."""
        print("")
        return True

    def emptyline(self):
        """ Nothing done when recieving an empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
