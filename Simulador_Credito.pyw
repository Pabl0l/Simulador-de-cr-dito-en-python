import tkinter as tk
from tkinter import messagebox
import pandas as pd
import csv

# Variable Global para almacenar datos

datos_usuarios = []

# Funciones

def continuar():
    # Obtener los datos de cada Entry
    nombre = inputNombre.get()
    edad = int(inputEdad.get())
    trabajo = inputTrabajo.get()
    ingresos = float(inputIngresos.get())
    meses_trabajando = int(inputMesesTrabajando.get())
    capital = float(inputCapital.get())
    tiempo = int(inputTiempo.get())
    motivoSeleccionado = motivo.get()

    # Lista de campos y sus etiquetas
    campos = [
        (nombre, "Nombre"),
        (edad, "Edad"),
        (trabajo, "Trabajo actual"),
        (ingresos, "Ingresos"),
        (meses_trabajando, "Meses trabajando"),
        (capital, "Cantidad a prestar (Capital)"),
        (tiempo, "Tiempo del préstamo (en meses)")
    ]

    # Verificar si hay campos vacíos
    for valor, etiqueta in campos:
        if not valor:  # Si el campo está vacío
            messagebox.showwarning("Advertencia", f"Por favor ingresa tu {etiqueta}.")
            return  # Salir de la función si falta algún dato

    # Ocultar los widgets existentes
    labelDatosUsuario.grid_forget()
    labelMotivo.grid_forget()
    labelDatosPrestamo.grid_forget()
    botonContinuar.grid_forget()
    botonCancelar.grid_forget()

    # Mostrar el nuevo LabelFrame con el mensaje
    labelMensaje.pack(padx=10, pady=10)

    # Crear un mensaje de saludo con todos los datos ingresados
    mensaje = f"{nombre},\n"
    mensaje += f"Edad: {edad}\n"
    mensaje += f"Trabajo actual: {trabajo}\n"
    mensaje += f"Ingresos: {ingresos}\n"
    mensaje += f"Meses trabajando: {meses_trabajando} meses\n"
    mensaje += f"Capital solicitado: {capital}\n"
    mensaje += f"Tiempo del préstamo: {tiempo} meses\n\n"
    mensaje += f"Motivo: {motivoSeleccionado}\n"

    # Lógica de evaluación según el motivo del préstamo
    apto = False  # Variable para determinar si es apto o no
    l = 0  # Interés
    M = 0  # Cantidad adeudada
    C = 0  # Cuotas mensuales

    if motivoSeleccionado == "Consumo":
        if meses_trabajando > 6:
            l = capital * tiempo * 0.05
            M = capital + l
            C = M / tiempo
            apto = True
        else:
            mensaje += "No aplica para el crédito de consumo.\n"

    elif motivoSeleccionado == "Estudiantil":
        if ingresos > 1602000:
            l = capital * tiempo * 0.02
            M = capital + l
            C = M / tiempo
            apto = True
        else:
            mensaje += "No aplica para el crédito estudiantil.\n"

    elif motivoSeleccionado == "Hipoteca":
        if ingresos > 602000:
            l = capital * tiempo * 0.015
            M = capital + l
            C = M / tiempo
            apto = True
        else:
            mensaje += "No aplica para el crédito hipotecario.\n"

    elif motivoSeleccionado == "Compra Cartera":
        if edad < 40:
            l = capital * tiempo * 0.02
            M = capital + l
            C = M / tiempo
            apto = True
        else:
            mensaje += "No aplica para el crédito de compra de cartera.\n"

    # Si es apto, mostrar los cálculos y guardar los datos
    if apto:
        mensaje += (f"El interés que pagará por el tiempo seleccionado es: {l:.2f}\n"
                    f"La cantidad adeudada es: {M:.2f}\n"
                    f"La cuota mensual por el préstamo es: {C:.2f}\n")

    with open('datos_usuarios.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([nombre, edad, trabajo, ingresos, meses_trabajando, capital, tiempo, motivoSeleccionado, l, M, C])

    # Mostrar el mensaje final en la ventana
    mensajeLabel = tk.Label(labelMensaje, text=mensaje, font=("Time New Roman", 14))
    mensajeLabel.pack(pady=20)
    botonExportar = tk.Button(labelMensaje, text="Exportar a Excel", command=exportar_datos_a_excel)
    botonExportar.pack(pady=5)

def cancelar():
    ventana.destroy()

def exportar_datos_a_excel():
    # Leer el archivo CSV y crear un DataFrame
    df = pd.read_csv('datos_usuarios.csv', header=None, names=['Nombre', 'Edad', 'Trabajo', 'Ingresos', 'Meses Trabajando', 'Capital', 'Tiempo (meses)', 'Motivo', 'Interés', 'Deuda Total', 'Cuota Mensual'])
    
    # Exportar a Excel
    df.to_excel('datos_prestamos.xlsx', index=False)
    print("Datos exportados exitosamente a 'datos_prestamos.xlsx'")


# Creando la ventana principal
ventana = tk.Tk()
ventana.title("Banco XY (Simulador de préstamos)")
ventana.iconbitmap("banco.ico")
ventana.resizable(0,0)


# Creando las ventanas internas y sus elementos
labelDatosUsuario = tk.LabelFrame(ventana, text="Datos personales", bd=2)
labelDatosUsuario.configure(width=300, height=290, font=("Time New Roman", 14, "bold"))
labelMotivo = tk.LabelFrame(ventana, text="Motivo del préstamo", bd=2)
labelMotivo.configure(width=300, height=140, font=("Time New Roman", 14, "bold"))
labelDatosPrestamo = tk.LabelFrame(ventana, text="Datos del préstamo", bd=2)
labelDatosPrestamo.configure(width=300, height=150, font=("Time New Roman", 14, "bold"))

labelMensaje = tk.LabelFrame(ventana, text="Estado del prestamo", bd=2)
labelMensaje.configure(width=300, font=("Time New Roman", 14, "bold"))


# Inputs y labels
labelNombre = tk.Label(labelDatosUsuario, text="Nombre:")
inputNombre = tk.Entry(labelDatosUsuario)

labelEdad = tk.Label(labelDatosUsuario, text="Edad:")
inputEdad = tk.Entry(labelDatosUsuario)

labelTrabajo = tk.Label(labelDatosUsuario, text="Trabajo actual:")
inputTrabajo = tk.Entry(labelDatosUsuario)

labelIngresos = tk.Label(labelDatosUsuario, text="Ingresos:")
inputIngresos = tk.Entry(labelDatosUsuario)

labelMesesTrabajando = tk.Label(labelDatosUsuario, text="Meses trabajando:")
inputMesesTrabajando = tk.Entry(labelDatosUsuario)

labelCapital = tk.Label(labelDatosPrestamo, text="Cantidad a prestar (Capital):")
inputCapital = tk.Entry(labelDatosPrestamo)

labelTiempo = tk.Label(labelDatosPrestamo, text="Tiempo del préstamo (en meses):")
inputTiempo = tk.Entry(labelDatosPrestamo)


# Variables de Control
motivo = tk.StringVar(value=None)
motivo.set("Consumo")


# Opciones de Motivos para el préstamo
radioBotonConsumo = tk.Radiobutton(labelMotivo, text="Consumo", variable=motivo, value="Consumo")
radioBotonHipoteca = tk.Radiobutton(labelMotivo, text="Hipoteca", variable=motivo, value="Hipoteca")
radioBotonEstudiantil = tk.Radiobutton(labelMotivo, text="Estudiantil", variable=motivo, value="Estudiantil")
radioBotonCompraCartera = tk.Radiobutton(labelMotivo, text="Compra Cartera", variable=motivo, value="Compra Cartera")


# Botones
botonContinuar = tk.Button(ventana, text="Continuar", command=continuar)
botonCancelar = tk.Button(ventana, text="Cancelar", command=cancelar)


# Orden de elementos
labelDatosUsuario.pack_propagate(False)
labelDatosUsuario.grid(row=0, column=0, padx=10, pady=10, sticky="n")

labelMotivo.pack_propagate(False)
labelMotivo.grid(row=1, column=0, padx=10, pady=10, sticky="n")

labelDatosPrestamo.pack_propagate(False)
labelDatosPrestamo.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="n")

labelNombre.pack(anchor="w")
inputNombre.pack(fill="x", expand=True, padx=5)

labelEdad.pack(anchor="w")
inputEdad.pack(fill="x", expand=True, padx=5)

labelTrabajo.pack(anchor="w")
inputTrabajo.pack(fill="x", expand=True, padx=5)

labelIngresos.pack(anchor="w")
inputIngresos.pack(fill="x", expand=True, padx=5)

labelMesesTrabajando.pack(anchor="w")
inputMesesTrabajando.pack(fill="x", expand=True, padx=5)

radioBotonConsumo.pack(anchor="w")
radioBotonHipoteca.pack(anchor="w")
radioBotonEstudiantil.pack(anchor="w")
radioBotonCompraCartera.pack(anchor="w")

labelCapital.pack(anchor="w")
inputCapital.pack(fill="x", expand=True, padx=5, pady=5)

labelTiempo.pack(anchor="w")
inputTiempo.pack(fill="x", expand=True, padx=5, pady=5)

botonContinuar.grid(row=2, column=1, sticky="e", padx=5, pady=5)
botonCancelar.grid(row=2, column=2, sticky="e", padx=5, pady=5)


ventana.mainloop()