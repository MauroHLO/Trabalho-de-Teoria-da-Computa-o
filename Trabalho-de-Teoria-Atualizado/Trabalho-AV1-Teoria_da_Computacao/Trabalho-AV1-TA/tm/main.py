from State import State
from Machine import Machine
from gui_turing import TuringGUI 

def rodar_simulacao_grafica():
    # 1. Configuração dos Estados (Algoritmo do fonte.mt)
    # Este bloco define a "lógica" ou o "programa" que a máquina vai executar
    qp = State('qp') # Estado: Percorre a palavra
    qx = State('qx') # Estado: Volta para o início
    qf = State('qf') # Estado: Final de aceitação
    qf.setFinal()

    # Definição das Regras de Transição
    # qp: Enquanto ler 0 ou 1, continua andando para a direita (>)
    qp.addTransition(qp, '1', '1', '>')
    qp.addTransition(qp, '0', '0', '>')
    # Ao encontrar o vazio (_) no fim, escreve 'X', muda para qx e volta (<)
    qp.addTransition(qx, '_', 'X', '<')

    # qx: Enquanto ler 0 ou 1, continua voltando para a esquerda (<)
    qx.addTransition(qx, '1', '1', '<')
    qx.addTransition(qx, '0', '0', '<')
    # Ao encontrar o vazio (_) no início, escreve 'Y', muda para qf e para (>)
    qx.addTransition(qf, '_', 'Y', '>')

    # 2. Interface de Liberdade ao Usuário
    print("=== Simulador de Máquina de Turing (UFC) ===")
    print("O algoritmo atual adiciona 'Y' no início e 'X' no fim.")
    
    # Recebe a entrada do teclado
    entrada_usuario = input("Digite a sequência binária (ou pressione Enter para '101001'): ").strip()
    
    # Validação simples: se estiver vazio, usa o padrão
    if not entrada_usuario:
        entrada_usuario = '101001'
    
    # 3. Inicialização da Máquina
    # Definimos um range de 30 para garantir que fita tenha espaço para crescer
    mt = Machine(qp, entrada_usuario, 30)

    # 4. Início da Interface Gráfica
    print(f"Iniciando interface visual para a entrada: {entrada_usuario}")
    app = TuringGUI(mt)
    app.root.mainloop()

if __name__ == "__main__":
    rodar_simulacao_grafica()