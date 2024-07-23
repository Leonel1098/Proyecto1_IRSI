from tkinter import Tk
from tkinter import Frame
from tkinter import Button, filedialog,Label
 

ventana_principal = Tk()
ventana_principal.title("Gestion de Biblioteca")
ventana_principal.geometry("%dx%d+%d+%d" % (700,500,360,120))
ventana_principal.resizable(0,0)

p_Frame = Frame(ventana_principal)
p_Frame.pack(side = "top")
p_Frame.place(width= "900", height ="500")
p_Frame.config(bg = "black")

label_titulo = Label(p_Frame, text = "Gestion de Biblioteca",font=("Victor Mono", 22), foreground= "white")
label_titulo.pack()
label_titulo.config(bg= "black")
label_titulo.place(x = 200, y = 20 , width= 300, height= 50)

button = Button(p_Frame, text="Cargar",  foreground = "white", highlightthickness=2)
button.pack()
button.config(bg = "black")
button.place(x = 150,y = 250,width= 100, height  = 40)


button2 = Button(p_Frame, text="Analizar", foreground = "white", highlightthickness=2)
button2.pack()
button2.config(bg = "black")
button2.place(x = 250,y = 250, width= 100, height  = 40 )

button3 = Button(p_Frame, text="Reportes", foreground = "white", highlightthickness=2)
button3.pack()
button3.config(bg = "black")
button3.place(x =350,y= 250, width= 100, height  = 40)

button4 = Button(p_Frame, text="Salir", foreground = "white", highlightthickness=2)
button4.pack()
button4.config(bg = "black")
button4.place(x =450, y = 250, width= 100, height  = 40)



ventana_principal.mainloop()


    
