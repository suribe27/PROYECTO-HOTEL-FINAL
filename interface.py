import tkinter as tk
from models import Usuario, Habitacion, Reserva

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Hotel")

        # Pestañas
        self.tab_control = tk.Frame(self.root)
        self.tab_control.pack()

        self.boton_crear_cuenta = tk.Button(self.tab_control, text="Crear Cuenta", command=self.mostrar_crear_cuenta)
        self.boton_crear_cuenta.grid(row=0, column=0)

        self.boton_iniciar_sesion = tk.Button(self.tab_control, text="Iniciar Sesión", command=self.mostrar_iniciar_sesion)
        self.boton_iniciar_sesion.grid(row=0, column=1)

        self.boton_cambiar_contraseña = tk.Button(self.tab_control, text="Cambiar Contraseña", command=self.mostrar_cambiar_contraseña)
        self.boton_cambiar_contraseña.grid(row=0, column=2)

        self.boton_registrar_habitacion = tk.Button(self.tab_control, text="Registrar Habitación", command=self.mostrar_registrar_habitacion)
        self.boton_registrar_habitacion.grid(row=0, column=3)

        self.boton_buscar_habitaciones = tk.Button(self.tab_control, text="Buscar Habitaciones", command=self.mostrar_buscar_habitaciones)
        self.boton_buscar_habitaciones.grid(row=0, column=4)

        self.boton_realizar_reserva = tk.Button(self.tab_control, text="Realizar Reserva", command=self.mostrar_realizar_reserva)
        self.boton_realizar_reserva.grid(row=0, column=5)

        self.boton_modificar_reserva = tk.Button(self.tab_control, text="Modificar Reserva", command=self.mostrar_modificar_reserva)
        self.boton_modificar_reserva.grid(row=0, column=6)

        self.boton_cancelar_reserva = tk.Button(self.tab_control, text="Cancelar Reserva", command=self.mostrar_cancelar_reserva)
        self.boton_cancelar_reserva.grid(row=0, column=7)

        self.boton_generar_reporte = tk.Button(self.tab_control, text="Generar Reporte", command=self.mostrar_generar_reporte)
        self.boton_generar_reporte.grid(row=0, column=8)

        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()

        self.mostrar_crear_cuenta()

    def limpiar_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def mostrar_crear_cuenta(self):
        self.limpiar_frame()
        tk.Label(self.main_frame, text="Nombre").grid(row=0, column=0)
        tk.Label(self.main_frame, text="Email").grid(row=1, column=0)
        tk.Label(self.main_frame, text="Contraseña").grid(row=2, column=0)

        nombre_entry = tk.Entry(self.main_frame)
        email_entry = tk.Entry(self.main_frame)
        contraseña_entry = tk.Entry(self.main_frame, show="*")

        nombre_entry.grid(row=0, column=1)
        email_entry.grid(row=1, column=1)
        contraseña_entry.grid(row=2, column=1)

        def crear_cuenta():
            Usuario.crear_cuenta(nombre_entry.get(), email_entry.get(), contraseña_entry.get())

        tk.Button(self.main_frame, text="Crear Cuenta", command=crear_cuenta).grid(row=3, column=1)

    def mostrar_iniciar_sesion(self):
        self.limpiar_frame()
        tk.Label(self.main_frame, text="Email").grid(row=0, column=0)
        tk.Label(self.main_frame, text="Contraseña").grid(row=1, column=0)

        email_entry = tk.Entry(self.main_frame)
        contraseña_entry = tk.Entry(self.main_frame, show="*")

        email_entry.grid(row=0, column=1)
        contraseña_entry.grid(row=1, column=1)

        def iniciar_sesion():
            Usuario.iniciar_sesion(email_entry.get(), contraseña_entry.get())

        tk.Button(self.main_frame, text="Iniciar Sesión", command=iniciar_sesion).grid(row=2, column=1)

    def mostrar_cambiar_contraseña(self):
        self.limpiar_frame()
        tk.Label(self.main_frame, text="Email").grid(row=0, column=0)
        tk.Label(self.main_frame, text="Contraseña Actual").grid(row=1, column=0)
        tk.Label(self.main_frame, text="Nueva Contraseña").grid(row=2, column=0)

        email_entry = tk.Entry(self.main_frame)
        contraseña_actual_entry = tk.Entry(self.main_frame, show="*")
        nueva_contraseña_entry = tk.Entry(self.main_frame, show="*")

        email_entry.grid(row=0, column=1)
        contraseña_actual_entry.grid(row=1, column=1)
        nueva_contraseña_entry.grid(row=2, column=1)

        def cambiar_contraseña():
            Usuario.cambiar_contraseña(email_entry.get(), contraseña_actual_entry.get(), nueva_contraseña_entry.get())

        tk.Button(self.main_frame, text="Cambiar Contraseña", command=cambiar_contraseña).grid(row=3, column=1)

    def mostrar_registrar_habitacion(self):
        self.limpiar_frame()
        tk.Label(self.main_frame, text="Número").grid(row=0, column=0)
        tk.Label(self.main_frame, text="Tipo").grid(row=1, column=0)
        tk.Label(self.main_frame, text="Precio").grid(row=2, column=0)
        tk.Label(self.main_frame, text="Descripción").grid(row=3, column=0)

        numero_entry = tk.Entry(self.main_frame)
        tipo_entry = tk.Entry(self.main_frame)
        precio_entry = tk.Entry(self.main_frame)
        descripcion_entry = tk.Entry(self.main_frame)

        numero_entry.grid(row=0, column=1)
        tipo_entry.grid(row=1, column=1)
        precio_entry.grid(row=2, column=1)
        descripcion_entry.grid(row=3, column=1)

        def registrar_habitacion():
            Habitacion.registrar_habitacion(numero_entry.get(), tipo_entry.get(), precio_entry.get(), descripcion_entry.get())

        tk.Button(self.main_frame, text="Registrar Habitación", command=registrar_habitacion).grid(row=4, column=1)

    def mostrar_buscar_habitaciones(self):
        self.limpiar_frame()
        habitaciones_disponibles = Habitacion.buscar_habitaciones_disponibles()
        tk.Label(self.main_frame, text="Habitaciones Disponibles").pack()
        tk.Label(self.main_frame, text=habitaciones_disponibles).pack()

    def mostrar_realizar_reserva(self):
        self.limpiar_frame()
        tk.Label(self.main_frame, text="Email").grid(row=0, column=0)
        tk.Label(self.main_frame, text="Número de Habitación").grid(row=1, column=0)
        tk.Label(self.main_frame, text="Fecha Inicio (YYYY-MM-DD)").grid(row=2, column=0)
        tk.Label(self.main_frame, text="Fecha Fin (YYYY-MM-DD)").grid(row=3, column=0)

        email_entry = tk.Entry(self.main_frame)
        habitacion_entry = tk.Entry(self.main_frame)
        fecha_inicio_entry = tk.Entry(self.main_frame)
        fecha_fin_entry = tk.Entry(self.main_frame)

        email_entry.grid(row=0, column=1)
        habitacion_entry.grid(row=1, column=1)
        fecha_inicio_entry.grid(row=2, column=1)
        fecha_fin_entry.grid(row=3, column=1)

        def realizar_reserva():
            Reserva.realizar_reserva(email_entry.get(), habitacion_entry.get(), fecha_inicio_entry.get(), fecha_fin_entry.get())

        tk.Button(self.main_frame, text="Realizar Reserva", command=realizar_reserva).grid(row=4, column=1)

    def mostrar_modificar_reserva(self):
        self.limpiar_frame()
        tk.Label(self.main_frame, text="Email").grid(row=0, column=0)
        tk.Label(self.main_frame, text="Nueva Fecha Inicio (YYYY-MM-DD)").grid(row=1, column=0)
        tk.Label(self.main_frame, text="Nueva Fecha Fin (YYYY-MM-DD)").grid(row=2, column=0)

        email_entry = tk.Entry(self.main_frame)
        nueva_fecha_inicio_entry = tk.Entry(self.main_frame)
        nueva_fecha_fin_entry = tk.Entry(self.main_frame)

        email_entry.grid(row=0, column=1)
        nueva_fecha_inicio_entry.grid(row=1, column=1)
        nueva_fecha_fin_entry.grid(row=2, column=1)

        def modificar_reserva():
            Reserva.modificar_reserva(email_entry.get(), nueva_fecha_inicio_entry.get(), nueva_fecha_fin_entry.get())

        tk.Button(self.main_frame, text="Modificar Reserva", command=modificar_reserva).grid(row=3, column=1)

    def mostrar_cancelar_reserva(self):
        self.limpiar_frame()
        tk.Label(self.main_frame, text="Email").grid(row=0, column=0)

        email_entry = tk.Entry(self.main_frame)
        email_entry.grid(row=0, column=1)

        def cancelar_reserva():
            Reserva.cancelar_reserva(email_entry.get())

        tk.Button(self.main_frame, text="Cancelar Reserva", command=cancelar_reserva).grid(row=1, column=1)

    def mostrar_generar_reporte(self):
        self.limpiar_frame()
        tk.Label(self.main_frame, text="Fecha Inicio (YYYY-MM-DD)").grid(row=0, column=0)
        tk.Label(self.main_frame, text="Fecha Fin (YYYY-MM-DD)").grid(row=1, column=0)

        fecha_inicio_entry = tk.Entry(self.main_frame)
        fecha_fin_entry = tk.Entry(self.main_frame)

        fecha_inicio_entry.grid(row=0, column=1)
        fecha_fin_entry.grid(row=1, column=1)

        def generar_reporte():
            Reserva.generar_reporte(fecha_inicio_entry.get(), fecha_fin_entry.get())

        tk.Button(self.main_frame, text="Generar Reporte", command=generar_reporte).grid(row=2, column=1)