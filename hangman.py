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

def guion_list(chosen_word):#funcion que llena de guiones una lista del tamaño de la palabra elegida
    list2=[]
    for i in range(len(chosen_word)):
        list2.append("_ ")
    return(list2)
def transform(list): #funcion que transforma listas en palabras
    palabra=""
    for i in range(len(list)):
        palabra=palabra+list[i]
    return(palabra)
def replacement(chosen_word): #funcion que cambia los acentos a palabras sin acentos
    chosen_word=chosen_word.replace("á","a")
    chosen_word=chosen_word.replace('é','e')
    chosen_word=chosen_word.replace('í','i')
    chosen_word=chosen_word.replace('ó','o')
    chosen_word=chosen_word.replace('ú','a')
    chosen_word=chosen_word.replace("Á","a")
    chosen_word=chosen_word.replace('É','e')
    chosen_word=chosen_word.replace('Í','i')
    chosen_word=chosen_word.replace('Ó','o')
    chosen_word=chosen_word.replace('Ú','a')
    return(chosen_word)



def ahorcado(list,chosen_word,list2,intentos): #esta funcion compara las listas para ver si la lista 2 que se va actualizando ya es igual a la lista original
    while list != list2:
        list3=list2
        os.system('clear')
        print("Bienvenido al juego del ahorcado")
        print(transform(list2))
        letter=input("ingresa una letra: ")
        letter=replacement(letter)
        letter=letter.upper()
        b=0 #contador para ver si entro al ciclo for 

        try:
            
            for i in range(len(chosen_word)):
                if letter==list[i]:
                    list2[i]=letter
                    b+=1
            if b==0:
                print(f"intentalo de nuevo la letra {letter} no se encuentra en la palabra")
                mensaje2=input("presiona  enter para continuar")
            if len(letter) !=1 or letter==" ":
                raise ValueError
            
        except ValueError:
            print("Rercuerda escribir letras unicamente, numeros y palabras no son validdos, tampoco espacios")
            mensaje=input("presiona  enter para continuar")
        intentos+=1
        
        
    if list==list2:
        os.system('clear')
        print(f"felicidades has ganado la palabra era {chosen_word} te tomo {intentos} intentos")
        


    
def run():
    words=read()
    chosen_word=words[random.randint(0,len(words)-1)]
    chosen_word=replacement(chosen_word)
    chosen_word=chosen_word.upper()    
    list=letter_list(chosen_word)
    list2=guion_list(chosen_word)
    intentos=0
    ahorcado(list,chosen_word,list2,intentos)
    

    
if __name__=='__main__':
    run()