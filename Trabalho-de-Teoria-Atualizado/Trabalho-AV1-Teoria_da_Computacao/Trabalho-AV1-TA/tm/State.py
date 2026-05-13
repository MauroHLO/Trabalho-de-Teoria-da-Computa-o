from Edge import Edge
from Transition import Transition

class State:
    def __init__(self, name: str):
        self.name = name
        self.isFinal = False
        self.transitions = []

    def getName(self): return self.name
    def setFinal(self): self.isFinal = True

    # Alterado para suportar os parâmetros da Máquina de Turing
    def addTransition(self, state, read: str, write: str = None, direction: str = '>'):
        edge = Edge.instance(read, write, direction)
        transition = Transition(state, edge)
        
        # Evita duplicatas simples
        if transition not in self.transitions:
            self.transitions.append(transition)
        return self

    def transition(self, _c: str):
        for t in self.transitions:
            if t.getEdge().getRead() == _c:
                return t
        return None

    def __eq__(self, other):
        if isinstance(other, State):
            return self.name == other.name
        return False

    def hashCode(self):
        return hash(self.name)