#!/usr/bin/env python
# coding: utf-8

# In[11]:


def sub(a,b):
    res = a-b
    return(res)
    
def soma(a,b):
    res = a+b
    return(res)

def mult(a,b):
    res = a*b
    return(res)

def div(a,b):
    if a == 0:
        print("Res não existe")
    else:
        res = a/b
        return(res)
    

print("Selecione o número da opção desejada: \n")

print("1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\n")

res = input("Digite sua opção: ")

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo Número: "))

if res == '1':
    print("%r + %r = %r "%(a,b,soma(a,b)))
elif res == '2':
    print("%r - %r = %r "%(a,b,sub(a,b)))
elif res == '3':
    print("%r * %r = %r "%(a,b,mult(a,b)))
elif res == '4':
    print("%r / %r = %r "%(a,b,div(a,b)))
else:
    "Nenhuma opção válida"

