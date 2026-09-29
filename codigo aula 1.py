import pyautogui
import time

pyautogui.PAUSE = 0.5
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Passo 1: Abrir o site para login
pyautogui.press("win")
pyautogui.write("Microsoft Edge")
pyautogui.press("enter")
pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3) # pyautogui hashtag - ver vídeo
 
# Passo 2: Preencher o formulário de login
pyautogui.click(x=-1187, y=367)  # Clique no campo de email
pyautogui.write("eduardo.anc@proton.me")  # Escreva seu email
pyautogui.press("tab")
pyautogui.write("@Andradeedu11")  # Escreva sua senha
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Abrir a base de dados
import pandas as pd
tabela = pd.read_csv("Produtos.csv")
print(tabela)

# Passo 4: Preencher o formulário de cadastro de produtos
for linha in tabela.index:
    pyautogui.click(x=-1239, y=251)
    codigo = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo)       
    pyautogui.press("tab")
    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")
    preco = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    pyautogui.press("tab")
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")      
    observacao = str(tabela.loc[linha, "obs"])
    if observacao != "nan":
        pyautogui.write(observacao)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("home")