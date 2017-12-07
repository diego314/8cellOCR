#Boa:Frame:Frame1

import wx
#import MySQLdb
import sys
import funciones
import sqlite3

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BOTONCANCELAR, wxID_FRAME1BUTTON5,
 wxID_FRAME1CARPETABASE, wxID_FRAME1CHECKLEER, wxID_FRAME1CHOICE1,
 wxID_FRAME1CHOICEDIGITO, wxID_FRAME1CHOICEDIGITO2, wxID_FRAME1ENCNOMBRE,
 wxID_FRAME1ENCPASS1, wxID_FRAME1ENCPASS2, wxID_FRAME1PANEL1,
 wxID_FRAME1PASSNO, wxID_FRAME1PASSSI, wxID_FRAME1RADIOBUTTON3,
 wxID_FRAME1RADIOBUTTON4, wxID_FRAME1SPINCTRL1, wxID_FRAME1STATICBOX1,
 wxID_FRAME1STATICBOX4, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT10,
 wxID_FRAME1STATICTEXT11, wxID_FRAME1STATICTEXT13, wxID_FRAME1STATICTEXT2,
 wxID_FRAME1STATICTEXT3, wxID_FRAME1STATICTEXT4, wxID_FRAME1STATICTEXT5,
 wxID_FRAME1STATICTEXT6, wxID_FRAME1STATICTEXT7, wxID_FRAME1TEXTDELIMITADOR,
 wxID_FRAME1TEXTPATRON,
] = [wx.NewId() for _init_ctrls in range(31)]

class Frame1(wx.Frame):

# Inicio definicion de variables

    esNueva=1

    # Inicio base de datos
    conn = sqlite3.connect(sys.path[0]+'/bbdd.db')
    conn.row_factory = sqlite3.Row
    cursor=conn.cursor()


# Fin definicion de variables

# Inicio definicion de GUI

    def _init_coll_sizerAceptarCancelar_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button5, 0, border=0, flag=0)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddWindow(self.botonCancelar, 0, border=0, flag=0)

    def _init_coll_sizerPrincipal_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.sizerIzquierdo, (0, 0), border=4, flag=wx.ALL,
              span=(1, 1))
        parent.AddSizer(self.sizerDerecho, (0, 1), border=4, flag=wx.ALL,
              span=(1, 1))
        parent.AddSizer(self.sizerAceptarCancelar, (1, 0), border=4,
              flag=wx.ALL | wx.ALIGN_CENTER_HORIZONTAL, span=(1, 2))

    def _init_coll_gridSizerEncuesta_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.staticText1, 0, border=0, flag=0)
        parent.AddWindow(self.encNombre, 0, border=0, flag=0)
        parent.AddWindow(self.staticText2, 0, border=0, flag=0)
        parent.AddSizer(self.sizerPasswordsino, 0, border=0,
              flag=wx.ADJUST_MINSIZE)
        parent.AddWindow(self.staticText3, 0, border=0, flag=0)
        parent.AddWindow(self.encPass1, 0, border=0, flag=0)
        parent.AddWindow(self.staticText4, 0, border=0, flag=0)
        parent.AddWindow(self.encPass2, 0, border=0, flag=0)
        parent.AddWindow(self.staticText7, 0, border=0, flag=0)
        parent.AddWindow(self.carpetaBase, 0, border=0, flag=0)

    def _init_coll_sizerPasswordsino_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.passNo, 0, border=0, flag=0)
        parent.AddWindow(self.passSi, 0, border=0, flag=0)

    def _init_coll_gridSizerIdentificador_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.checkLeer, 0, border=0, flag=0)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddWindow(self.staticText10, 0, border=0, flag=0)
        parent.AddWindow(self.spinCtrl1, 0, border=0, flag=0)
        parent.AddWindow(self.staticText11, 0, border=0, flag=0)
        parent.AddWindow(self.radioButton3, 0, border=0, flag=0)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddWindow(self.radioButton4, 0, border=0, flag=0)
        parent.AddWindow(self.staticText13, 0, border=0, flag=0)
        parent.AddWindow(self.choice1, 0, border=0, flag=0)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddWindow(self.textDelimitador, 0, border=0, flag=0)
        parent.AddWindow(self.staticText5, 0, border=0, flag=0)
        parent.AddWindow(self.textPatron, 0, border=0, flag=0)
        parent.AddWindow(self.staticText6, 0, border=0, flag=0)
        parent.AddWindow(self.choiceDigito, 0, border=0, flag=0)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddWindow(self.choiceDigito2, 0, border=0, flag=0)

    def _init_coll_sizerIdentificador_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.gridSizerIdentificador, 0, border=0,
              flag=wx.EXPAND)

    def _init_coll_sizerIzquierdo_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.sizerEncuesta, 0, border=0, flag=0)

    def _init_coll_sizerEncuesta_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.gridSizerEncuesta, 0, border=0, flag=0)

    def _init_coll_sizerDerecho_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.sizerIdentificador, 0, border=0, flag=0)

    def _init_sizers(self):
        # generated method, don't edit
        self.sizerPrincipal = wx.GridBagSizer(hgap=5, vgap=5)
        self.sizerPrincipal.SetCols(1)
        self.sizerPrincipal.SetRows(3)

        self.sizerIzquierdo = wx.BoxSizer(orient=wx.VERTICAL)

        self.sizerDerecho = wx.BoxSizer(orient=wx.VERTICAL)

        self.sizerEncuesta = wx.StaticBoxSizer(box=self.staticBox1,
              orient=wx.VERTICAL)

        self.gridSizerEncuesta = wx.GridSizer(cols=2, hgap=0, rows=8, vgap=0)
        self.gridSizerEncuesta.SetMinSize(wx.Size(260, 108))

        self.sizerPasswordsino = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.sizerIdentificador = wx.StaticBoxSizer(box=self.staticBox4,
              orient=wx.VERTICAL)

        self.gridSizerIdentificador = wx.GridSizer(cols=2, hgap=0, rows=9,
              vgap=0)
        self.gridSizerIdentificador.SetMinSize(wx.Size(292, 300))

        self.sizerAceptarCancelar = wx.BoxSizer(orient=wx.HORIZONTAL)

        self._init_coll_sizerPrincipal_Items(self.sizerPrincipal)
        self._init_coll_sizerIzquierdo_Items(self.sizerIzquierdo)
        self._init_coll_sizerDerecho_Items(self.sizerDerecho)
        self._init_coll_sizerEncuesta_Items(self.sizerEncuesta)
        self._init_coll_gridSizerEncuesta_Items(self.gridSizerEncuesta)
        self._init_coll_sizerPasswordsino_Items(self.sizerPasswordsino)
        self._init_coll_sizerIdentificador_Items(self.sizerIdentificador)
        self._init_coll_gridSizerIdentificador_Items(self.gridSizerIdentificador)
        self._init_coll_sizerAceptarCancelar_Items(self.sizerAceptarCancelar)

        self.SetSizer(self.sizerPrincipal)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(838, 398), size=wx.Size(599, 383),
              style=wx.STAY_ON_TOP | wx.CAPTION | wx.CLOSE_BOX,
              title=u'Opciones de la encuesta')
        self.SetClientSize(wx.Size(599, 383))
        self.Enable(True)
        self.SetIcon(wx.Icon(sys.path[0]+"/"+u'Edit.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(595, 377),
              style=wx.TAB_TRAVERSAL)
        self.panel1.SetBestFittingSize(wx.Size(595, 377))

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label='Encuesta', name='staticBox1', parent=self.panel1,
              pos=wx.Point(4, 4), size=wx.Size(272, 160), style=0)
        self.staticBox1.SetMinSize(wx.Size(300, 130))
        self.staticBox1.SetBestFittingSize(wx.Size(260, 160))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Nombre', name='staticText1', parent=self.panel1,
              pos=wx.Point(9, 21), size=wx.Size(71, 17), style=0)

        self.encNombre = wx.TextCtrl(id=wxID_FRAME1ENCNOMBRE, name=u'encNombre',
              parent=self.panel1, pos=wx.Point(140, 21), size=wx.Size(100, 27),
              style=0, value=u'')
        self.encNombre.SetBestFittingSize(wx.Size(100, 27))

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'\xbfUsar contrase\xf1a?', name='staticText2',
              parent=self.panel1, pos=wx.Point(9, 48), size=wx.Size(131, 20),
              style=0)
        self.staticText2.SetAutoLayout(False)

        self.staticText3 = wx.StaticText(id=wxID_FRAME1STATICTEXT3,
              label=u'Contrase\xf1a', name='staticText3', parent=self.panel1,
              pos=wx.Point(9, 75), size=wx.Size(91, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_FRAME1STATICTEXT4,
              label=u'Repetir contrase\xf1a', name='staticText4',
              parent=self.panel1, pos=wx.Point(9, 102), size=wx.Size(131, 17),
              style=0)

        self.passNo = wx.RadioButton(id=wxID_FRAME1PASSNO, label=u'No',
              name=u'passNo', parent=self.panel1, pos=wx.Point(140, 48),
              size=wx.Size(42, 22), style=wx.RB_GROUP)
        self.passNo.SetValue(False)
        self.passNo.SetToolTipString(u'passNo')
        self.passNo.Bind(wx.EVT_RADIOBUTTON, self.OnPassNoRadiobutton,
              id=wxID_FRAME1PASSNO)

        self.passSi = wx.RadioButton(id=wxID_FRAME1PASSSI, label=u'Si',
              name=u'passSi', parent=self.panel1, pos=wx.Point(182, 48),
              size=wx.Size(36, 22), style=0)
        self.passSi.SetValue(False)
        self.passSi.Bind(wx.EVT_RADIOBUTTON, self.OnPassSiRadiobutton,
              id=wxID_FRAME1PASSSI)

        self.encPass1 = wx.TextCtrl(id=wxID_FRAME1ENCPASS1, name=u'encPass1',
              parent=self.panel1, pos=wx.Point(140, 75), size=wx.Size(100, 27),
              style=0, value=u'')
        self.encPass1.SetBestFittingSize(wx.Size(100, 27))
        self.encPass1.Enable(False)

        self.encPass2 = wx.TextCtrl(id=wxID_FRAME1ENCPASS2, name=u'encPass2',
              parent=self.panel1, pos=wx.Point(140, 102), size=wx.Size(100, 27),
              style=0, value=u'')
        self.encPass2.SetBestFittingSize(wx.Size(100, 27))
        self.encPass2.Enable(False)

        self.staticBox4 = wx.StaticBox(id=wxID_FRAME1STATICBOX4,
              label=u'Identificador', name='staticBox4', parent=self.panel1,
              pos=wx.Point(289, 4), size=wx.Size(302, 322), style=0)
        self.staticBox4.SetBestFittingSize(wx.Size(250, 255))
        self.staticBox4.SetMinSize(wx.Size(250, 220))

        self.checkLeer = wx.CheckBox(id=wxID_FRAME1CHECKLEER,
              label=u'Leer identificador', name=u'checkLeer',
              parent=self.panel1, pos=wx.Point(294, 21), size=wx.Size(146, 22),
              style=0)
        self.checkLeer.SetValue(True)
        self.checkLeer.SetToolTipString(u'checkLeer')
        self.checkLeer.Bind(wx.EVT_CHECKBOX, self.OnCheckLeerCheckbox,
              id=wxID_FRAME1CHECKLEER)

        self.staticText10 = wx.StaticText(id=wxID_FRAME1STATICTEXT10,
              label=u'Long. Identificador', name='staticText10',
              parent=self.panel1, pos=wx.Point(294, 54), size=wx.Size(146, 17),
              style=0)
        self.staticText10.Enable(False)

        self.spinCtrl1 = wx.SpinCtrl(id=wxID_FRAME1SPINCTRL1, initial=1, max=99,
              min=1, name='spinCtrl1', parent=self.panel1, pos=wx.Point(440,
              54), size=wx.Size(95, 27), style=wx.SP_ARROW_KEYS)
        self.spinCtrl1.Enable(True)

        self.staticText11 = wx.StaticText(id=wxID_FRAME1STATICTEXT11,
              label=u'Tipo', name='staticText11', parent=self.panel1,
              pos=wx.Point(294, 87), size=wx.Size(146, 17), style=0)
        self.staticText11.Enable(False)

        self.radioButton3 = wx.RadioButton(id=wxID_FRAME1RADIOBUTTON3,
              label=u'Num\xe9rico', name='radioButton3', parent=self.panel1,
              pos=wx.Point(440, 87), size=wx.Size(108, 22), style=wx.RB_GROUP)
        self.radioButton3.SetValue(False)
        self.radioButton3.Enable(True)

        self.radioButton4 = wx.RadioButton(id=wxID_FRAME1RADIOBUTTON4,
              label=u'Texto', name='radioButton4', parent=self.panel1,
              pos=wx.Point(440, 120), size=wx.Size(108, 22), style=0)
        self.radioButton4.SetValue(False)
        self.radioButton4.Enable(True)

        self.choice1 = wx.Choice(choices=[u'No', u'Antes', u'Despues',
              u'Ambos'], id=wxID_FRAME1CHOICE1, name='choice1',
              parent=self.panel1, pos=wx.Point(440, 153), size=wx.Size(95, 29),
              style=0)
        self.choice1.Enable(True)
        self.choice1.SetSelection(0)
        self.choice1.SetBestFittingSize(wx.Size(95, 29))
        self.choice1.SetHelpText(u'')
        self.choice1.Bind(wx.EVT_CHOICE, self.OnChoice1Choice,
              id=wxID_FRAME1CHOICE1)

        self.textDelimitador = wx.TextCtrl(id=wxID_FRAME1TEXTDELIMITADOR,
              name=u'textDelimitador', parent=self.panel1, pos=wx.Point(440,
              186), size=wx.Size(95, 27), style=0, value=u'')
        self.textDelimitador.SetMaxLength(1)
        self.textDelimitador.SetEditable(True)
        self.textDelimitador.Enable(False)
        self.textDelimitador.SetBestFittingSize(wx.Size(95, 27))

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5, label=u'Aceptar',
              name='button5', parent=self.panel1, pos=wx.Point(200, 339),
              size=wx.Size(93, 34), style=0)
        self.button5.Bind(wx.EVT_BUTTON, self.OnButton5Button,
              id=wxID_FRAME1BUTTON5)

        self.botonCancelar = wx.Button(id=wxID_FRAME1BOTONCANCELAR,
              label=u'Cancelar', name=u'botonCancelar', parent=self.panel1,
              pos=wx.Point(301, 339), size=wx.Size(93, 34), style=0)
        self.botonCancelar.Bind(wx.EVT_BUTTON, self.OnBotonCancelarButton,
              id=wxID_FRAME1BOTONCANCELAR)

        self.staticText13 = wx.StaticText(id=wxID_FRAME1STATICTEXT13,
              label=u'Delimitador', name='staticText13', parent=self.panel1,
              pos=wx.Point(294, 153), size=wx.Size(85, 17), style=0)
        self.staticText13.Enable(False)

        self.staticText5 = wx.StaticText(id=wxID_FRAME1STATICTEXT5,
              label=u'Patr\xf3n', name='staticText5', parent=self.panel1,
              pos=wx.Point(294, 219), size=wx.Size(114, 19), style=0)

        self.textPatron = wx.TextCtrl(id=wxID_FRAME1TEXTPATRON,
              name=u'textPatron', parent=self.panel1, pos=wx.Point(440, 219),
              size=wx.Size(95, 27), style=0, value=u'')
        self.textPatron.SetBestFittingSize(wx.Size(95, 27))
        self.textPatron.Show(True)
        self.textPatron.Enable(True)

        self.staticText6 = wx.StaticText(id=wxID_FRAME1STATICTEXT6,
              label=u'D\xedgito de control', name='staticText6',
              parent=self.panel1, pos=wx.Point(294, 252), size=wx.Size(122, 17),
              style=0)

        self.choiceDigito = wx.Choice(choices=[u'No', u'Al final',
              u'Al comienzo'], id=wxID_FRAME1CHOICEDIGITO, name=u'choiceDigito',
              parent=self.panel1, pos=wx.Point(440, 252), size=wx.Size(95, 29),
              style=0)
        self.choiceDigito.SetMinSize(wx.Size(95, 29))
        self.choiceDigito.SetSelection(0)
        self.choiceDigito.Bind(wx.EVT_CHOICE, self.OnChoiceDigitoChoice,
              id=wxID_FRAME1CHOICEDIGITO)

        self.choiceDigito2 = wx.Choice(choices=[u'Modulo 10', u'Modulo 11',
              u'Bit de paridad'], id=wxID_FRAME1CHOICEDIGITO2,
              name=u'choiceDigito2', parent=self.panel1, pos=wx.Point(440, 285),
              size=wx.Size(95, 29), style=0)
        self.choiceDigito2.SetBestFittingSize(wx.Size(95, 29))
        self.choiceDigito2.SetSelection(0)

        self.staticText7 = wx.StaticText(id=wxID_FRAME1STATICTEXT7,
              label=u'Carpeta base', name='staticText7', parent=self.panel1,
              pos=wx.Point(9, 129), size=wx.Size(103, 17), style=0)

        self.carpetaBase = wx.TextCtrl(id=wxID_FRAME1CARPETABASE,
              name=u'carpetaBase', parent=self, pos=wx.Point(140, 129),
              size=wx.Size(100, 27), style=0, value=u'')
        self.carpetaBase.SetBestFittingSize(wx.Size(100, 27))
        self.carpetaBase.SetInsertionPoint(0)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.MakeModal(True)
        self.ventanaPadre=parent
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.encNombre.SetFocus()
        self.Centre()
        self.choiceDigito.Hide()
        self.choiceDigito2.Hide()
        self.staticText6.Hide()

# fin generacion GUI

    def on_close(self, event):
        self.MakeModal(False)
        #self.db.close()
        event.Skip()

# Inicio botones

    # boton aceptar
    def OnButton5Button(self, event):
        if self.encNombre.GetValue()=="":
            funciones.mensaje(self,"Debe escribir un nombre para la encuesta")
        elif self.passSi.GetValue() and self.encPass1.GetValue()=="":
            funciones.mensaje(self,"Debe escribir una contrasenya")
        elif self.passSi.GetValue() and self.encPass1.GetValue()!=self.encPass2.GetValue():
            funciones.mensaje(self,"Las contrasenyas no coinciden")
        elif self.checkLeer.GetValue() and self.choice1.GetStringSelection()!="No" and self.textDelimitador.GetValue()=="":
            funciones.mensaje(self,"Debe seleccionar un valor para el delimitador")
        elif self.checkLeer.GetValue() and self.textPatron.GetValue()!="" and len(self.textPatron.GetValue())!=self.spinCtrl1.GetValue():
            funciones.mensaje(self,"La longitud del patron no coincide con la longitud del identificador")
        else:
            sql='SELECT * FROM Encuestas WHERE Nombre="'+self.encNombre.GetValue()+'"'
            self.cursor.execute(sql)
            resultado=self.cursor.fetchall()
            if self.cursor.rowcount>0 and self.esNueva==1:
                funciones.mensaje(self,"El nombre que ya elegido ya existe")
            else:
                nombre=self.encNombre.GetValue()
                rutaBase=self.carpetaBase.GetValue()
                if self.passSi.GetValue():
                    contrasenyas=self.encPass1.GetValue()
                else:
                    contrasenya=""

                if self.checkLeer.GetValue():
                    optIdentificador="12"
                    longId=str(self.spinCtrl1.GetValue())
                    if len(longId)==1:
                        longId="0"+longId
                    optIdentificador=optIdentificador+longId
                    if self.radioButton3.GetValue():
                        optIdentificador=optIdentificador+"1"
                    else:
                        optIdentificador=optIdentificador+"2"
                    if self.choice1.GetStringSelection()=="No":
                        optIdentificador=optIdentificador+"0"
                    elif self.choice1.GetStringSelection()=="Antes":
                        optIdentificador=optIdentificador+"1"
                    elif self.choice1.GetStringSelection()=="Despues":
                        optIdentificador=optIdentificador+"2"
                    elif self.choice1.GetStringSelection()=="Ambos":
                        optIdentificador=optIdentificador+"3"
                    if self.textDelimitador.GetValue()=="":
                        optIdentificador=optIdentificador+"0"
                    else:
                        optIdentificador=optIdentificador+self.textDelimitador.GetValue()
                else:
                    optIdentificador="0100100"
                digitoControl=str(self.choiceDigito.GetSelection())+str(self.choiceDigito2.GetSelection())
                textPatron=self.textPatron.GetValue()
                if self.esNueva:
                    sql='INSERT INTO Encuestas '
                    sql+='(Nombre, Password, OptIdentificador, PatronId, DigitoControl, RutaBase) '
                    sql+='VALUES ("'+nombre+'", "'+contrasenya+'", "'+optIdentificador+'", "'+textPatron+'", "'+digitoControl+'", "'+rutaBase+'")'
                else:
                    sql='UPDATE Encuestas SET '
                    sql+='Password="'+contrasenya+'", OptIdentificador="'+optIdentificador+'", PatronId="'+textPatron+'", DigitoControl="'+digitoControl+'", RutaBase="'+rutaBase+'" '
                    sql+='WHERE Nombre="'+nombre+'"'
                self.cursor.execute(sql)
                self.conn.commit()
                self.ventanaPadre.ActivarControles(nombre)
                self.Close()
                self.Destroy()

    # boton cancelar
    def OnBotonCancelarButton(self, event):
        self.Close()
        self.Destroy()

# Fin botones


# Inicio funciones

    # Cargar las opciones de una encuesta
    def cargarOpciones(self, encuesta):
        self.SetTitle(u"Opciones de la encuesta - "+encuesta)
        self.esNueva=0
        sql='SELECT * FROM Encuestas WHERE Nombre="'+encuesta+'"'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            self.encNombre.SetValue(encuesta)
            self.carpetaBase.SetValue(registro["RutaBase"])
            if registro["Password"]!="":
                self.passSi.SetValue(True)
                self.passNo.SetValue(False)
                self.encPass1.Enable(True)
                self.encPass2.Enable(True)
                self.encPass1.SetValue(registro["Password"])
                self.encPass2.SetValue(registro["Password"])
            else:
                self.passSi.SetValue(False)
                self.passNo.SetValue(True)
                self.encPass1.Enable(False)
                self.encPass2.Enable(False)

            if registro["OptIdentificador"][0]=="1":
                self.checkLeer.SetValue(True)
                self.radioButton3.Enable(True)
                self.radioButton4.Enable(True)
                self.staticText10.Enable(True)
                self.staticText11.Enable(True)
                self.staticText13.Enable(True)
                self.spinCtrl1.Enable(True)
                self.textPatron.Enable(True)
                self.choice1.Enable(True)
                valor=(int(registro["OptIdentificador"][2])*10)+int(registro["OptIdentificador"][3])
                self.spinCtrl1.SetValue(valor)
                if registro["OptIdentificador"][4]=="1":
                    self.radioButton3.SetValue(True)
                    self.radioButton4.SetValue(False)
                else:
                    self.radioButton3.SetValue(False)
                    self.radioButton4.SetValue(True)
                self.choice1.SetSelection(int(registro["OptIdentificador"][5]))
                self.textDelimitador.SetValue(registro["OptIdentificador"][6])
                if self.choice1.GetStringSelection()=="No":
                    self.textDelimitador.Enable(False)
                else:
                    self.textDelimitador.Enable(True)
                self.textPatron.SetValue(registro["PatronId"])
                self.choiceDigito.SetSelection(int(registro["DigitoControl"][0]))
                self.choiceDigito2.SetSelection(int(registro["DigitoControl"][1]))
                if registro["DigitoControl"][0]!=0:
                    self.choiceDigito2.Enable(True)
                else:
                    self.choiceDigito2.Enable(False)
            else:
                self.checkLeer.SetValue(False)
                self.radioButton3.Enable(False)
                self.radioButton4.Enable(False)
                self.staticText10.Enable(False)
                self.staticText11.Enable(False)
                self.staticText13.Enable(False)
                self.spinCtrl1.Enable(False)
                self.textPatron.Enable(False)
                self.choice1.Enable(False)
                self.textDelimitador.Enable(False)
                self.choiceDigito.Enable(False)
                self.choiceDigito2.Enable(False)

# Fin funciones


# Inicio eventos

    # Seleccionar password si
    def OnPassSiRadiobutton(self, event):
        self.encPass1.Enable(True)
        self.encPass2.Enable(True)

    # Seleccionar password no
    def OnPassNoRadiobutton(self, event):
        self.encPass1.Enable(False)
        self.encPass2.Enable(False)

    # Checkbox leer identificador
    def OnCheckLeerCheckbox(self, event):
        if self.checkLeer.IsChecked():
            self.radioButton3.Enable(True)
            self.radioButton4.Enable(True)
            self.staticText10.Enable(True)
            self.staticText11.Enable(True)
            self.staticText13.Enable(True)
            self.spinCtrl1.Enable(True)
            self.textPatron.Enable(True)
            self.choice1.Enable(True)
            if self.choice1.GetStringSelection()=="No":
                self.textDelimitador.Enable(False)
            else:
                self.textDelimitador.Enable(True)
            self.choiceDigito.Enable(True)
            if self.choiceDigito.GetStringSelection()=="No":
                self.choiceDigito2.Enable(False)
            else:
                self.choiceDigito2.Enable(True)
        else:
            self.radioButton3.Enable(False)
            self.radioButton4.Enable(False)
            self.staticText10.Enable(False)
            self.staticText11.Enable(False)
            self.staticText13.Enable(False)
            self.spinCtrl1.Enable(False)
            self.textPatron.Enable(False)
            self.choice1.Enable(False)
            self.textDelimitador.Enable(False)
            self.choiceDigito.Enable(False)
            self.choiceDigito2.Enable(False)

    # Evento cambio lista delimitador
    def OnChoice1Choice(self, event):
        if self.choice1.GetStringSelection()=="No":
            self.textDelimitador.Enable(False)
        else:
            self.textDelimitador.Enable(True)

    # Evento cambio lista digito de control
    def OnChoiceDigitoChoice(self, event):
        if self.choiceDigito.GetStringSelection()=="No":
            self.choiceDigito2.Enable(False)
        else:
            self.choiceDigito2.Enable(True)

    # Evento cambio checkbox numero paginas indeterminado
    def OnCheckPagVariableCheckbox(self, event):
        if self.checkPagVariable.IsChecked():
            self.pagsCuest.Enable(False)
        else:
            self.pagsCuest.Enable(True)



# Fin eventos
