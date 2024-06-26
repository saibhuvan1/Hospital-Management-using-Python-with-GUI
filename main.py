from tkinter import *
root=Tk()
def doctor():
    doctorwindow =Toplevel(root)
    doctorwindow.geometry('500x300')
    doctorwindow.title("doctor info")
    #doctorwindow.iconbitmap(r'C:\Users\heman\Downloads\qiBXx4AaT.ico')
    de = Button(doctorwindow,text="Exit",bd=5,command=doctorwindow.destroy,activeforeground='red')
    de.config(font=("Borealis",15))
    ddw=Button(doctorwindow,text="doctor details",bd=10,activeforeground='blue4',command=docdetail)
    ddw.pack()
    daw=Button(doctorwindow,text="doctor appointment avilability",bd=10,activeforeground='blue4',command=appointment)
    daw.pack()
    dfdw=Button(doctorwindow,text="Doctor fees details",bd=10,activeforeground="blue4",command=docfee)
    dfdw.pack()
    de.pack(side='bottom')
    
def docdetail():
    doctordetailwindow=Toplevel(root)
    doctordetailwindow.title("Doctor details")
    #doctordetailwindow.iconbitmap(r'C:\Users\heman\Downloads\qiBXx4AaT.ico')
    for i in range(10):
        for j in range(4):
            if i==0:
                t=Entry(doctordetailwindow,width=30,fg='black',font=('book antiqua',16,'bold'),justify=CENTER)
                t.grid(row=i,column=j)
                t.insert(END,lst[i][j])
            else:
                t=Entry(doctordetailwindow,width=30,fg='blue',font=('book antiqua',14))
                t.grid(row=i,column=j)
                t.insert(END,lst[i][j])
           
    ddwe=Button(doctordetailwindow,text="Exit",bd=5,width=20,activeforeground='red',command=doctordetailwindow.destroy)
    ddwe.config(font=("Borealis",15))
    ddwe.grid(row=11,column=2,sticky=W,pady=2)
def appointment():
    appwindow =Toplevel(root,width=500,height=300)
    appwindow.title("appoinment ")
    #appwindow.iconbitmap(r'C:\Users\heman\Downloads\qiBXx4AaT.ico')
    for i in range(10):
        for j in range(3):
           if i==0:
               t1=Entry(appwindow,width=30,fg='black',font=('book antiqua',16,'bold'))
               t1.grid(row=i,column=j)
               t1.insert(END,lst1[i][j])
           else:
               t1=Entry(appwindow,width=30,fg='blue',font=('book antiqua',14))
               t1.grid(row=i,column=j)
               t1.insert(END,lst1[i][j]) 
           
    le=Button(appwindow,text="Exit",bd=5,font="borealis",command=appwindow.destroy,activeforeground='red')
    le.config(font=("Borealis",13))
    le.grid(row=11,column=1,sticky=W,pady=5)
def docfee():
    doctorfee=Toplevel(root)
    doctorfee.title("Doctor fee")
    #doctorfee.iconbitmap(r'C:\Users\heman\Downloads\qiBXx4AaT.ico')
    for i in range(10):
        for j in range(3):
           if i==0:
               t2=Entry(doctorfee,width=30,fg='black',font=('book antiqua',16,'bold'))
               t2.grid(row=i,column=j)
               t2.insert(END,lst2[i][j])
           else:
               t2=Entry(doctorfee,width=30,fg='blue',font=('book antiqua',14))
               t2.grid(row=i,column=j)
               t2.insert(END,lst2[i][j])
    dfe=Button(doctorfee,activeforeground='red',text="Exit",bd=5,command=doctorfee.destroy)
    dfe.config(font=("Borealis",13))
    dfe.grid(row=11,column=1,sticky=W,pady=5)
    
def precautions():
    pre =Toplevel(root,width=500,height=300)
    pre.title("PRECAUTIONS")
    #pre.iconbitmap(r'C:\Users\heman\Downloads\qiBXx4AaT.ico')
    pe = Button(pre,text="Exit",bd=5,command=pre.destroy,activeforeground='red')
    for i in range(7):
        for j in range(3):
            if i==0 and j==2 :
                t6=Text(pre,height=2,width=150,fg='black',font=('book antiqua',12,'bold'))
                t6.grid(row=i,column=j)
                t6.insert(END,lst5[i][j])
            elif i==0 and j!=2:
                 t6=Text(pre,height=2,width=13,fg='black',font=('book antiqua',12,'bold'))
                 t6.grid(row=i,column=j)
                 t6.insert(END,lst5[i][j])
            elif i!=0 and j==2 :
                t7=Text(pre,height=3,width=150,fg='blue',font=('book antiqua',12,'bold'))
                t7.grid(row=i,column=j)
                t7.insert(END,lst5[i][j])
          
            elif i!=0 and j!=2 :
                t6=Text(pre,height=3,width=13,fg='blue',font=('book antiqua',12,'bold'))
                t6.grid(row=i,column=j)
                t6.insert(END,lst5[i][j])
              
    pe.config(font=("Borealis",13))      
    pe.grid(row=11,column=2,sticky=W,pady=2)  
def lab():
    lab1 =Toplevel(root,width=500,height=300)
    lab1.title("LAB")
    lab1.geometry('500x300')
    #lab1.iconbitmap(r'C:\Users\heman\Downloads\qiBXx4AaT.ico')
    el = Button(lab1,text="Exit",bd=5,command=lab1.destroy,activeforeground='red')
    ltw=Button(lab1,text="available tests",activeforeground='blue',bd=10,command=labtest)
    ltw.pack()
    lfw=Button(lab1,text="lab fees",activeforeground='blue',bd=10,command=labfee)
    lfw.pack()
    el.config(font=("Borealis",13))
    el.pack(side='bottom')   
def labfee():
    feewindow=Toplevel(root)
    feewindow.title("LAB TESTS")
    #feewindow.iconbitmap(r'C:\Users\heman\Downloads\qiBXx4AaT.ico')
    lfe=Button(feewindow,text="exit",bd=5,command=feewindow.destroy,activeforeground='red')
    for i in range(24):
        for j in range(3):
           if i==0:
               t4=Entry(feewindow,width=20,fg='black',font=('book antiqua',16,'bold'))
               t4.grid(row=i,column=j)
               t4.insert(END,lst4[i][j])
           else:
               t4=Entry(feewindow,width=25,fg='blue',font=('arial',14))
               t4.grid(row=i,column=j)
               t4.insert(END,lst4[i][j])
    lfe.config(font=("Borealis",13))
    lfe.grid(row=24,column=1,sticky=W,pady=5)
def labtest():
    testwindow=Toplevel(root)
    testwindow.title("LAB TESTS")
    #testwindow.iconbitmap(r'C:\Users\heman\Downloads\qiBXx4AaT.ico')
    lte=Button(testwindow,text="exit",bd=5,command=testwindow.destroy,activeforeground='red')
    for i in range(24):
        for j in range(2):
           if i==0:
               t3=Entry(testwindow,width=20,fg='black',font=('book antiqua',16,'bold'))
               t3.grid(row=i,column=j)
               t3.insert(END,lst3[i][j])
           else:
               t3=Entry(testwindow,width=25,fg='blue',font=('arial',14))
               t3.grid(row=i,column=j)
               t3.insert(END,lst3[i][j])
    lte.config(font=("Borealis",13))
    lte.grid(row=24,column=1,sticky=W,pady=5)           
root.title("AYUDA HOSPITAL HELPDESK")
#root.iconbitmap(r'C:\Users\heman\Downloads\qiBXx4AaT.ico')
root.geometry('500x300')
bdi=Button(root,text="doctor info",bd=10,command=doctor,activeforeground='blue4')
be=Button(root,text="EXIT",bd=5,command=root.destroy,activeforeground='red')
bp=Button(root,text="safety precautions",bd=10,command=precautions,activeforeground='blue')
bl=Button(root,text="lab info",bd='10',activeforeground='blue4',command=lab)
ld=Label(root,text="Welcome to AYUDA Hospital Helpdesk")
ld.config(font=("algerian",18))
ld.pack()
bdi.pack()
bp.pack()
bl.pack()
be.config(font=("Borealis",13))
be.pack(side='bottom')
lst=[("Sno","Doctor name","Specialization","Designation"),
     (1,"Dr.HEMANTH","CARDILOGIST","MBBS,M.D in CARDIOLOGY"),
     (2,"Dr.SIVA","DENTIST","BDS"),
     (3,"Dr.VARUN","PEDIATRIST","MBBS,M.D in PAEDIATRICS"),
     (4,"Dr.JANHAVI","NEUROLOGIST","MBBS,M.D in NEUROLOGY"),
     (5,"Dr.BHAGHI","GYNECOLOGIST","MBBS,M.D in GYNECOLOGY"),
     (6,"Dr.SAMHITHA","DERMATOLOGIST","MBBS,M.D in DERTMATOLGY"),
     (7,"Dr.RAMYA","PSYCHIATRIST","MBBS,MS in PSYCHIATRY"),
     (8,"Dr.SAKETH","ORTOPAEDICS","MBBS,MS in ORTHOPAEDICS"),
     (9,"Dr.ROHITH","GENERAL SURGEON","MBBS")] 
lst1=[("Sno","Doctor name","Appointment Availability",),
     (1,"Dr.HEMANTH","10AM to 5 PM,EXCEPT SUNDAY"),
     (2,"Dr.SIVA","11 AM to 7 PM,EXCEPT SUNDAY"),
     (3,"Dr.VARUN","10 AM to 9 PM,EVERY DAY"),
     (4,"Dr.JANHAVI","11 AM to 6 PM,EXCEPT SUNDAY"),
     (5,"DR.BHAGHI","12 NOON to 7 PM,EVERY DAY"),
     (6,"Dr.SAMHITHA","10 AM to 9 PM,EVERY DAY"),
     (7,"Dr.RAMYA","11 AM to 6 PM, EXCEPT SUNDAY"),
     (8,"Dr.SAKETH","10 AM to 7 PM,EVERY DAY"),
     (9,"Dr.ROHITH","10 AM to 8 PM, EVERY DAY")]
lst2=[("Sno","Doctor name","Fee",),
     (1,"Dr.HEMANTH","Rs.1000"),
     (2,"Dr.SIVA","Rs.500"),
     (3,"Dr.VARUN","Rs.400"),
     (4,"Dr.JANHAVI","Rs.700"),
     (5,"DR.BHAGHI","Rs.600"),
     (6,"Dr.SAMHITHA","Rs.600"),
     (7,"Dr.RAMYA","Rs.700"),
     (8,"Dr.SAKETH","Rs.750"),
     (9,"Dr.ROHITH","Rs.900")]
lst3=[("Sno","TEST NAME"),(1,"semen analysis"),(2,"IAT (Indirect antiglobulin)"),
      (3,"DAT"),(4,"RTPCR for Covid"),(5,"Glucose panel"),(6,"Lipid panel"),
      (7,"Blood count"),(8,"MRI Scan"),(9,"CT Scan"),
      (10,"Ultra sound scan"),(11,"ANA"),(12,"Bmp(basic metabolic panel)"),
      (13,"Flu test (influenza A&B screen)"),(14,"Hemoglobin A1C"),(15,"Urinalysis"),
      (16,"TSH"),(17,"PTT"),(18,"PT"),(19,"Microalbumin"),(20,"LFT"),(21,"Lyme antibody"),
      (22,"IGM"),(23,"NS1")]
lst4=[("Sno","TEST NAME","FEE"),(1,"semen analysis","Rs.150"),(2,"IAT (Indirect antiglobulin)","Rs.550"),
      (3,"DAT","700"),(4,"RTPCR for Covid","Rs.1400"),(5,"Glucose panel","Rs.200"),(6,"Lipid panel","Rs.500"),
      (7,"Blood count","Rs.400"),(8,"MRI Scan","Rs.4000"),(9,"CT Scan","Rs.3500"),
      (10,"Ultra sound scan","Rs.700"),(11,"ANA","Rs.1500"),(12,"Bmp(basic metabolic panel)","Rs.1500"),
      (13,"Flu test (influenza A&B screen)","Rs.1700"),(14,"Hemoglobin A1C","Rs.600"),(15,"Urinalysis","Rs.350"),
      (16,"TSH","Rs.700"),(17,"PTT","Rs.350"),(18,"PT","Rs.250"),(19,"Microalbumin","Rs.600"),(20,"LFT","Rs.1500"),(21,"Lyme antibody","Rs.4500"),
      (22,"IGM","Rs.600"),(23,"NS1","Rs.550")]
lst5=[("Sno.","Category","Precaution"),("1.","cuts","Apply gentle pressure on the wound with a clean cloth to stop the bleeding. Try to elevate the affected part of the body if possible.Rinse the Cut thoroughly with      clean water. Apply an antibiotic ointment (like Neosporin)"),
      ("2.","Blister","Make a hole at the edge of blister Use a sterilized needle or pin Pin/needle sterilized by passing over flame.Drain the accumulated fluid.Keep skin intact to prevent   infection.Clean blister with gauze containing iodine/alcohol.Apply antibiotic ointment Cover with adhesive bandage for small blister.Use porous, bandage for large ones"),
      ("3.","Wounds","Control bleeding Use a clean towel to apply light pressure to the area until bleeding stops. Gently rinse the wound with clean, lukewarm water to cleanse and              remove any fragments of dirt Use a non-stick or gentle dressing and lightly bandage in place"),
      ("4.","Cpr","Lay the person on their back and open their airway.Check for breathing. If they are not breathing, start CPR.Perform 30 chest compressions Perform two rescue          breaths.Repeat until an ambulance or automated external defibrillator (AED) arrives."),
      ("5.","Burns","Hold the burned area under cool (not cold) running water or apply a cool, wet compress until the pain eases. Remove rings or other tight items from the burned area. Try to do this quickly and gently, before the area swells. Don't break blisters. Fluid-filled blisters protect against infection."),
      ("6.","Panic attack","Remove any triggers of the panic attack (or remove the patient from the trigger!). Provide lots of reassurance and remain calm yourself. Focus on controlling the           patient’s breathing – encourage them to breath in slowly through their nose, hold their breath, then breath out through their mouth.")]

root.mainloop()

    