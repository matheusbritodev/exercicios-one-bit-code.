import os


def Desligar(x):
    desligar = os.system(f"shutdown /s /t {x}")
    return desligar

def Reiniciar(x):
    reiniciar = os.system(f"shutdown /r /t {x}")
    return reiniciar

def ReiniciarAgora():
    reiniciar = os.system("shutdown /r /t 1")
    return reiniciar

def DesligarAgora():
    desligar = os.system("shutdown /s /t 1")
    return desligar

def Cancelar():
    cancelar = os.system("shutdown /a")
    return cancelar
