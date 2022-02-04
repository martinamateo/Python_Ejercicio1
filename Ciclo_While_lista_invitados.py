
# Mientras los invitados a un evento van llegando, se dividen en tres listas: invitados, Asistentes y Ausentes. 
# Mientras la lista de invitados no se complete el ciclo while no se cierra, salvo que se coloque "FIN".
# Por ultimo, muestra cuantas personas hay en cada lista.

invitados=['Marcelo', 'Jose', 'Micaela', 'Lia','Mariana', 'Pablo', 'Facundo', 'Daniel', 'Abril', 'Martina']
Asistentes=[]

while len(invitados) > 0:
    nombre= input("Ingresar nombre o ingresar <FIN> para finalizar: ")
    if (nombre == 'FIN'): 
        break
    elif nombre in invitados:
        print("Puede ingresar al salón") 
        Asistentes.append(nombre)  
        invitados.remove(nombre)  
    else:
        print("No puede ingresar al salón")

print('Numero de invitados: ',(len(Asistentes) + len(invitados)))
print('Numero de Asistentes: ', len(Asistentes))  
print('Numero de Ausentes: ', len(invitados))   