horarios=["lunes(20/05/2024)hora(8:00 AM)","miercoles(22/05/2024)hora(11:00 AM)","viernes(24/05/2024)hora(2:00 PM)"]
while True:
    print("1. horarios disponibles")
    print("2. reservar un horario disponible")
    print("3.pagar alquiler")
    print("4. verificar el horario")
    opcion=input("ingrese una opcion (1/2/3/4): ")
    if opcion=="1":
        print(f"los horarios disponibles son:{horarios} ")
    elif opcion=="2":
        reservar=input("ingrese el horario que quiere reservar: ")
        horarios.append(reservar)
        print("usted reservo el dia", (reservar))
    elif opcion=="3":
        print("debe pagar un monton de $30 por el dia",(reservar))
    elif opcion=="4":
        print("el horario que reservo es",(reservar))
        



