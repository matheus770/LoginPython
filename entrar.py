from PyQt5 import uic
import PyQt5.QtWidgets as QtWidgets
import mysql.connector
import sys

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cad_logi"
)

def chama_segunda_tela():
    
    login.label_7.setText("")
    
    username = login.lineEdit.text()
    password = login.lineEdit_2.text()
    cursor = banco.cursor()
    try:
        cursor.execute(f"SELECT senha from dados WHERE nome ='{username}'")
        catpass = cursor.fetchall()
        print(catpass[0][0])
        banco.close()
    except:
        login.label_7.setText("Erro ao validar")
    
    if password == catpass[0][0]:
        login.close()
        sgtela.show()
    else:
        login.label_7.setText("Erro ao validar")


app = QtWidgets.QApplication([])
login = uic.loadUi("login.ui")
sgtela = uic.loadUi("login_2.ui")
login.pushButton_2.clicked.connect(chama_segunda_tela)

login.show()
app.exec()

