import sys
import os
import json

#sys.path.append(os.getcwd())

import wx
from Visual_Matrix_Functions import *
from Global_Functions import *
from Checks import *

class MyFrame(wx.Frame):
     
    def __init__(self,parent,ID,title):
        Selection_Mode=0
        wx.Frame.__init__(self,parent,ID,title)

        Box=wx.BoxSizer(wx.VERTICAL)
        
        Grid_1=wx.GridSizer(Grid_Lenght)
        Grid_2=wx.GridSizer(Grid_Lenght)
        Grid_3=wx.GridSizer(Grid_Lenght)

        #This dictionary is needed to create the label of each button.
        Dictionary_Alphabet={0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H',8:'I',9:'J'}
        Array_Of_Buttons=[[[wx.Button(self,id=ID_Buttons(i,u,p),label=Dictionary_Alphabet[u]+str(p+1)) for p in range(0,Grid_Lenght)] for u in range(0,Grid_Height)] for i in range(0,Number_Of_Grids)]
        Pipeting_Field=[[[True for i in range(0,Grid_Lenght)] for u in range(0,Grid_Height)] for p in range(0,Number_Of_Grids)]

        Green_For_Buttons=wx.Colour(0,255,30,200)
        Red_For_Buttons=wx.Colour(255,0,0,200)

        #Now adding the function that happens when you click a button
        #First the grid buttons
        def Change(ID):
            Grid=Grid_Of_ID(ID)
            Row=Row_Of_ID(ID)
            Colum=Colum_Of_ID(ID)
            if()
            if(Pipeting_Field[Grid][Row][Colum]):
                Array_Of_Buttons[Grid][Row][Colum].SetBackgroundColour(Red_For_Buttons)
            else:
                Array_Of_Buttons[Grid][Row][Colum].SetBackgroundColour(Green_For_Buttons)
            Pipeting_Field[Grid][Row][Colum]=not Pipeting_Field[Grid][Row][Colum]
        
        def OnButton(self):
            ID=self.Id
            Change(ID)

        #Now the other buttons
        #But first a auviliary function
        def Binary_TOF(bool):
            if(bool):
                return '1'
            else:
                return '0'

        def Finish_And_Write(self):
            if(Checks(Final_Volume_Text,Initial_Temperature,Final_Temperature)):
                File=open(File_Name_Text.GetLineText(0)+".txt",'w')
                for i in range(0,Number_Of_Grids):
                    for u in range(0,Grid_Height):
                        for p in range(0,Grid_Lenght):
                            File.write(Binary_TOF(Pipeting_Field[i][u][p]))
                File.write("\n")
                File.write(Ratio_Text.GetLineText(0))
                File.write("\n")
                File.write(Final_Volume_Text.GetLineText(0))
                File.write("\n")    
                File.write(Initial_Temperature.GetLineText(0))
                File.write("\n")
                File.write(Final_Temperature.GetLineText(0))
                File.close()

        for i in range(0,Number_Of_Grids):
            for u in range(0,Grid_Height):
                for p in range(0,Grid_Lenght):
                    Array_Of_Buttons[i][u][p].SetBackgroundColour(Green_For_Buttons)
                    Array_Of_Buttons[i][u][p].Bind(wx.EVT_BUTTON,OnButton,Array_Of_Buttons[i][u][p])
                    if(i==0):
                        Grid_1.Add(Array_Of_Buttons[i][u][p],1,wx.EXPAND)
                    elif(i==1):
                        Grid_2.Add(Array_Of_Buttons[i][u][p],1,wx.EXPAND)
                    else:
                        Grid_3.Add(Array_Of_Buttons[i][u][p],1,wx.EXPAND)
        
        Box_Options=wx.BoxSizer(wx.VERTICAL)

        Box_First_Options=wx.BoxSizer(wx.HORIZONTAL)

        Finish_Botton=wx.Button(self,id=2000,label='Write file')
        Finish_Botton.Bind(wx.EVT_BUTTON,Finish_And_Write,Finish_Botton)

        File_Name_Text=wx.TextCtrl(self,id=2001,value="Folder Name ( we will add the .txt )")

        Ratio_Text=wx.TextCtrl(self,id=2002,value="Ratio: Use dot to separate decimal")

        Final_Volume_Text=wx.TextCtrl(self,id=2003,value="Here the volume you want to make of DNA origami, in microliters, minimun of 1")

        Box_First_Options.Add(Finish_Botton,1,wx.EXPAND)
        Box_First_Options.Add(File_Name_Text,3,wx.EXPAND)
        Box_First_Options.Add(Ratio_Text,2,wx.EXPAND)
        Box_First_Options.Add(Final_Volume_Text,3,wx.EXPAND)


        Box_Temperature=wx.BoxSizer(wx.HORIZONTAL)

        Initial_Temperature=wx.TextCtrl(self,id=2004,value="Here the starting temperature of your temperature lader ( must be a integer )")
        Final_Temperature=wx.TextCtrl(self,id=2005,value="Here the final temperature of your temperature lader ( must be a integer )")

        Box_Temperature.Add(Initial_Temperature,1,wx.EXPAND)
        Box_Temperature.Add(Final_Temperature,1,wx.EXPAND)

        Box_Options.Add(Box_First_Options,1,wx.EXPAND)
        Box_Options.Add(Box_Temperature,1,wx.EXPAND)


        Box.Add(Grid_1,8,wx.EXPAND)
        Box.Add(Grid_2,8,wx.EXPAND|wx.TOP,10)
        Box.Add(Grid_3,8,wx.EXPAND|wx.TOP,10)
        Box.Add(Box_Options,2, wx.EXPAND)


        self.SetAutoLayout(True)
        self.SetSizer(Box)
        self.Layout()
        

App=wx.App()
Frame=MyFrame(None,-1,'Hello Markus')

Frame.Show()

App.MainLoop()