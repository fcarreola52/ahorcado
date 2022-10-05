import random
def read():
    palabras=[]
    with open("./data.txt","r", encoding="utf=8") as f: 
        for line in f:
            palabras.extend((line.split()))
    #print(palabras)
    return(palabras)
def run():
    palabras=read()
    chosen_word=palabras[random.randint(0,len(palabras)-1)]
    print(chosen_word)

    
if __name__=='__main__':
    run()