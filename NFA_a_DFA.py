#Equipo
#Alejandro Cámara Martínez      A01370909
#Jonathan Samuel Cedillo Belmán A01377844

nombreArchivo = input("Dame el nombre del archivo: ");
try:
    archivo = open(nombreArchivo,"r");
    lineas = archivo.read();
    lineas = lineas.split("\n");
    archivo.close()

    salidaTemp = open("outputTemp.txt", "w")
    salidaTemp.close()

    # GUARDAR SALIDAS EN UN OUTPUT.TXT
    salidaTemp = open("outputTemp.txt", "r");
    cnf = open("instance_3SAT_Output.txt","w");

    final = salidaTemp.read()
    final = final.split("\n")

    salidaTemp.close()
    cnf.close()

except FileNotFoundError:
        print("No encuentro el archivo");