# coding: utf-8
#Boa:Frame:ventanaOcr

import wx
from wx.lib.anchors import LayoutAnchors
import wx.lib.scrolledpanel
import os
import glob
import sys
#import MySQLdb
import op_encuesta
import abrir_encuesta
#import abrir_opc_ocr
import editar_bbdd
import funciones
import datetime
import rubberband
import re
import sqlite3
#import crop
#import wxWidgets

def create(parent):
    return ventanaOcr(parent)

[wxID_VENTANAOCR, wxID_VENTANAOCRAREABORRAR, wxID_VENTANAOCRAREAXY,
 wxID_VENTANAOCRBOTONOCR, wxID_VENTANAOCRBOTONOPCIONES,
 wxID_VENTANAOCRBOTONPRUEBA, wxID_VENTANAOCRBOTONSALIR,
 wxID_VENTANAOCRBUTOCRDEL, wxID_VENTANAOCRBUTTON1, wxID_VENTANAOCRBUTTON8,
 wxID_VENTANAOCRBUTTON9, wxID_VENTANAOCRBUTTONOCRNEW,
 wxID_VENTANAOCRBUTTONOCRSAVE, wxID_VENTANAOCRCHECKCONTRASTE,
 wxID_VENTANAOCRCHOICEETIQUETA, wxID_VENTANAOCRCHOICEOCR,
 wxID_VENTANAOCRCHOICEROTAR, wxID_VENTANAOCRCHOICERUIDO,
 wxID_VENTANAOCRCHOICEZOOM, wxID_VENTANAOCRDATEPICKERCTRL1,
 wxID_VENTANAOCRENCABRIR, wxID_VENTANAOCRENCBORRAR, wxID_VENTANAOCRENCDATOS,
 wxID_VENTANAOCRENCNUEVA, wxID_VENTANAOCRLISTBOX1, wxID_VENTANAOCRPANEL1,
 wxID_VENTANAOCRSCROLLEDPANEL1, wxID_VENTANAOCRSLIDER1,
 wxID_VENTANAOCRSTATICBITMAP1, wxID_VENTANAOCRSTATICBOXOCR,
 wxID_VENTANAOCRSTATICTEXT1, wxID_VENTANAOCRSTATICTEXT2,
 wxID_VENTANAOCRSTATICTEXT4, wxID_VENTANAOCRSTATUSBAR1,
 wxID_VENTANAOCRTEXTCTRL1, wxID_VENTANAOCRTEXTCTRL2,
 wxID_VENTANAOCRTEXTETIQUETA,
] = [wx.NewId() for _init_ctrls in range(37)]

[wxID_VENTANAOCRMENUARCHIVOITEMS0, wxID_VENTANAOCRMENUARCHIVOITEMS1,
] = [wx.NewId() for _init_coll_menuArchivo_Items in range(2)]

[wxID_VENTANAOCRMENUAYUDAACERCA] = [wx.NewId() for _init_coll_menuAyuda_Items in range(1)]

class ventanaOcr(wx.Frame):

# Inicio definicion de variables

    imagenes=list()
    imagenesRutas=list()
    choicesOpciones=list()
    encuestaActiva=""

    OriginalW=0
    OriginalH=0
    proporcion=1

    marcando=0
    areaMarcada=""

    # Inicio base de datos
    conn = sqlite3.connect(sys.path[0]+'/bbdd.db')
    conn.row_factory = sqlite3.Row
    cursor=conn.cursor()

# Fin definicion de variables

    def _init_coll_staticBoxSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.choiceRuido, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.choiceZoom, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.checkContraste, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.slider1, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.choiceRotar, 0, border=0, flag=0)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddWindow(self.choiceOcr, 0, border=0, flag=0)
        parent.AddSizer(self.sizerBotocr, 0, border=0, flag=0)

    def _init_coll_sizerCentral_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.listBox1, 1, border=2, flag=wx.EXPAND | wx.ALL)
        parent.AddSizer(self.sizerCentroAbajo, 0, border=0, flag=wx.EXPAND)

    def _init_coll_sizerBotocr_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.buttonOcrNew, 0, border=0, flag=0)
        parent.AddWindow(self.buttonOcrSave, 0, border=0, flag=0)
        parent.AddWindow(self.butOcrDel, 0, border=0, flag=0)

    def _init_coll_sizerCentroAbajo_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button9, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.button8, 0, border=2,
              flag=wx.ALIGN_RIGHT | wx.ALL)

    def _init_coll_sizerDerecho1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.scrolledPanel1, 1, border=0, flag=wx.EXPAND)

    def _init_coll_sizerDerecho3_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.staticText1, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.textCtrl2, 0, border=2, flag=wx.ALL)

    def _init_coll_sizerDerecho25_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.botonPrueba, 0, border=2, flag=wx.ALL)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddWindow(self.botonOCR, 0, border=2, flag=wx.ALL)

    def _init_coll_sizerPrincipal_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.sizerIzquierdo, 0, border=0, flag=0)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddSizer(self.sizerCentral, 0, border=0, flag=wx.EXPAND)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddSizer(self.sizerDerecho, 1, border=0, flag=wx.EXPAND)

    def _init_coll_sizerIzquierdo_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.sizerNewOpen, 0, border=2, flag=wx.ALL)
        parent.AddSpacer(wx.Size(60, 5), border=0, flag=0)
        parent.AddWindow(self.button1, 0, border=2, flag=wx.ALL | wx.EXPAND)
        parent.AddSpacer(wx.Size(60, 5), border=0, flag=0)
        parent.AddSizer(self.staticBoxSizer1, 0, border=0, flag=0)
        parent.AddSpacer(wx.Size(60, 5), border=0, flag=0)
        parent.AddWindow(self.staticText2, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.choiceEtiqueta, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.textEtiqueta, 0, border=2, flag=wx.ALL)
        parent.AddSpacer(wx.Size(60, 5), border=0, flag=0)
        parent.AddWindow(self.staticText4, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.datePickerCtrl1, 0, border=2, flag=wx.ALL)

    def _init_coll_sizerNewOpen_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.encNueva, 0, border=0, flag=0)
        parent.AddWindow(self.encAbrir, 0, border=0, flag=0)
        parent.AddWindow(self.encBorrar, 0, border=0, flag=0)
        parent.AddWindow(self.botonOpciones, 0, border=0, flag=0)
        parent.AddWindow(self.encDatos, 0, border=0, flag=0)
        parent.AddWindow(self.botonSalir, 0, border=0, flag=0)

    def _init_coll_sizerDerecho2_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.areaBorrar, 0, border=0, flag=0)
        parent.AddWindow(self.areaxy, 0, border=0, flag=0)

    def _init_coll_sizerDerecho_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.sizerDerecho1, 1, border=2,
              flag=wx.EXPAND | wx.ALL)
        parent.AddSizer(self.sizerDerecho2, 0, border=0, flag=0)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddSizer(self.sizerDerecho25, 0, border=0, flag=0)
        parent.AddWindow(self.textCtrl1, 0, border=2, flag=wx.EXPAND | wx.ALL)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddSizer(self.sizerDerecho3, 0, border=0, flag=0)

    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuArchivo, title=u'Sesion')
        parent.Append(menu=self.menuAyuda, title=u'Ayuda')

    def _init_coll_menuArchivo_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_VENTANAOCRMENUARCHIVOITEMS0,
              kind=wx.ITEM_NORMAL, text=u'Nuevo')
        parent.Append(help='', id=wxID_VENTANAOCRMENUARCHIVOITEMS1,
              kind=wx.ITEM_NORMAL, text=u'Abrir')

    def _init_coll_menuAyuda_Items(self, parent):
        # generated method, don't edit

        parent.Append(help=u'Sobre \xe9ste programa',
              id=wxID_VENTANAOCRMENUAYUDAACERCA, kind=wx.ITEM_NORMAL,
              text=u'Acerca De...')
        self.Bind(wx.EVT_MENU, self.OnMenuAyudaAcercaMenu,
              id=wxID_VENTANAOCRMENUAYUDAACERCA)

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text=u'Estado')

        parent.SetStatusWidths([-1])

    def _init_sizers(self):
        # generated method, don't edit
        self.sizerPrincipal = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.sizerIzquierdo = wx.BoxSizer(orient=wx.VERTICAL)
        self.sizerIzquierdo.SetMinSize(wx.Size(170, 300))

        self.sizerCentral = wx.BoxSizer(orient=wx.VERTICAL)
        self.sizerCentral.SetMinSize(wx.Size(20, 20))

        self.sizerDerecho = wx.BoxSizer(orient=wx.VERTICAL)
        self.sizerDerecho.SetMinSize(wx.Size(20, 20))

        self.sizerCentroAbajo = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.sizerDerecho2 = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.sizerDerecho1 = wx.BoxSizer(orient=wx.VERTICAL)
        self.sizerDerecho1.SetMinSize(wx.Size(150, 150))

        self.sizerNewOpen = wx.GridSizer(cols=2, hgap=0, rows=3, vgap=0)

        self.staticBoxSizer1 = wx.StaticBoxSizer(box=self.staticBoxOCR,
              orient=wx.VERTICAL)

        self.sizerBotocr = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.scrollSizer = wx.BoxSizer(orient=wx.VERTICAL)

        self.sizerDerecho3 = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.sizerDerecho25 = wx.BoxSizer(orient=wx.HORIZONTAL)

        self._init_coll_sizerPrincipal_Items(self.sizerPrincipal)
        self._init_coll_sizerIzquierdo_Items(self.sizerIzquierdo)
        self._init_coll_sizerCentral_Items(self.sizerCentral)
        self._init_coll_sizerDerecho_Items(self.sizerDerecho)
        self._init_coll_sizerCentroAbajo_Items(self.sizerCentroAbajo)
        self._init_coll_sizerDerecho2_Items(self.sizerDerecho2)
        self._init_coll_sizerDerecho1_Items(self.sizerDerecho1)
        self._init_coll_sizerNewOpen_Items(self.sizerNewOpen)
        self._init_coll_staticBoxSizer1_Items(self.staticBoxSizer1)
        self._init_coll_sizerBotocr_Items(self.sizerBotocr)
        self._init_coll_sizerDerecho3_Items(self.sizerDerecho3)
        self._init_coll_sizerDerecho25_Items(self.sizerDerecho25)

        self.panel1.SetSizer(self.sizerPrincipal)
        self.scrolledPanel1.SetSizer(self.scrollSizer)

    def _init_utils(self):
        # generated method, don't edit
        self.menuArchivo = wx.Menu(title=u'')

        self.menuAyuda = wx.Menu(title=u'Ayuda')

        self.menuBar1 = wx.MenuBar()

        self._init_coll_menuArchivo_Items(self.menuArchivo)
        self._init_coll_menuAyuda_Items(self.menuAyuda)
        self._init_coll_menuBar1_Menus(self.menuBar1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_VENTANAOCR, name=u'ventanaOcr',
              parent=prnt, pos=wx.Point(308, 60), size=wx.Size(798, 635),
              style=wx.DEFAULT_FRAME_STYLE, title=u'8-cell OCR')
        self._init_utils()
        self.SetClientSize(wx.Size(798, 635))
        self.SetMenuBar(self.menuBar1)
        self.SetIcon(wx.Icon(sys.path[0]+"/"+u'Edit.ico',wx.BITMAP_TYPE_ICO))

        self.statusBar1 = wx.StatusBar(id=wxID_VENTANAOCRSTATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.panel1 = wx.Panel(id=wxID_VENTANAOCRPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(798, 610),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_VENTANAOCRBUTTON1,
              label=u'Seleccionar im\xe1genes', name='button1',
              parent=self.panel1, pos=wx.Point(2, 113), size=wx.Size(196, 34),
              style=0)
        self.button1.Enable(False)
        self.button1.SetBestFittingSize(wx.Size(185, 34))
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_VENTANAOCRBUTTON1)

        self.botonOpciones = wx.Button(id=wxID_VENTANAOCRBOTONOPCIONES,
              label=u'Opciones', name='botonOpciones', parent=self.panel1,
              pos=wx.Point(95, 36), size=wx.Size(93, 34), style=0)
        self.botonOpciones.Enable(False)
        self.botonOpciones.SetBestFittingSize(wx.Size(93, 34))
        self.botonOpciones.SetHelpText(u'')
        self.botonOpciones.Bind(wx.EVT_BUTTON, self.OnBotonOpcionesButton,
              id=wxID_VENTANAOCRBOTONOPCIONES)

        self.button9 = wx.Button(id=wxID_VENTANAOCRBUTTON9, label=u'Borrar',
              name='button9', parent=self.panel1, pos=wx.Point(210, 574),
              size=wx.Size(95, 34), style=0)
        self.button9.Enable(False)
        self.button9.Bind(wx.EVT_BUTTON, self.OnButton9Button,
              id=wxID_VENTANAOCRBUTTON9)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_VENTANAOCRLISTBOX1,
              name='listBox1', parent=self.panel1, pos=wx.Point(210, 2),
              size=wx.Size(200, 568), style=0)
        self.listBox1.SetMinSize(wx.Size(200, 264))
        self.listBox1.Bind(wx.EVT_LISTBOX, self.OnListBox1Listbox,
              id=wxID_VENTANAOCRLISTBOX1)

        self.textCtrl1 = wx.TextCtrl(id=wxID_VENTANAOCRTEXTCTRL1,
              name='textCtrl1', parent=self.panel1, pos=wx.Point(422, 409),
              size=wx.Size(374, 160), style=wx.TE_MULTILINE, value=u'')
        self.textCtrl1.SetAutoLayout(False)
        self.textCtrl1.SetMinSize(wx.Size(141, 200))
        self.textCtrl1.SetBestFittingSize(wx.Size(302, 160))

        self.button8 = wx.Button(id=wxID_VENTANAOCRBUTTON8, label=u'Limpiar',
              name='button8', parent=self.panel1, pos=wx.Point(309, 574),
              size=wx.Size(95, 34), style=0)
        self.button8.Enable(False)
        self.button8.Bind(wx.EVT_BUTTON, self.OnButton8Button,
              id=wxID_VENTANAOCRBUTTON8)

        self.encNueva = wx.Button(id=wxID_VENTANAOCRENCNUEVA, label=u'Nueva',
              name=u'encNueva', parent=self.panel1, pos=wx.Point(2, 2),
              size=wx.Size(93, 34), style=0)
        self.encNueva.Bind(wx.EVT_BUTTON, self.OnEncNuevaButton,
              id=wxID_VENTANAOCRENCNUEVA)

        self.encAbrir = wx.Button(id=wxID_VENTANAOCRENCABRIR, label=u'Abrir',
              name=u'encAbrir', parent=self.panel1, pos=wx.Point(95, 2),
              size=wx.Size(93, 34), style=0)
        self.encAbrir.Bind(wx.EVT_BUTTON, self.OnEncAbrirButton,
              id=wxID_VENTANAOCRENCABRIR)

        self.checkContraste = wx.CheckBox(id=wxID_VENTANAOCRCHECKCONTRASTE,
              label=u'Ajustar contraste (70%)', name=u'checkContraste',
              parent=self.panel1, pos=wx.Point(7, 239), size=wx.Size(184, 22),
              style=0)
        self.checkContraste.SetValue(False)
        self.checkContraste.Enable(False)
        self.checkContraste.Bind(wx.EVT_CHECKBOX, self.OnCheckContrasteCheckbox,
              id=wxID_VENTANAOCRCHECKCONTRASTE)

        self.slider1 = wx.Slider(id=wxID_VENTANAOCRSLIDER1, maxValue=99,
              minValue=1, name='slider1', parent=self.panel1, pos=wx.Point(7,
              265), size=wx.Size(184, 19), style=wx.SL_HORIZONTAL, value=70)
        self.slider1.SetLabel(u'')
        self.slider1.Enable(False)
        self.slider1.Bind(wx.EVT_SCROLL, self.OnSlider1Scroll)

        self.encDatos = wx.Button(id=wxID_VENTANAOCRENCDATOS, label=u'BBDD',
              name=u'encDatos', parent=self.panel1, pos=wx.Point(2, 70),
              size=wx.Size(93, 34), style=0)
        self.encDatos.Enable(False)
        self.encDatos.Bind(wx.EVT_BUTTON, self.OnEncDatosButton,
              id=wxID_VENTANAOCRENCDATOS)

        self.encBorrar = wx.Button(id=wxID_VENTANAOCRENCBORRAR, label=u'Borrar',
              name=u'encBorrar', parent=self.panel1, pos=wx.Point(2, 36),
              size=wx.Size(93, 34), style=0)
        self.encBorrar.Enable(False)
        self.encBorrar.Bind(wx.EVT_BUTTON, self.OnEncBorrarButton,
              id=wxID_VENTANAOCRENCBORRAR)

        self.staticBoxOCR = wx.StaticBox(id=wxID_VENTANAOCRSTATICBOXOCR,
              label=u'Opciones OCR', name=u'staticBoxOCR', parent=self.panel1,
              pos=wx.Point(0, 154), size=wx.Size(200, 237), style=0)
        self.staticBoxOCR.SetBestFittingSize(wx.Size(209, 131))
        self.staticBoxOCR.SetMinSize(wx.Size(200, 131))

        self.buttonOcrSave = wx.Button(id=wxID_VENTANAOCRBUTTONOCRSAVE,
              label=u'Guardar', name=u'buttonOcrSave', parent=self.panel1,
              pos=wx.Point(70, 352), size=wx.Size(65, 34), style=0)
        self.buttonOcrSave.SetBestFittingSize(wx.Size(65, 34))
        self.buttonOcrSave.Enable(False)
        self.buttonOcrSave.Bind(wx.EVT_BUTTON, self.OnButtonOcrSaveButton,
              id=wxID_VENTANAOCRBUTTONOCRSAVE)

        self.butOcrDel = wx.Button(id=wxID_VENTANAOCRBUTOCRDEL, label=u'Borrar',
              name=u'butOcrDel', parent=self.panel1, pos=wx.Point(135, 352),
              size=wx.Size(60, 34), style=0)
        self.butOcrDel.Enable(False)
        self.butOcrDel.Bind(wx.EVT_BUTTON, self.OnButOcrDelButton,
              id=wxID_VENTANAOCRBUTOCRDEL)

        self.scrolledPanel1 = wx.lib.scrolledpanel.ScrolledPanel(id=wxID_VENTANAOCRSCROLLEDPANEL1,
              name='scrolledPanel1', parent=self.panel1, pos=wx.Point(422, 2),
              size=wx.Size(374, 323), style=wx.TAB_TRAVERSAL)
        self.scrolledPanel1.SetBestFittingSize(wx.Size(349, 275))
        self.scrolledPanel1.Bind(wx.EVT_MOUSEWHEEL,
              self.scrolledPanel1Mousewheel)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_VENTANAOCRSTATICBITMAP1, name='staticBitmap1',
              parent=self.scrolledPanel1, pos=wx.Point(0, 0), size=wx.Size(344,
              304), style=wx.VSCROLL | wx.HSCROLL | wx.SIMPLE_BORDER)
        self.staticBitmap1.Bind(wx.EVT_LEFT_UP, self.OnStaticBitmap1LeftUp)

        self.areaBorrar = wx.Button(id=wxID_VENTANAOCRAREABORRAR,
              label=u'Reset', name=u'areaBorrar', parent=self.panel1,
              pos=wx.Point(420, 327), size=wx.Size(65, 34), style=0)
        self.areaBorrar.SetBestFittingSize(wx.Size(65, 34))
        self.areaBorrar.Enable(False)
        self.areaBorrar.Bind(wx.EVT_BUTTON, self.OnAreaBorrarButton,
              id=wxID_VENTANAOCRAREABORRAR)

        self.areaxy = wx.StaticText(id=wxID_VENTANAOCRAREAXY, label=u'',
              name=u'areaxy', parent=self.panel1, pos=wx.Point(485, 327),
              size=wx.Size(68, 17), style=0)

        self.staticText1 = wx.StaticText(id=wxID_VENTANAOCRSTATICTEXT1,
              label=u'Identificador encontrado:', name='staticText1',
              parent=self.panel1, pos=wx.Point(422, 581), size=wx.Size(162, 17),
              style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_VENTANAOCRTEXTCTRL2,
              name='textCtrl2', parent=self.panel1, pos=wx.Point(588, 581),
              size=wx.Size(128, 27), style=0, value=u'')

        self.choiceZoom = wx.Choice(choices=["zoom 50%", "zoom 100%",
              "zoom 200%"], id=wxID_VENTANAOCRCHOICEZOOM, name=u'choiceZoom',
              parent=self.panel1, pos=wx.Point(7, 206), size=wx.Size(153, 29),
              style=0)
        self.choiceZoom.Enable(False)

        self.choiceRotar = wx.Choice(choices=["No rotar", "90", "180", "270"],
              id=wxID_VENTANAOCRCHOICEROTAR, name=u'choiceRotar',
              parent=self.panel1, pos=wx.Point(5, 286), size=wx.Size(153, 29),
              style=0)
        self.choiceRotar.SetBestFittingSize(wx.Size(153, 29))
        self.choiceRotar.Enable(False)

        self.botonSalir = wx.Button(id=wxID_VENTANAOCRBOTONSALIR,
              label=u'Salir', name=u'botonSalir', parent=self.panel1,
              pos=wx.Point(95, 70), size=wx.Size(93, 34), style=0)
        self.botonSalir.SetBestFittingSize(wx.Size(93, 34))
        self.botonSalir.Bind(wx.EVT_BUTTON, self.OnBotonSalirButton,
              id=wxID_VENTANAOCRBOTONSALIR)

        self.choiceEtiqueta = wx.Choice(choices=[],
              id=wxID_VENTANAOCRCHOICEETIQUETA, name=u'choiceEtiqueta',
              parent=self.panel1, pos=wx.Point(2, 419), size=wx.Size(153, 29),
              style=0)
        self.choiceEtiqueta.SetBestFittingSize(wx.Size(153, 29))
        self.choiceEtiqueta.Enable(False)
        self.choiceEtiqueta.Bind(wx.EVT_CHOICE, self.OnChoiceEtiquetaChoice,
              id=wxID_VENTANAOCRCHOICEETIQUETA)

        self.textEtiqueta = wx.TextCtrl(id=wxID_VENTANAOCRTEXTETIQUETA,
              name=u'textEtiqueta', parent=self.panel1, pos=wx.Point(2, 452),
              size=wx.Size(153, 27), style=0, value=u'')
        self.textEtiqueta.SetBestFittingSize(wx.Size(153, 27))
        self.textEtiqueta.Enable(False)

        self.choiceRuido = wx.Choice(choices=["Sin antiruido", "Nivel1",
              "Nivel 5", "Nivel 10"], id=wxID_VENTANAOCRCHOICERUIDO,
              name=u'choiceRuido', parent=self.panel1, pos=wx.Point(7, 173),
              size=wx.Size(153, 29), style=0)
        self.choiceRuido.SetBestFittingSize(wx.Size(153, 29))
        self.choiceRuido.Enable(False)
        self.choiceRuido.SetSelection(0)

        self.botonPrueba = wx.Button(id=wxID_VENTANAOCRBOTONPRUEBA,
              label=u'Prueba', name=u'botonPrueba', parent=self.panel1,
              pos=wx.Point(422, 371), size=wx.Size(85, 34), style=0)
        self.botonPrueba.SetBestFittingSize(wx.Size(85, 34))
        self.botonPrueba.Enable(False)
        self.botonPrueba.Bind(wx.EVT_BUTTON, self.OnBotonPruebaButton,
              id=wxID_VENTANAOCRBOTONPRUEBA)

        self.botonOCR = wx.Button(id=wxID_VENTANAOCRBOTONOCR,
              label=u'Hacer OCR', name=u'botonOCR', parent=self.panel1,
              pos=wx.Point(519, 371), size=wx.Size(105, 34), style=0)
        self.botonOCR.SetBestFittingSize(wx.Size(105, 34))
        self.botonOCR.Enable(False)
        self.botonOCR.Bind(wx.EVT_BUTTON, self.OnBotonOCRButton,
              id=wxID_VENTANAOCRBOTONOCR)

        self.staticText2 = wx.StaticText(id=wxID_VENTANAOCRSTATICTEXT2,
              label=u'Etiquetas:', name='staticText2', parent=self.panel1,
              pos=wx.Point(2, 398), size=wx.Size(65, 17), style=0)

        self.staticText4 = wx.StaticText(id=wxID_VENTANAOCRSTATICTEXT4,
              label=u'Fecha escaneado', name='staticText4', parent=self.panel1,
              pos=wx.Point(2, 488), size=wx.Size(112, 17), style=0)

        self.datePickerCtrl1 = wx.DatePickerCtrl(id=wxID_VENTANAOCRDATEPICKERCTRL1,
              name='datePickerCtrl1', parent=self.panel1, pos=wx.Point(2, 509),
              size=wx.Size(126, 27), style=wx.DP_SHOWCENTURY)

        self.choiceOcr = wx.Choice(choices=[], id=wxID_VENTANAOCRCHOICEOCR,
              name=u'choiceOcr', parent=self.panel1, pos=wx.Point(5, 323),
              size=wx.Size(153, 29), style=0)
        self.choiceOcr.SetBestFittingSize(wx.Size(153, 29))
        self.choiceOcr.Enable(False)
        self.choiceOcr.Bind(wx.EVT_CHOICE, self.OnChoiceOcrChoice,
              id=wxID_VENTANAOCRCHOICEOCR)

        self.buttonOcrNew = wx.Button(id=wxID_VENTANAOCRBUTTONOCRNEW,
              label=u'Nuevo', name=u'buttonOcrNew', parent=self.panel1,
              pos=wx.Point(5, 352), size=wx.Size(65, 34), style=0)
        self.buttonOcrNew.SetMinSize(wx.Size(65, 34))
        self.buttonOcrNew.Bind(wx.EVT_BUTTON, self.OnButtonOcrNewButton,
              id=wxID_VENTANAOCRBUTTONOCRNEW)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Centre()
        self.scrollSizer.Add(self.staticBitmap1 , 0, wx.ALL, 0)
        self.scrolledPanel1.SetupScrolling()
        self.choiceZoom.SetSelection ( 1 )
        self.rubberBand = rubberband.RubberBand(drawingSurface=self.staticBitmap1)

    def on_close(self, event):
        self.conn.close()
        event.Skip()


# Inicio menus

    # Menu ayuda
    def OnMenuAyudaAcercaMenu(self, event):
        dlg = wx.MessageDialog(self, 'OCR 8Cell, Diego Martinez Blanco para Dephimatica S.A.', 'About', wx.OK | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
        finally:
            dlg.Destroy()

# Fin menus


# Inicio botones

    # Boton elegir imagenes
    def OnButton1Button(self, event):
        dlg = wx.FileDialog(self, 'Elija las imagenes que desee anadir', '.', '', 'Imagenes|*.gif;*.jpg;*.jpeg;*.png;*.bmp;*.tif|Todos los ficheros |*.*', wx.OPEN| wx.MULTIPLE)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                rutas = dlg.GetFilenames()
                for selection in rutas:
                    self.listBox1.Append(selection)
                nombres = dlg.GetPaths()
                ruta=dlg.GetDirectory()
                for selection in nombres:
                    self.imagenes.append(selection)
                    self.imagenesRutas.append(ruta)
                #self.textRuta.Clear()
                #self.textRuta.AppendText(dlg.GetDirectory())
        finally:
            dlg.Destroy()
        self.button8.Enable(True)
        self.button9.Enable(True)

    # boton anyadir carpeta (eliminado)
    """
    def OnBotonCarpetaButton(self, event):
        dlg = wx.DirDialog(self, "elija una carpeta", sys.path[0])
        try:
            if dlg.ShowModal() == wx.ID_OK:
                path = dlg.GetPath()
                ficheros=glob.glob(os.path.join(path, '*.*'))
                ficheros.sort()
                for fichero in ficheros:
                    a=len(path)
                    nombre=fichero[a+1:len(fichero)]
                    extension=fichero[-3:]
                    if extension=="jpg" or extension=="gif" or extension=="tif" or extension=="png":
                        self.listBox1.Append(nombre)
                        self.imagenes.append(fichero)
        finally:
            dlg.Destroy()
        self.button8.Enable(True)
        self.button9.Enable(True)
    """

    # Boton prueba
    def OnBotonPruebaButton(self, event):
        self.textCtrl1.Clear()
        seleccionado = self.listBox1.GetSelection()
        #dlg = wx.MessageDialog(self, 'Procesando...', 'Caption', wx.PD_ELAPSED_TIME)
        #dlg.ShowModal()

        self.preprocesarImagen(self.imagenes[seleccionado])

        # Hacer OCR
        funciones.ejecutar("tesseract 'temp.tif' '"+sys.path[0]+"/prueba' -l spa")
        fichero = open(sys.path[0]+"/prueba.txt", "r")

        textoOCR=fichero.read()

        self.textCtrl1.AppendText(textoOCR)

        sql='SELECT * FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'"'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        patronId=resultado[0]["PatronId"]

        sql='SELECT OptIdentificador FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'"'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            optIdentificador= str(registro["OptIdentificador"])
        idEncontrados,identificador=self.buscarIdentificador(textoOCR, patronId, optIdentificador)
        #funciones.mensaje(self,textoOCR+" "+patronId+" "+optIdentificador)

        fichero.close()
        self.textCtrl1.ShowPosition(0)
        if idEncontrados==0:
            identificador="ninguno"
        self.textCtrl2.SetValue(identificador)

        self.borrarImgTemporales()
        #dlg.Destroy()

    # hacer OCR de toda la lista
    def OnBotonOCRButton(self, event):
        '''
        if self.textRuta.GetValue()[0:1]!="/":
            funciones.mensaje(self,"El primer caracter de la ruta debe ser una barra inclinada \"/\"")
        elif self.textRuta.GetValue()[-1:]=="/":
            funciones.mensaje(self,"El ultimo caracter de la ruta no puede ser una barra inclinada \"/\"")
        else:
        '''
        self.textCtrl1.Clear()
        #Mostrar dialogo "procesando"
        #dlg = wx.MessageDialog(self, 'Procesando...', 'Caption', wx.PD_ELAPSED_TIME)
        #dlg.ShowModal()
        textoError=""

        sql='SELECT * FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'"'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        patronId=resultado[0]["PatronId"]
        digitoControl=resultado[0]["DigitoControl"]
        rutaBase=resultado[0]["RutaBase"]

        sql='UPDATE Hojas SET Actual=0 WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'")'
        self.cursor.execute(sql)
        self.conn.commit()

        identificadorActual="0"
        identificadorAnterior=""
        paginaActual=0
        for indice in range(self.listBox1.GetCount()):
            #si hemos llegado al numero de paginas por cuestionario, empezamos uno nuevo
            paginaActual+=1

            self.preprocesarImagen(self.imagenes[indice])

            #crear directorios, si no existen
            if rutaBase in self.imagenesRutas[indice]:
                rutaInicial=self.imagenesRutas[indice]
                posicionRuta=rutaInicial.find(rutaBase)
                #posicionRuta=posicionRuta+len(rutaBase)
                rutaResultado="/"+rutaInicial[posicionRuta:]
            else:
                rutaResultado=self.imagenesRutas[indice]

            funciones.ejecutar("mkdir -p $HOME'/Escritorio/Proyectos/"+self.encuestaActiva+rutaResultado+"/Originales'" )
            funciones.ejecutar("mkdir -p $HOME'/Escritorio/Proyectos/"+self.encuestaActiva+rutaResultado+"/PDF'" )

            # Hacer OCR
            funciones.ejecutar("tesseract 'temp.tif' '"+sys.path[0]+"/prueba' -l spa")
            fichero = open(sys.path[0]+"/prueba.txt", "r")
            textoOCR=fichero.read()

            sql='SELECT OptIdentificador FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'"'
            self.cursor.execute(sql)
            resultado=self.cursor.fetchall()
            for registro in resultado:
                optIdentificador= str(registro["OptIdentificador"])

            identificador=""
            #identificadorAnterior=""
            if optIdentificador[0]=="1":

                #buscar en textoOCR un identificador acorde a lo especificado en optIdentificador
                idEncontrados,identificador=self.buscarIdentificador(textoOCR, patronId, optIdentificador)

                if idEncontrados>=1:
                    identificadorActual=identificador

                #si el numero de paginas es variable, y hemos encontrado ID, empezamos un cuest. nuevo
                if idEncontrados>0 and identificadorActual!=identificadorAnterior:
                    paginaActual=1
                #si es el primer cuest, y no hemos encontrado id, devolvemos error
                elif (idEncontrados==0 and paginaActual==1):
                    identificador="error"
                    #generamos un identificador de error
                    ok=0
                    n=0
                    while ok==0:
                        n+=1
                        sql='SELECT * FROM Hojas WHERE Identificador="error_'+str(n)+'"'
                        self.cursor.execute(sql)
                        resultado=self.cursor.fetchall()
                        if self.cursor.rowcount==0:
                            ok=1
                    identificadorActual="error_"+str(n)
                    textoError+="No se ha detectado ningun identificador en la hoja numero "+str(indice+1)+"\r"

                if idEncontrados>=2:
                    textoError+="Se han encontrado "+str(idEncontrados)+" identificadores en la hoja numero "+str(indice+1)+"\r"
                    #comprobar digito de control
                    if digitoControl[0]=="1":
                        if not funciones.checkDigitoControl(identificador, digitoControl[1], digitoControl[0]):
                            textoError+="El digito de control del identificador en la hoja numero "+str(indice+1)+" es incorrecto\r"

                #si la pagina es la 1, comprobamos que el identificador encontrado no existe ya en la base de datos
                if paginaActual==1 and identificador!="error":
                    sql='SELECT * FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'") AND Identificador="'+identificador+'"'
                    self.cursor.execute(sql)
                    resultado=self.cursor.fetchall()
                    if self.cursor.rowcount>0:
                        textoError+="Se ha encontrado el identificador "+identificador+", que ya existe previamente en la base de datos\r"
                        ok=0
                        n=0
                        while ok==0:
                            n+=1
                            sql='SELECT * FROM Hojas WHERE Identificador="'+str(n)+"_"+identificador+'"'
                            self.cursor.execute(sql)
                            resultado=self.cursor.fetchall()
                            if self.cursor.rowcount==0:
                                ok=1
                        identificadorActual=str(n)+"_"+identificador


            sql='SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'"'
            self.cursor.execute(sql)
            resultado=self.cursor.fetchall()
            for registro in resultado:
                idTemp= str(registro["IDEncuesta"])

            if paginaActual==1: #asignamos un nuevo numero de cuestionario
                sql='SELECT MAX(CuestionarioNum) AS cuestMaxima FROM Hojas WHERE Encuesta="'+idTemp+'"'
                self.cursor.execute(sql)
                resultado=self.cursor.fetchall()
                for registro in resultado:
                    numCuest= str(registro["cuestMaxima"])
                if numCuest=="None":
                    numCuest="1"
                else:
                    numCuest=str(int(numCuest)+1)

            #etiquetas
            if self.choiceEtiqueta.GetSelection()==0:
                etiquetaNum=0
            elif self.choiceEtiqueta.GetSelection()==1:
                if self.textEtiqueta.GetValue()=="":
                    etiquetaNum=0
                else:
                    #insertar nueva etiqueta en tabla etiquetas
                    sql='SELECT IDEtiqueta FROM Etiquetas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'") AND Nombre="'+self.textEtiqueta.GetValue()+'"'
                    self.cursor.execute(sql)
                    resultado=self.cursor.fetchall()
                    if self.cursor.rowcount==0:
                        """
                        sql='SELECT MAX(IDEtiqueta) AS idMaxima FROM Etiquetas'
                        self.cursor.execute(sql)
                        resultado=self.cursor.fetchall()
                        if str(resultado[0]["idMaxima"])!="None":
                            idMaxima=resultado[0]["idMaxima"]
                        else:
                            idMaxima=0
                        """

                        sql='INSERT INTO Etiquetas (IDEtiqueta, Encuesta, Nombre)'
                        sql+=' VALUES ('
                        sql+=' (SELECT IDEncuesta FROM Encuestas'
                        sql+=' WHERE Nombre="'+self.encuestaActiva+'"), "'+self.textEtiqueta.GetValue()+'")'
                        #funciones.mensaje(self,sql)
                        self.cursor.execute(sql)
                        etiquetaNum=self.cursor.lastrowid
                        self.conn.commit()

                        #etiquetaNum=idMaxima+1
                    else:
                        etiquetaNum=resultado[0]["IDEtiqueta"]

            else:
                etiquetaStr=self.choiceEtiqueta.GetStringSelection()
                sql='SELECT IDEtiqueta FROM Etiquetas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'") AND Nombre="'+etiquetaStr+'"'
                self.cursor.execute(sql)
                resultado=self.cursor.fetchall()
                etiquetaNum=resultado[0]["IDEtiqueta"]
            #fin etiquetas

            """
            sql='SELECT MAX(IDHoja) AS idMaxima FROM Hojas'
            self.cursor.execute(sql)
            resultado=self.cursor.fetchall()
            for registro in resultado:
                idMaxima=str(registro["IDHoja"])
            if idMaxima=="None":
                idMaxima="1"
            else:
                idMaxima=str(int(idMaxima)+1)
            """

            fechaScan=self.datePickerCtrl1.GetValue().FormatISODate()

            textoOCR=textoOCR.replace('"',"'")
            sql='INSERT INTO Hojas '
            sql+='(Encuesta, CuestionarioNum, PaginaNum, Texto, Identificador, FechaScan, Actual, Etiqueta, Ruta) '
            sql+='VALUES ('+idTemp+' ,'+numCuest+' ,'+str(paginaActual)+' , "'+textoOCR+'","'+identificadorActual+'" ,"'+str(fechaScan)+'", 1, '+str(etiquetaNum)+', "'+str(rutaResultado)+'")'
            self.cursor.execute(sql)
            idMaxima=self.cursor.lastrowid
            self.conn.commit()

            if identificador=="":
                funciones.ejecutar("cp '"+self.imagenes[indice]+"' $HOME'/Escritorio/Proyectos/"+str(self.encuestaActiva)+rutaResultado+"/Originales/"+str(idMaxima)+self.imagenes[indice][-4:]+"'")
            else:
                funciones.ejecutar("cp '"+self.imagenes[indice]+"' $HOME'/Escritorio/Proyectos/"+str(self.encuestaActiva)+rutaResultado+"/Originales/"+identificadorActual+"_"+str(paginaActual)+self.imagenes[indice][-4:]+"'")

            #creamos el pdf de la anterior (?)
            if paginaActual==1 and identificadorAnterior!="" and identificadorAnterior!="-1":
                funciones.ejecutar("IFS=$'\n' && convert `ls -v $HOME'/Escritorio/Proyectos/"+str(self.encuestaActiva)+rutaResultado+"/Originales/'"+identificadorAnterior+"_*.*` $HOME'/Escritorio/Proyectos/"+str(self.encuestaActiva)+rutaResultado+"/PDF/"+identificadorAnterior+".pdf'")
            identificadorAnterior=identificadorActual

            #copiamos la imagen recortada
            funciones.ejecutar("cp 'temp.tif' '"+sys.path[0]+"/imagenes/"+str(idMaxima)+".tif'" )
            self.borrarImgTemporales()
            #dlg.Destroy()

            if paginaActual!=1 and idEncontrados>0 and identificadorActual!=identificadorAnterior:
                paginaActual=0
            ultimaRuta=rutaResultado

        #TODO: mejorar el sistema para aceptar varias imagenes con diferentes rutas
        funciones.ejecutar("IFS=$'\n' && convert `ls -v $HOME'/Escritorio/Proyectos/"+str(self.encuestaActiva)+ultimaRuta+"/Originales/'"+identificadorAnterior+"_*.*` $HOME'/Escritorio/Proyectos/"+str(self.encuestaActiva)+ultimaRuta+"/PDF/"+identificadorAnterior+".pdf'")

        funciones.mensaje(self, "OCR terminado")
        if textoError!="":
            funciones.mensaje(self,textoError)
        self.childFrame = editar_bbdd.Frame1(self)
        self.childFrame.Show()
        self.childFrame.iniciarPantalla(self.encuestaActiva)


    # limpiar lista
    def OnButton8Button(self, event):
        self.listBox1.Clear()
        while 0<len(self.imagenes):
            del self.imagenes[0]
        self.button8.Enable(False)
        self.button9.Enable(False)

    # boton borrar un elemento de lista
    def OnButton9Button(self, event):
        seleccionado = self.listBox1.GetSelection()
        del self.imagenes[seleccionado]
        del self.imagenesRutas[seleccionado]
        self.listBox1.Delete(seleccionado)
        if len(self.imagenes) == 0:
            self.button8.Enable(False)
            self.button9.Enable(False)

    # boton opciones encuesta
    def OnBotonOpcionesButton(self, event):
        self.childFrame = op_encuesta.Frame1(self)
        self.childFrame.Show()
        self.childFrame.cargarOpciones(self.encuestaActiva)

    # boton encuesta nueva
    def OnEncNuevaButton(self, event):
        self.childFrame = op_encuesta.Frame1(self)
        self.childFrame.Show()

    # Boton abrir
    def OnEncAbrirButton(self, event):
        self.childFrame = abrir_encuesta.Frame1(self)
        self.childFrame.Show()

    # Boton administrar datos de la encuesta
    def OnEncDatosButton(self, event):
        self.childFrame = editar_bbdd.Frame1(self)
        self.childFrame.Show()
        self.childFrame.iniciarPantalla(self.encuestaActiva)

    # Boton borrar encuesta
    def OnEncBorrarButton(self, event):
        mensaje='Esta seguro de que desea borrar la encuesta '+self.encuestaActiva+'?'

        sql='SELECT IDHoja FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'")'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        cuantas=0
        for registro in resultado:
            cuantas+=1

        if cuantas!=0:
            mensaje+=" Esto borrara tambien "+str(cuantas)+" paginas asociadas a la encuesta."
        #if hay cuestionarios' Esto borrara los n cuestionarios que han sido procesados anteriormente.'
        dlg = wx.MessageDialog(self, mensaje, 'Aviso', wx.YES_NO | wx.YES_DEFAULT | wx.ICON_EXCLAMATION | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
            if str(result)=="5103":
                sql='SELECT IDHoja FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'")'
                self.cursor.execute(sql)
                resultado=self.cursor.fetchall()
                for registro in resultado:
                    idImagen=str(registro["IDHoja"])
                    funciones.ejecutar("rm '"+sys.path[0]+"/imagenes/"+idImagen+".tif'" )

                sql="DELETE FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre='"+self.encuestaActiva+"')"
                self.cursor.execute(sql)
                self.conn.commit()
                sql="DELETE FROM Encuestas WHERE Nombre='"+self.encuestaActiva+"'"
                self.cursor.execute(sql)
                self.conn.commit()
                funciones.mensaje(self,"Encuesta "+str(self.encuestaActiva)+" borrada")
                self.DesactivarControles()
        finally:
            dlg.Destroy()

    # boton salir
    def OnBotonSalirButton(self, event):
        self.Close()

    def OnButtonOcrNewButton(self, event):
        dlg = wx.TextEntryDialog(self, 'Escriba un nombre para el grupo de opciones', 'Guardar opciones', '')
        try:
            if dlg.ShowModal() == wx.ID_OK:
                result = dlg.GetValue()

                """
                sql='SELECT MAX(IDPreproceso) AS idMaxima FROM Preprocesos'
                self.cursor.execute(sql)
                resultado=self.cursor.fetchall()
                for registro in resultado:
                    idTemp= str(registro["idMaxima"])
                if idTemp=="None":
                    idTemp="1"
                else:
                    idTemp=str(int(idTemp)+1)
                """

                ruido=str(self.choiceRuido.GetCurrentSelection())

                zoom=str(self.choiceZoom.GetCurrentSelection())
                rotar=str(self.choiceRotar.GetCurrentSelection())
                zona=self.areaMarcada

                if self.checkContraste.GetValue():
                    contraste=str(self.slider1.GetValue())
                else:
                    contraste="0"

                sql='INSERT INTO Preprocesos'
                sql+='(Nombre, Antiruido, Zoom, Contraste, Rotar, Encuesta, ZonaIdentificador) '
                sql+='VALUES ("'+result+'" ,'+ruido+' ,'+zoom+' ,'+contraste+' ,'+rotar+', (SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'"), "'+zona+'")'
                self.cursor.execute(sql)
                self.conn.commit()

                self.choiceOcr.Append(result)
                self.choiceOcr.SetSelection(self.choiceOcr.GetCount()-1)

                self.ActivarControlesOCR(result,int(ruido),int(zoom),int(contraste),int(rotar),zona)

                self.staticBoxOCR.SetLabel("Opciones OCR - "+result)
        finally:
            dlg.Destroy()

    def OnButtonOcrSaveButton(self, event):
        ruido=str(self.choiceRuido.GetCurrentSelection())
        zoom=str(self.choiceZoom.GetCurrentSelection())
        rotar=str(self.choiceRotar.GetCurrentSelection())

        if self.checkContraste.GetValue():
            contraste=str(self.slider1.GetValue())
        else:
            contraste="0"

        sql='UPDATE Preprocesos '
        sql+='SET Antiruido='+ruido+', Zoom='+zoom+', Contraste='+contraste+', Rotar='+rotar+', ZonaIdentificador="'+self.areaMarcada+'"'
        sql+=' WHERE Nombre="'+self.choiceOcr.GetStringSelection()+'" AND Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'")'
        self.cursor.execute(sql)
        self.conn.commit()

    def OnButOcrDelButton(self, event):
        preprocesoNombre=self.choiceOcr.GetStringSelection()
        sql="DELETE FROM Preprocesos WHERE Nombre='"+preprocesoNombre+"' AND Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre='"+self.encuestaActiva+"')"
        self.cursor.execute(sql)
        self.conn.commit()

        sql='SELECT * FROM Preprocesos WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'")'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        self.choiceOcr.Clear()
        flag=1
        for registro in resultado:
            self.choiceOcr.Append(registro["Nombre"])
            if (flag==1):
                tempNombre=registro["Nombre"]
                tempAntiruido=registro["Antiruido"]
                tempZoom=registro["Zoom"]
                tempContraste=registro["Contraste"]
                tempRotar=registro["Rotar"]
                tempZona=registro["ZonaIdentificador"]
                self.ActivarControlesOCR(tempNombre,tempAntiruido,tempZoom,tempContraste,tempRotar,tempZona)
                flag=0
        if (flag==0):
            self.choiceOcr.SetSelection(0)

    #comenzar seleccion de area
    def OnSelAreaButton(self, event):
        """
        if self.marcando==0:
            self.rubberBand = rubberband.RubberBand(drawingSurface=self.staticBitmap1)
            self.rubberBand.reset()
            self.areaBorrar.Enable(True)
            self.selArea.SetLabel(u'Ok')
            self.marcando=1
        else:
        """
        posicion=self.rubberBand.getCurrentExtent()
        if posicion!=None:
            a,b=self.scrolledPanel1.GetViewStart()
            c,d=self.scrolledPanel1.GetScrollPixelsPerUnit()
            scrollx=a*c
            scrolly=b*d

            punto1x=str(int((posicion[0]+scrollx)/self.proporcion))
            punto1y=str(int((posicion[1]+scrolly)/self.proporcion))
            punto2x=str(int((posicion[2]+scrollx)/self.proporcion))
            punto2y=str(int((posicion[3]+scrolly)/self.proporcion))
            self.areaxy.SetLabel('p1:'+punto1x+', '+punto1y+'\np2:'+punto2x+', '+punto2y)
            punto1x=punto1x.zfill(4)
            punto1y=punto1y.zfill(4)
            punto2x=punto2x.zfill(4)
            punto2y=punto2y.zfill(4)
            self.areaMarcada=str(int(punto2x)-int(punto1x))+"x"+str(int(punto2y)-int(punto1y))+"+"+punto1x+"+"+punto1y

        else:
            funciones.mensaje(self,'No has seleccionado ningun area aun')

    def OnAreaBorrarButton(self, event):
        self.rubberBand.reset()
        self.areaxy.SetLabel('')
        #self.marcando=0
        self.areaMarcada=""

# Fin botones


# Inicio funciones

    def ActivarControlesOCR(self, nombre, ruido, zoom, contraste, rotar,zona):
        self.buttonOcrSave.Enable(True)
        self.butOcrDel.Enable(True)
        self.choiceRuido.SetSelection(ruido)

        self.choiceZoom.SetSelection(zoom)
        self.choiceRotar.SetSelection(rotar)

        if contraste==0:
            self.checkContraste.SetValue(False)
            self.checkContraste.SetLabel("Ajustar contraste (70%)")
            self.slider1.SetValue(70)
            self.slider1.Enable(False)
        else:
            self.checkContraste.SetValue(True)
            self.checkContraste.SetLabel("Ajustar contraste ("+str(contraste)+"%)")
            self.slider1.SetValue(contraste)
            self.slider1.Enable(True)

        self.staticBoxOCR.SetLabel("Opciones OCR - "+nombre)

        self.areaMarcada=zona
        #self.areaMarcada=str(int(punto2x)-int(punto1x))+"x"+str(int(punto2y)-int(punto1y))+"+"+punto1x+"+"+punto1y
        if (zona!=""):
            indice1=self.areaMarcada.find("x")
            indice2=self.areaMarcada.find("+")
            resta1=self.areaMarcada[:indice1]
            resta2=self.areaMarcada[indice1+1:indice2]
            punto1x=str(int(self.areaMarcada[indice2+1:indice2+5]))
            punto1y=str(int(self.areaMarcada[indice2+6:indice2+10]))
            punto2x=str(int(punto1x)+int(resta1))
            punto2y=str(int(punto1y)+int(resta2))
            self.areaxy.SetLabel('p1:'+punto1x+', '+punto1y+'\np2:'+punto2x+', '+punto2y)
        else:
            self.areaxy.SetLabel('')

    def ActivarControles(self, nombre):
        self.botonOpciones.Enable(True)
        self.botonPrueba.Enable(True)
        self.botonOCR.Enable(True)
        self.choiceRuido.Enable(True)
        self.choiceZoom.Enable(True)
        self.checkContraste.Enable(True)
        self.choiceRotar.Enable(True)
        self.encDatos.Enable(True)
        self.encBorrar.Enable(True)
        self.choiceEtiqueta.Enable(True)

        self.buttonOcrSave.Enable(True)
        self.butOcrDel.Enable(True)

        self.SetTitle(u"OCR Dephim\xe1tica - "+nombre)
        self.encuestaActiva=nombre
        self.button1.Enable(True)
        self.choiceEtiqueta.Append("Sin etiqueta")
        self.choiceEtiqueta.Append("Nueva etiqueta")
        sql='SELECT Nombre FROM Etiquetas WHERE IDEtiqueta IN (SELECT DISTINCT(Etiqueta) FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'"))'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            self.choiceEtiqueta.Append(registro["Nombre"])
        self.choiceEtiqueta.SetSelection(0)

        self.choiceOcr.Enable(True)

        sql='SELECT * FROM Preprocesos WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'")'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        self.choiceOcr.Clear()
        flag=1
        for registro in resultado:
            self.choiceOcr.Append(registro["Nombre"])
            if (flag==1):
                tempNombre=registro['Nombre']
                tempAntiruido=registro["Antiruido"]
                tempZoom=registro["Zoom"]
                tempContraste=registro["Contraste"]
                tempRotar=registro["Rotar"]
                tempZona=registro["ZonaIdentificador"]
                self.ActivarControlesOCR(tempNombre,tempAntiruido,tempZoom,tempContraste,tempRotar, tempZona)
                flag=0
        if (flag==0):
            self.choiceOcr.SetSelection(0)

    def DesactivarControles(self):
        self.botonOpciones.Enable(False)
        self.botonPrueba.Enable(False)
        self.botonOCR.Enable(False)
        self.choiceRuido.Enable(False)
        self.choiceZoom.Enable(False)
        self.checkContraste.Enable(False)
        self.choiceRotar.Enable(False)
        self.encDatos.Enable(False)
        self.encBorrar.Enable(False)
        self.choiceEtiqueta.Enable(False)
        self.textEtiqueta.Enable(False)

        self.buttonOcrSave.Enable(False)
        self.butOcrDel.Enable(False)

        self.SetTitle(u"OCR Dephim\xe1tica")
        self.encuestaActiva=""
        self.button1.Enable(False)
        self.choiceOcr.Enable(False)

    # actualiza la imagen segun la seleccionada en la lista
    def actualizarImagen(self):
        seleccionado = self.listBox1.GetSelection()
        img = wx.Image(self.imagenes[seleccionado], wx.BITMAP_TYPE_ANY)
        if self.OriginalW==0:
            self.OriginalW, self.OriginalH = self.scrollSizer.GetSize()
        W = img.GetWidth()
        H = img.GetHeight()
        if W > H:
            #NewW = self.OriginalW * self.proporcion
            NewW = W * self.proporcion
            #NewH = self.OriginalW * H / W * self.proporcion
            NewH = H * self.proporcion
        else:
            #NewH = self.OriginalH * self.proporcion
            NewH = H * self.proporcion
            #NewW = self.OriginalH * H / W * self.proporcion
            NewW = W * self.proporcion
            #NewH = origen.staticBitmap1.GetHeight()
            #NewW = origen.staticBitmap1.GetWidth() * W / H
        img = img.Scale(NewW,NewH)
        self.staticBitmap1.SetBitmap(wx.BitmapFromImage(img))
        #self.staticBitmap1.SetWidth(NewW)
        #self.staticBitmap1.SetHeight(NewH)
        self.scrolledPanel1.SetupScrolling()
        #self.selArea.Enable(True)

        self.rubberBand.reset()
        self.areaBorrar.Enable(True)

    def preprocesarImagen(self, imagen):
        #convertimos a jpg calidad 100
        funciones.ejecutar("convert -compress None -quality 100 '"+imagen+"' 'temp.jpg' ;" )
        #funciones.mensaje(self,"1convert -compress None -quality 100 '"+imagen+"' 'temp.jpg' ;" )

        opcOCR=""
        if self.areaMarcada!="":
            opcCrop="-crop '"+self.areaMarcada+"'"
        else:
            opcCrop=""

        if self.choiceRuido.GetCurrentSelection()!=0:
            ruido=0
            if self.choiceRuido.GetCurrentSelection()==1:
                ruido=1
            elif self.choiceRuido.GetCurrentSelection()==2:
                ruido=5
            elif self.choiceRuido.GetCurrentSelection()==3:
                ruido=10
            opcOCR="-scale 200%x200% -despeckle -noise "+str(ruido)

        if self.choiceZoom.GetCurrentSelection()==0:
            if self.choiceRuido.GetCurrentSelection()==0:
                opcOCR=opcOCR+" -scale 50%x50%"
            else:
                opcOCR=opcOCR+" -scale 25%x25%"
        elif self.choiceZoom.GetCurrentSelection()==1:
            if self.choiceRuido.GetCurrentSelection()!=0:
                opcOCR=opcOCR+" -scale 50%x50%"
        else:
            if self.choiceRuido.GetCurrentSelection()==0:
                opcOCR=opcOCR+" -scale 200%x200%"

        #recortar la imagen
        if opcCrop != "":
            funciones.ejecutar("mogrify -compress None "+opcCrop+" 'temp.jpg'" )

        #aplicar contraste
        if self.checkContraste.GetValue():
            opcOCRcont="-level "+str(self.slider1.GetValue())+"%,"+str(self.slider1.GetValue())+"% -monochrome"
            funciones.ejecutar("mogrify -compress None "+opcOCRcont+" 'temp.jpg'" )
            #funciones.mensaje(self,"2mogrify -compress None "+opcOCRcont+" 'temp.jpg'" )

        #aplicar antiruido y zoom,
        if self.choiceRuido.GetCurrentSelection()!=0 or self.choiceZoom.GetCurrentSelection()!=1:
            funciones.ejecutar("mogrify -compress None "+opcOCR+" 'temp.jpg'" )
            #funciones.mensaje(self,"3mogrify -compress None "+opcOCR+" 'temp.jpg'" )

        #rotar la imagen
        if self.choiceRotar.GetCurrentSelection()>0:
            funciones.ejecutar("mogrify -rotate "+str(90*self.choiceRotar.GetCurrentSelection())+" 'temp.jpg'")
            #funciones.mensaje(self,"4mogrify -rotate "+str(90*self.choiceRotar.GetCurrentSelection())+" 'temp.jpg'")

        #convertir a tiff
        funciones.ejecutar("convert -compress None -depth 8 'temp.jpg'  'temp.tif'" )
        #funciones.mensaje(self,"5convert -compress None -depth 8 'temp.jpg'  'temp.tif'" )

    def borrarImgTemporales(self):
        comando="rm '"+sys.path[0]+"/prueba.txt'"
        funciones.ejecutar(comando)
        comando="rm '"+sys.path[0]+"/temp.jpg'"
        funciones.ejecutar(comando)
        comando="rm '"+sys.path[0]+"/temp.tif'"
        funciones.ejecutar(comando)

    def buscarIdentificador(self, textoOCR, patronId, optIdentificador):
        longId=optIdentificador[2]+optIdentificador[3]
        textoOCR = filter(lambda c: c not in ". :;­", textoOCR)#aviso: despues del ; hay un caracter invisible
        textoOCR=textoOCR.replace("O","0")
        textoOCR=textoOCR.replace("—","-")
        textoOCR=textoOCR.replace("―","-")#este guion es distinto del anterior
        textoOCR=textoOCR.replace("~","-")

        primero=""
        ultimo=""
        patron=""
        if optIdentificador[4]=="2":
            #detectar un identificador no numerico
            patron="[a-zA-Z0-9]"
        else:
            #detectar un identificador numerico
            patron="[0-9]"
        patron=patron+"{"+str(int(longId))+"}"
        if optIdentificador[5]=="2" or optIdentificador[5]=="3":
            primero="["+optIdentificador[6]+"]"
        if optIdentificador[5]=="1" or optIdentificador[5]=="3":
            ultimo="["+optIdentificador[6]+"]"

        encontrados=re.findall(primero+patron+ultimo,textoOCR)
        #funciones.mensaje(self,primero+patron+ultimo)
        #funciones.mensaje(self,textoOCR)
        if len(encontrados)==0:
            identificador="error"
        else:
            identificador=encontrados[0]
            if optIdentificador[5]=="2" or optIdentificador[5]=="3":
                identificador=identificador[1:]
            if optIdentificador[5]=="1" or optIdentificador[5]=="3":
                identificador=identificador[:-1]

        idEncontrados=len(encontrados)
        return idEncontrados,identificador

# Fin funciones


# Inicio control de eventos

    # Evento de cambio de seleccion de la listbox
    def OnListBox1Listbox(self, event):
        #self.proporcion=1
        self.actualizarImagen()
        #TODO activar botones + y -

    # Evento de seleccion de contraste
    def OnCheckContrasteCheckbox(self, event):
        if self.checkContraste.IsChecked():
            self.slider1.Enable(True)
        else:
            self.slider1.SetValue(70)
            self.checkContraste.SetLabel("Ajustar contraste ("+str(self.slider1.GetValue())+"%)")
            self.slider1.Enable(False)

    # Evento del slider
    def OnSlider1Scroll(self, event):
        self.checkContraste.SetLabel("Ajustar contraste ("+str(self.slider1.GetValue())+"%)")

    def scrolledPanel1Mousewheel(self, event):
        #funciones.mensaje(self)
        slider = event.GetEventObject()
        if (event.GetWheelRotation() > 0):
            self.proporcion=self.proporcion+0.1
            self.actualizarImagen()
        else:
            self.proporcion=self.proporcion-0.1
            self.actualizarImagen()

    def OnChoiceEtiquetaChoice(self, event):
        #funciones.mensaje(self,self.choiceEtiqueta.GetStringSelection())
        if self.choiceEtiqueta.GetSelection()==0:
            self.textEtiqueta.Enable(False)
        else:
            self.textEtiqueta.Enable(True)

    #evento para marcar el rubberband
    def OnStaticBitmap1LeftUp(self, event):
        #funciones.mensaje(self,"up")
        posicion=self.rubberBand.getCurrentExtent()
        if posicion!=None:
            a,b=self.scrolledPanel1.GetViewStart()
            c,d=self.scrolledPanel1.GetScrollPixelsPerUnit()
            scrollx=a*c
            scrolly=b*d

            punto1x=str(int((posicion[0]+scrollx)/self.proporcion))
            punto1y=str(int((posicion[1]+scrolly)/self.proporcion))
            punto2x=str(int((posicion[2]+scrollx)/self.proporcion))
            punto2y=str(int((posicion[3]+scrolly)/self.proporcion))
            self.areaxy.SetLabel('p1:'+punto1x+', '+punto1y+'\np2:'+punto2x+', '+punto2y)
            punto1x=punto1x.zfill(4)
            punto1y=punto1y.zfill(4)
            punto2x=punto2x.zfill(4)
            punto2y=punto2y.zfill(4)
            self.areaMarcada=str(int(punto2x)-int(punto1x))+"x"+str(int(punto2y)-int(punto1y))+"+"+punto1x+"+"+punto1y

    # Evento del choice de opciones OCR
    def OnChoiceOcrChoice(self, event):
        sql='SELECT * FROM Preprocesos WHERE Nombre="'+self.choiceOcr.GetStringSelection()+'" AND Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuestaActiva+'")'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()

        tempNombre=resultado[0]["Nombre"]
        tempAntiruido=resultado[0]["Antiruido"]
        tempZoom=resultado[0]["Zoom"]
        tempContraste=resultado[0]["Contraste"]
        tempRotar=resultado[0]["Rotar"]
        tempZona=resultado[0]["ZonaIdentificador"]
        self.ActivarControlesOCR(tempNombre,tempAntiruido,tempZoom,tempContraste,tempRotar,tempZona)

 # Fin control de eventos
