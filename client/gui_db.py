import tkinter as tk
from tkinter import messagebox

def MostrarAyuda():
    ventana_ayuda = tk.Toplevel()  # Crea una nueva ventana
    ventana_ayuda.title("Ayuda")  # Establece el título de la ventana
    ventana_ayuda.geometry("550x450") # Establece el tamaño de la ventana

    mensaje = (
        "Hola! Bienvenidos a Droomi Store Database!\n\n"
        "Esta aplicación te permite gestionar la base de datos de clientes de Droomi Store. "
        "Podrás realizar diversas operaciones, como añadir, eliminar, modificar y visualizar los datos de los clientes.\n\n"
        "¡Esperamos que esta herramienta te sea útil y eficiente en la gestión de la base de datos de nuestra tienda!\n\n"
        "- El equipo de Droomi Store\n\n" 
        "Droomi Store Database Version 0.1"
    )

    texto_ayuda = tk.Text(ventana_ayuda, wrap="word", font=("Consolas", 12))
    texto_ayuda.tag_configure("center", justify="center")
    texto_ayuda.insert(tk.END, mensaje, "center")
    texto_ayuda.pack(expand=True, fill="both", padx=15, pady=15)
    texto_ayuda.config(state="disabled")  # Hacer el texto de solo lectura

def menu_tools(root):
    menu_tools = tk.Menu(root)
    root.config(menu=menu_tools, width=300, height=300)
    
    #menu inicio
    inicio_menu = tk.Menu(menu_tools, tearoff=0)
    menu_tools.add_cascade(label='Inicio', menu = inicio_menu)
    
    #menu Inicio cascade
    inicio_menu.add_command(label='Crear registro en Base Datos')
    inicio_menu.add_command(label='Eliminar registro en Base Datos')
    inicio_menu.add_command(label='Salir', command=root.destroy)
    
    #menu ayuda
    menu_ayuda = tk.Menu(menu_tools, tearoff=False)
    menu_tools.add_cascade(label="Ayuda", menu=menu_ayuda)
    menu_ayuda.add_command(label="Acerca de", command=MostrarAyuda)

class mainframe(tk.Frame):
    def __init__(self, root = None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.pack()
        #self.config(background="#00A99D")

        self.InfoCliente()
        self.InputDeActivate()


    def InfoCliente(self):
        #labels para el nombre de cliente
        self.label_nombre = tk.Label(self, text="Nombre del Cliente")
        self.label_nombre.config(font=('Consolas', 12, 'bold'))
        self.label_nombre.grid(column=0, row=0, padx=10, pady=10)

        #labels para el numero de cliente
        self.label_num_cliente = tk.Label(self, text="Numero del Cliente")
        self.label_num_cliente.config(font=('Consolas', 12, 'bold'))
        self.label_num_cliente.grid(column=0, row=1, padx=10, pady=10)

        #labels para el telefono
        self.label_Telefono = tk.Label(self, text="Telefono")
        self.label_Telefono.config(font=('Consolas', 12, 'bold'))
        self.label_Telefono.grid(column=0, row=2, padx=10, pady=10)

        #labels para el numero de orden
        self.label_num_orden = tk.Label(self, text="Numero de orden")
        self.label_num_orden.config(font=('Consolas', 12, 'bold'))
        self.label_num_orden.grid(column=0, row=3, padx=10, pady=10)

        #labels para el articulos
        self.label_articulos = tk.Label(self, text="Articulos Ordenados")
        self.label_articulos.config(font=('Consolas', 12, 'bold'))
        self.label_articulos.grid(column=0, row=4, padx=10, pady=10)

        #labels para el fecha pedido
        self.label_fecha = tk.Label(self, text="Fecha del pedido")
        self.label_fecha.config(font=('Consolas', 12, 'bold'))
        self.label_fecha.grid(column=0, row=5, padx=10, pady=10)

        #labels para el nombre de comercial
        self.label_comercial = tk.Label(self, text="Nombre del Comercial")
        self.label_comercial.config(font=('Consolas', 12, 'bold'))
        self.label_comercial.grid(column=0, row=6, padx=10, pady=10)

        #Inputs de cada label
        #input para el nombre
        self.nombre_clear = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre_clear)
        self.entry_nombre.config(width=50, font=('Consolas', 12, 'bold'))
        self.entry_nombre.grid(column=1, row=0, padx=10, pady=10, columnspan=2)

        #input para el numero del cliente
        self.num_client_clear = tk.StringVar()
        self.entry_num_client = tk.Entry(self, textvariable=self.num_client_clear)
        self.entry_num_client.config(width=50, font=('Consolas', 12, 'bold'))
        self.entry_num_client.grid(column=1, row=1, padx=10, pady=10, columnspan=2)
        
        #input para el telefono
        self.telefono_clear = tk.StringVar()
        self.entry_telefono = tk.Entry(self, textvariable=self.telefono_clear)
        self.entry_telefono.config(width=50, font=('Consolas', 12, 'bold'))
        self.entry_telefono.grid(column=1, row=2, padx=10, pady=10, columnspan=2)
        
        #input para el numero de orden
        self.num_orden_clear = tk.StringVar()
        self.entry_num_orden = tk.Entry(self, textvariable=self.num_orden_clear)
        self.entry_num_orden.config(width=50, font=('Consolas', 12, 'bold'))
        self.entry_num_orden.grid(column=1, row=3, padx=10, pady=10, columnspan=2)

        #input para articulos
        self.articulos_clear = tk.StringVar()
        self.entry_articulos = tk.Entry(self, textvariable=self.articulos_clear)
        self.entry_articulos.config(width=50, font=('Consolas', 12, 'bold'))
        self.entry_articulos.grid(column=1, row=4, padx=10, pady=10, columnspan=2)

        #input para fecha
        self.fecha_clear = tk.StringVar()
        self.entry_fecha = tk.Entry(self, textvariable=self.fecha_clear)
        self.entry_fecha.config(width=50, font=('Consolas', 12, 'bold'))
        self.entry_fecha.grid(column=1, row=5, padx=10, pady=10, columnspan=2)
        
        #input para comercial
        self.comercial_clear = tk.StringVar()
        self.entry_comercial = tk.Entry(self, textvariable=self.comercial_clear)
        self.entry_comercial.config(width=50, font=('Consolas', 12, 'bold'))
        self.entry_comercial.grid(column=1, row=6, padx=10, pady=10, columnspan=2)

        #Botones
        
        #Boton Agregar
        self.button_add = tk.Button(self, text="Agregar", command=self.InputActivate)
        self.button_add.config(width=20, font=('Consolas', 12, 'bold'), background="#F0563D", foreground="black", cursor='hand2', activebackground="#C13A2B")
        self.button_add.grid(row=7, column=0, padx=10, pady=10)

        #Boton Modificar
        self.button_modify = tk.Button(self, text="Modificar", command=self.InputActivate)
        self.button_modify.config(width=20, font=('Consolas', 12, 'bold'), background="#00A99D", foreground="black", cursor='hand2', activebackground="#07685F")
        self.button_modify.grid(row=7, column=1, padx=10, pady=10)

        #Boton Eliminar
        self.button_erase = tk.Button(self, text="Eliminar", command=self.InputDeActivate)
        self.button_erase.config(width=20, font=('Consolas', 12, 'bold'), background="#000000", foreground="white", cursor='hand2', activebackground="#494949")
        self.button_erase.grid(row=7, column=2, padx=10, pady=10)

    def InputActivate(self):
        self.entry_nombre.config(state='normal')
        self.entry_num_client.config(state='normal')
        self.entry_telefono.config(state='normal')
        self.entry_fecha.config(state='normal')
        self.entry_num_orden.config(state='normal')
        self.entry_articulos.config(state='normal')
        self.entry_comercial.config(state='normal')

        #self.button_add.config(state='normal')
        self.button_modify.config(state='normal')
        self.button_erase.config(state='normal')
        
    def InputDeActivate(self):
        self.nombre_clear.set('')
        self.num_client_clear.set('')
        self.num_orden_clear.set('')
        self.fecha_clear.set('')
        self.telefono_clear.set('')
        self.comercial_clear.set('')
        self.articulos_clear.set('')

        self.entry_nombre.config(state='disable')
        self.entry_num_client.config(state='disable')
        self.entry_telefono.config(state='disable')
        self.entry_fecha.config(state='disable')
        self.entry_num_orden.config(state='disable')
        self.entry_articulos.config(state='disable')
        self.entry_comercial.config(state='disable')

        #self.button_add.config(state='disable')
        self.button_modify.config(state='disable')
        self.button_erase.config(state='disable')