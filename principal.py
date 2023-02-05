from bd.conexion import DAO
import funciones


def menuPrincipal():
    continuar = True
    while(continuar):
        opcionCorrecta = False
        while(not opcionCorrecta):
            print("====================   MENÚ PRINCIPAL HOTEL WC   ====================")
            print("=========TARIFAS DISPONIBLES==========")
            print("1.-INDIVIDUAL( 1 persona ) ")
            print("2.-DOBLE( parejas ) ")
            print("3.- FAMILIAR ( mas de 4 personas )")
            print()
            print()
           
            print("- ======= FUNCIONES O CONSULTAS==========")
            print("4.- CONSULTAR TARIFA")
            print("5.- ACTUALIZAR TARIFA")
            print("6.- CANCELAR TARIFA")
            print("7.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una tarifa: "))

            if opcion < 1 or opcion > 7:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 7:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)


def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        datos= funciones.pedirDatosRegistroI()
        try:
            dao.registrarTarifa(datos)
        except:
            print("Ocurrió un error...")
 # --------------------------------------------------------------------------------
    elif opcion == 2:
        datos= funciones.pedirDatosRegistroD()
    
        try:
            dao.registrarTarifa(datos)
        except:
            print("Ocurrió un error...")
#--------------------------------------------------------------------------------
            
    elif opcion == 3:
        datos= funciones.pedirDatosRegistroF()
    
        try:
            dao.registrarTarifa(datos)
        except:
            print("Ocurrió un error...")
            #--------------------------------------------------------------------------------
            
    elif opcion == 4:
         try:
             tarifas = dao.listarTarifas()
             if len(tarifas) > 0:
                 funciones.listarTarifas(tarifas)
             else:
                 print("No se encontraron cursos...")
         except:
             print("Ocurrió un error...")
            #--------------------------------------------------------------------------------
    elif opcion == 5:
        try:
            tarifas = dao.listarTarifas()
            if len(tarifas) > 0:
                tarifa = funciones.pedirDatosActualizacion(tarifas)
                if tarifa:
                    dao.actualizarTarifa(tarifa)
                else:
                    print("Código de curso a actualizar no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 6:
        try:
            tarifas = dao.listarTarifas()
            if len(tarifas) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(tarifas)
                if not(codigoEliminar ==""):
                    dao.eliminarTarifa(codigoEliminar)
                else:
                    print("Código de curso no encontrado...\n")
            else:
                print("No se encontraron cursos...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")


menuPrincipal()