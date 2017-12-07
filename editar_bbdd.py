#Boa:Frame:Frame1

import wx
import wx.lib.scrolledpanel
import os
import sys
#import MySQLdb
import funciones
import sqlite3

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BOTONBORRARPAG, wxID_FRAME1BOTONBUSCAR,
 wxID_FRAME1BOTONCHECKIDS, wxID_FRAME1BOTONCOMBINAR, wxID_FRAME1BOTONOCR,
 wxID_FRAME1BOTONSALIR, wxID_FRAME1BUTACTUALIZARID, wxID_FRAME1BUTTONORIGINAL,
 wxID_FRAME1BUTTONPDF, wxID_FRAME1CHOICE1, wxID_FRAME1CHOICEETIQUETA,
 wxID_FRAME1CHOICEFECHA, wxID_FRAME1CHOICERUTA, wxID_FRAME1CHOICESESION,
 wxID_FRAME1IDENTIFICADOR, wxID_FRAME1LISTCTRL1, wxID_FRAME1PANEL1,
 wxID_FRAME1SCROLLEDPANEL1, wxID_FRAME1SCROLLEDWINDOW1,
 wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2,
 wxID_FRAME1TEXTO, wxID_FRAME1TEXTODATOS, wxID_FRAME1TEXTORUTA,
 wxID_FRAME1TXTBUSCARID,
] = [wx.NewId() for _init_ctrls in range(27)]

class Frame1(wx.Frame):

# Inicio definicion de variables

    imagenes=list()
    cuestionarios=list()
    hojas=list()
    identificadores=list()
    encuesta=""
    longIdentificador=0
    orden=1

    OriginalW=0
    OriginalH=0
    proporcion=1

    filtro1=" AND Actual=1"
    filtro2=""
    filtro4=""
    filtro5=""
    filtroPag1=""

    # Inicio base de datos
    conn = sqlite3.connect(sys.path[0]+'/bbdd.db')
    conn.row_factory = sqlite3.Row
    cursor=conn.cursor()

# Fin definicion de variables

    def _init_coll_sizerPrincipal_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.sizerIzquierdo, 0, border=5, flag=wx.RIGHT)
        parent.AddSizer(self.sizerCentral, 0, border=5,
              flag=wx.EXPAND | wx.RIGHT)
        parent.AddSizer(self.sizerDerecho, 1, border=0, flag=wx.EXPAND)

    def _init_coll_sizerCentral_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.listCtrl1, 1, border=2, flag=wx.EXPAND | wx.ALL)
        parent.AddWindow(self.choice1, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.botonBorrarPag, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.botonCombinar, 0, border=2, flag=wx.ALL)

    def _init_coll_sizerIdent_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.identificador, 0, border=0, flag=0)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddWindow(self.butActualizarId, 0, border=0, flag=0)

    def _init_coll_sizerIzquierdo_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.botonCheckIds, 0, border=2, flag=wx.ALL)
        parent.AddSpacer(wx.Size(12, 12), border=0, flag=0)
        parent.AddWindow(self.txtBuscarId, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.botonBuscar, 0, border=2, flag=wx.ALL)
        parent.AddSpacer(wx.Size(12, 12), border=0, flag=0)
        parent.AddWindow(self.botonOcr, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.botonSalir, 0, border=2, flag=wx.ALL)
        parent.AddSpacer(wx.Size(8, 8), border=0, flag=0)
        parent.AddWindow(self.staticText2, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.choiceSesion, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.choiceEtiqueta, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.choiceFecha, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.choiceRuta, 0, border=2, flag=wx.ALL)

    def _init_coll_sizerMasmenos_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.buttonOriginal, 0, border=0, flag=0)
        parent.AddSpacer(wx.Size(10, 8), border=0, flag=0)
        parent.AddWindow(self.buttonPDF, 0, border=0, flag=0)

    def _init_coll_sizerDerecho_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.scrolledPanel1, 1, border=0, flag=wx.EXPAND)
        parent.AddWindow(self.textoDatos, 0, border=0, flag=0)
        parent.AddWindow(self.textoRuta, 0, border=0, flag=0)
        parent.AddSizer(self.sizerMasmenos, 0, border=2,
              flag=wx.ALL | wx.ALIGN_LEFT)
        parent.AddWindow(self.texto, 0, border=2, flag=wx.EXPAND | wx.ALL)
        parent.AddSpacer(wx.Size(12, 12), border=0, flag=0)
        parent.AddWindow(self.staticText1, 0, border=2, flag=wx.ALL)
        parent.AddSizer(self.sizerIdent, 0, border=2, flag=wx.ALL)

    def _init_coll_listCtrl1_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT, heading=u'N\xba',
              width=40)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading=u'Identificador', width=90)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT,
              heading=u'Paginas', width=70)

    def _init_sizers(self):
        # generated method, don't edit
        self.sizerPrincipal = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.sizerIzquierdo = wx.BoxSizer(orient=wx.VERTICAL)

        self.sizerCentral = wx.BoxSizer(orient=wx.VERTICAL)

        self.sizerDerecho = wx.BoxSizer(orient=wx.VERTICAL)

        self.sizerMasmenos = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.sizerIdent = wx.BoxSizer(orient=wx.HORIZONTAL)

        self.scrollSizer = wx.BoxSizer(orient=wx.VERTICAL)

        self._init_coll_sizerPrincipal_Items(self.sizerPrincipal)
        self._init_coll_sizerIzquierdo_Items(self.sizerIzquierdo)
        self._init_coll_sizerCentral_Items(self.sizerCentral)
        self._init_coll_sizerDerecho_Items(self.sizerDerecho)
        self._init_coll_sizerMasmenos_Items(self.sizerMasmenos)
        self._init_coll_sizerIdent_Items(self.sizerIdent)

        self.panel1.SetSizer(self.sizerPrincipal)
        self.scrolledPanel1.SetSizer(self.scrollSizer)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(503, 226), size=wx.Size(689, 489),
              style=wx.DEFAULT_FRAME_STYLE, title=u'Edici\xf3n de datos')
        self.SetClientSize(wx.Size(689, 489))
        self.SetIcon(wx.Icon(sys.path[0]+"/"+u'Edit.ico',wx.BITMAP_TYPE_ICO))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(689, 489),
              style=wx.TAB_TRAVERSAL)

        self.botonOcr = wx.Button(id=wxID_FRAME1BOTONOCR, label=u'Volver a OCR',
              name=u'botonOcr', parent=self.panel1, pos=wx.Point(2, 133),
              size=wx.Size(142, 34), style=0)
        self.botonOcr.Bind(wx.EVT_BUTTON, self.OnBotonOcrButton,
              id=wxID_FRAME1BOTONOCR)

        self.botonSalir = wx.Button(id=wxID_FRAME1BOTONSALIR, label=u'Salir',
              name=u'botonSalir', parent=self.panel1, pos=wx.Point(2, 171),
              size=wx.Size(142, 34), style=0)
        self.botonSalir.Bind(wx.EVT_BUTTON, self.OnBotonSalirButton,
              id=wxID_FRAME1BOTONSALIR)

        self.choice1 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE1,
              name='choice1', parent=self.panel1, pos=wx.Point(153, 382),
              size=wx.Size(120, 29), style=0)
        self.choice1.SetBestFittingSize(wx.Size(120, 29))
        self.choice1.Bind(wx.EVT_CHOICE, self.OnChoice1Choice,
              id=wxID_FRAME1CHOICE1)

        self.scrolledWindow1 = wx.ScrolledWindow(id=wxID_FRAME1SCROLLEDWINDOW1,
              name='scrolledWindow1', parent=self.panel1, pos=wx.Point(366, 6),
              size=wx.Size(300, 100), style=wx.HSCROLL | wx.VSCROLL)
        self.scrolledWindow1.SetBestFittingSize(wx.Size(300, 100))
        self.scrolledWindow1.SetMinSize(wx.Size(300, 200))

        self.texto = wx.TextCtrl(id=wxID_FRAME1TEXTO, name=u'texto',
              parent=self.panel1, pos=wx.Point(362, 296), size=wx.Size(325,
              120), style=wx.TE_MULTILINE | wx.VSCROLL, value=u'')
        self.texto.SetBestFittingSize(wx.Size(300, 70))
        self.texto.SetMinSize(wx.Size(300, 120))

        self.identificador = wx.TextCtrl(id=wxID_FRAME1IDENTIFICADOR,
              name=u'identificador', parent=self.panel1, pos=wx.Point(362, 453),
              size=wx.Size(120, 27), style=0, value=u'')
        self.identificador.SetBestFittingSize(wx.Size(120, 27))
        self.identificador.Bind(wx.EVT_KEY_DOWN, self.OnIdentificadorKeyDown)

        self.butActualizarId = wx.Button(id=wxID_FRAME1BUTACTUALIZARID,
              label=u'Actualizar', name=u'butActualizarId', parent=self.panel1,
              pos=wx.Point(490, 453), size=wx.Size(90, 34), style=0)
        self.butActualizarId.SetBestFittingSize(wx.Size(90, 34))
        self.butActualizarId.Bind(wx.EVT_BUTTON, self.OnButActualizarIdButton,
              id=wxID_FRAME1BUTACTUALIZARID)

        self.botonBorrarPag = wx.Button(id=wxID_FRAME1BOTONBORRARPAG,
              label=u'Borrar cuestionario', name=u'botonBorrarPag',
              parent=self.panel1, pos=wx.Point(153, 415), size=wx.Size(148, 34),
              style=0)
        self.botonBorrarPag.Bind(wx.EVT_BUTTON, self.OnBotonBorrarPagButton,
              id=wxID_FRAME1BOTONBORRARPAG)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label=u'Identificador', name='staticText1', parent=self.panel1,
              pos=wx.Point(362, 432), size=wx.Size(110, 17), style=0)

        self.txtBuscarId = wx.TextCtrl(id=wxID_FRAME1TXTBUSCARID,
              name=u'txtBuscarId', parent=self.panel1, pos=wx.Point(2, 52),
              size=wx.Size(142, 27), style=0, value=u'')
        self.txtBuscarId.SetBestFittingSize(wx.Size(142, 27))
        self.txtBuscarId.SetHelpText(u'')
        self.txtBuscarId.Bind(wx.EVT_KEY_DOWN, self.OnTxtBuscarIdKeyDown)

        self.botonBuscar = wx.Button(id=wxID_FRAME1BOTONBUSCAR,
              label=u'Buscar ID', name=u'botonBuscar', parent=self.panel1,
              pos=wx.Point(2, 83), size=wx.Size(142, 34), style=0)
        self.botonBuscar.SetBestFittingSize(wx.Size(142, 34))
        self.botonBuscar.Bind(wx.EVT_BUTTON, self.OnBotonBuscarButton,
              id=wxID_FRAME1BOTONBUSCAR)

        self.botonCheckIds = wx.Button(id=wxID_FRAME1BOTONCHECKIDS,
              label=u'Comprobar IDs', name=u'botonCheckIds', parent=self.panel1,
              pos=wx.Point(2, 2), size=wx.Size(142, 34), style=0)
        self.botonCheckIds.SetBestFittingSize(wx.Size(142, 34))
        self.botonCheckIds.Bind(wx.EVT_BUTTON, self.OnBotonCheckIdsButton,
              id=wxID_FRAME1BOTONCHECKIDS)

        self.scrolledPanel1 = wx.lib.scrolledpanel.ScrolledPanel(id=wxID_FRAME1SCROLLEDPANEL1,
              name='scrolledPanel1', parent=self.panel1, pos=wx.Point(360, 0),
              size=wx.Size(329, 222), style=wx.TAB_TRAVERSAL)
        self.scrolledPanel1.SetBestFittingSize(wx.Size(298, 200))
        self.scrolledPanel1.SetMinSize(wx.Size(324, 200))
        self.scrolledPanel1.Bind(wx.EVT_MOUSEWHEEL,
              self.scrolledPanel1Mousewheel)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.NullBitmap,
              id=wxID_FRAME1STATICBITMAP1, name='staticBitmap1',
              parent=self.scrolledPanel1, pos=wx.Point(0, 0),
              style=wx.SIMPLE_BORDER | wx.HSCROLL | wx.VSCROLL)
        self.staticBitmap1.SetHelpText(u'')

        self.listCtrl1 = wx.ListCtrl(id=wxID_FRAME1LISTCTRL1, name='listCtrl1',
              parent=self.panel1, pos=wx.Point(153, 2), size=wx.Size(200, 376),
              style=wx.LC_VRULES | wx.LC_HRULES | wx.LC_AUTOARRANGE | wx.LC_REPORT)
        self.listCtrl1.SetBestFittingSize(wx.Size(200, 225))
        self._init_coll_listCtrl1_Columns(self.listCtrl1)
        self.listCtrl1.Bind(wx.EVT_LIST_ITEM_SELECTED,
              self.OnListCtrl1ListItemSelected, id=wxID_FRAME1LISTCTRL1)
        self.listCtrl1.Bind(wx.EVT_LIST_COL_CLICK, self.OnListCtrl1ListColClick,
              id=wxID_FRAME1LISTCTRL1)

        self.buttonOriginal = wx.Button(id=wxID_FRAME1BUTTONORIGINAL,
              label=u'Ver pagina', name=u'buttonOriginal', parent=self.panel1,
              pos=wx.Point(362, 258), size=wx.Size(105, 34), style=0)
        self.buttonOriginal.SetBestFittingSize(wx.Size(105, 34))
        self.buttonOriginal.Bind(wx.EVT_BUTTON, self.OnButtonOriginalButton,
              id=wxID_FRAME1BUTTONORIGINAL)

        self.buttonPDF = wx.Button(id=wxID_FRAME1BUTTONPDF, label=u'Ver PDF',
              name=u'buttonPDF', parent=self.panel1, pos=wx.Point(477, 258),
              size=wx.Size(85, 34), style=0)
        self.buttonPDF.SetBestFittingSize(wx.Size(85, 34))
        self.buttonPDF.Bind(wx.EVT_BUTTON, self.OnButtonPDFButton,
              id=wxID_FRAME1BUTTONPDF)

        self.botonCombinar = wx.Button(id=wxID_FRAME1BOTONCOMBINAR,
              label=u'Agregar cuestionario', name=u'botonCombinar',
              parent=self.panel1, pos=wx.Point(153, 453), size=wx.Size(148, 34),
              style=0)
        self.botonCombinar.SetBestFittingSize(wx.Size(148, 34))
        self.botonCombinar.Bind(wx.EVT_BUTTON, self.OnBotonCombinarButton,
              id=wxID_FRAME1BOTONCOMBINAR)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label=u'Filtros:', name='staticText2', parent=self.panel1,
              pos=wx.Point(2, 217), size=wx.Size(48, 17), style=0)

        self.choiceSesion = wx.Choice(choices=["Ultima sesion", "Sesion: Todas"],
              id=wxID_FRAME1CHOICESESION, name=u'choiceSesion',
              parent=self.panel1, pos=wx.Point(2, 238), size=wx.Size(142, 29),
              style=0)
        self.choiceSesion.SetBestFittingSize(wx.Size(142, 29))
        self.choiceSesion.Bind(wx.EVT_CHOICE, self.OnChoiceSesionChoice,
              id=wxID_FRAME1CHOICESESION)

        self.choiceEtiqueta = wx.Choice(choices=[],
              id=wxID_FRAME1CHOICEETIQUETA, name=u'choiceEtiqueta',
              parent=self.panel1, pos=wx.Point(2, 271), size=wx.Size(142, 29),
              style=0)
        self.choiceEtiqueta.SetBestFittingSize(wx.Size(142, 29))
        self.choiceEtiqueta.Bind(wx.EVT_CHOICE, self.OnChoiceEtiquetaChoice,
              id=wxID_FRAME1CHOICEETIQUETA)

        self.choiceFecha = wx.Choice(choices=[], id=wxID_FRAME1CHOICEFECHA,
              name=u'choiceFecha', parent=self.panel1, pos=wx.Point(2, 304),
              size=wx.Size(142, 29), style=0)
        self.choiceFecha.SetBestFittingSize(wx.Size(142, 29))
        self.choiceFecha.Bind(wx.EVT_CHOICE, self.OnChoiceFechaChoice,
              id=wxID_FRAME1CHOICEFECHA)

        self.textoDatos = wx.StaticText(id=wxID_FRAME1TEXTODATOS,
              label=u'Fecha: , Etiqueta: ', name=u'textoDatos',
              parent=self.panel1, pos=wx.Point(360, 222), size=wx.Size(157, 17),
              style=0)

        self.textoRuta = wx.StaticText(id=wxID_FRAME1TEXTORUTA, label=u'Ruta:',
              name=u'textoRuta', parent=self.panel1, pos=wx.Point(360, 239),
              size=wx.Size(33, 17), style=0)

        self.choiceRuta = wx.Choice(choices=[], id=wxID_FRAME1CHOICERUTA,
              name=u'choiceRuta', parent=self.panel1, pos=wx.Point(2, 337),
              size=wx.Size(142, 29), style=0)
        self.choiceRuta.SetBestFittingSize(wx.Size(142, 29))
        self.choiceRuta.Bind(wx.EVT_CHOICE, self.OnChoiceRutaChoice,
              id=wxID_FRAME1CHOICERUTA)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.ventanaPadre=parent
        self.MakeModal(True)
        self.Bind(wx.EVT_CLOSE, self.on_close)
        self.Centre()
        self.scrollSizer.Add(self.staticBitmap1 , 0, wx.ALL, 5)
        self.scrolledPanel1.SetupScrolling()

    def on_close(self, event):
        self.MakeModal(False)
        #self.db.close()
        event.Skip()

    def iniciarPantalla(self, encuesta):
        self.SetTitle(u"Edici\xf3n de datos - "+encuesta)
        self.encuesta=encuesta
        self.llenarLista()
        sql="SELECT * FROM Encuestas WHERE Nombre='"+encuesta+"'"
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        self.longIdentificador=(10*int(resultado[0]["OptIdentificador"][2]))+int(resultado[0]["OptIdentificador"][3])

        self.choiceEtiqueta.Append("Etiqueta: Todas")
        sql='SELECT Nombre FROM Etiquetas WHERE IDEtiqueta IN (SELECT DISTINCT(Etiqueta) FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'"))'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            self.choiceEtiqueta.Append(registro["Nombre"])
        self.choiceEtiqueta.SetSelection(0)

        self.choiceFecha.Append("Fecha: Todas")
        sql='SELECT DISTINCT(FechaScan) FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") ORDER BY FechaScan'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            if str(registro["FechaScan"])!="None":
                self.choiceFecha.Append(str(registro["FechaScan"]))
        self.choiceFecha.SetSelection(0)

        self.choiceRuta.Append("Ruta: Todas")
        sql='SELECT DISTINCT(Ruta) FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") ORDER BY Ruta'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            if str(registro["Ruta"])!="None":
                self.choiceRuta.Append(str(registro["Ruta"]))
        self.choiceRuta.SetSelection(0)

    def llenarLista(self):
        sql=""
        #funciones.mensaje(self,str(self.orden))
        sql=self.generarSQL()
        sql2='SELECT * FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") ORDER BY Identificador, PaginaNum'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        self.cursor.execute(sql2)
        resultado2=self.cursor.fetchall()
        self.listCtrl1.DeleteAllItems()
        self.identificador.Clear()
        self.texto.Clear()
        self.choice1.Clear()
        imagenNew = wx.Image(sys.path[0]+"/blanco.tif", wx.BITMAP_TYPE_ANY)
        self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagenNew))
        del self.hojas[:]
        del self.cuestionarios[:]
        del self.imagenes[:]
        del self.identificadores[:]
        num=1
        for registro in resultado:
            if registro["PaginaNum"]==1:
                tempTotal=0
                for registro2 in resultado2:
                    if registro2["CuestionarioNum"]==registro["CuestionarioNum"]:
                        tempTotal=tempTotal+1
                cuantos=self.listCtrl1.GetItemCount()
                posicion=self.listCtrl1.InsertStringItem(cuantos,str(num))
                self.listCtrl1.SetStringItem(posicion,1,str(registro["Identificador"]))
                self.listCtrl1.SetStringItem(posicion,2,str(tempTotal))
                num+=1
                self.hojas.append(str(registro["IDHoja"]))
                self.cuestionarios.append(str(registro["CuestionarioNum"]))
                self.imagenes.append(sys.path[0]+"/imagenes/"+str(registro["IDHoja"])+".tif")
                self.identificadores.append(str(registro["Identificador"]))

# Inicio botones

    # volver a OCR
    def OnBotonOcrButton(self, event):
        self.Close()
        self.Destroy()

    # cerrar la aplicacion
    def OnBotonSalirButton(self, event):
        self.ventanaPadre.Close()
        self.ventanaPadre.Destroy()

    #Boton corregir identificador
    def OnButActualizarIdButton(self, event):
        seleccionado = self.listCtrl1.GetFirstSelected()
        cuestionario=self.cuestionarios[seleccionado]
        paginaSel=self.choice1.GetStringSelection()[7:]
        identificadorNuevo=self.identificador.GetValue()

        sql='SELECT Identificador, Ruta FROM Hojas '
        sql+='WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+cuestionario+' AND PaginaNum=1'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        ruta=resultado[0]["Ruta"]

        sql='SELECT * FROM Hojas '
        sql+='WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND Identificador="'+identificadorNuevo+'"'
        self.cursor.execute(sql)
        resultadoCheck=self.cursor.fetchall()
        cuantos=0
        for registro in resultadoCheck:
            cuantos=cuantos+1

        #si el identificador ya existe, devolvemos un mensaje de error
        if cuantos!=0:
            funciones.mensaje(self,"El identificador elegido ya existe")

        #Si la pagina es la 1, actualizar todas las hojas
        elif paginaSel=="1":
            sql='UPDATE Hojas '
            sql+='SET Identificador="'+identificadorNuevo+'" '
            sql+='WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+cuestionario
            self.cursor.execute(sql)
            self.conn.commit()

            #si las paginas tienen id reconocida, renombrar todas
            if resultado[0]["Identificador"]!="-1":
                funciones.ejecutar("rename 's/"+resultado[0]["Identificador"]+"_/"+identificadorNuevo+"_/' $HOME'/Escritorio/Proyectos/"+self.encuesta+ruta+"/Originales/'*.*")
                funciones.ejecutar("rename 's/"+resultado[0]["Identificador"]+"/"+identificadorNuevo+"/' $HOME'/Escritorio/Proyectos/"+self.encuesta+ruta+"/PDF/'*.*")

            #si las paginas no tienen id reconocida, renombrar las ids y crear el pdf
            else:
                #seleccionamos el IDHoja y numero de pagina para todo el cuestionario
                sql='SELECT IDHoja, PaginaNum, Ruta FROM Hojas '
                sql+='WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+cuestionario
                self.cursor.execute(sql)
                resultadoNoid=self.cursor.fetchall()
                for registro in resultadoNoid:
                    #renombramos las imagenes
                    funciones.ejecutar("rename 's/"+str(registro["IDHoja"])+"\./"+identificadorNuevo+"_"+str(registro["PaginaNum"])+"\./' $HOME'/Escritorio/Proyectos/"+self.encuesta+ruta+"/Originales/'"+str(registro["IDHoja"])+".*")

                #creamos el pdf
                funciones.ejecutar("IFS=$'\n' && convert `ls -v $HOME'/Escritorio/Proyectos/"+self.encuesta+ruta+"/Originales/'"+identificadorNuevo+"_*.*` $HOME'/Escritorio/Proyectos/"+self.encuesta+ruta+"/PDF/"+identificadorNuevo+".pdf'")

            self.llenarLista()

        #si la pagina no es la 1, la pagina pasa a ser la 1, y
        #   el identificador nuevo pasa a ser el identificador de
        #   la nueva pagina 1 y de las siguientes, que se renumeran.
        #   se renombran las imagenes y se regeneran 2 pdf, el del
        #   antiguo identificador y el del nuevo
        else:
            sql='SELECT MAX(CuestionarioNum) AS cuestMaxima FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'")'
            self.cursor.execute(sql)
            resultadoMax=self.cursor.fetchall()
            for registro in resultadoMax:
                cuestionarioMax= str(registro["cuestMaxima"])
            cuestionarioMax=str(int(cuestionarioMax)+1)

            #cambiamos el identificador a las paginas de la paginaSel en adelante
            sql='UPDATE Hojas '
            sql+='SET Identificador="'+identificadorNuevo+'", CuestionarioNum='+cuestionarioMax+' '
            sql+='WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+cuestionario+' AND PaginaNum>='+paginaSel
            self.cursor.execute(sql)
            self.conn.commit()

            #seleccionamos las paginas antiguas
            sql='SELECT PaginaNum FROM Hojas '
            sql+='WHERE Identificador="'+identificadorNuevo+'" AND PaginaNum>='+paginaSel+' ORDER BY PaginaNum'
            self.cursor.execute(sql)
            resultado2=self.cursor.fetchall()
            n=0
            for registro in resultado2:
                n=n+1
                sql='UPDATE Hojas '
                sql+='SET PaginaNum="'+str(n)+'" '
                sql+='WHERE Identificador="'+identificadorNuevo+'" AND PaginaNum='+str(registro["PaginaNum"])
                self.cursor.execute(sql)
                self.conn.commit()

                #renombramos las paginas
                funciones.ejecutar("rename 's/"+resultado[0]["Identificador"]+"_"+str(registro["PaginaNum"])+"/"+identificadorNuevo+"_"+str(n)+"/' $HOME'/Escritorio/Proyectos/"+self.encuesta+ruta+"/Originales/'*.*")

            #creamos el pdf nuevo
            #funciones.mensaje(self,"creando PDF nuevo")
            funciones.ejecutar("IFS=$'\n' && convert `ls -v $HOME'/Escritorio/Proyectos/"+self.encuesta+ruta+"/Originales/'"+identificadorNuevo+"_*.*` $HOME'/Escritorio/Proyectos/"+self.encuesta+ruta+"/PDF/"+identificadorNuevo+".pdf'")

            #si el idantiguo no es -1, regeneramos el antiguo pdf
            if resultado[0]["Identificador"]!="-1":
                #funciones.mensaje(self,"creando PDF antiguo")
                funciones.ejecutar("IFS=$'\n' &&  convert `ls -v $HOME'/Escritorio/Proyectos/"+self.encuesta+ruta+"/Originales/'"+resultado[0]["Identificador"]+"_*.*` $HOME'/Escritorio/Proyectos/"+self.encuesta+ruta+"/PDF/"+resultado[0]["Identificador"]+".pdf'")

            self.llenarLista()

    #Insertar nueva pagina: (eliminado)
    """
    def OnBotonNuevaPagButton(self, event):
        seleccionado = self.listCtrl1.GetFirstSelected()
        cuestionario=self.cuestionarios[seleccionado]
        mensaje='Desea insertar una pagina en blanco en el cuestionario '+cuestionario+'?'
        dlg = wx.MessageDialog(self, mensaje, 'Aviso', wx.YES_NO | wx.YES_DEFAULT | wx.ICON_EXCLAMATION | wx.ICON_INFORMATION)
        try:
            result = dlg.ShowModal()
            if str(result)=="5103":
                sql='SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'"'
                self.cursor.execute(sql)
                resultado4=self.cursor.fetchall()
                encuestaNum=resultado4[0][0]

                sql='SELECT max(PaginaNum) FROM Hojas WHERE Encuesta='+str(encuestaNum)+' AND CuestionarioNum='+str(cuestionario)
                self.cursor.execute(sql)
                resultado=self.cursor.fetchall()

                sql='SELECT max(IDHoja) FROM Hojas'
                self.cursor.execute(sql)
                resultado2=self.cursor.fetchall()

                sql='SELECT * FROM Hojas WHERE Encuesta='+str(encuestaNum)+' AND CuestionarioNum=1'
                self.cursor.execute(sql)
                resultado3=self.cursor.fetchall()

                sql='INSERT INTO Hojas '
                sql+='(IDHoja, Encuesta, CuestionarioNum, PaginaNum, Texto, Identificador, FechaScan) '
                sql+='VALUES ('+str(resultado2[0][0]+1)+', '+str(encuestaNum)+' ,'+str(cuestionario)+' ,'+str(resultado[0][0]+1)+' , "","'+resultado3[0][5]+'" ,"'+str(resultado3[0][6])+'")'
                self.cursor.execute(sql)

                funciones.ejecutar("cp '"+sys.path[0]+"/vacia.tif' '"+sys.path[0]+"/imagenes/"+str(resultado2[0][0]+1)+".tif'" )

                self.llenarLista()
                #seleccionar cuestionario en lista
                #seleccionar nueva pagina en lista
                #mostrar pagina vacia en imagen
        finally:
            dlg.Destroy()
    """

    #Borrar una pagina o un cuestionario
    #ahora solo borra un cuestionario
    def OnBotonBorrarPagButton(self, event):
        cuestionarios=[]
        seleccionado = self.listCtrl1.GetFirstSelected()
        cual=self.listCtrl1.GetItem(seleccionado,1).GetText()
        cuestionarios.append(self.cuestionarios[seleccionado])
        mensaje='Esta seguro de que desea borrar el cuestionario '+cual+'?'

        cuantosHay=self.listCtrl1.GetSelectedItemCount()
        if cuantosHay >1:
            n=2
            while n<=cuantosHay:
                seleccionado = self.listCtrl1.GetNextSelected(seleccionado)
                cual+=", "+self.listCtrl1.GetItem(seleccionado,1).GetText()
                cuestionarios.append(self.cuestionarios[seleccionado])
                n+=1
            mensaje='Esta seguro de que desea borrar los cuestionarios '+cual+'?'

        dlg = wx.MessageDialog(self, mensaje, 'Aviso', wx.YES_NO | wx.YES_DEFAULT | wx.ICON_EXCLAMATION | wx.ICON_INFORMATION)

        try:
            result = dlg.ShowModal()
            if str(result)=="5103":
                for cuestionario in cuestionarios:
                    sql='SELECT IDHoja, Identificador, PaginaNum, Ruta FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+cuestionario
                    self.cursor.execute(sql)
                    resultado=self.cursor.fetchall()
                    for registro in resultado:
                        funciones.ejecutar("rm '"+sys.path[0]+"/imagenes/"+str(registro["IDHoja"])+".tif'" )

                        extension=funciones.ejecutar("cd $HOME'/Escritorio/Proyectos/"+self.encuesta+registro["Ruta"]+"/Originales/'&&ls "+registro["Identificador"]+"_"+str(registro["PaginaNum"])+".*")
                        funciones.ejecutar("rm $HOME'/Escritorio/Proyectos/"+self.encuesta+registro["Ruta"]+"/Originales/"+registro[1]+"_"+str(registro["PaginaNum"])+"."+extension[-3:]+"'")
                        funciones.ejecutar("rm $HOME'/Escritorio/Proyectos/"+self.encuesta+registro[3]+"/PDF/"+registro["Identificador"]+".pdf'")

                        funciones.ejecutar("rm '"+sys.path[0]+"/imagenes/"+str(registro["IDoHoja"])+".tif'" )

                        sql='DELETE FROM Hojas WHERE IDHoja='+str(registro["IDHoja"])
                        self.cursor.execute(sql)
                        self.conn.commit()
                    self.llenarLista()
        finally:
            dlg.Destroy()

    #Mover una pagina a otro cuestionario, o dentro del mismo cuestionario
    #funcion borrada
    def OnBotonMoverPagButton(self, event):
        seleccionado = self.listCtrl1.GetFirstSelected()
        cuestionarioSel=self.cuestionarios[seleccionado]
        elementos = list()
        for unIdentificador in self.identificadores:
            elementos.append(unIdentificador)
        dialog = wx.SingleChoiceDialog ( None, 'Elija el cuestionario al que desea mover la hoja', 'Mover hoja', elementos )
        if dialog.ShowModal() == wx.ID_OK:
            # Si hemos seleccionado el mismo cuestionario, movemos la hoja a otro lugar dentro del mismo
            if dialog.GetStringSelection()==str(cuestionarioSel):
                elementos2 = list()
                sql='SELECT PaginaNum FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+str(cuestionarioSel)+' ORDER BY PaginaNum'
                self.cursor.execute(sql)
                resultado=self.cursor.fetchall()
                for registro in resultado:
                    elementos2.append(str(registro["PaginaNum"]))
                dialog2 = wx.SingleChoiceDialog ( None, 'Elija la posicion a la que desea mover la hoja', 'Mover hoja en su cuestionario', elementos2 )
                if dialog2.ShowModal() == wx.ID_OK:
                    if not self.choice1.GetStringSelection()[7:]==dialog2.GetStringSelection():
                        sql='SELECT IDHoja FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+str(cuestionarioSel)+' AND PaginaNum='+self.choice1.GetStringSelection()[7:]
                        self.cursor.execute(sql)
                        resultado=self.cursor.fetchall()
                        IDHoja=resultado[0]["IDHoja"]

                        sql='UPDATE Hojas '
                        sql+='SET PaginaNum='+self.choice1.GetStringSelection()[7:]
                        sql+=' WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+str(cuestionarioSel)+' AND PaginaNum='+dialog2.GetStringSelection()
                        self.cursor.execute(sql)
                        self.conn.commit()

                        sql='UPDATE Hojas '
                        sql+='SET PaginaNum='+dialog2.GetStringSelection()
                        sql+=' WHERE IDHoja='+str(IDHoja)
                        self.cursor.execute(sql)
                        self.conn.commit()

                dialog2.destroy()
            #TODO: si la hoja es la numero 1, tambien la movemos dentro del mismo cuestionario
            #si la hoja es la numero 1, intercambiamos las posiciones de dos cuestionarios
            elif self.choice1.GetStringSelection()[7:]=="1":
                #cuestionario origen
                sql='SELECT IDHoja FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+str(cuestionarioSel)
                self.cursor.execute(sql)
                resultado=self.cursor.fetchall()

                #cuestionario destino
                sql='SELECT IDHoja FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+dialog.GetStringSelection()
                self.cursor.execute(sql)
                resultado2=self.cursor.fetchall()

                for registro in resultado:
                    sql='UPDATE Hojas'
                    sql+=' SET CuestionarioNum='+dialog.GetStringSelection()
                    sql+=' WHERE IDHoja='+str(registro["IDHoja"])
                    self.cursor.execute(sql)
                    self.conn.commit()

                for registro in resultado2:
                    sql='UPDATE Hojas'
                    sql+=' SET CuestionarioNum='+str(cuestionarioSel)
                    sql+=' WHERE IDHoja='+str(registro["IDHoja"])
                    self.cursor.execute(sql)
                    self.conn.commit()

            #movemos una sola hoja a otro cuestionario
            else:
                sql='SELECT IDHoja FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+str(cuestionarioSel)+' AND PaginaNum='+self.choice1.GetStringSelection()[7:]
                self.cursor.execute(sql)
                resultado=self.cursor.fetchall()
                IDHoja=resultado[0]["IDHoja"]

                sql='SELECT max(PaginaNum) AS paginaMax FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND CuestionarioNum='+dialog.GetStringSelection()
                self.cursor.execute(sql)
                resultado=self.cursor.fetchall()
                maxPag=resultado[0]["paginaMax"]

                sql='UPDATE Hojas '
                sql+='SET CuestionarioNum='+dialog.GetStringSelection()+', PaginaNum='+str(maxPag+1)
                sql+=' WHERE IDHoja='+str(IDHoja)
                self.cursor.execute(sql)
                self.conn.commit()
        dialog.Destroy()
        self.llenarLista()

    #boton comprobar identificadores
    def OnBotonCheckIdsButton(self, event):
        mensaje=""
        self.filtroPag1=" AND PaginaNum=1"
        sql=self.generarSQL()
        self.filtroPag1=""
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()

        sql='SELECT PatronId FROM Encuestas WHERE Nombre="'+self.encuesta+'"'
        self.cursor.execute(sql)
        resultado2=self.cursor.fetchall()
        patron=resultado2[0]["PatronId"]

        n=0
        while n<len(resultado):
            self.listCtrl1.SetItemBackgroundColour(n, "White")
            n+=1

        #inicio comprobar identificadores repetidos
        #funciones.mensaje(self,str(len(resultado)))
        n=0
        while n<len(resultado):
            m=n+1
            while m<len(resultado):
                if resultado[n]["Identificador"]==resultado[m]["Identificador"]:
                    self.listCtrl1.SetItemBackgroundColour(n, "Red")
                    self.listCtrl1.SetItemBackgroundColour(m, "Red")
                    mensaje+="Los identificadores de los cuestionarios "+str(resultado[n]["Identificador"])+" y "+str(resultado[m]["Identificador"])+" son iguales\r"
                m+=1
            n+=1
        #fin comprobar identificadores repetidos

        n=0
        while n<len(resultado):
            if len(resultado[n]["Identificador"])!=self.longIdentificador and resultado[n]["Identificador"]!="error":
                self.listCtrl1.SetItemBackgroundColour(n, "Red")
                mensaje+="La longitud del identificador del cuestionario "+str(resultado[n]["Identificador"])+" es incorrecta\r"
            n+=1

        n=0
        while n<len(resultado):
            if resultado[n]["Identificador"]=="error":
                self.listCtrl1.SetItemBackgroundColour(n, "Red")
                mensaje+="El identificador del cuestionario "+str(resultado[n]["Identificador"])+" no se pudo detectar\r"
            n+=1

        #inicio comprobar patron
        n=0
        while n<len(resultado):
            if resultado[n]["Identificador"]!="error":
                ok=1
                if patron!="":
                    m=0
                    while m<len(patron):
                        if not(patron[m]=="*" or patron[m]==resultado[n]["Identificador"][m]):
                            ok=0
                        m+=1
            if ok==0:
                self.listCtrl1.SetItemBackgroundColour(n, "Red")
                mensaje+="El identificador del cuestionario "+str(resultado[n]["Identificador"])+" no coincide con el patron marcado\r"
            n+=1

        #fin comprobar patron

        if mensaje=="":
            mensaje="No se han encontrado errores"
        funciones.mensaje(self,mensaje)

    #buscar por identificador
    def OnBotonBuscarButton(self, event):
        #funciones.mensaje(self,str(self.listCtrl1.GetScrollPos(wx.VERTICAL)))
        sql='SELECT * FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND PaginaNum=1 ORDER BY CuestionarioNum'
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            if registro["Identificador"]==self.txtBuscarId.GetValue():
                sql='SELECT MAX(PaginaNum) FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND Identificador="'+registro["Identificador"]+'"'
                self.cursor.execute(sql)
                resultado2=self.cursor.fetchall()

                indice=0
                n=0
                while n<self.listCtrl1.GetItemCount():
                    if registro["Identificador"]==str(self.listCtrl1.GetItem(n,1).GetText()):
                        indice=n
                    n+=1

                self.listCtrl1.Select(indice, True)
                self.listCtrl1.EnsureVisible(indice)
                self.txtBuscarId.Clear()
                break


    #botones mas y menos (eliminados)
    """
    def OnBotonMasButton(self, event):
        self.proporcion=self.proporcion+0.1
        self.actualizarImagen()

    def OnBotonMenosButton(self, event):
        self.proporcion=self.proporcion-0.1
        self.actualizarImagen()
    """


    #mostrar imagen original
    def OnButtonOriginalButton(self, event):
        seleccionado = self.listCtrl1.GetFirstSelected()
        sql="SELECT * FROM Hojas WHERE IDHoja="+self.hojas[seleccionado]
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            pagina=self.choice1.GetStringSelection()[7:]
            sql='SELECT * FROM Hojas WHERE CuestionarioNum='+str(registro["CuestionarioNum"])+' AND Encuesta='+str(registro["Encuesta"])+' AND PaginaNum='+pagina
            self.cursor.execute(sql)
            resultado=self.cursor.fetchall()
            for registro in resultado:
                extension=funciones.ejecutar("cd $HOME'/Escritorio/Proyectos/"+self.encuesta+resultado[0]["Ruta"]+"/Originales/'&&ls "+registro["Identificador"]+"_"+str(registro["PaginaNum"])+".*")
                funciones.ejecutar("xdg-open $HOME'/Escritorio/Proyectos/"+self.encuesta+resultado[0]["Ruta"]+"/Originales/"+registro["Identificador"]+"_"+str(registro["PaginaNum"])+"."+extension[-3:]+"'")

    #mostrar PDF original
    def OnButtonPDFButton(self, event):
        seleccionado = self.listCtrl1.GetFirstSelected()
        sql="SELECT * FROM Hojas WHERE IDHoja="+self.hojas[seleccionado]
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            pagina=self.choice1.GetStringSelection()[7:]
            sql='SELECT * FROM Hojas WHERE CuestionarioNum='+str(registro["CuestionarioNum"])+' AND Encuesta='+str(registro["Encuesta"])+' AND PaginaNum='+pagina
            self.cursor.execute(sql)
            resultado=self.cursor.fetchall()
            for registro in resultado:
                funciones.ejecutar("xdg-open $HOME'/Escritorio/Proyectos/"+self.encuesta+resultado[0]["Ruta"]+"/PDF/"+registro["Identificador"]+".pdf'")

    #ordenar listado
    def OnListCtrl1ListColClick(self, event):
        if event.GetColumn()==1:
            if self.orden==1:
                self.orden=2
            else:
                self.orden=1
        elif event.GetColumn()==2:
            if self.orden==3:
                self.orden=4
            else:
                self.orden=3
        self.llenarLista()

    #combinar dos cuestionarios
    def OnBotonCombinarButton(self, event):
        seleccionado = self.listCtrl1.GetFirstSelected()
        cuestionarioOrigen=str(self.identificadores[seleccionado])
        #funciones.mensaje(self,"origen "+cuestionarioOrigen)

        #seleccionamos cuestionario destino
        elementos = list()
        for unIdentificador in self.identificadores:
            elementos.append(unIdentificador)
        dialog = wx.SingleChoiceDialog ( None, u'Elija el cuestionario base para combinar.\r\rEL cuestionario '+cuestionarioOrigen+u' desaparecer\xe1, y sus\rp\xe1ginas se a\xf1adir\xe1n al cuestionario elegido.', 'Combinar cuestionarios', elementos )
        if dialog.ShowModal() == wx.ID_OK:
            # Si hemos seleccionado el mismo cuestionario, mostramos un mensaje de error
            cuestionarioDestino=dialog.GetStringSelection()
            if cuestionarioDestino==cuestionarioOrigen:
                funciones.mensaje(self,"No se puede combinar un cuestionario consigo mismo")
            else:
                #buscamos la pagina mas alta en el cuestionario destino y origen
                sql='SELECT MAX(PaginaNum) AS paginaMax, CuestionarioNum, Ruta FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND Identificador="'+cuestionarioDestino+'"'
                self.cursor.execute(sql)
                resultado=self.cursor.fetchall()
                paginaDestinoMax=resultado[0]["paginaMax"]
                cuestionarioNumDestino=resultado[0]["CuestionarioNum"]
                rutaDestino=resultado[0]["Ruta"]

                sql='SELECT MAX(PaginaNum) AS paginaMax, Ruta FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND Identificador="'+cuestionarioOrigen+'"'
                self.cursor.execute(sql)
                resultado=self.cursor.fetchall()
                paginaOrigenMax=resultado[0]["paginaMax"]
                rutaOrigen=resultado[0]["Ruta"]

                #renombramos las paginas del cuestionario origen
                for n in range(1,paginaOrigenMax+1):
                    #funciones.mensaje(self,str(n)+" "+str(paginaOrigenMax+1))
                    funciones.ejecutar("rename 's/"+cuestionarioOrigen+"_"+str(n)+"/"+cuestionarioDestino+"_"+str(n+paginaDestinoMax)+"/' $HOME'/Escritorio/Proyectos/"+self.encuesta+rutaOrigen+"/Originales/'*.*")

                    sql='UPDATE Hojas '
                    sql+='SET Identificador="'+cuestionarioDestino+'", PaginaNum='+str(n+paginaDestinoMax)+', CuestionarioNum='+str(cuestionarioNumDestino)+' '
                    sql+='WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND Identificador="'+cuestionarioOrigen+'" and PaginaNum='+str(n)
                    #funciones.mensaje(self,sql)
                    self.cursor.execute(sql)
                    self.conn.commit()

                #borramos ambos pdf
                funciones.ejecutar("rm $HOME'/Escritorio/Proyectos/"+self.encuesta+rutaOrigen+"/PDF/"+cuestionarioOrigen+".pdf'")
                funciones.ejecutar("rm $HOME'/Escritorio/Proyectos/"+self.encuesta+rutaOrigen+"/PDF/"+cuestionarioDestino+".pdf'")

                #creamos el nuevo pdf
                funciones.ejecutar("IFS=$'\n' && convert `ls -v $HOME'/Escritorio/Proyectos/"+self.encuesta+rutaOrigen+"/Originales/'"+cuestionarioDestino+"_*.*` $HOME'/Escritorio/Proyectos/"+self.encuesta+rutaOrigen+"/PDF/"+cuestionarioDestino+".pdf'")

        dialog.Destroy()
        self.llenarLista()



# Fin botones


# Inicio funciones

    def cambiarImagen(self, imagen):
        imagenNew = wx.Image(sys.path[0]+"/imagenes/"+imagen+".tif", wx.BITMAP_TYPE_ANY)

        if self.OriginalW==0:
            self.OriginalW, self.OriginalH = self.scrollSizer.GetSize()
        W = imagenNew.GetWidth()
        H = imagenNew.GetHeight()
        if W > H:
            NewW = self.OriginalW * self.proporcion
            NewH = self.OriginalW * H / W * self.proporcion
        else:
            NewH = self.OriginalH * self.proporcion
            NewW = self.OriginalH * H / W * self.proporcion
        imagenNew = imagenNew.Scale(NewW,NewH)
        self.staticBitmap1.SetBitmap(wx.BitmapFromImage(imagenNew))
        self.scrolledPanel1.SetupScrolling()

    # actualiza la imagen segun la seleccionada en la lista
    def actualizarImagen(self):
        seleccionado = self.listCtrl1.GetFirstSelected()
        sql="SELECT * FROM Hojas WHERE IDHoja="+self.hojas[seleccionado]
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            pagina=self.choice1.GetStringSelection()[7:]
            sql='SELECT * FROM Hojas WHERE CuestionarioNum='+str(registro["CuestionarioNum"])+' AND Encuesta='+str(registro["Encuesta"])+' AND PaginaNum='+pagina
            self.cursor.execute(sql)
            resultado=self.cursor.fetchall()
            for registro in resultado:
                self.texto.Clear()
                if registro["Texto"]=="":
                    self.texto.AppendText("Texto en blanco")
                else:
                    self.texto.AppendText(registro["Texto"])
                    self.texto.ShowPosition(0)
                self.identificador.SetValue(registro["Identificador"])
                self.cambiarImagen(str(registro["IDHoja"]))

    def generarSQL(self):
        sql='SELECT * FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'")'
        sql+=self.filtro1
        sql+=self.filtro2
        sql+=self.filtroPag1
        sql+=self.filtro4
        sql+=self.filtro5
        #funciones.mensaje(self,sql)
        if self.orden==1:
            sql+=' ORDER BY Identificador, PaginaNum'
        elif self.orden==2:
            sql+=' ORDER BY Identificador DESC, PaginaNum'
        elif self.orden==3:
            sql='SELECT IDHoja, Encuesta, CuestionarioNum, 1 as PaginaNum, Texto, Identificador, FechaScan, Actual, Etiqueta, Ruta, max(PaginaNum) as mpag FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'")'
            sql+=self.filtro1
            sql+=self.filtro2
            sql+=self.filtroPag1
            sql+=self.filtro4
            sql+=self.filtro5
            sql+=' GROUP BY CuestionarioNum ORDER BY mpag DESC'
        else:
            sql='SELECT IDHoja, Encuesta, CuestionarioNum, 1 as PaginaNum, Texto, Identificador, FechaScan, Actual, Etiqueta, Ruta, max(PaginaNum) as mpag FROM Hojas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'")'
            sql+=self.filtro1
            sql+=self.filtro2
            sql+=self.filtroPag1
            sql+=self.filtro4
            sql+=self.filtro5
            sql+=' GROUP BY CuestionarioNum ORDER BY mpag'
        return sql


# Fin funciones


# Inicio control de eventos

    # evento lista
    def OnListCtrl1ListItemSelected(self, event):
        seleccionado = self.listCtrl1.GetFirstSelected()
        sql="SELECT * FROM Hojas WHERE IDHoja="+self.hojas[seleccionado]
        self.cursor.execute(sql)
        resultado=self.cursor.fetchall()
        for registro in resultado:
            sql='SELECT * FROM Hojas WHERE CuestionarioNum='+str(registro["CuestionarioNum"])+' AND Encuesta='+str(registro["Encuesta"])+' ORDER BY PaginaNum'
            self.cursor.execute(sql)
            resultado2=self.cursor.fetchall()
            paginas=0
            self.choice1.Clear()
            for registro2 in resultado2:
                #funciones.mensaje(self,str(i)+str(paginas))
                self.choice1.Append("pagina "+str(registro2["PaginaNum"]))
                self.choice1.SetSelection(0)

            sql='SELECT Nombre FROM Etiquetas WHERE IDEtiqueta='+str(resultado2[0]["Etiqueta"])
            self.cursor.execute(sql)
            resultado3=self.cursor.fetchall()
            etiqueta=""
            if str(resultado2[0]["Etiqueta"])=="0" or str(resultado3[0]["Nombre"])=="None":
                etiqueta="Ninguna"
            else:
                etiqueta=str(resultado3[0]["Nombre"])

            self.texto.Clear()
            self.texto.AppendText(registro["Texto"])
            self.texto.ShowPosition(0)
            self.identificador.SetValue(registro["Identificador"])
            #TODO: scroll
            self.textoDatos.SetLabel("Fecha: "+str(resultado2[0]["FechaScan"])+", Etiqueta: "+etiqueta)
            self.textoRuta.SetLabel("Ruta: "+str(resultado2[0]["Ruta"][-30:]))
            self.actualizarImagen()

    # evento cambiar de pagina
    def OnChoice1Choice(self, event):
        self.actualizarImagen()

    #control de la rueda del raton para hacer scroll sobre la imagen
    def scrolledPanel1Mousewheel(self, event):
        #funciones.mensaje(self)
        slider = event.GetEventObject()
        if (event.GetWheelRotation() > 0):
            self.proporcion=self.proporcion+0.1
            self.actualizarImagen()
        else:
            self.proporcion=self.proporcion-0.1
            self.actualizarImagen()

    #evento para capturar el boton enter en el cuadro de corregir identificador
    def OnIdentificadorKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_RETURN or event.GetKeyCode() == wx.WXK_NUMPAD_ENTER:
            self.OnButActualizarIdButton(event)
        else:
            event.Skip()

    #evento para capturar el boton enter en el cuadro de buscar identificador
    def OnTxtBuscarIdKeyDown(self, event):
        if event.GetKeyCode() == wx.WXK_RETURN or event.GetKeyCode() == wx.WXK_NUMPAD_ENTER:
            self.OnBotonBuscarButton(event)
        else:
            event.Skip()

    #evento filtro por sesion
    def OnChoiceSesionChoice(self, event):
        if self.choiceSesion.GetSelection()==0:
            self.filtro1=' AND Actual=1'
        else:
            self.filtro1=''
        self.llenarLista()

    #evento filtro por etiqueta
    def OnChoiceEtiquetaChoice(self, event):
        if self.choiceEtiqueta.GetSelection()==0:
            self.filtro2=''
        else:
            self.filtro2=' AND Etiqueta=(SELECT IDEtiqueta FROM Etiquetas WHERE Encuesta=(SELECT IDEncuesta FROM Encuestas WHERE Nombre="'+self.encuesta+'") AND Nombre="'+self.choiceEtiqueta.GetStringSelection()+'")'
            #funciones.mensaje(self,filtro2)
        self.llenarLista()

    #evento filtro por fecha
    def OnChoiceFechaChoice(self, event):
        if self.choiceFecha.GetSelection()==0:
            self.filtro4=''
        else:
            self.filtro4=' AND FechaScan="'+self.choiceFecha.GetStringSelection()+'"'
            #funciones.mensaje(self,filtro2)
        self.llenarLista()

    def OnChoiceRutaChoice(self, event):
        if self.choiceRuta.GetSelection()==0:
            self.filtro5=''
        else:
            self.filtro5=' AND Ruta="'+self.choiceRuta.GetStringSelection()+'"'
            #funciones.mensaje(self,filtro2)
        self.llenarLista()

 # Fin control de eventos


