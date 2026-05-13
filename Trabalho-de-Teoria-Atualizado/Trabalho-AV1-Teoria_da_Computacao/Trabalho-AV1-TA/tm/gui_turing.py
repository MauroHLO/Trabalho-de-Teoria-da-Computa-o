import tkinter as tk
import time

class TuringGUI:
    def __init__(self, machine):
        self.machine = machine
        self.root = tk.Tk()
        self.root.title("Simulador de Máquina de Turing - UFC")
        self.root.geometry("900x300")
        
        # Canvas principal
        self.canvas = tk.Canvas(self.root, width=850, height=200, bg="#f0f0f0", highlightthickness=0)
        self.canvas.pack(pady=20)
        
        # Label de estado
        self.status_label = tk.Label(self.root, text="Aguardando início...", font=("Helvetica", 14, "bold"), fg="#333")
        self.status_label.pack()

        # Botão
        self.btn_run = tk.Button(self.root, text="EXECUTAR", command=self.run_visual, 
                                 bg="#4CAF50", fg="white", font=("Arial", 8, "bold"), padx=20)
        self.btn_run.pack(pady=10)
        
        self.draw_tape()

    def draw_tape(self):
        self.canvas.delete("all")
        
        cell_size = 50
        canvas_mid_x = 425 # Centro do canvas (850/2)
        y_top = 80         # Posição vertical da fita
        
        # 1. DESENHO DO TRIÂNGULO (CABEÇOTE) - AGORA ACIMA E CENTRALIZADO
        # Coordenadas: (Ponta inferior centralizada, Ponta superior esquerda, Ponta superior direita)
        # O x central é o canvas_mid_x, o y é logo acima da fita (y_top - 5)
        self.canvas.create_polygon(
            canvas_mid_x, y_top - 5,           # Ponta de baixo (apontando para a célula)
            canvas_mid_x - 15, y_top - 30,     # Ponta superior esquerda
            canvas_mid_x + 15, y_top - 30,     # Ponta superior direita
            fill="#d9534f", outline="black"    # Vermelho escuro para destaque
        )

        # 2. DESENHO DAS CÉLULAS DA FITA
        # Calculamos o deslocamento para que a célula 'self.machine.current' fique no centro
        for i in range(-8, 9):
            idx = self.machine.current + i
            char = self.machine.fita[idx] if 0 <= idx < len(self.machine.fita) else "_"
            
            # Cálculo de X para centralizar a célula atual
            x1 = canvas_mid_x + (i * cell_size) - (cell_size // 2)
            y1 = y_top
            x2 = x1 + cell_size
            y2 = y1 + cell_size
            
            # Cor: Amarelo para a célula atual, Branco para as outras
            fill_color = "#fff3cd" if i == 0 else "white"
            outline_color = "#856404" if i == 0 else "#ccc"
            width = 3 if i == 0 else 1

            self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline=outline_color, width=width)
            self.canvas.create_text(x1 + cell_size//2, y1 + cell_size//2, text=char, 
                                    font=("Courier New", 18, "bold"), fill="black")

    def run_visual(self):
        self.btn_run.config(state="disabled") # Evita múltiplos cliques
        
        while True:
            char_atual = self.machine.fita[self.machine.current]
            t = self.machine.q.transition(char_atual)
            
            if t is None:
                break

            edge = t.getEdge()
            
            # Atualiza a fita e o estado
            self.machine.fita[self.machine.current] = edge.getWrite()
            
            if edge.getDirection() == '>':
                self.machine.current += 1
            elif edge.getDirection() == '<':
                self.machine.current -= 1
            
            self.machine.q = t.getState()
            
            # Atualiza interface
            self.status_label.config(text=f"ESTADO ATUAL: {self.machine.q.getName()} | LENDO: '{char_atual}'")
            self.draw_tape()
            self.root.update()
            
            time.sleep(1) # Velocidade da animaçãoS
        
        final_text = "ACEITO!" if self.machine.q.isFinal else "PAROU (REJEITADO)"
        color = "green" if self.machine.q.isFinal else "red"
        self.status_label.config(text=f"FIM: {final_text}", fg=color)