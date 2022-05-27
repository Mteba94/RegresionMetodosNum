# RegresionMetodosNum

Programa que proyecta los precios del combustible de Guatemala del año 2018 al 2022

Ejecutar proyecto.py instala todas las librerias requeridas y el programa se encargara de actualizar la informacion, borrara todos los documentos existentes y descargara directamente de la pagina donde se extrae la informacion actualizada,

Utiliza las siguiente librerias:
Pandas = utilizada para extraer informacion, crear el dataframe del pdf descargado.
Requests = peticion HTTP a la pagina donde extraemos la informacion.
Os = utilizada para poder eliminar la informacion (Data) anteriormente descargada con nuestro codigo.
Tabula = Necesaria para poder converitir el PDF a excel o csv, poder leerlo y extraer lo necesario.
Matplotlib = Utilizada para poder mostrar la informacion por medio de graficas con pyplot.
Openpyxl = Manipula la informacion de excel, se puede eliminar columnas, agregar, modificar filas, campos, etc.
cProfile = se utilizo para poder cambiar el tipo de letra de la grafica.
