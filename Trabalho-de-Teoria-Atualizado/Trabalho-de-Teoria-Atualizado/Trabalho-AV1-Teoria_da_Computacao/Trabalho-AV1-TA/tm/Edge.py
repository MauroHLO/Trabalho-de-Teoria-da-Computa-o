class Edge:
    def __init__(self, read: str, write: str = None, direction: str = '>'):
        self.read = read
        # Se não for especificado um caractere de escrita, mantém o original
        self.write = write if write is not None else read
        self.direction = direction # '>' para Direita (Right), '<' para Esquerda (Left)

    def getRead(self): return self.read
    def getWrite(self): return self.write
    def getDirection(self): return self.direction

    @staticmethod
    def instance(read: str, write: str = None, direction: str = '>'):
        return Edge(read, write, direction)

    def equals(self, o):
        if isinstance(o, Edge):
            return self.read == o.read
        return False

    def __repr__(self):
        return f'[{self.read} -> {self.write}, {self.direction}]'