#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import principal

modules ={u'Edit': [0, '', u'Edit.ico'],
 u'abrir_encuesta': [0, '', u'abrir_encuesta.py'],
 u'crop': [0, '', u'crop.py'],
 u'editar_bbdd': [0, '', u'editar_bbdd.py'],
 u'funciones': [0, '', u'funciones.py'],
 u'op_encuesta': [0, '', u'op_encuesta.py'],
 u'principal': [1, u'Ventana principal OCR', u'principal.py'],
 u'rubberband': [0, '', u'rubberband.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = principal.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
