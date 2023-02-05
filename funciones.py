def listarTarifas(tarifas):
    print("\nSOLICITUDES ACTUALES: \n")
    contador = 1
    for cur in tarifas:
        datos = " id: {0} | Nombre Completo: {1}, Tarifa seleccionada:{2}, ({3} dias) Precio ${4} total a pagar ${5}"
        print(datos.format(cur[0], cur[1], cur[2], cur[3], cur[4], cur[5]))
        #contador = contador + 1
    print(" ")

# ------------------------------------------------------------------------------------------------
def pedirDatosRegistroI():
    

    nombre = input("Ingrese Su Nombre Completo: ")
    tipo_tarifa= input("Ingrese la tarifa selecionada (primera letra) =>")
    dias= int(input("ingrese los dias hospedados => "))
    precio= 2.50
    precio_total=dias*precio
    iva=19/100*precio_total
    total=precio_total+iva
    

    datos = (nombre, tipo_tarifa, dias, precio, total)
    return datos
#------------------------------------------------------------------------------------------------
def pedirDatosRegistroD():
    

    nombre = input("Ingrese Su Nombre Completo: ")
    tipo_tarifa= input("Ingrese la tarifa selecionada (primera letra) =>")
    dias= int(input("ingrese los dias hospedados => "))
    
    precio= 4.60
    precio_total=dias*precio
    iva=19/100*precio_total
    total=precio_total+iva
    descuento = 5/100*total
    total_2= total-descuento
    print("descuento",total_2)
    

    datos = (nombre, tipo_tarifa, dias, precio, total)
    return datos
#------------------------------------------------------------------------------------------------
def pedirDatosRegistroF():
    

    nombre = input("Ingrese Su Nombre Completo: ")
    tipo_tarifa= input("Ingrese la tarifa selecionada (primera letra) =>")
    dias= int(input("ingrese los dias hospedados => "))
    precio= 5.20
    precio_total=dias*precio
    iva=19/100*precio_total
    total=precio_total+iva
    

    datos = (nombre, tipo_tarifa, dias, precio, total)
    return datos
#------------------------------------------------------------------------------------------------



def pedirDatosActualizacion(tarifas):
    listarTarifas(tarifas)
    existeCodigo = False
    codigoEditar = int(input("Ingrese el código de la solicitud a editar: "))
    for cur in tarifas:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre = input("Ingrese el nombre a modificar: ")
        tipo_tarifa= input("Ingrese la tarifa a modificar (primera letra) =>")
        dias= int(input("ingrese los dias hospedados a modificar => "))
    
        precio= 4.60
        precio_total=dias*precio
        iva=19/100*precio_total
        total=precio_total+iva
        descuento = 5/100*total
        total_2= total-descuento
        
    

        datos = (codigoEditar, nombre, tipo_tarifa, dias, precio, total)
        return datos

    else:
        curso = None

    return curso

#-----------------------------------------------------------------------------------------------
def pedirDatosEliminacion(tarifa):
    listarTarifas(tarifa)
    existeCodigo = True
    codigoEliminar = int(input("Ingrese el código de la solicitud a eliminar: "))
    for cur in tarifa:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    # if not existeCodigo:
    #     codigoEliminar = ""

    return codigoEliminar

