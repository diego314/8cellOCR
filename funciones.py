import wx
import subprocess

# ejecuta un comando externo
def ejecutar(cmd):
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out = p.stdout.read().strip()
    return out

# presenta un mensaje por pantalla
def mensaje(origen, texto):
    dlg = wx.MessageDialog(origen, texto, '', wx.OK | wx.ICON_INFORMATION)
    try:
        result = dlg.ShowModal()
    finally:
        dlg.Destroy()

#comprueba si el digito de control de una cadena es correcto
def checkDigitoControl(identificador, metodo, posicion):
    if posicion=="1":
        numero=int(identificador[0:-1])
        digitoControl=int(identificador[len(identificador)-1])
    elif posicion=="2":
        numero=int(identificador[1:])
        digitoControl=int(identificador[1])
    if metodo=="1": #modulo 10
        digits=str(numero)
        odds, evens = digits[-2::-2], digits[-1::-2]
        suma=""
        for elemento in evens:
            suma = suma + str(2*int(elemento))
        for elemento in odds:
            suma = suma + elemento
        suma2=0
        for caracter in suma:
            suma2=suma2+int(caracter)
        digito=(-1*suma2)%10
    elif metodo=="2": #modulo 11
        digits=numero
        por2, por3, por4, por5, por6, por7 = digits[-1::-6], digits[-2::-6], digits[-3::-6], digits[-4::-6], digits[-5::-6], digits[-6::-6]
        suma=0
        for elemento in por2:
            suma = suma + (2*int(elemento))
        for elemento in por3:
            suma = suma + (3*int(elemento))
        for elemento in por4:
            suma = suma + (4*int(elemento))
        for elemento in por5:
            suma = suma + (5*int(elemento))
        for elemento in por6:
            suma = suma + (6*int(elemento))
        for elemento in por7:
            suma = suma + (7*int(elemento))
        digito=(-1*suma)%11
    elif metodo=="3": #bit de paridad
        numeroBin=bin(numero)[2:]
        digito=0
        for digitoNumeroBin in numeroBin:
            if digitoNumeroBin=="1":
                if digito==0:
                    digito=1
                else:
                    digito=0
    if digito==digitoControl:
        return("no error. numero:"+str(numero)+" digito:"+str(digito)+" digitoControl:"+str(digitoControl))
        #return(True)
    else:
        return("error. numero:"+str(numero)+" digito:"+str(digito)+" digitoControl:"+str(digitoControl))
        #return(False)

