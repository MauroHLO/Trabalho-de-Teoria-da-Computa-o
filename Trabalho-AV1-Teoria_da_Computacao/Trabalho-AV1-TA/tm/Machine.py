from State import State

class Machine:
    def __init__(self, q: State, w: str, _range: int):
        self.q = q # Estado atual/inicial
        self.w = w # Palavra de entrada
        self.range = _range
        self.fita = []
        self.current = _range # A cabeça começa no início da palavra (meio da fita)
        
        self.set_fita_space(_range)
        self.init_fita(w)

    def set_fita_space(self, _range):
        # Cria uma fita preenchida com o símbolo de vazio '_' 
        # O tamanho é o dobro do range para permitir movimento para ambos os lados
        self.fita = ['_'] * (_range * 2)

    def init_fita(self, w):
        # Coloca a palavra de entrada na fita a partir da posição 'range'
        for i, char in enumerate(list(w)):
            self.fita[self.current + i] = char

    def run(self):
        if self.q is None:
            return False
        
        print(f"Iniciando simulação. Estado: {self.q.getName()}")
        
        while True:
            char_atual = self.fita[self.current]
            t = self.q.transition(char_atual)
            
            if t is None:
                # Se não há transição definida, a máquina para
                break

            edge = t.getEdge()
            
            # 1. Escreve o novo símbolo na fita
            self.fita[self.current] = edge.getWrite()
            
            # 2. Log da operação
            print(f"Lê({char_atual}) -> Escreve({edge.getWrite()}), Move({edge.getDirection()}), Estado({t.getState().getName()})")
            
            # 3. Move a cabeça de leitura/escrita
            if edge.getDirection() == '>':
                self.current += 1
            elif edge.getDirection() == '<':
                self.current -= 1
            
            # 4. Atualiza o estado atual
            self.q = t.getState()
            
            # Se atingir um estado de aceitação, para a execução [cite: 145]
            if self.q.isFinal:
                break

        return self.print_result()

    def print_result(self):
        # Remove os símbolos vazios para mostrar o resultado final da fita
        resultado_fita = "".join(self.fita).strip('_')
        
        if self.q.isFinal:
            print(f"RESULTADO: ACEITO [cite: 154]")
            print(f"Fita Final: {resultado_fita}")
            return True
        else:
            print(f"RESULTADO: REJEITADO (Parou no estado {self.q.getName()})")
            print(f"Fita Final: {resultado_fita}")
            return False