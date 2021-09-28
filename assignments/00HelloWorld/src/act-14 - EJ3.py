def main():
    #escribe tu código abajo de esta línea
    n=int(input('Total de datos a capturar: '))

    lista =[]

    for i in range(n):
        dato = int(input('>>>'))
        lista.append(dato)

    print(lista)

    listacuadrados=[]

    for i in range(n):
        listacuadrados.append(lista[i]**2)

    print(listacuadrados)



if __name__=='__main__':
    main()
