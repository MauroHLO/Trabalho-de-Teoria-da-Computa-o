from State import State
from Machine import Machine

def teste_anbn():
    """Valida a linguagem {a^n b^n | n >= 0}"""
    print("--- Testando Linguagem {a^n b^n} ---")
    
    q0 = State('q0') # Estado inicial: procura 'a' para marcar
    q1 = State('q1') # Estado: move para a direita até o fim dos 'a's
    q2 = State('q2') # Estado: procura 'b' para marcar
    q3 = State('q3') # Estado: move para a esquerda voltando ao início
    q4 = State('q4') # Estado: validação final (vazio)
    qf = State('qf') # Estado de aceitação
    qf.setFinal()

    # q0: Marca 'a' com 'A' e vai buscar 'b'
    q0.addTransition(q1, 'a', 'A', '>')
    q0.addTransition(q4, 'B', 'B', '>') # Se não houver mais 'a', verifica se restam 'b's
    q0.addTransition(qf, '_', '_', '>') # Palavra vazia aceita

    # q1: Pula 'a's e 'B's indo para a direita
    q1.addTransition(q1, 'a', 'a', '>')
    q1.addTransition(q1, 'B', 'B', '>')
    q1.addTransition(q2, 'b', 'B', '<') # Achou 'b', marca com 'B' e volta

    # q2: Volta para a esquerda até encontrar o último 'A' marcado
    q2.addTransition(q2, 'a', 'a', '<')
    q2.addTransition(q2, 'B', 'B', '<')
    q2.addTransition(q0, 'A', 'A', '>')

    # q4: Verifica se não sobraram 'b's isolados
    q4.addTransition(q4, 'B', 'B', '>')
    q4.addTransition(qf, '_', '_', '>')

    palavra = "aaabbb"
    mt = Machine(q0, palavra, 20)
    mt.run()

if __name__ == "__main__":
    teste_anbn()