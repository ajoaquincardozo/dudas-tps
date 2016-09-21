
def preparando_lista_a_modificar_inicial(Lista_Niv_predeterminada,nivel):
      lista_nivel=Lista_Niv_predeterminada[nivel-1] 
      lista_a_modificar=Lista_Niv_predeterminada[nivel-1][:]
      for i in range(len(lista_a_modificar)):
        lista_a_modificar[i]=lista_nivel[i][:]


# Lista_Niv_predeterminada=[LN1,LN2,LN3,LN4,LN5]
#LN1=[lista_1,lista_2,lista_3,lista_4,lista_5]
#Lista_1=["O","O","-","O","O"] por ejemplo
#nivel=1 por ej
