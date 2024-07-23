from tkinter import Tk
import tkinter as tk
from tkinter import Frame
from tkinter import Button, filedialog,Label


class Interfaz:

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

        button_libros = Button(p_Frame, text="Libros", command= self.ventana_Libros,font=("Modern", 16), foreground = "white", highlightthickness=2)
        button_libros.pack()
        button_libros.config(bg = "black")
        button_libros.place(x = 95,y = 250,width= 100, height  = 40)


        button_usuarios = Button(p_Frame, text="Usuarios", command=self.ventana_Usuarios,font=("Modern", 16), foreground = "white", highlightthickness=2)
        button_usuarios.pack()
        button_usuarios.config(bg = "black")
        button_usuarios.place(x = 195,y = 250, width= 100, height  = 40 )

        button_prestamo = Button(p_Frame, text="Prestamos",font=("Modern", 16), foreground = "white", highlightthickness=2)
        button_prestamo.pack()
        button_prestamo.config(bg = "black")
        button_prestamo.place(x =295,y= 250, width= 100, height  = 40)

        button_utilidades = Button(p_Frame, text="Utilidades",font=("Modern", 16), foreground = "white", highlightthickness=2)
        button_utilidades.pack()
        button_utilidades.config(bg = "black")
        button_utilidades.place(x =395, y = 250, width= 100, height  = 40)

        button_morosidad = Button(p_Frame, text="Morosidad",font=("Modern", 16), foreground = "white", highlightthickness=2)
        button_morosidad.pack()
        button_morosidad.config(bg = "black")
        button_morosidad.place(x =495, y = 250, width= 100, height  = 40)
        self.ventana_principal.mainloop()

    # Estructura y componentes de la ventana de libros
    def ventana_Libros(self):

        self.ventana_principal.iconify()
        self.ventana_libros = tk.Toplevel()
        self.ventana_libros.title("Gestionando Libros")
        self.ventana_libros.geometry("%dx%d+%d+%d" % (500, 300, 450, 220))
        self.ventana_libros.resizable(0, 0)

        libros_Frame = Frame(self.ventana_libros)
        libros_Frame.pack(side="top")
        libros_Frame.place(width="500", height="300")
        libros_Frame.config(bg="black")

        label_nombre = Label(libros_Frame, text="Titulo del Libro", font=("Modern", 12), foreground="white")
        label_nombre.pack()
        label_nombre.config(bg="black")
        label_nombre.place(x=20, y=40, width=200, height=20)

        entrada_nombre = tk.Entry(libros_Frame)
        entrada_nombre.pack()
        entrada_nombre.place(x = 200, y = 40, width = 160, height = 20)

        label_autor = Label(libros_Frame, text="Nombre del Autor", font=("Modern", 12), foreground="white")
        label_autor.pack()
        label_autor.config(bg="black")
        label_autor.place(x=20, y=70, width=200, height=20)

        entrada_autor = tk.Entry(libros_Frame)
        entrada_autor.pack()
        entrada_autor.place(x= 200, y=70, width=160, height=20)

        label_isbn = Label(libros_Frame, text="Ingrese el ISBN del libro", font=("Modern", 12), foreground="white")
        label_isbn.pack()
        label_isbn.config(bg="black")
        label_isbn.place(x=20, y=100, width=200, height=20)

        entrada_isbn = tk.Entry(libros_Frame)
        entrada_isbn.pack()
        entrada_isbn.place(x=200, y=100, width=160, height=20)

        button_guardar = Button(libros_Frame, text="Guardar Libro", font=("Modern", 12), foreground="white",highlightthickness=2)
        button_guardar.pack()
        button_guardar.config(bg="black")
        button_guardar.place(x=370, y=100, width=110, height=20)

        label_eliminar = Label(libros_Frame, text="Ingrese el ISBN", font=("Modern", 12), foreground="white")
        label_eliminar.pack()
        label_eliminar.config(bg="black")
        label_eliminar.place(x=20, y=180, width=200, height=20)

        entrada_eliminar = tk.Entry(libros_Frame)
        entrada_eliminar.pack()
        entrada_eliminar.place(x=200, y=180, width=160, height=20)

        button_eliminar = Button(libros_Frame, text="Eliminar Libro", font=("Modern", 12), foreground="white", highlightthickness=2)
        button_eliminar.pack()
        button_eliminar.config(bg="black")
        button_eliminar.place(x=370, y=180, width=110, height=20)

        label_buscar = Label(libros_Frame, text="Ingrese el Título", font=("Modern", 12), foreground="white")
        label_buscar.pack()
        label_buscar.config(bg="black")
        label_buscar.place(x=20, y=220, width=200, height=20)

        entrada_buscar = tk.Entry(libros_Frame)
        entrada_buscar.pack()
        entrada_buscar.place(x=200, y=220, width=160, height=20)

        button_buscar = Button(libros_Frame, text="Buscar Libro", font=("Modern", 12), foreground="white", highlightthickness=2)
        button_buscar.pack()
        button_buscar.config(bg="black")
        button_buscar.place(x=370, y=220, width=110, height=20)

        button_regresar = Button(libros_Frame, text="Regresar", command= self.regresar, font=("Modern", 12), foreground="white", highlightthickness=2)
        button_regresar.pack()
        button_regresar.config(bg="black")
        button_regresar.place(x=370, y=265, width=110, height=20)

        self.ventana_libros.mainloop()

    def ventana_Usuarios(self):

        self.ventana_principal.iconify()
        self.ventana_usuarios = tk.Toplevel()
        self.ventana_usuarios.title("Gestionando Libros")
        self.ventana_usuarios.geometry("%dx%d+%d+%d" % (500, 300, 450, 220))
        self.ventana_usuarios.resizable(0, 0)

        usuarios_Frame = Frame(self.ventana_usuarios)
        usuarios_Frame.pack(side="top")
        usuarios_Frame.place(width="500", height="300")
        usuarios_Frame.config(bg="black")

        label_nombre = Label(usuarios_Frame, text="Titulo del Libro", font=("Modern", 12), foreground="white")
        label_nombre.pack()
        label_nombre.config(bg="black")
        label_nombre.place(x=20, y=40, width=200, height=20)

        entrada_nombre = tk.Entry(usuarios_Frame)
        entrada_nombre.pack()
        entrada_nombre.place(x = 200, y = 40, width = 160, height = 20)

        label_autor = Label(usuarios_Frame, text="Nombre del Autor", font=("Modern", 12), foreground="white")
        label_autor.pack()
        label_autor.config(bg="black")
        label_autor.place(x=20, y=70, width=200, height=20)

        entrada_autor = tk.Entry(usuarios_Frame)
        entrada_autor.pack()
        entrada_autor.place(x= 200, y=70, width=160, height=20)

        label_isbn = Label(usuarios_Frame, text="Ingrese el ISBN del libro", font=("Modern", 12), foreground="white")
        label_isbn.pack()
        label_isbn.config(bg="black")
        label_isbn.place(x=20, y=100, width=200, height=20)

        entrada_isbn = tk.Entry(usuarios_Frame)
        entrada_isbn.pack()
        entrada_isbn.place(x=200, y=100, width=160, height=20)

        button_guardar = Button(usuarios_Frame, text="Guardar Libro", font=("Modern", 12), foreground="white",highlightthickness=2)
        button_guardar.pack()
        button_guardar.config(bg="black")
        button_guardar.place(x=370, y=100, width=110, height=20)


        self.ventana_usuarios.mainloop()



    def regresar(self):
        self.ventana_principal.deiconify()
        self.ventana_libros.destroy()


if __name__ == "__main__":
    app = Interfaz()
    root = tk.Tk()
    app.ventana_Principal(root)
