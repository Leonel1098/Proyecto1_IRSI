from tkinter import Tk
import tkinter as tk
from tkinter import Frame
from tkinter import Button, filedialog,Label

class Libros:
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

        button_regresar = Button(libros_Frame, text="Regresar", command= lambda: self.regresar(self.ventana_libros), font=("Modern", 12), foreground="white", highlightthickness=2)
        button_regresar.pack()
        button_regresar.config(bg="black")
        button_regresar.place(x=370, y=265, width=110, height=20)

        self.ventana_libros.mainloop()







    


    
