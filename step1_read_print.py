# TODO Fix '?' on the prompt

from cmd import Cmd
import readline

class OtterPrompt(Cmd):
    def default(self, line):
        print(rep(line))

    def do_quit(self, args):
        """Quits the program."""
        print ("Quitting.")
        raise SystemExit


def READ(line: str) -> str:
    return line

def EVAL(line: str) -> str:
    return line

def PRINT(line: str) -> str:
    return line

def rep(line: str) -> str:
    re = READ(line)
    ev = EVAL(re)
    return PRINT(ev)

if __name__ == '__main__':
    prompt = OtterPrompt()
    prompt.prompt = 'user> '
    prompt.default
    prompt.cmdloop()
