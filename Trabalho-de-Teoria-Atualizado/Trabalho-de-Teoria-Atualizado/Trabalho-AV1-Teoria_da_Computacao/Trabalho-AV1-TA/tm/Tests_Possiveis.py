from State import State
from Machine import Machine
from gui_turing import TuringGUI 

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

    palavra = 'bbaa'
    mt = Machine(q0, palavra, 20)
    
    print(f"Iniciando interface visual para a entrada: {palavra}")
    app = TuringGUI(mt)
    app.root.mainloop()
    mt.print_result()

def test_q1_prova():
    """Valida a linguagem múltiplo de 3"""
    print("--- Testando Linguagem múltiplo de 3 ---")
    
    qA = State('qA') # Estado inicial
    q0 = State('q0') 
    q1 = State('q1')
    q2 = State('q2') 
    q3 = State('q3') 
    q6 = State('q6')
    qq1 = State('qq1') 
    qq0 = State('qq0')
    qV = State('qV')
    qVI = State('qVI')
    qq0.setFinal()
    q0.setFinal()
    q3.setFinal()
    q6.setFinal()
    qVI.setFinal()

    qA.addTransition(q0, '0', '0', '>')
    qA.addTransition(q1, '1', '1', '>')
     
    q0.addTransition(q0, '0', '0', '>') 
    q0.addTransition(q1, '1', '1', '>') 

    q1.addTransition(q2, '0', '0', '>')
    q1.addTransition(q3, '1', '1', '>')

    q2.addTransition(q2, '1', '1', '>')
    q2.addTransition(q1, '0', '0', '>')

    q3.addTransition(q6, '0', '0', '>')
    q3.addTransition(qq1, '1', '1', '>')
    
    q6.addTransition(qq1, '1', '1', '>')
    q6.addTransition(qq0, '0', '0', '>')
    q6.addTransition(qV, '_', 'V', '>')

    qq0.addTransition(qq0, '0', '0', '>')
    qq0.addTransition(qq1, '1', '1', '>')
    
    qq1.addTransition(q2, '0', '0', '>')
    qq1.addTransition(qq0, '1', '1', '>')
    
    qV.addTransition(qVI, '_', 'I', '>')

    palavra = '11'
    mt = Machine(qA, palavra, 30)
    
    print(f"Iniciando interface visual para a entrada: {palavra}")
    app = TuringGUI(mt)
    app.root.mainloop()
    mt.print_result()

    
if __name__ == "__main__":
    #teste_anbn()
    test_q1_prova()