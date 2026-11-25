from antlr4 import *
from gramLexer import gramLexer
from gramListener import gramListener
from gramParser import gramParser
import sys
from model import MDP

        
class gramPrintListener(gramListener):

    def __init__(self):
        self.mdp = MDP()
        
    def enterDefstates(self, ctx):
        #print("States: %s" % str([str(x) for x in ctx.ID()]))
        self.mdp.set_states([str(x) for x in ctx.ID()])

    def enterDefactions(self, ctx):
        #print("Actions: %s" % str([str(x) for x in ctx.ID()]))
        self.mdp.set_actions([str(x) for x in ctx.ID()])

    def enterTransact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        act = ids.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]
        #print("Transition from " + dep + " with action "+ act + " and targets " + str(ids) + " with weights " + str(weights))
        self.mdp.add_transition(dep,ids,weights,act)

    def enterTransnoact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]
        #print("Transition from " + dep + " with no action and targets " + str(ids) + " with weights " + str(weights))
        self.mdp.add_transition(dep,ids,weights,'N')
            

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "ex.mdp"
    lexer = gramLexer(FileStream(path))
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    tree = parser.program()
    printer = gramPrintListener()
    walker = ParseTreeWalker() # mettre à jour les états et actions
    walker.walk(printer, tree)
    print("MDP:")
    print(printer.mdp.transitions)
    simulated = printer.mdp.simulate()
    print(f'Simulated states in order: {simulated}')

if __name__ == '__main__':
    main()
