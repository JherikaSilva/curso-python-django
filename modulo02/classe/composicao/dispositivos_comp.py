
class Teclado:
    def __init__(self):
        pass
    
    def ligar(self):
        print("O teclado foi ligado.") 


class Mouse:
    def __init__(self):
        pass
    
    def ligar(self):
        print("O mouse foi ligado.") 


class Monitor:
    def __init__(self):
        pass
    
    def ligar(self):
        print("O monitor foi ligado.") 

class Computador:
    def __init__(self):
        self.mouse=Mouse()
        self.monitor=Monitor()
        self.teclado=Teclado()
        
    def ligar_computador(self):
        print("Ligando computador...\n")
        self.monitor.ligar()
        self.teclado.ligar()
        self.mouse.ligar()
        print("\nMaquina ligada e pronta para uso!")
        
note=Computador()

note.ligar_computador()        
    
        