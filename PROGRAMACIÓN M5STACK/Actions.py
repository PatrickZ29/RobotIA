import sys
import serial
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QVBoxLayout
from PyQt5.QtCore import Qt, QTimer, QThread, pyqtSignal

# --- CONFIGURACIÓN ---
PUERTO_USB = 'COM9'  # Cambia por tu puerto real
BAUDIOS = 115200
MINUTOS = 2

# Estilos CSS
ESTILO_NORMAL = """
    QLabel {
        color: #FFFFFF;
        font-size: 70px;
        font-weight: bold;
        font-family: 'Segoe UI', 'Arial', sans-serif;
        background-color: rgba(20, 25, 30, 220);
        border-radius: 15px;
        padding: 10px 30px;
        border: 2px solid #FFFFFF;
    }
"""

ESTILO_FINALIZADO = """
    QLabel {
        color: #FF1744;
        font-size: 70px;
        font-weight: bold;
        font-family: 'Segoe UI', 'Arial', sans-serif;
        background-color: rgba(20, 25, 30, 220);
        border-radius: 15px;
        padding: 10px 30px;
        border: 2px solid #FF1744;
    }
"""

class HiloSerial(QThread):
    # Ahora la señal envía un string (el comando detectado)
    senal_comando = pyqtSignal(str)

    def run(self):
        try:
            ser = serial.Serial(PUERTO_USB, BAUDIOS, timeout=1)
            print(f"Escuchando comandos en {PUERTO_USB}...")
            while True:
                if ser.in_waiting > 0:
                    linea = ser.readline().decode('utf-8', errors='ignore').strip()
                    
                    if "iniciar timer" in linea:
                        self.senal_comando.emit("iniciar")
                    elif "parar timer" in linea:
                        self.senal_comando.emit("parar")
                        
        except serial.SerialException:
            print(f"Error: Conexión perdida en {PUERTO_USB}.")

class TemporizadorStream(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(ESTILO_NORMAL)
        
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

        self.tiempo_restante = MINUTOS * 60
        self.actualizar_pantalla() 

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.tick_reloj) 

        # Conectamos la nueva señal al procesador de comandos
        self.hilo_serial = HiloSerial()
        self.hilo_serial.senal_comando.connect(self.procesar_comando_usb)
        self.hilo_serial.start()

        self.oldPos = self.pos()

    def procesar_comando_usb(self, comando):
        """Maneja las señales específicas que llegan desde la placa"""
        if comando == "iniciar":
            if not self.timer.isActive():
                if self.tiempo_restante <= 0:
                    self.resetear_timer()
                self.timer.start(1000)
                print("USB: Timer Iniciado")
                
        elif comando == "parar":
            if self.timer.isActive():
                self.timer.stop()
                print("USB: Timer Detenido")

    def tick_reloj(self):
        if self.tiempo_restante > 0:
            self.tiempo_restante -= 1
            self.actualizar_pantalla()
        
        if self.tiempo_restante <= 0:
            self.timer.stop()
            self.label.setText("00:00")
            self.label.setStyleSheet(ESTILO_FINALIZADO)

    def actualizar_pantalla(self):
        minutos, segundos = divmod(self.tiempo_restante, 60)
        self.label.setText(f"{minutos:02d}:{segundos:02d}")

    def resetear_timer(self):
        self.timer.stop()
        self.tiempo_restante = MINUTOS * 60
        self.label.setStyleSheet(ESTILO_NORMAL)
        self.actualizar_pantalla()

    # --- CONTROLES DE TECLADO ---
    def keyPressEvent(self, event):
        # Espacio: Toggle (Play/Pausa)
        if event.key() == Qt.Key_Space:
            if self.timer.isActive():
                self.timer.stop()
            elif self.tiempo_restante > 0:
                self.timer.start(1000)

        # Tecla 'R': Reset total
        elif event.key() == Qt.Key_R:
            self.resetear_timer()

        # Tecla 'S': Iniciar (Manual)
        elif event.key() == Qt.Key_S:
            self.procesar_comando_usb("iniciar")

    # --- ARRASTRE DE VENTANA ---
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = event.globalPos() - self.oldPos
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.oldPos = event.globalPos()

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.RightButton:
            sys.exit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = TemporizadorStream()
    ventana.show()
    sys.exit(app.exec_())