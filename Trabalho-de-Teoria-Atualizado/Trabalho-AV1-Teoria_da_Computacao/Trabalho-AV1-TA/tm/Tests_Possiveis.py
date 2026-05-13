from State import State
from Machine import Machine
from gui_turing import TuringGUI 

def teste_anbn():
    """Valida a linguagem {a^n b^n | n >= 0}"""
    print("\n--- Testando Linguagem {a^n b^n} ---")
    print("Exemplos: 'aaabbb' (Aceito), 'aabbb' (Rejeitado), 'bbbaaa' (Rejeitado)")
    
    q0 = State('q0') # Estado inicial: procura 'a' para marcar
    q1 = State('q1') # Estado: move para a direita até o fim dos 'a's
    q2 = State('q2') # Estado: procura 'b' para marcar
    q3 = State('q3') # Estado: move para a esquerda voltando ao início
    q4 = State('q4') # Estado: validação final (vazio)
    qf = State('qf') # Estado de aceitação
    qf.setFinal()

    # q0: Marca 'a' com 'A' e vai buscar 'b'
    q0.addTransition(q1, 'a', 'A', '>')
    q0.addTransition(q4, 'B', 'B', '>') 
    q0.addTransition(qf, '_', '_', '>') 

    # q1: Pula 'a's e 'B's indo para a direita
    q1.addTransition(q1, 'a', 'a', '>')
    q1.addTransition(q1, 'B', 'B', '>')
    q1.addTransition(q2, 'b', 'B', '<') 

    # q2: Volta para a esquerda até encontrar o último 'A' marcado
    q2.addTransition(q2, 'a', 'a', '<')
    q2.addTransition(q2, 'B', 'B', '<')
    q2.addTransition(q0, 'A', 'A', '>')

    # q4: Verifica se não sobraram 'b's isolados
    q4.addTransition(q4, 'B', 'B', '>')
    q4.addTransition(qf, '_', '_', '>')

    palavra = input("Digite a sequência para {a^n b^n}: ").strip()
    if not palavra: palavra = 'aaabbb'
    
    mt = Machine(q0, palavra, 20)
    print(f"Iniciando interface visual para: {palavra}")
    app = TuringGUI(mt)
    app.root.mainloop()
    mt.print_result()

def test_multiplo_3():
    """Valida a linguagem múltiplo de 3 em binário"""
    print("\n--- Testando Linguagem Múltiplo de 3 ---")
    print("Exemplos: '0' (0), '110' (6), '1001' (9) são aceitos.")
    
    qA = State('qA') 
    q0 = State('q0') 
    q1 = State('q1')
    q2 = State('q2') 
    q3 = State('q3') 
    q6 = State('q6')
    qq1 = State('qq1') 
    qq0 = State('qq0')
    qV = State('qV')
    qVI = State('qVI')
    
    # Estados de aceitação conforme a lógica de múltiplos de 3
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

    palavra = input("Digite o binário para testar múltiplo de 3: ").strip()
    if not palavra: palavra = '110'
    
    mt = Machine(qA, palavra, 30)
    app = TuringGUI(mt)
    app.root.mainloop()
    mt.print_result()

if __name__ == "__main__":
    print("Selecione o teste extra:")
    print("1 - Linguagem {a^n b^n}")
    print("2 - Múltiplo de 3 (Binário)")
    opcao = input("Opção: ")
    
    if opcao == '1':
        teste_anbn()
    else:
        test_multiplo_3()