from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainApp2(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,250)
        self.setWindowTitle("Configura tu plan")

        self.var=False
        
        self.text=QLabel("Plan plus s/ 14,99 ",self)
        self.text.setGeometry(20,10,170,30)
        

        self.entrada_text=QLineEdit(self)
        self.entrada_text.setPlaceholderText("numero de tarjeta")
        self.entrada_text.setClearButtonEnabled(True)
        self.entrada_text.setGeometry(20,50,170,30)
        self.entrada_text.setMaxLength(10)

        self.entrada_text2=QLineEdit(self)
        self.entrada_text2.setPlaceholderText("fecha de caducidad")
        self.entrada_text2.setClearButtonEnabled(True)
        self.entrada_text2.setGeometry(20,90,170,30)
        self.entrada_text2.setMaxLength(10)

        self.entrada_text3=QLineEdit(self)
        self.entrada_text3.setPlaceholderText("CVV")
        self.entrada_text3.setClearButtonEnabled(True)
        self.entrada_text3.setGeometry(240,50,70,30)
        self.entrada_text3.setMaxLength(10)
        

        self.btn=QPushButton("suscribirme",self)
        self.btn.setGeometry(20,130,180,30)
        self.var=self.btn.clicked.connect(self.suscrib)
        #self.btn.clicked.connect(self.suscrib)

        self.btn2=QPushButton("salir",self)
        self.btn2.setGeometry(210,130,90,30)
        self.btn2.clicked.connect(self.close)

        self.text2=QLabel("",self)
        self.text2.setGeometry(20,170,100,30)

             #---------style---------

        self.setStyleSheet("background-color: #000000;")

        self.text.setStyleSheet("background-color:#000000 ;color:#ffffff ;font-size: 20px;font-weight: bold")
        self.text2.setStyleSheet("background-color:#000000 ;color:#ffffff ;font-size: 20px;font-weight: bold")

        self.btn.setStyleSheet("background-color:#700188 ;color: #FFFFFF;border-radius: 8px;padding: 1px;font-size: 12px;font-weight: bold;")
        self.btn2.setStyleSheet("background-color:#700188 ;color: #FFFFFF;border-radius: 8px;padding: 1px;font-size: 12px;font-weight: bold;")

        self.entrada_text.setStyleSheet("background-color: #292929;color: #ffffff;border: 2px solid #700188;border-radius:8px")

        self.entrada_text2.setStyleSheet("background-color: #292929;color: #ffffff;border: 2px solid #700188;border-radius:8px")
        self.entrada_text3.setStyleSheet("background-color: #292929;color: #ffffff;border: 2px solid #700188;border-radius:8px")


        

    def suscrib(self):
        self.var=True
        self.text2.setText("gracias")
        
        return self.var




class MainApp(QMainWindow):
    def __init__(self,parent=None, *args):
        super(MainApp,self).__init__(parent=parent)
        self.setFixedSize(400,200)
        self.setWindowTitle("calculadora")

        self.Segunda_ventan=MainApp2()

        self.entrada_text=QLineEdit(self)
        self.entrada_text.setPlaceholderText("ingrese primer numero")
        self.entrada_text.setClearButtonEnabled(True)
        self.entrada_text.setGeometry(20,20,220,35)
        self.entrada_text.setMaxLength(10)

        self.entrada_text2=QLineEdit(self)
        self.entrada_text2.setPlaceholderText("ingrese segundo numero")
        self.entrada_text2.setClearButtonEnabled(True)
        self.entrada_text2.setGeometry(20,65,220,35)
        self.entrada_text2.setMaxLength(10)
        
        self.btn_sumar=QPushButton("sumar",self)
        self.btn_sumar.setGeometry(20,110,70,30)
        self.btn_sumar.clicked.connect(self.validar_suscripcion)

        self.text=QLabel(f"resultado:",self)
        self.text.setGeometry(20,155,350,30)
        
        self.suscripcion=False


        #---------style---------

        self.setStyleSheet("background-color: #000000;")

        self.text.setStyleSheet("background-color:#000000 ;color:#ffffff;font-size: 18px;font-weight: bold")

        self.btn_sumar.setStyleSheet("background-color:#700188 ;color: #FFFFFF;border-radius: 8px;padding: 1px;font-size: 12px;font-weight: bold;")

        self.entrada_text.setStyleSheet("background-color: #292929;color: #ffffff;border: 2px solid #700188;border-radius:8px")

        self.entrada_text2.setStyleSheet("background-color: #292929;color: #ffffff;border: 2px solid #700188;border-radius:8px")

    

    def sumar(self):
        try:
            num1=float(self.entrada_text.text())
            num2=float(self.entrada_text2.text())
            res=num2+num1
            self.text.setText(f"resultado:{res}")

        except:
            self.text.setText(f"igrese solo numeros >:v ")
                

    def validar_suscripcion(self):
        if self.suscripcion is False:
            self.Segunda_ventan.show()
            self.suscripcion=self.Segunda_ventan.var
            self.text.setText("Cambiate a plus")

        else:
            self.sumar()
            

if __name__ == '__main__':
    app=QApplication([])
    window = MainApp()
    app.setStyleSheet(window.styleSheet()) 
    window.show()
    app.exec_()
