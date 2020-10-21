# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 14:11:37 2020

@author: krupali
"""
import tkinter  as tkr

def showpopUpWindow(title,message):
    """ 
       The function  is to show popupwindow
  
       Parameters: 
          title: title of popup
          message: meassage print in popup  window

    """
    NORM_FONT= ("Verdana", 14)
    popUp = tkr.Tk()
    popUp.title(title)
    popUp.geometry('500x500')


    yBar = tkr.Scrollbar(popUp)
    yBar.pack(side = tkr.RIGHT ,fill = "y")
    
    xBar = tkr.Scrollbar(popUp, orient = tkr.HORIZONTAL)
    xBar.pack(side = tkr.BOTTOM ,fill = "x")
    
    txtBox=tkr.Text(popUp,height=500,width=350,yscrollcommand = yBar.set,xscrollcommand = xBar.set, wrap = "none",font=NORM_FONT)  
    txtBox.pack(expand=0,fill=tkr.BOTH) 
    yBar.config(command=txtBox.yview)
    xBar.config(command=txtBox.xview)

    txtBox.insert(tkr.END,message)
    
    popUp.mainloop()