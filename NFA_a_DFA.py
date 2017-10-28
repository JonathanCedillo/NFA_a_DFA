#Equipo
#Alejandro Cámara Martínez      A01370909
#Jonathan Samuel Cedillo Belmán A01377844

from itertools import chain,combinations

nombreArchivo = input("Dame el nombre del archivo: ");

try:
    archivo = open(nombreArchivo,"r");
    NFA = archivo.read();
    archivo.close()
    # SEPARAR LAS TRANSICIONES DEL NFA
    NFA = NFA[2:]
    NFA = NFA[:(len(NFA)-2)]
    NFA = NFA.split("),(");
    estadosNFA = set();
    transNFA = []
    #print("NFA COMPLETO\n",NFA)

    # OBTENER ESTADOS NFA
    for trans in NFA:
        transTemp = trans.split(",")
        transNFA.append(transTemp)
        for estado in transTemp:
            estadosNFA.add(transTemp[1]);
    #print("CONJUNTO DE ESTADOS DEL NFA: ",estadosNFA)
    #print("LISTA DE TRANSCISIONES DEL NFA: ", transNFA)

    # OBTENER CONJUNTO POTENCIA
    listaEstados = list(estadosNFA);
    conjPotencia = list((chain.from_iterable(combinations(listaEstados, n) for n in range (len(listaEstados) + 1))))
    #print("CONJUNTO POTENCIA: ",conjPotencia)

    # TRANSICIONES DEL CONJUNTO VACIO
    transDFA = ["0,,","1,,"]

    isNumber = False;
    # DETERMINAR ALFABETO
    if (transNFA[0][0] == "0" or transNFA[0][0] == "1"):
        isNumber = True;

    # CREAR TRANSICIONES BÁSICAS
    for estado in estadosNFA:
        strCaso0 = ""
        strCaso1 = ""

        for trans in transNFA:
            if estado == trans[1]:  #SI CORRESPONDE LA TRANSICIÓN
                if (trans[0] == "0" or trans[0] == "a"):
                    strCaso0 = strCaso0+trans[2];

                elif (trans[0] == "1" or trans[0] == "b"):
                    strCaso1 = strCaso1 + trans[2];

        if (isNumber):
            transDFA.append("0," + estado + "," + strCaso0);
            transDFA.append("1," + estado + "," + strCaso1);
        else:
            transDFA.append("a," + estado + "," + strCaso0);
            transDFA.append("b," + estado + "," + strCaso1);

    # COMBINACIONES DE ESTADOS DEL CONJUNTO POTENCIA
    for elemento in conjPotencia[(len(estadosNFA)+1):]:
        strCombinacion = "";
        strResComb0 = "";
        strResComb1 = "";
        conjTemp0 = set();
        conjTemp1 = set();

        for n in range(len(elemento)):
            strCombinacion = strCombinacion +elemento[n]

            for trans in transDFA[2:]:
                transSplit = trans.split(",")

                if (elemento[n] == transSplit[1]):  # SI CORRESPONDE LA TRANSICIÓN
                    if (transSplit[0] == "0" or transSplit[0] == "a"):
                        conjTemp0.add(transSplit[2])

                    elif (transSplit[0] == "1" or transSplit[0] == "b"):
                        conjTemp1.add(transSplit[2])

        # CONCATENAR UNIONES
        for x in conjTemp0:
            strResComb0 = strResComb0 + x
        for x in conjTemp1:
            strResComb1 = strResComb1 + x

        # AGREGAR TRANSICIONES A LA LISTA DE TRANSICIONES DEL DFA
        if (isNumber):
            transDFA.append("0," + strCombinacion + "," + strResComb0);
            transDFA.append("1," + strCombinacion + "," + strResComb1);
        else:
            transDFA.append("a," + strCombinacion + "," + strResComb0);
            transDFA.append("b," + strCombinacion + "," + strResComb1);

    # ESCRIBIR ARCHIVO DE SALIDA

    salida = open("outputDFA.txt","w");
    for transicion in range(0,len(transDFA)):
        if (transicion == 0):
            salida.write("{("+transDFA[transicion]+")\n")
        elif (transicion != len(transDFA)-1):
            salida.write("("+transDFA[transicion]+"),\n")
        else:
            salida.write("(" + transDFA[transicion]+ ")}\n")
    salida.close()

except FileNotFoundError:
        print("No encuentro el archivo");