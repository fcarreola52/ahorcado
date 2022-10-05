import random
import os
def read():#funcion que lee el archivo y lo guarda en una lista, la funcion regresa la lista
    words=[]
    with open("./data.txt","r", encoding="utf=8") as f: 
        for line in f:
            words.extend((line.split()))
    
    return(words)

def letter_list(chosen_word): #funcion que guarda cada letra del archivo en una lista, la funcion regresa la lista
    list=[]
    for i in chosen_word:
        list.append(i)
    print(list)
    return(list)

def ahorcado(list,chosen_word): 
    os.system('clear')
    print("Bienvenido al juego del ahorcado")
    print(len(chosen_word)*"_ ")
    letter=input("ingresa una letra:")
    
def run():
    words=read()
    chosen_word=words[random.randint(0,len(words)-1)]
    list=letter_list(chosen_word)
    ahorcado(list,chosen_word)
    

    
if __name__=='__main__':
    run()