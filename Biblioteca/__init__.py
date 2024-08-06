#Importaciones de las librerias
from tkinter import Tk
import tkinter as tk
from tkinter import Frame
from tkinter import Button, filedialog,Label

#Importando las otras clases 
from Libros import Libros
from Usuarios import Usuarios
from Morosidad import Morosidad
from Prestamos import Prestamos


class Interfaz:
    #Varibles que contienen los metodos de las ventanas de las otras clases
    guardar_libros = Libros.guardar_libros
    ventana_prestamos = Prestamos.ventana_Prestamo
    ventana_morosidad = Morosidad.ventana_Morosidad
    ventana_usuarios = Usuarios.ventana_Usuarios
    ventana_libros = Libros.ventana_Libros

    #Estructura y componentes de la Ventana principal del Programa
    def ventana_Principal(self,root):
        self.ventana_principal = root
        self.ventana_principal.title("Gestion de Biblioteca")
        self.ventana_principal.geometry("%dx%d+%d+%d" % (700,500,360,120))
        self.ventana_principal.resizable(0,0)

        p_Frame = Frame(self.ventana_principal)
        p_Frame.pack(side = "top")
        p_Frame.place(width= "900", height ="500")
        p_Frame.config(bg = "black")

        label_titulo = Label(p_Frame, text = "Gestion de Biblioteca",font=("Modern", 28), foreground= "white")
        label_titulo.pack()
        label_titulo.config(bg= "black")
        label_titulo.place(x = 200, y = 110 , width= 300, height= 50)

        button_libros = Button(p_Frame, text="Libros", command= self.ventana_libros,font=("Modern", 16), foreground = "white", highlightthickness=2)
        button_libros.pack()
        button_libros.config(bg = "black")
        button_libros.place(x = 95,y = 250,width= 100, height  = 40)


        button_usuarios = Button(p_Frame, text="Usuarios", command=self.ventana_usuarios,font=("Modern", 16), foreground = "white", highlightthickness=2)
        button_usuarios.pack()
        button_usuarios.config(bg = "black")
        button_usuarios.place(x = 195,y = 250, width= 100, height  = 40 )

        button_prestamo = Button(p_Frame, text="Prestamos",font=("Modern", 16), command= self.ventana_prestamos, foreground = "white", highlightthickness=2)
        button_prestamo.pack()
        button_prestamo.config(bg = "black")
        button_prestamo.place(x =295,y= 250, width= 100, height  = 40)

        button_utilidades = Button(p_Frame, text="Abrir Archivo",font=("Modern", 16), foreground = "white", highlightthickness=2)
        button_utilidades.pack()
        button_utilidades.config(bg = "black")
        button_utilidades.place(x =395, y = 250, width= 120, height  = 40)

        button_morosidad = Button(p_Frame, text="Morosidad", command= self.ventana_morosidad,font=("Modern", 16), foreground = "white", highlightthickness=2)
        button_morosidad.pack()
        button_morosidad.config(bg = "black")
        button_morosidad.place(x =510, y = 250, width= 100, height  = 40)
        self.ventana_principal.mainloop()

    def regresar(self,ventana):
        
        self.ventana_principal.deiconify()
        ventana.destroy()


if __name__ == "__main__":
    app = Interfaz()
    root = tk.Tk()
    app.ventana_Principal(root)
