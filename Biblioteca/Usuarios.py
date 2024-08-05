from tkinter import Tk
import tkinter as tk
from tkinter import Frame
from tkinter import Button, filedialog,Label

class Usuarios:
    # Estructura y componentes de la ventana de Usuarios
    def ventana_Usuarios(self):

        self.ventana_principal.iconify()
        self.ventana_usuarios = tk.Toplevel()
        self.ventana_usuarios.title("Gestionando Usuarios")
        self.ventana_usuarios.geometry("%dx%d+%d+%d" % (500, 300, 450, 220))
        self.ventana_usuarios.resizable(0, 0)

        usuarios_Frame = Frame(self.ventana_usuarios)
        usuarios_Frame.pack(side="top")
        usuarios_Frame.place(width="500", height="300")
        usuarios_Frame.config(bg="black")

        label_nombre = Label(usuarios_Frame, text="Nombre del Usuario", font=("Modern", 12), foreground="white")
        label_nombre.pack()
        label_nombre.config(bg="black")
        label_nombre.place(x=20, y=40, width=200, height=20)

        entrada_nombre = tk.Entry(usuarios_Frame)
        entrada_nombre.pack()
        entrada_nombre.place(x = 200, y = 40, width = 160, height = 20)

        label_id = Label(usuarios_Frame, text="ID Usuario", font=("Modern", 12), foreground="white")
        label_id.pack()
        label_id.config(bg="black")
        label_id.place(x=20, y=70, width=200, height=20)

        entrada_id = tk.Entry(usuarios_Frame)
        entrada_id.pack()
        entrada_id.place(x= 200, y=70, width=160, height=20)

        button_registrar_usuario = Button(usuarios_Frame, text="Registrar Usuario", font=("Modern", 12), foreground="white",highlightthickness=2)
        button_registrar_usuario.pack()
        button_registrar_usuario.config(bg="black")
        button_registrar_usuario.place(x=230, y=100, width=110, height=20)

        label_eliminar_usuario = Label(usuarios_Frame, text="Ingrese el ID del Usuario", font=("Modern", 12), foreground="white")
        label_eliminar_usuario.pack()
        label_eliminar_usuario.config(bg="black")
        label_eliminar_usuario.place(x=20, y=180, width=200, height=20)

        entrada_eliminar_usuario = tk.Entry(usuarios_Frame)
        entrada_eliminar_usuario.pack()
        entrada_eliminar_usuario.place(x=200, y=180, width=160, height=20)

        button_eliminar_usuario = Button(usuarios_Frame, text="Eliminar Usuario", font=("Modern", 12), foreground="white",highlightthickness=2)
        button_eliminar_usuario.pack()
        button_eliminar_usuario.config(bg="black")
        button_eliminar_usuario.place(x=370, y=180, width=110, height=20)

        button_regresar = Button(usuarios_Frame, text="Regresar", command= lambda: self.regresar(self.ventana_usuarios), font=("Modern", 12), foreground="white", highlightthickness=2)
        button_regresar.pack()
        button_regresar.config(bg="black")
        button_regresar.place(x=370, y=255, width=110, height=20)
        self.ventana_usuarios.mainloop()