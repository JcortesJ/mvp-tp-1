from antlr4 import *
from gramLexer import gramLexer
from gramListener import gramListener
from gramParser import gramParser
import sys
from markov_chain import MarkovChain

        
class gramPrintListener(gramListener):

    def __init__(self):
        self.markov_chain = MarkovChain()
        
    def enterDefstates(self, ctx):
        #print("States: %s" % str([str(x) for x in ctx.ID()]))
        self.markov_chain.set_states([str(x) for x in ctx.ID()])
        self.markov_chain.set_transitions()

    def enterDefactions(self, ctx):
        #print("Actions: %s" % str([str(x) for x in ctx.ID()]))
        self.markov_chain.set_actions([str(x) for x in ctx.ID()])

    def enterTransact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        act = ids.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]
        print("Transition from " + dep + " with action "+ act + " and targets " + str(ids) + " with weights " + str(weights))
        for i in range(len(ids)):
            self.markov_chain.add_transition(dep, ids[i], weights[i], act)
    def enterTransnoact(self, ctx):
        ids = [str(x) for x in ctx.ID()]
        dep = ids.pop(0)
        weights = [int(str(x)) for x in ctx.INT()]
        print("Transition from " + dep + " with no action and targets " + str(ids) + " with weights " + str(weights))
        for i in range(len(ids)):
            self.markov_chain.add_transition(dep, ids[i], weights[i], 'NoAction')
            

def main():
    lexer = gramLexer(StdinStream())
    #path = "ex.mdp"
    #lexer = gramLexer(FileStream(path))
    # Pour lire directement depuis le fichier
    stream = CommonTokenStream(lexer)
    parser = gramParser(stream)
    tree = parser.program()
    printer = gramPrintListener()
    walker = ParseTreeWalker() # mettre à jour les états et actions
    walker.walk(printer, tree)
    print("Markov Chain:")
    print(printer.markov_chain)

if __name__ == '__main__':
    main()
