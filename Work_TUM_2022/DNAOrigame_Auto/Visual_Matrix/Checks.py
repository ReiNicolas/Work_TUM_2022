from tkinter.tix import INTEGER
import wx

def Checks(Final_Volume_Text,Initial_Temperature,Final_Temperature):
    Final_Volume=float(Final_Volume_Text.GetLineText(0))
    I_Temperature=int(Initial_Temperature.GetLineText(0))
    F_Temperature=int(Final_Temperature.GetLineText(0))
    
    if(Final_Volume<1.0):
        Message=wx.MessageBox(message="Volume to make of DNA origami too small").ShowModal()
        return False
    elif(I_Temperature>=100):
        Message=wx.MessageBox(message="Initial temperature too high, thermocycler can only go to 99 degress").ShowModal()
    elif(F_Temperature>=I_Temperature):
        Message=wx.MessageBox(message="Final temperature must be smaller than initial temperature")
    else:
        return True