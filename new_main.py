import tkinter
from tkinter import ttk
# from csv import *
import csv
from tkinter import messagebox
import sqlite3



def savedata():
    pt_name = lblpt_entry.get()
    doc_name =lbldoc_entry.get()
    tre_type = Treatment_type_combo.get()
    sono_date = lbldate_spinbox.get()
    sono_type = lblscp_combo.get()
    rs = lblrs_entry.get()
    sono_doc = lblsonodoc_entry.get()

    print("Patient name:",pt_name)
    print("Ref Doctor Name:",doc_name)
    print("Treatment Type:",tre_type)
    print("SonoGraphy Date:",sono_date)
    print("Sonography Report type:",sono_type)
    print("SonoGraphy Price:",rs)
    print("SonoGraphy Doctor:",sono_doc)
    
    # connect sqlite3 database

    conn = sqlite3.connect('data.db')
    table_create_query = ''' CREATE TABLE IF NOT EXISTS Muktajivan_Data
            (Pt_Name TEXT, Ref_Doctor TEXT, Treatment_type TEXT, Sonography_Date TEXT, Treatment_Report_Type TEXT, Sonography_price TEXT, Sonography_doctor TEXT)
    '''
    conn.execute(table_create_query)

    # insert data
    data_insert_query = '''
    INSERT INTO Muktajivan_Data(Pt_Name, Ref_Doctor, Treatment_type, Sonography_Date, Treatment_Report_Type, Sonography_price, Sonography_doctor) VALUES
    (?,?,?,?,?,?,?)'''
    data_insert_tuple =(pt_name, doc_name, tre_type, sono_date, sono_type, rs, sono_doc)
    cursor = conn.cursor()
    cursor.execute(data_insert_query,data_insert_tuple)
    cursor.execute("SELECT * FROM Muktajivan_Data")
    data = cursor.fetchall()
    with open ('output.csv','w',newline ='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(data)

    conn.commit()
    conn.close()

    # ,,,,,
    

    
    # sono_lst = [pt_name,doc_name,tre_type,sono_date,sono_type,rs]
    # with open("data_entry.csv","w") as file:
    #   Writer=writer(file)
    #   Writer.writerow(["Patient Name","Ref Doctor Name","Treatment Type","sonography Date","Treatment Report type","sonography price"])
    #   Writer.writerows(str(sono_lst))
   
    # messagebox.showinfo("information","save sucessfully")
        
window = tkinter.Tk()
window.title("Muktajivan Data")

frame = tkinter.Frame(window)
frame.pack()

# saving data info
info_frame = tkinter.LabelFrame(frame,text="Patient Name and Doctor name")
info_frame.grid(row=0,column=0,sticky="news")

lblpt= tkinter.Label(info_frame,text="Patient Name")
lblpt.grid(row=0,column=0)

lbldoc=tkinter.Label(info_frame,text="Ref Doctor Name")
lbldoc.grid(row=0,column=1)

lblpt_entry= tkinter.Entry(info_frame)
lbldoc_entry= tkinter.Entry(info_frame)
lblpt_entry.grid(row=1,column=0)
lbldoc_entry.grid(row=1,column=1)

Treatment_type = tkinter.Label(info_frame, text="Treatment Type")
Treatment_type_combo= ttk.Combobox(info_frame, values=["USG Abdomen","Doppler","Memography","Neck","Gravid Uterus","Tapping","Scrotum","Breast","Brain","Local Part","Ovulation Study","Chest"])
Treatment_type.grid(row=0,column=2)
Treatment_type_combo.grid(row=1,column=2)

lbldate = tkinter.Label(info_frame,text="Sonography Date")
lbldate_spinbox =tkinter.Spinbox(info_frame,from_=1, to=31)
lbldate.grid(row=2,column=0)
lbldate_spinbox.grid(row=3,column=0)

lblscp = tkinter.Label(info_frame,text="Treatment Report Type")
lblscp_combo = ttk.Combobox(info_frame,values=["SC -Only Report","P - Report With Sonography Photo"])
lblscp.grid(row=2,column=1)
lblscp_combo.grid(row=3,column=1)

for a in info_frame.winfo_children():
    a.grid_configure(padx =10,pady=5)

# saving data info
info2_frame = tkinter.LabelFrame(frame,text="")
info2_frame.grid(row=1,column=0,sticky="news")


lblrs = tkinter.Label(info2_frame,text="Sonography Price")
lblrs.grid(row=0,column=0)
lblrs_entry= tkinter.Entry(info2_frame)
lblrs_entry.grid(row=1, column=0)

lblsonodoc = tkinter.Label(info2_frame,text="Sonography Doctor")
lblsonodoc.grid(row=0,column=1)
lblsonodoc_entry= tkinter.Entry(info2_frame)
lblsonodoc_entry.grid(row=1, column=1)


button = tkinter.Button(frame,text="Submit Data",command=savedata)
button.grid(row=3,column=0)


window.mainloop()
