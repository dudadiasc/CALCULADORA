import streamlit as st
import math

def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    return x / y

def potenciacao(x, y):

    return x**y

def raiz(x):

    return math.sqrt(x)


st.title('Calculadora Python')

x = st.number_input("Número um")
y = st.number_input("Número dois")

opcao = st.selectbox(
    'Escolha uma operação:',
    ('Soma', 'Subtração', 'Multiplicação', 'Divisão', 'Potenciação', 'raiz')
)

if st.button('Calcular'):
    if opcao == 'Soma':
        resultado = soma(x, y)
    elif opcao == 'Subtração':
        resultado = subtracao(x, y)
    elif opcao == 'Multiplicação':
        resultado = multiplicacao(x, y)
    elif opcao == 'Divisão':
        resultado = divisao(x, y)
    elif opcao == 'Potenciação':
        resultado = potenciacao(x,y)
    elif opcao == 'raiz':
        resultado = raiz(x)

    st.write('Resultado: ', resultado)