# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/operaciones_basicas.ipynb.

# %% auto 0
__all__ = ['suma', 'resta', 'multiplicacion', 'division']

# %% ../nbs/operaciones_basicas.ipynb 2
def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"
