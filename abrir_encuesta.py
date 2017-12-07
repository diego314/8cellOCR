#Boa:Frame:Frame1

import wx
import os
import sys
#import MySQLdb
import funciones
import sqlite3

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTABRIR, wxID_FRAME1BUTCANCELAR,
 wxID_FRAME1LISTAENCUESTAS, wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1,
 wxID_FRAME1TEXTPASS,
] = [wx.NewId() for _init_ctrls in range(7)]

class Frame1(wx.Frame):

    # Inicio base de datos
    conn = sqlite3.connect(sys.path[0]+'/bbdd.db')
    conn.row_factory = sqlite3.Row
    cursor=conn.cursor()

    def _init_coll_sizerPrincipal_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.listaEncuestas, 0, border=2, flag=wx.ALL)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddSizer(self.gridBagSizer1, 2, border=2,
              flag=wx.EXPAND | wx.ALL)

    def _init_coll_gridBagSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.staticText1, (0, 0), border=0, flag=0, span=(1,1))
        parent.AddWindow(self.textPass, (0, 1), border=0, flag=0, span=(1, 1))
        parent.AddWindow(self.butAbrir, (1, 0), border=0, flag=wx.ALIGN_CENTER,
              span=(1, 1))
        parent.AddWindow(self.butCancelar, (1, 1), border=0,
              flag=wx.ALIGN_CENTER, span=(1, 1))

    def _init_sizers(self):
        # generated method, don't edit
        self.sizerPrincipal = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.gridBagSizer1 = wx.GridBagSizer(hgap=5, vgap=5)

        self._init_coll_sizerPrincipal_Items(self.sizerPrincipal)
        self._init_coll_gridBagSizer1_Items(self.gridBagSizer1)

        self.panel1.SetSizer(self.sizerPrincipal)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(510, 258), size=wx.Size(372, 274),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Abrir encuesta')
        self.SetClientSize(wx.Size(372, 274))
        self.SetIcon(wx.Icon(sys.path[0]+"/"+u'Edit.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(372, 274),
              style=wx.TAB_TRAVERSAL)
        self.panel1.Bind(wx.EVT_KEY_DOWN, self.OnFrame1KeyDown)

        self.listaEncuestas = wx.ListBox(choices=[],
              id=wxID_FRAME1LISTAENCUESTAS, name=u'listaEncuestas',
              parent=self.panel1, pos=wx.Point(2, 2), size=wx.Size(150, 267),
              style=0)
        self.listaEncuestas.SetBestFittingSize(wx.Size(150, 267))
        self.listaEncuestas.SetLabel(u'')
        self.listaEncuestas.Bind(wx.EVT_LEFT_DCLICK,
              self.OnListaEncuestasLeftDclick)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Contrase\xf1a', name='staticText1', parent=self.panel1,
              pos=wx.Point(164, 2), size=wx.Size(80, 17), style=0)
        self.staticText1.SetBestFittingSize(wx.Size(80, 17))

        self.textPass = wx.TextCtrl(id=wxID_FRAME1TEXTPASS, name=u'textPass',
              parent=self.panel1, pos=wx.Point(262, 2), size=wx.Size(107, 27),
              style=0, value=u'')

        self.butAbrir = wx.Button(id=wxID_FRAME1BUTABRIR, label=u'Abrir',
              name=u'butAbrir', parent=self.panel1, pos=wx.Point(164, 34),
              size=wx.Size(93, 34), style=0)
        self.butAbrir.Bind(wx.EVT_BUTTON, self.OnButAbrirButton,
              id=wxID_FRAME1BUTABRIR)

        self.butCancelar = wx.Button(id=wxID_FRAME1BUTCANCELAR,
              label=u'Cancelar', name=u'butCancelar', parent=self.panel1,
              pos=wx.Point(269, 34), size=wx.Size(93, 34), style=0)
        self.butCancelar.Bind(wx.EVT_BUTTON, self.OnButCancelarButton,
              id=wxID_FRAME1BUTCANCELAR)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.MakeModal(True)
        self.ventanaPadre=parent
        self.Bind(wx.EVT_CLOSE, self.on_close)

        sql='SELECT * FROM Encuestas'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            self.listaEncuestas.Append(registro["Nombre"])
        self.Centre()
        self.panel1.SetFocus()

    def on_close(self, event):
        self.MakeModal(False)
        #self.db.close()
        event.Skip()

# botones

    # boton abrir
    def OnButAbrirButton(self, event):
        self.eventoAbrir()

	# boton cancelar
    def OnButCancelarButton(self, event):
        self.Close()
        self.Destroy()

    def OnListaEncuestasLeftDclick(self, event):
        self.eventoAbrir()

    def eventoAbrir(self):
        #elementos=self.listaEncuestas.GetSelections()
        seleccionado = self.listaEncuestas.GetStringSelection()
        if seleccionado=="":
            funciones.mensaje(self,"Primero debe seleccionar una encuesta")
        else:
            sql='SELECT * FROM Encuestas WHERE Nombre="'+seleccionado+'"'
            self.cursor.execute(sql)
            resultado=self.cursor.fetchall()
            contrasenya=""
            tempNombre=seleccionado
            for registro in resultado:
                contrasenya=registro["Password"]
                tempNombre=registro["Nombre"]
            if contrasenya==self.textPass.GetValue() or contrasenya=="":
                #funciones.mensaje(self,tempNombre)
                self.ventanaPadre.ActivarControles(tempNombre)
                self.Close()
                self.Destroy()
            else:
                funciones.mensaje(self,"La contrasena es incorrecta")

    def OnFrame1KeyDown(self, event):
        keyCode = event.GetKeyCode()
        #funciones.mensaje(self,str(keyCode))
        if keyCode == wx.WXK_ESCAPE:
            self.Close()
            self.Destroy()
