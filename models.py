from tkinter import messagebox
from fpdf import FPDF
import datetime

# Base de datos simulada
usuarios_db = {}
habitaciones_db = {}
reservas_db = {}

# Clase Usuario
class Usuario:
    def __init__(self, nombre, email, contraseña):
        self.nombre = nombre
        self.email = email
        self.contraseña = contraseña

    @classmethod
    def crear_cuenta(cls, nombre, email, contraseña):
        if email in usuarios_db:
            messagebox.showerror("Error", "Ya existe una cuenta con este correo.")
        else:
            nuevo_usuario = cls(nombre, email, contraseña)
            usuarios_db[email] = nuevo_usuario
            messagebox.showinfo("Éxito", f"Cuenta creada exitosamente para {nombre}.")

    @classmethod
    def iniciar_sesion(cls, email, contraseña):
        usuario = usuarios_db.get(email)
        if usuario and usuario.contraseña == contraseña:
            messagebox.showinfo("Bienvenido", f"Inicio de sesión exitoso. Bienvenido {usuario.nombre}!")
            return True
        else:
            messagebox.showerror("Error", "Correo o contraseña incorrectos.")
            return False

    @classmethod
    def cambiar_contraseña(cls, email, contraseña_actual, nueva_contraseña):
        usuario = usuarios_db.get(email)
        if usuario and usuario.contraseña == contraseña_actual:
            usuario.contraseña = nueva_contraseña
            messagebox.showinfo("Éxito", "Contraseña cambiada exitosamente.")
        else:
            messagebox.showerror("Error", "La contraseña actual es incorrecta.")

# Clase Habitación
class Habitacion:
    def __init__(self, numero, tipo, precio, descripcion):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.descripcion = descripcion

    @classmethod
    def registrar_habitacion(cls, numero, tipo, precio, descripcion):
        if numero in habitaciones_db:
            messagebox.showerror("Error", "Ya existe una habitación con ese número.")
        else:
            nueva_habitacion = cls(numero, tipo, precio, descripcion)
            habitaciones_db[numero] = nueva_habitacion
            messagebox.showinfo("Éxito", "Habitación registrada exitosamente.")

    @classmethod
    def buscar_habitaciones_disponibles(cls):
        if habitaciones_db:
            lista_habitaciones = [f"Habitación {num}: {hab.tipo}, Precio: {hab.precio}" for num, hab in habitaciones_db.items()]
            return "\n".join(lista_habitaciones)
        else:
            return "No hay habitaciones disponibles."

# Clase Reserva
class Reserva:
    def __init__(self, email, habitacion, fecha_inicio, fecha_fin):
        self.email = email
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    @classmethod
    def realizar_reserva(cls, email, numero_habitacion, fecha_inicio, fecha_fin):
        if numero_habitacion not in habitaciones_db:
            messagebox.showerror("Error", "Habitación no disponible.")
        elif any(reserva.numero_habitacion == numero_habitacion for reserva in reservas_db.values()):
            messagebox.showerror("Error", "La habitación ya está reservada en esas fechas.")
        else:
            nueva_reserva = cls(email, numero_habitacion, fecha_inicio, fecha_fin)
            reservas_db[email] = nueva_reserva
            messagebox.showinfo("Éxito", "Reserva realizada exitosamente.")

    @classmethod
    def modificar_reserva(cls, email, nueva_fecha_inicio, nueva_fecha_fin):
        reserva = reservas_db.get(email)
        if reserva:
            reserva.fecha_inicio = nueva_fecha_inicio
            reserva.fecha_fin = nueva_fecha_fin
            messagebox.showinfo("Éxito", "Reserva modificada exitosamente.")
        else:
            messagebox.showerror("Error", "No se encontró una reserva para ese usuario.")

    @classmethod
    def cancelar_reserva(cls, email):
        if email in reservas_db:
            del reservas_db[email]
            messagebox.showinfo("Éxito", "Reserva cancelada exitosamente.")
        else:
            messagebox.showerror("Error", "No se encontró una reserva para ese usuario.")

    @classmethod
    def generar_reporte(cls, fecha_inicio, fecha_fin):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Reporte de Reservas", ln=True, align="C")

        for reserva in reservas_db.values():
            if fecha_inicio <= reserva.fecha_inicio <= fecha_fin:
                texto = f"Usuario: {reserva.email}, Habitación: {reserva.habitacion}, " \
                        f"Fecha Inicio: {reserva.fecha_inicio}, Fecha Fin: {reserva.fecha_fin}"
                pdf.cell(200, 10, txt=texto, ln=True)
        
        pdf.output("reporte_reservas.pdf")
        messagebox.showinfo("Éxito", "Reporte generado exitosamente en reporte_reservas.pdf")