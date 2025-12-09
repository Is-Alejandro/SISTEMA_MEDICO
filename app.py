import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk

# ============================
# IMPORTAR PANTALLAS
# ============================
from pantallas.inicio import PantallaInicio
from pantallas.menu_principal import MenuPrincipal
from pantallas.imc import PantallaIMC
from pantallas.control_medico import PantallaControlMedico
from pantallas.urgencias import PantallaUrgencias

# Módulo Admin
from pantallas.admin import PantallaAdmin

# Módulos de Citas
from pantallas.registro_usuario import PantallaRegistroUsuario
from pantallas.crear_cita import PantallaCrearCita
from pantallas.ver_citas import PantallaVerCitas

# Módulo Doctores
from pantallas.gestion_doctores import PantallaGestionDoctores

# Configuración del sistema
from pantallas.configuracion_sistema import PantallaConfiguracionSistema

# Logs
from pantallas.logs_sistema import PantallaLogsSistema


class Aplicacion(ttk.Window):   # <-- AHORA USAMOS ttk.Window
    def __init__(self):
        super().__init__(themename="minty")   # <-- TEMA PROFESIONAL RECOMENDADO

        self.title("Sistema Experto de Control Médico")
        self.geometry("1100x700")

        # Contenedor principal donde se cargan las pantallas
        self.contenedor = ttk.Frame(self)
        self.contenedor.pack(fill="both", expand=True)

        # Estructuras dinámicas
        self.usuarios = []
        self.doctores = []
        self.citas = []

        # Cargar primera pantalla
        self.mostrar_pantalla("inicio")

    # =================================================================
    # CAMBIO DE PANTALLAS
    # =================================================================
    def mostrar_pantalla(self, nombre_pantalla):

        # Limpiar contenedor actual
        for widget in self.contenedor.winfo_children():
            widget.destroy()

        # Identificar qué pantalla cargar
        if nombre_pantalla == "inicio":
            pantalla = PantallaInicio(self.contenedor, self)

        elif nombre_pantalla == "menu":
            pantalla = MenuPrincipal(self.contenedor, self)

        # ============================
        # MÓDULOS MÉDICOS
        # ============================
        elif nombre_pantalla == "imc":
            pantalla = PantallaIMC(self.contenedor, self)

        elif nombre_pantalla == "control_medico":
            pantalla = PantallaControlMedico(self.contenedor, self)

        elif nombre_pantalla == "urgencias":
            pantalla = PantallaUrgencias(self.contenedor, self)

        # ============================
        # MÓDULOS DE CITAS
        # ============================
        elif nombre_pantalla == "registro_usuario":
            pantalla = PantallaRegistroUsuario(
                self.contenedor, self, lambda: self.mostrar_pantalla("menu")
            )

        elif nombre_pantalla == "crear_cita":
            pantalla = PantallaCrearCita(
                self.contenedor, self, lambda: self.mostrar_pantalla("menu")
            )

        elif nombre_pantalla == "ver_citas":
            pantalla = PantallaVerCitas(
                self.contenedor, self, lambda: self.mostrar_pantalla("menu")
            )

        # ============================
        # ADMIN
        # ============================
        elif nombre_pantalla == "admin":
            pantalla = PantallaAdmin(
                self.contenedor, lambda: self.mostrar_pantalla("menu")
            )

        elif nombre_pantalla == "gestion_doctores":
            pantalla = PantallaGestionDoctores(
                self.contenedor, lambda: self.mostrar_pantalla("admin")
            )

        elif nombre_pantalla == "configuracion_sistema":
            pantalla = PantallaConfiguracionSistema(
                self.contenedor, lambda: self.mostrar_pantalla("admin")
            )

        elif nombre_pantalla == "logs_sistema":
            pantalla = PantallaLogsSistema(
                self.contenedor, lambda: self.mostrar_pantalla("admin")
            )

        else:
            raise ValueError(f"Pantalla '{nombre_pantalla}' no está definida.")

        # Mostrar pantalla seleccionada
        pantalla.pack(fill="both", expand=True)


# =====================================================================
# EJECUCIÓN DE LA APLICACIÓN
# =====================================================================
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
