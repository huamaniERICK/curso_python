# horarios=["lunes(20/05/2024)hora(8:00 AM)","miercoles(22/05/2024)hora(11:00 AM)","viernes(24/05/2024)hora(2:00 PM)"]
# while True:
#     print("1. horarios disponibles")
#     print("2. reservar un horario disponible")
#     print("3.pagar alquiler")
#     print("4. verificar el horario")
#     opcion=input("ingrese una opcion (1/2/3/4): ")
#     if opcion=="1":
#         print(f"los horarios disponibles son:{horarios} ")
#     elif opcion=="2":
#         reservar=input("ingrese el horario que quiere reservar: ")
#         horarios.append(reservar)
#         print("usted reservo el dia", (reservar))
#     elif opcion=="3":
#         print("debe pagar un monton de $30 por el dia",(reservar))
#     elif opcion=="4":
#         print("el horario que reservo es",(reservar))

# El usuario tiene un gras el cual administra de manera manual, el usuario necesita que se automatize el proceso de la reserva y pago del alquiler , para lo cual solicita automatizar los siguientes casos de uso:
# -el usario podra ver la lista  de horarios disponibles
# -el usuario podra reservar en uno de los horarios disponibles
# -el usuario podra pagar por el alquiler de la reserva realizada
# -el usuario podra verificar su alquiler el cual le mostre los detalles como la fecha, hora y costo del alquiler que realizo.
        


horarios_disponibles={
    "lunes 8:00 AM":50,
    "miercoles 10:00 AM":40,
    "viernes 2:00 PM":25
}
reserva_realizada=False
alquiler_realizado=False
while True:
    print("1.horarios disponibles")
    print("2. reservar horario disponibles")
    print("3. pagar alquiler")
    print("4. verificar el horario")
    opcion=input("ingrese el numero de la opcion que desea realizar(1/2/3/4): ")
    if opcion=="1":
        print("horarios disponibles: ")
        for horario, costo in horarios_disponibles.items():
            print(f"{horario}-costo:${costo}")
    elif opcion=="2":
        if not reserva_realizada:
            horario_reserva=input("ingrese el horario que desea reservar: ")
            if horario_reserva in horarios_disponibles:
                reserva_realizada= True
                print(f"reserva realizada para el horario {horario_reserva}")
            else:
                print("horario no valida.por favor elija un horario disponible.")
        else:
            print("ya ha realizado una reserva")
    elif opcion=="3":
        if reserva_realizada and not alquiler_realizado:
            costo_reserva=horarios_disponibles.get(horario_reserva)
            print(f"por favor realize el pago de ${costo_reserva} por el alquiler.")
            alquiler_realizado=True
        elif not reserva_realizada:
            print("primero debe realizar una reserva antes de realizar el pago del alquiler.")
        else:
            print("ya ha realizado el pago del alquiler.")
    elif opcion=="4":
        if alquiler_realizado:
            print(f"detalles de su alquiler - Horario:{horario_reserva}")
            break
        else:
            print("opcion no valida.porfavor , elija una opcion que sea valida.")

    

    


