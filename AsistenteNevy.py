from tkinter import *  # se importa toda la libreria
import os
import sys
import time
from datetime import date
import pyttsx3
import getpass
import subprocess32
import subprocess
from tqdm.auto import tqdm
import cv2
import uuid
import serial
from tkinter import messagebox as MessageBox
import time
import socket  # Importamos la librería socket para poder comunicarnos con nuestro ESP8266
import plyer.platforms.win.notification
from plyer import notification
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os import remove
from ctypes import windll, byref
from ctypes.wintypes import DWORD
from socket import gethostbyname, create_connection, error
import threading
import webbrowser
import speech_recognition as sr
import serial 

# Configuracion de la voz del asistente
usuario = getpass.getuser()
engine = pyttsx3.init()
voices = engine.getProperty('voices')  # a voices se le carga un vector con la información de todas las voces
# getPropierty es para obtener información de algo, ya sea el volumen o la velocidad con que habla
engine.setProperty('voice', voices[0].id)  # setProperty es para cambiar una propiedad, ya sea voz o volumen
volume = engine.getProperty('volume')  # para obtener el volumen actual
engine.setProperty('volume', volume + 0.1)  # cambiar el volumen
rate = engine.getProperty('rate')  # para obtener la velocidad actual
engine.setProperty('rate', rate - 15)  # cambiar la velocidad con que habla
notification.notify(  # Notifcación de inicio de la aplicación
	title = "Notificación",
	message = "Sistema iniciando ",
	app_icon = "LogoNevy.ico",
	timeout = 3, )

# Inicio de saludo, depende de la hora en la que se ejecute el programa
try:
	hora = time.strftime("%H")  # se obtiene la hora, el formato "%H" define que es de 24 horas
	if int(hora) >= 0 and int(hora) <= 12:
		notification.notify(
			title = "Notificación",
			message = "Bienvenido" " " + usuario,
			app_icon = "LogoNevy.ico",
			timeout = 2, )
		engine.say('Buenos días')
		engine.say("Bienvenido, soy tu asistente virtual")
		engine.say("")
		engine.runAndWait()

	if int(hora) >= 13 and int(hora) <= 17:
		notification.notify(
			title = "Notificación",
			message = "Bienvenido" " " + usuario,
			app_icon = "LogoNevy.ico",
			timeout = 2, )

		engine.say("Bienvenido  soy su asistente personal")
		print("Bienvenido", usuario)
		engine.say('Buenas tardes')
		engine.runAndWait()

	if int(hora) >= 18 and int(hora) <= 24:
		notification.notify(

			title = "Notificación",
			message = "Bienvenido" " " + usuario,
			app_icon = "LogoNevy.ico",
			timeout = 2, )

		print("Bienvenido ", usuario)
		engine.say("Bienvenido soy su asistente personal")
		engine.say('Buenas noches')
		engine.runAndWait()
		time.sleep(0.2)
		engine.say('¿ en que puedo ayudarle?')
		engine.runAndWait()
except:
	pass

engine.say("Por favor espere mientras cargo los archivos")
engine.runAndWait()

ventana = Tk()
ventana.title("Nevy")
ventana.geometry("1150x600")
ventana.resizable(0, 0)
ventana.config(bg = "#572364")
ventana.iconbitmap(r"LogoNevy.ico")
notification.notify(
	title = "Notificación",
	message = "Asistente Nevy listo para trabajar con tigo" " " + usuario,
	app_icon = "LogoNevy.ico",
	timeout = 2, )
engine.say("Su asistente cargó correctamente todos los archivos")
engine.runAndWait()
Noty = PhotoImage(file = "Notificacion.png")

# -------------Herramientas de Google----------------------
def VerGoogle():
	try:

		engine.say("Ejecutando Navegador")
		engine.runAndWait()
		webbrowser.open("http://www.Google.com", new = 2, autoraise = True)
		notification.notify(
			title = "Notificación",
			message = "Tarea realizada con éxito ",
			app_icon = "LogoNevy.ico",
			timeout = 3, )
	except:
		engine.say("Error al ingresar, ruta no encontrada")
		engine.runAndWait()


def VerYoutube():
	try:
		engine.say("Accediendo a Youtube")
		engine.runAndWait()
		webbrowser.open("http://www.Youtube.com", new = 2, autoraise = True)
		notification.notify(
			title = "Notificación",
			message = "Tarea realizada con éxito ",
			app_icon = "LogoNevy.ico",
			timeout = 3, )
	except:
		engine.say("Error al ingresar ruta no encontrada")
		engine.runAndWait()


def Busqueda():
	try:
		engine.say("Realizando la busqueda ")
		engine.runAndWait()
		Busqueda1.get()

		if Busqueda1.get() == "":
			MessageBox.showinfo("Aviso de actividad ", "No hay nada por buscar")
		else:
			webbrowser.open("https://www.google.com/search?q=" + Busqueda1.get(), new = 2, autoraise = True)
			textBusq.delete(0, END)
			notification.notify(

				title = "Notificación",
				message = "Tarea realizada con éxito ",
				app_icon = "LogoNevy.ico",
				timeout = 3, )
	except:
		engine.say("Error al ingresar, ruta no encontrada")
		engine.runAndWait()


# ------------LIMPIAR--------------
def Limpiar():
	lstMaterias.delete(0, END)
	engine.say("Limpiando la lista")
	engine.runAndWait()
	MessageBox.showinfo("Aviso de actividad ", "Acción realizada excitosamente")


# ////////////////PARA LA MUSICA////////////////////////////////////////

def VerMusica():
	lstMaterias.delete(0, END)
	home = os.environ['USERPROFILE']
	carpetas = os.listdir(home)
	ruta = home + "\\Music"
	archivos = os.listdir(ruta)
	for i in range(len(archivos)):
		lstMaterias.insert(END, (str(i) + ')' + str(archivos[i])))


def AsistenteVersion():
	engine.say("Ingresando a los datos de Nevy")
	engine.runAndWait()
	lstMaterias.delete(0, END)
	lstMaterias.insert(0, "Version 2.0\n")
	lstMaterias.insert(1, "_______________________________________________________")
	lstMaterias.insert(2, "Creador: Alex Ochoa ")
	lstMaterias.insert(3, "Aun es desarrollo")
	lstMaterias.insert(4, "Mejoras en el rendimiento")
	lstMaterias.insert(5, "Apaciencia mas amigable")
	lstMaterias.insert(6, "_______________________________________________________")


def ReproducirMusica():
	engine.say("Ejecutando Musica")
	engine.runAndWait()
	home = os.environ['USERPROFILE']
	carpetas = os.listdir(home)
	ruta = home + "\\Music"
	archivos = os.listdir(ruta)
	try:
		for i in range(len(archivos)):
			ejecutar = ruta + '\\' + archivos[(entrada.get())]
			try:
				os.startfile(ejecutar)
				notification.notify(
				title = "Notificación",
				message = "Tarea realizada con éxito ",
				app_icon = "LogoNevy.ico",
				timeout = 3, )


			except:
				subprocess32.Popen(ejecutar, shell = True)
				notification.notify(
				title = "Notificación",
				message = "Tarea realizada con éxito ",
				app_icon = "LogoNevy.ico",
				timeout = 3, )
			break
			textMateria.delete(0, END)
	except:
		engine.say("Error esta fuera de rango")
		engine.runAndWait()
		MessageBox.showinfo("Aviso de actividad ", "Opción fuera de rango")


# ///////////////////////CODIGO PARA LOS DOCUMENTOS///////////////////////////////

def VerDocumentos():
	lstMaterias.delete(0, END)
	home = os.environ['USERPROFILE']
	carpetas = os.listdir(home)
	ruta = home + "\\Documents"
	archivos = os.listdir(ruta)
	for i in range(len(archivos)):
		lstMaterias.insert(END, (str(i) + ')' + str(archivos[i])))

def ReproducirDocumentos():
	engine.say("Ejecutando Documentos")
	engine.runAndWait()
	home = os.environ['USERPROFILE']
	carpetas = os.listdir(home)
	ruta = home + "\\Documents"
	archivos = os.listdir(ruta)
	try:
		for i in range(len(archivos)):

			ejecutar = ruta + '\\' + archivos[int(entrada.get())]
			os.startfile(ejecutar)
			notification.notify(
				title = "Notificación",
				message = "Tarea realizada con éxito ",
				app_icon = "LogoNevy.ico",
				timeout = 3, )
			break
			textMateria.delete(0, END)

	except:
		engine.say("Error esta fuera de la Opción")
		engine.runAndWait()
		MessageBox.showinfo("Aviso de actividad ", "Opción fuera de rango")


# ////////////////////PARA EL ESCRITORIO//////////////////////////////////////

def VerEscritorio():
	lstMaterias.delete(0, END)
	home = os.environ['USERPROFILE']
	carpetas = os.listdir(home)
	ruta = home + "\\Desktop"
	archivos = os.listdir(ruta)
	for i in range(len(archivos)):
		lstMaterias.insert(END, (str(i) + ')' + str(archivos[i])))


def ReproducirEscritorio():
	engine.say("Ejecutando Acciónes ")
	engine.runAndWait()
	home = os.environ['USERPROFILE']
	carpetas = os.listdir(home)
	ruta = home + "\\Desktop"
	archivos = os.listdir(ruta)
	try:
		for i in range(len(archivos)):
			ejecutar = ruta + '\\' + archivos[int(entrada.get())]
			os.startfile(ejecutar)
			notification.notify(
				title = "Notificación",
				message = "Tarea realizada con éxito ",
				app_icon = "LogoNevy.ico",
				timeout = 3, )
			break
			textMateria.delete(0, END)

	except:
		engine.say("Error, esta fuera de las opciones")
		engine.runAndWait()
		MessageBox.showinfo("Aviso de actividad ", "Opción fuera de rango")

lblMateria = Label(ventana, text = "Listado de Archivos encontrados:", fg = "black", bg = "#ffff00", justify = "right",font = ("Helvética", 10)).place(x = 50, y = 150)
# creando lista

lstMaterias = Listbox(ventana, width = 50, height = 20, bg = "#FFFFFF")
# lstMaterias.insert(1,"Hola")
lstMaterias.place(x = 50, y = 200)
# Scrollbar(lstMaterias, orient="vertical")

# ************************CODIGO PARA LA MUSICA **********************************************************************
lblMat      = Label(ventana, text = "Ingrese un dato", bg = "#ffff00").place(x = 3, y = 90)
entrada     = IntVar()
textMateria = Entry(ventana, textvariable = entrada, width = 25, bg = "#F4DECB")
textMateria.place(x = 93, y = 92)
# ////////////////////////Musica////////////////////////////////////////////
lblMat     = Label(ventana, text = "MUSICA", fg = "black", bg = "#ffff00", justify = "right",font = ("Helvética", 10)).place(x = 290, y = 10)
btnBuscar  = Button(ventana, text = "Ver Musica", bg = "#F4DECB", height = 2, width = 15, command = VerMusica).place(x = 256, y = 40)
btnAgregar = Button(ventana, text = "Reproducir Musica", bg = "#F4DECB", height = 2, width = 15,command = ReproducirMusica).place(x = 255, y = 90)
# ********************CODIGO PARA LOS DOCUMENTOS****************************************************************
lblMat     = Label(ventana, text = "DOCUMENTOS", fg = "black", bg = "#ffff00", justify = "right", font = ("Helvética", 10)).place(x = 445, y = 10)
btnBuscar  = Button(ventana, text = "Ver Documentos", bg = "#F4DECB", height = 2, width = 15,command = VerDocumentos).place(x = 425, y = 40)
btnAgregar = Button(ventana, text = "Abrir Documentos", bg = "#F4DECB", height = 2, width = 15,command = ReproducirDocumentos).place(x = 425, y = 90)
# ********************CODIGO PARA EL ESCRITORIO******************************************************************
lblMat     = Label(ventana, text = "ESCRITORIO", fg = "black", bg = "#ffff00", justify = "right",font = ("Helvética", 10)).place(x = 600, y = 10)
btnBuscar  = Button(ventana, text = "Ver Escritorio", bg = "#F4DECB", height = 2, width = 15,command = VerEscritorio).place(x = 580, y = 40)
btnAgregar = Button(ventana, text = "Abrir Escritorio", bg = "#F4DECB", height = 2, width = 15,command = ReproducirEscritorio).place(x = 580, y = 90)
# *********************************LIMPIAR*******************************************************************
lblMat     = Label(ventana, text = "LIMPIAR", fg = "black", bg = "#ffff00", justify = "right", font = ("Helvética", 10)).place(x = 50, y = 10)
btnAgregar = Button(ventana, text = "Limpiar", bg = "#F4DECB", height = 2, width = 5, command = Limpiar).place(x = 55,y = 40)
# ------------------GOOGLE---------------------------------------
lblMat     = Label(ventana, text = "Herramientas de Google", fg = "black", bg = "#ffff00", justify = "right",font = ("Helvética", 10)).place(x = 730, y = 10)
btnBuscar  = Button(ventana, text = "Navegar Google", bg = "#F4DECB", height = 2, width = 15, command = VerGoogle).place(x = 730, y = 40)
btnAgregar = Button(ventana, text = "Abrir Youtube", bg = "#F4DECB", height = 2, width = 15,command = VerYoutube).place(x = 730, y = 90)
Busque     = Label(ventana, text = "¿Que desea buscar en Google?", fg = "black", bg = "#ffff00", justify = "right", font = ("Helvética", 10)).place(x = 900, y = 10)
Busqueda1  = StringVar()
textBusq   = Entry(ventana, textvariable = Busqueda1, width = 25, bg = "#F4DECB")
textBusq.place(x = 920, y = 40)
btnAgregar = Button(ventana, text = "Realizar Busqueda", bg = "#F4DECB", height = 2, width = 15,command = Busqueda).place(x = 940, y = 65)


# Contol de version -
lblMat = Label(ventana, text = "Datos Asistente", fg = "black", bg = "#ffff00", justify = "right",font = ("Helvética", 10)).place(x = 120, y = 10)

btnVersion = Button(ventana, text = "Version", bg = "#F4DECB", height = 2, width = 6, command = AsistenteVersion).place(x = 140, y = 40)


def agregar():
	# ESCRIBIR EL FICHERO
	archivo = open("datosDeEnvio.txt", "a")
	palabra = (datosDeEnvio2.get())
	archivo.write("El usuario dice:" + palabra + '\n')
	archivo.close()
	engine.say("registrando")
	engine.runAndWait()

	if datosDeEnvio2.get() == "":
		engine.say("No se puede enviar un mensaje en blanco")
		engine.runAndWait()

	else:

		msg = MIMEMultipart()
		password = "Ingresa Tu contraseña"
		msg['From'] = "Correo electronico"
		msg['To'] = "Correo electronico"
		msg['Subject'] = "Nevy Asistente"
		msg.attach(MIMEText(open('datosDeEnvio.txt').read()))

		try:
			server = smtplib.SMTP('smtp.gmail.com:587')
			server.starttls()
			server.login(msg['From'], password)
			server.sendmail(msg['From'], msg['To'], msg.as_string())
			server.quit()
			MessageBox.showinfo("Mensaje enviado correctamente", "!!!Gracias por informarnos¡¡¡ ")
			engine.say("Tu mensaje se ah enviado correctamente")
			engine.runAndWait()
		except:
			MessageBox.showwarning("ERROR DE ENVIO", "SE GENERO UN ERROR DE ENVIO")
			engine.say("Se genero un error de envío")
			engine.runAndWait()

		archivo = open("datosDeEnvio.txt", "w")
		archivo.close()
		remove("datosDeEnvio.txt")
		Envio.delete(0, END)


lblMat2 = Label(ventana, text = "Puedo resolver su problema", bg = "#ffff00").place(x = 90, y = 530)
datosDeEnvio2 = StringVar()
Envio = Entry(ventana, textvariable = datosDeEnvio2, width = 30, bg = "#F4DECB")
Envio.place(x = 80, y = 560)
Notyficacion = Button(ventana, image = Noty, command = agregar, height = 50, width = 50).place(x = 10,
																							   y = 540)  # LUS LCP ENCENDIDO



ventana.mainloop()
'''
	Este es el asistente nevy en su version 2.0 me llevo aproximadamente 1 año poder desarrollar esta versión, esta pensado en ayudar a gestionar
	los archivos de la computadora, tiene parte del codigo comentado ya que se utiliza para la automatización si desean esa parte del codigo y completar todo 
	pueden escribirme al siguiente correo nevyproyec@gmail.com 
	les dejo tambien mi canal de YouTube donde estare compartiendo la versión 3 de nevy https://www.youtube.com/channel/UCeOIAAOu3pKjsh9hqdZpRJg


	Si quieres apoyarme con la creación de nevy le dejo mi cuenta de paypal https://www.paypal.com/paypalme/AlexOchoaNevy 
	cualquier donación sera bienvenida y muchas gracias por ayudar con la creación de nevy 


'''