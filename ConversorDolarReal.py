import tkinter as tk
from tkinter import ttk
import requests

class ConversorDolarReal:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor Dólar para Real")
        self.root.geometry("400x300")
        
        self.cotacao_atual = self.obter_cotacao()
        
        self.criar_interface()
    
    def obter_cotacao(self):
        """Obtém a cotação atual do dólar"""
        try:
            url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
            response = requests.get(url)
            data = response.json()
            return float(data['USDBRL']['bid'])
        except:
            return 5.50  # Valor padrão
    
    def converter(self):
        """Realiza a conversão"""
        try:
            valor_dolar = float(self.entry_dolar.get())
            valor_real = valor_dolar * self.cotacao_atual
            
            self.label_resultado.config(
                text=f"${valor_dolar:.2f} = R${valor_real:.2f}\n"
                     f"Taxa: R$ {self.cotacao_atual:.2f}"
            )
        except ValueError:
            self.label_resultado.config(text="Digite um valor válido!")
    
    def criar_interface(self):
        """Cria a interface gráfica"""
        # Frame principal
        frame = ttk.Frame(self.root, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        ttk.Label(frame, text="Conversor Dólar → Real", 
                 font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
        
        # Cotação atual
        ttk.Label(frame, text=f"Cotação atual: R$ {self.cotacao_atual:.2f}",
                 font=("Arial", 10)).grid(row=1, column=0, columnspan=2, pady=5)
        
        # Entrada de valor
        ttk.Label(frame, text="Valor em Dólar ($):").grid(row=2, column=0, sticky=tk.W, pady=10)
        self.entry_dolar = ttk.Entry(frame, width=15, font=("Arial", 12))
        self.entry_dolar.grid(row=2, column=1, pady=10)
        
        # Botão de conversão
        btn_converter = ttk.Button(frame, text="Converter", command=self.converter)
        btn_converter.grid(row=3, column=0, columnspan=2, pady=20)
        
        # Resultado
        self.label_resultado = ttk.Label(frame, text="", font=("Arial", 12, "bold"))
        self.label_resultado.grid(row=4, column=0, columnspan=2, pady=10)
        
        # Configurar expansão
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

# Executar a aplicação
if __name__ == "__main__":
    root = tk.Tk()
    app = ConversorDolarReal(root)
    root.mainloop()




#Versão do programa com API


import requests

def obter_cotacao_atual():
    """
    Obtém a cotação atual do dólar em tempo real usando uma API
    """
    try:
        url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"
        response = requests.get(url)
        data = response.json()
        
        cotacao = float(data['USDBRL']['bid'])
        return cotacao
    
    except Exception as e:
        print(f"Erro ao obter cotação: {e}")
        return 5.50  # Valor padrão em caso de erro

def converter_dolar_para_real():
    """
    Converte dólar para real usando cotação em tempo real
    """
    print("=== Conversor de Dólar para Real ===")
    
    # Obter cotação atual
    cotacao = obter_cotacao_atual()
    print(f"Cotação atual: R$ {cotacao:.2f}")
    
    try:
        valor_dolar = float(input("\nDigite o valor em dólar (USD): $"))
        valor_real = valor_dolar * cotacao
        
        print(f"\nResultado:")
        print(f"${valor_dolar:.2f} dólares = R${valor_real:.2f} reais")
        print(f"Taxa de câmbio: R$ {cotacao:.2f}")
    
    except ValueError:
        print("Por favor, digite um valor numérico válido.")

# Executar o programa
if __name__ == "__main__":
    converter_dolar_para_real()
