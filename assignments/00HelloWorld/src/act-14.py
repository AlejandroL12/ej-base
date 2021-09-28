def main():
    #escribe tu código abajo de esta línea
    n=0
    while n<=0:
        n=int(input('Numero de datos que ingresar: '))
    
        l=[]

    for i in range(n):
        dato=int(input(f'Dame el dato: {i}'))
        l.append(dato)

    for i in range(n):
        print(f'Lista[{i}]={l[i]}')

if __name__=='__main__':
    main()
