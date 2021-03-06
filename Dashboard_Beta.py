from tkinter import Frame, Entry, Tk, Label, Button, ttk, HORIZONTAL, RAISED, SUNKEN, S, W, E, N
import openpyxl
import xlrd as xl
import array as arr
import Dictionery as dic
from datetime import datetime
import time
from time import gmtime, strftime
import Excel_Display_Window
#from Target_Entry_Window import Target_button
import Target_Entry_Window as tew

import reading_excel_sheet as res
import readsheet_functions as rsf


#master and frame are main window for CPW, PAC, SBP, ALCP
master=Tk()
master.title("DashBoard")
master.grid_columnconfigure(0,weight=1)

frame= Frame(master, highlightbackground="green", highlightcolor="green", highlightthickness=2, bd= 0)
frame.grid_columnconfigure(0,weight=1)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid(row=0, column=0)
Heading=Label(frame, text="DASHBOARD", font=("Courier", 44))
Heading.grid(row=0, columnspan=2)


#### DATE
Date = Label(frame, font=('Courier', 15), bg='grey', text = strftime("%d %b %Y", gmtime()))
Date.grid(row=0, column = 20, sticky = N+E+W)
#### DATE

#### CLOCK
time1 = ''
clock = Label(frame, font=('Courier', 15), bg='grey')
clock.grid(row=0, column=20, sticky = E+W)
def tick():
    global time1
   
    time2 = time.strftime('%a,%H:%M:%S')
  
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)

    clock.after(200, tick)

tick()
#### CLOCK










def Act1(i):
        
        master2 = Tk()
        frame2= Frame(master2, highlightbackground="red", highlightcolor="green", highlightthickness=2, width=400, height = 50, bd= 0)
        frame2.grid()

        if i==0:
                       
                L1=Label(frame2, text=buttonCP.cget('text'))
                L1.grid(row=0, column=3)
                SAP_code = rsf.get_col('DR-june-18.xlsx', res.sheet, 'SAP code')
                
                for j in range(1,len(SAP_code) ):      #up down
 #                       L2=Label(frame2, text=dic.a[j])
 #                       L2.grid(row=int(L1.grid_info()['row'])+ 1 , column=int(L1.grid_info()['column']))
                        L2e=Label(frame2, text=SAP_code[j])
                        L2e.grid(row=int(L1.grid_info()['row'])+ j + 2 , column=int(L1.grid_info()['column']))
                        for q in range(1, len(dic.a)):    #left right
 #                           L2=Label(frame2, text=dic.a[q])
 #                            L2.grid(row=int(L2e.grid_info()['row']) , column=int(L1.grid_info()['column']))
                            L3e=Label(frame2, text=rsf.find_val('DR-june-18.xlsx', res.sheet, dic.a[q], SAP_code[i]) )
                            L3e.grid(row=int(L2e.grid_info()['row']), column=int(L2e.grid_info()['column']) + q)


#rsf.find_val('DR-june-18.xlsx','sheet_names(1)', 'OPENING BALANCE (MT)',  'S40000000066')
        #if i==1:

        #if i==2:

        #if i==3:









#### Seperater
ttk.Separator(frame, orient = HORIZONTAL).grid(row=1, columnspan = 5 , sticky ="sew")
#### Seperater

#arr = []

### 4 Prod Button

buttonCP=Button(frame, text="Chlorinated Paraffin", bg="red", fg="white", width=25)
buttonCP.grid(rowspan=2, column=0)
info = buttonCP.grid_info()
buttonCP.configure(command= lambda k=buttonCP: Act1(int(info["column"])))

buttonPAC=Button(frame, text="Poly-Alluminum Chloride", bg="red", fg="white", width=25)
buttonPAC.grid(row=2, column=int(info["column"])+1)
buttonPAC.configure(command= lambda k=buttonPAC: Act1(int(info["column"]))+1)

buttonSBP=Button(frame, text="Stable Bleaching Powder", bg="red", fg="white", width=25)
buttonSBP.grid(row=2, column=int(info["column"])+2)
buttonSBP.configure(command= lambda k=buttonSBP: Act1(int(info["column"]))+2)

buttonALCP=Button(frame, text="Anhydrous Alluminium Chloride", bg="red", fg="white", width=25)
buttonALCP.grid(row=2, column=int(info["column"])+3)
buttonALCP.configure(command= lambda k=buttonALCP: Act1(int(info["column"])+3))
        

"""#### Prod BUTTONS
for i in range(1, res.worksheet.nrows - 1):
        button=Button(frame, text=res.rowval[i], bg="red", fg="white", width=10)
        button.grid(row=2, column=i-1)
        button.configure(command= lambda k=button: Act1(i))
        
        arr.append(res.rowval[i])
#### Prod BUTTONS"""




master.mainloop()




