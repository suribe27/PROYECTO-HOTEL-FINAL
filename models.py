from tkinter import messagebox
from fpdf import FPDF
import datetime

# Definición de excepciones personalizadas
class UsuarioYaExisteError(Exception):
    """Excepción lanzada cuando se intenta crear un usuario con un email que ya existe"""
    def __init__(self, mensaje="Ya existe una cuenta con este correo."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class CredencialesInvalidasError(Exception):
    """Excepción lanzada cuando las credenciales de inicio de sesión son incorrectas"""
    def __init__(self, mensaje="Correo o contraseña incorrectos."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class HabitacionNoDisponibleError(Exception):
    """Excepción lanzada cuando se intenta reservar una habitación que no está disponible"""
    def __init__(self, mensaje="Habitación no disponible."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

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
        try:
            if not nombre or not email or not contraseña:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return
            if email in usuarios_db:
                raise UsuarioYaExisteError()
            nuevo_usuario = cls(nombre, email, contraseña)
            usuarios_db[email] = nuevo_usuario
            messagebox.showinfo("Éxito", f"Cuenta creada exitosamente para {nombre}.")
        except UsuarioYaExisteError as e:
            messagebox.showerror("Error", str(e))

    @classmethod
    def iniciar_sesion(cls, email, contraseña):
        try:
            if not email or not contraseña:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return False
            usuario = usuarios_db.get(email)
            if not usuario or usuario.contraseña != contraseña:
                raise CredencialesInvalidasError()
            messagebox.showinfo("Bienvenido", f"Inicio de sesión exitoso. Bienvenido {usuario.nombre}!")
            return True
        except CredencialesInvalidasError as e:
            messagebox.showerror("Error", str(e))
            return False

    @classmethod
    def cambiar_contraseña(cls, email, contraseña_actual, nueva_contraseña):
        try:
            if not email or not contraseña_actual or not nueva_contraseña:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return
            usuario = usuarios_db.get(email)
            if not usuario or usuario.contraseña != contraseña_actual:
                raise CredencialesInvalidasError("La contraseña actual es incorrecta.")
            usuario.contraseña = nueva_contraseña
            messagebox.showinfo("Éxito", "Contraseña cambiada exitosamente.")
        except CredencialesInvalidasError as e:
            messagebox.showerror("Error", str(e))

# Clase Habitación
class Habitacion:
    def __init__(self, numero, tipo, precio, descripcion):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.descripcion = descripcion

    @classmethod
    def registrar_habitacion(cls, numero, tipo, precio, descripcion):
        try:
            if not numero or not tipo or not precio or not descripcion:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return
            if numero in habitaciones_db:
                raise HabitacionNoDisponibleError("Ya existe una habitación con ese número.")
            nueva_habitacion = cls(numero, tipo, precio, descripcion)
            habitaciones_db[numero] = nueva_habitacion
            messagebox.showinfo("Éxito", "Habitación registrada exitosamente.")
        except HabitacionNoDisponibleError as e:
            messagebox.showerror("Error", str(e))

    @classmethod
    def buscar_habitaciones_disponibles(cls):
        try:
            if not habitaciones_db:
                return "No hay habitaciones disponibles."
            lista_habitaciones = [f"Habitación {num}: {hab.tipo}, Precio: {hab.precio}" 
                                for num, hab in habitaciones_db.items()]
            return "\n".join(lista_habitaciones)
        except Exception as e:
            messagebox.showerror("Error", "Error al buscar habitaciones disponibles.")
            return "Error al buscar habitaciones."

# Clase Reserva
class Reserva:
    def __init__(self, email, habitacion, fecha_inicio, fecha_fin):
        self.email = email
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin

    @classmethod
    def realizar_reserva(cls, email, numero_habitacion, fecha_inicio, fecha_fin):
        try:
            if not email or not numero_habitacion or not fecha_inicio or not fecha_fin:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return
            if numero_habitacion not in habitaciones_db:
                raise HabitacionNoDisponibleError("La habitación seleccionada no existe.")
            if any(reserva.habitacion == numero_habitacion for reserva in reservas_db.values()):
                raise HabitacionNoDisponibleError("La habitación ya está reservada en esas fechas.")
            
            nueva_reserva = cls(email, numero_habitacion, fecha_inicio, fecha_fin)
            reservas_db[email] = nueva_reserva
            messagebox.showinfo("Éxito", "Reserva realizada exitosamente.")
        except HabitacionNoDisponibleError as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "Error al realizar la reserva.")

    @classmethod
    def modificar_reserva(cls, email, nueva_fecha_inicio, nueva_fecha_fin):
        try:
            if not email or not nueva_fecha_inicio or not nueva_fecha_fin:
                messagebox.showerror("Error", "Todos los campos son obligatorios.")
                return
            if email not in reservas_db:
                raise Exception("No se encontró una reserva para ese usuario.")
            
            reserva = reservas_db[email]
            reserva.fecha_inicio = nueva_fecha_inicio
            reserva.fecha_fin = nueva_fecha_fin
            messagebox.showinfo("Éxito", "Reserva modificada exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    @classmethod
    def cancelar_reserva(cls, email):
        try:
            if not email:
                messagebox.showerror("Error", "El campo email es obligatorio.")
                return
            if email not in reservas_db:
                raise Exception("No se encontró una reserva para ese usuario.")
            
            del reservas_db[email]
            messagebox.showinfo("Éxito", "Reserva cancelada exitosamente.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    @classmethod
    def generar_reporte(cls, fecha_inicio, fecha_fin):
        try:
            if not fecha_inicio or not fecha_fin:
                messagebox.showerror("Error", "Las fechas son obligatorias.")
                return
            
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
        except Exception as e:
            messagebox.showerror("Error", "Error al generar el reporte.")
