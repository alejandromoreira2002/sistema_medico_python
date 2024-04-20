### CREATED BY: TEDDY ALEJANDRO MOREIRA VÉLEZ

from tkinter.font import BOLD
from tkinter import messagebox
from tkinter import ttk
from tkinter import *
from datetime import datetime

import sqlite3

#USUARIOS:
#Administrador: admin, admin123
#Enfermero: 
#Medico: 
#Recepcionista: 

class Login:

    def __init__(self, window, conex):
        self.wind = window
        self.conex = conex
        self.wind.title("Ingreso de Usuario")
        #self.wind.iconbitmap('imagenes/icono.ico')
        #self.wind.geometry(str("350x350+"+str(self.wind.winfo_screenwidth()//2 - 350//2)+"+"+str(self.wind.winfo_screenheight()//2 - 350//2)))
        self.wind.resizable(0, 0)

        #Agrega campos y labels al programa
        Label(self.wind, text="Ingrese sus datos de Usuario", font = ("Arial Bold", 13)).pack(fill=X, pady=(10, 10))
        f = LabelFrame(self.wind, pady=50, padx=30, bg="cyan")
        f.pack(fill=X)

        #Usuario
        Label(f, text="Usuario: ", bg="cyan").grid(row=0, column=0, padx=(10,100), pady=(10,20))
        self.usuario = Entry(f, width=30)
        self.usuario.grid(row = 0, column = 1, pady=(10,20))

        #Contraseña
        Label(f, text = "Contraseña: ", bg="cyan").grid(row=1, column=0, padx=(10,80))
        self.contrasena = Entry(f, width=30)
        self.contrasena.grid(row = 1, column = 1)

        #Boton de Confirmacion
        btn = Button(f, text="INGRESAR", command = self.VerificarDatos)
        btn.grid(row=2, column=0, padx=(180,0), pady=(40, 0))

    def VerificarDatos(self):
        cursor = self.conex.cursor()
        try:
            #Consulta en la base de datos
            cursor.execute("SELECT nombres, usuario, contrasena, rol FROM usuarios WHERE usuario = '{}' AND contrasena = '{}' GROUP BY id".format(self.usuario.get(), self.contrasena.get()))
            datoUser = cursor.fetchone()

            #mensaje de texto de acceso
            msg = messagebox.showinfo('Acceso Exitoso!', 'Bienvenido/a ' + datoUser[0] + '.')
            
            if msg:
                self.wind.destroy()
                
                windmain = Tk()
                wMain = Main(windmain, self.conex, datoUser[0], datoUser[3])
                windmain.mainloop()
                
        except(TypeError):
            #En caso de un exeso erroneo
            msg = messagebox.askretrycancel(title="Acceso Denegado!", message="Datos erroneos. Vuelva a ingresar sus datos")
            if not msg:
                self.window.destroy()
                self.conex.close()


class Main:
    def __init__(self, mainwind, conex, nombre, rol):

        roles = {
            "Administrador": ("normal" ,"normal", "normal", "normal"),
            "Enfermero": ("normal", "disabled", "disabled", "normal"),
            "Medico": ("disabled", "disabled", "normal", "disabled"),
            "Recepcionista": ("disabled", "normal", "disabled", "disabled"),
        }

        self.wind = mainwind
        self.conex = conex
        self.wind.title('Sistema de Centro de Salud')
        #self.wind.iconphoto(False, PhotoImage(file='icono.png'))
        self.wind.resizable(0, 0)
        self.wind.geometry(str("600x400+"+str(self.wind.winfo_screenwidth()//2 - 600//2)+"+"+str(self.wind.winfo_screenheight()//2 - 400//2)))
        f = LabelFrame(self.wind, pady=30, padx=30, bg="yellow")
        f.pack(fill=X)
        Label(f, text="SESION ACTUAL: ", font = ("Arial Bold", 15), bg="yellow").grid(row=0, column=0, padx=(10,40))
        Label(f, text="{}".format(nombre.upper()), font = ("Arial Bold", 15, BOLD), bg="yellow").grid(row=0, column=1, padx=(10,40))
        Label(self.wind, text="SISTEMA CLINICO", font = ("Arial Bold", 18)).pack(fill=X, pady=(8, 8))
        Label(self.wind, text="Sistema {}".format(rol), font = ("Arial Bold", 13, BOLD)).pack(fill=X, pady=(8, 8))

        #Menu
        menubar = Menu(self.wind)
        self.wind.config(menu = menubar)
        areasMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label='Menu', menu=areasMenu)
        areasMenu.add_command(label='Actualizacion de Pacientes', state = '{}'.format(roles[rol][0]), command = self.abrePacientes)
        areasMenu.add_command(label='Agendamiento de Citas', state = '{}'.format(roles[rol][1]), command = self.abreCitas)
        areasMenu.add_command(label='Actualizacion de historial clinico', state='{}'.format(roles[rol][2]), command = self.abreHC)
        areasMenu.add_command(label='Registro de Seguimiento de Tratamiento', state='{}'.format(roles[rol][3]), command = self.abreST)
        
        infoMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = 'Info', menu=infoMenu)
        infoMenu.add_command(label='Acerca de...', command=self.mostrarAcercaDe)

    def mostrarAcercaDe(self):
        infoWind = Tk()
        infoWind.title('Integrantes del grupo')
        #infoWind.iconphoto(False, PhotoImage(file='icono.png'))
        infoWind.resizable(0, 0)
        infoWind.geometry(str("500x300+"+str(self.wind.winfo_screenwidth()//2 - 500//2)+"+"+str(self.wind.winfo_screenheight()//2 - 300//2)))
        infoWind.config(bg="#fde9c3")
        Label(infoWind, text="GRUPO 10",font = ("Arial Bold", 16, BOLD), bg="#fde9c3").pack(fill= X, pady=(15,15))
        Label(infoWind, text="- Acosta Rosado Josthin Xavier",font = ("Arial Bold", 13), bg="#fde9c3").pack(fill= X, pady=(8, 8))
        Label(infoWind, text="- Carreño Loor Lesly Dalay",font = ("Arial Bold", 13), bg="#fde9c3").pack(fill= X, pady=(8, 8))
        Label(infoWind, text="- Cedeño Delgado Ibeth Selenny",font = ("Arial Bold", 13), bg="#fde9c3").pack(fill= X, pady=(8, 8))
        Label(infoWind, text="- De La Cruz Zambrano Jose Pastor",font = ("Arial Bold", 13), bg="#fde9c3").pack(fill= X, pady=(8, 8))
        Label(infoWind, text="- Moreira Velez Teddy Alejandro",font = ("Arial Bold", 13), bg="#fde9c3").pack(fill= X, pady=(8, 8))

    def abrePacientes(self):
        wPac = Tk()
        app = Enfermero(wPac, self.conex)
        wPac.mainloop()
    
    
    def abreCitas(self):
        wCit = Tk()
        app = Recepcionista(wCit, self.conex)
        wCit.mainloop()
    

    def abreHC(self):
        wHC = Tk()
        app = Medico(wHC, self.conex)
        wHC.mainloop()
        
    def abreST(self):
        wST = Tk()
        app = SeguimientoTratamiento(wST, self.conex)
        wST.mainloop()

class Pacientes:
    __cedula = ""
    __apellidos = ""
    __nombres = ""
    __direccion = ""
    __edad = 0
    __email = ""
    __pariente_cercano = ""
    __enfermedades_hereditarias = ""

    def __init__(self, cedula, conex):
        self.__cedula = cedula
        self.conex = conex
    
    def Actualizar_Pacientes(self):
        self.__cedula = self.entryCed.get()
        def almacenar():
            self.__cedula = self.entryCed.get()
            self.__apellidos = self.entryApel.get()
            self.__nombres = self.entryNom.get()
            self.__direccion = self.entryDir.get()
            self.__edad = int(self.entryEd.get())
            self.__email = self.entryEma.get()
            self.__pariente_cercano = self.entryPar.get()
            self.__enfermedades_hereditarias = self.entryEnf.get()

            datos = [self.__cedula, self.__apellidos, self.__nombres, self.__direccion, self.__edad, self.__email, self.__pariente_cercano, self.__enfermedades_hereditarias]
            cursor = self.conex.cursor()

            try:
                cursor.execute("INSERT INTO pacientes VALUES(?,?,?,?,?,?,?,?)", datos)
                self.conex.commit()
            except:
                messagebox.showerror('Error', 'Ocurrió un error al almacenar los datos en la base de datos')
            else:
                messagebox.showinfo('Guardado Exitoso!', 'Los datos han sido almacenados con exito')
                self.btnAlm.config(state='disabled')

        def actualizar():
            self.__apellidos = self.entryApel.get()
            self.__nombres = self.entryNom.get()
            self.__direccion = self.entryDir.get()
            self.__edad = int(self.entryEd.get())
            self.__email = self.entryEma.get()
            self.__pariente_cercano = self.entryPar.get()
            self.__enfermedades_hereditarias = self.entryEnf.get()

            #datos = [self.__cedula, self.__apellidos, self.__nombres, self.__direccion, self.__edad, self.__email, self.__pariente_cercano, self.__enfermedades_hereditarias]
            cursor = self.conex.cursor()
            try:
                cursor.execute("UPDATE pacientes SET apellidos='{}', nombres='{}', direccion='{}', edad={}, email='{}', pariente_cercano='{}', enfermedades_hereditarias='{}' WHERE cedula='{}'".format(self.__apellidos, self.__nombres, self.__direccion, str(self.__edad), self.__email, self.__pariente_cercano, self.__enfermedades_hereditarias, self.__cedula))
                self.conex.commit()
            except:
                messagebox.showerror('Error', 'Ocurrió un error al almacenar los datos en la base de datos')
            else:
                messagebox.showinfo('Guardado Exitoso!', 'Los datos han sido actualizados con exito')
                self.btnAct.config(state='disabled')
                self.btnEli.config(state='disabled')

        def eliminar():
            self.__cedula = self.entryCed.get()
            cursor = self.conex.cursor()
            try:
                cursor.execute("DELETE FROM pacientes WHERE cedula = '{}'".format(self.__cedula))
                self.conex.commit()
            except:
                messagebox.showerror('Error', 'Ocurrió un error al almacenar los datos en la base de datos')
            else:
                messagebox.showinfo('Borrado Exitoso!', 'Los datos han sido eliminados con exito')
                self.btnAct.config(state='disabled')
                self.btnEli.config(state='disabled')

        def aparecerCampos():
            
            #LabelFrame
            self.f = LabelFrame(self.wind, text="Datos del paciente", pady=40, padx=20)
            self.f.grid(row=3, column=0, columnspan=3)

            #Apellidos
            Label(self.f, text="Apellidos: ").grid(row=0, column=0, pady=(10,5)) #, padx=(10, 30)

            self.entryApel = Entry(self.f, width=20)
            self.entryApel.grid(row=0, column=1, pady=(10,5)) #, padx=(10,10)

            #Nombres
            Label(self.f, text="Nombres: ").grid(row=1, column=0, pady=(5,5))

            self.entryNom = Entry(self.f, width=20)
            self.entryNom.grid(row=1, column=1, pady=(5,5))
            
            #Direccion
            Label(self.f, text="Direccion: ").grid(row=2, column=0, pady=(5,5))

            self.entryDir = Entry(self.f, width=20)
            self.entryDir.grid(row=2, column=1, pady=(5,5))

            #Edad
            Label(self.f, text="Edad: ").grid(row=3, column=0, pady=(5,5))

            self.entryEd = Entry(self.f, width=20)
            self.entryEd.grid(row=3, column=1, pady=(5,5))

            #Email
            Label(self.f, text="Email: ").grid(row=4, column=0, pady=(5,5))

            self.entryEma = Entry(self.f, width=20)
            self.entryEma.grid(row=4, column=1, pady=(5,5))

            #Pariente_Cercano
            Label(self.f, text="Pariente Cercano: ").grid(row=5, column=0, pady=(10,5))

            self.entryPar = Entry(self.f, width=20)
            self.entryPar.grid(row=5, column=1, pady=(10,5))

            #Enfermedades_Hereditarias
            Label(self.f, text="Enfermedades Hereditarias: ").grid(row=6, column=0, pady=(5,10))

            self.entryEnf = Entry(self.f, width=20)
            self.entryEnf.grid(row=6, column=1, pady=(5,10))
            
            #btn = Button(self.f, text='Actualizar', command=almacenar)
            #btn.grid(row=7, column=0, columnspan=2, pady=(5,10))

        if self.Consultar_Pacientes():
            print("Paciente encontrado")
            try:
                self.btnAlm.destroy()
            except(AttributeError):
                pass

            self.inteMsg = Label(self.wind, text="Paciente encontrado!", bg='#b7fca4', fg='#02bd02')
            self.inteMsg.grid(row=2, column=0, columnspan=3)

            aparecerCampos()

            self.entryApel.insert(0, self.__apellidos)
            self.entryNom.insert(0, self.__nombres)
            self.entryDir.insert(0, self.__direccion)
            self.entryEd.insert(0, self.__edad)
            self.entryEma.insert(0, self.__email)
            self.entryPar.insert(0, self.__pariente_cercano)
            self.entryEnf.insert(0, self.__enfermedades_hereditarias)

            self.btnAct = Button(self.f, text='Actualizar', command=actualizar, width=30)
            self.btnAct.grid(row=7, column=0, columnspan=2, pady=(5,5))

            self.btnEli = Button(self.f, text='Eliminar Paciente', command=eliminar, width=30)
            self.btnEli.grid(row=8, column=0, columnspan=2, pady=(5,0))

        else:
            print("No existe el registro en la base de datos")
            try:
                self.btnAct.destroy()
                self.btnEli.destroy()
            except(AttributeError):
                pass

            self.inteMsg = Label(self.wind, text="No existe el paciente", bg='#f56464', fg='#d92222')
            self.inteMsg.grid(row=2, column=0, columnspan=3)
            aparecerCampos()

            self.btnAlm = Button(self.f, text='Guardar', command=almacenar, width=30)
            self.btnAlm.grid(row=7, column=0, columnspan=2, pady=(5,0))
    
    def Consultar_Pacientes(self):
        cursor = self.conex.cursor()
        cursor.execute("SELECT cedula, apellidos, nombres, direccion, edad, email, pariente_cercano, enfermedades_hereditarias FROM pacientes WHERE cedula = '{}' GROUP BY cedula".format(self.__cedula))
        #cursor.execute("SELECT cedula, apellidos, nombres, direccion, edad, email, pariente_cercano, enfermedades_hereditarias FROM pacientes WHERE cedula = '{}' GROUP BY cedula".format(self.__cedula))
        dato = cursor.fetchone()
        if not dato is None:
            self.__cedula = dato[0]
            self.__apellidos = dato[1]
            self.__nombres = dato[2]
            self.__direccion = dato[3]
            self.__edad = dato[4]
            self.__email = dato[5]
            self.__pariente_cercano = dato[6]
            self.__enfermedades_hereditarias = dato[7]
            return True
        else:
            return False
    
    #admin

class Citas:
    __cod_cita = 0
    __fecha = datetime.now().strftime('%Y-%m-%d')
    __hora = datetime.now().strftime("%H:%M")
    __cedula = ""
    __consultorio = ""
    __medico = ""

    def Agendar_Citas(self):
        self.__cedula = self.entryCed.get()

        def almacenar():
            self.__cedula = self.entryCed.get()
            self.__consultorio = self.entryCons.get()
            self.__medico = self.entryMed.get()
            self.__fecha = self.entryFec.get()
            self.__hora = self.entryHor.get()

            datos = [self.__fecha, self.__hora, self.__cedula, self.__consultorio, self.__medico]
            cursor = self.conex.cursor()

            try:
                cursor.execute("INSERT INTO citas(fecha, hora, cedula, consultorio, medico) VALUES(?,?,?,?,?)", datos)
                self.conex.commit()
            except:
                messagebox.showerror('Error', 'Ocurrió un error al almacenar los datos en la base de datos')
            else:
                messagebox.showinfo('Guardado Exitoso!', 'Los datos han sido almacenados con exito')
                self.btn.config(state='disabled')

        def aparecerCampos():

            #LabelFrame
            self.f = LabelFrame(self.wind, text="Datos de las Citas", pady=40, padx=20)
            self.f.grid(row=3, column=0, columnspan=3)

            #Consultorio
            Label(self.f, text="Consultorio: ").grid(row=0, column=0, pady=(10,5))

            self.entryCons = Entry(self.f, width=30)
            self.entryCons.grid(row=0, column=1, pady=(10,5), columnspan = 2)

            #Medico
            Label(self.f, text="Nombre medico: ").grid(row=1, column=0, pady=(5,5))

            self.entryMed = Entry(self.f, width=30)
            self.entryMed.grid(row=1, column=1, pady=(5,5), columnspan = 2)
            
            #Fecha
            Label(self.f, text="Fecha: ").grid(row=2, column=0, pady=(5,5))

            self.entryFec = Entry(self.f, width=20)
            self.entryFec.grid(row=2, column=1, pady=(5,5))

            Label(self.f, text="yyyy-mm-dd", fg="grey").grid(row=2, column=2, pady=(5,5))

            #Hora
            Label(self.f, text="Hora: ").grid(row=3, column=0, pady=(5,5))

            self.entryHor = Entry(self.f, width=20)
            self.entryHor.grid(row=3, column=1, pady=(5,5))

            Label(self.f, text="hh:ss", fg="grey").grid(row=3, column=2, pady=(5,5))
            
            self.btn = Button(self.f, text='Guardar', command=almacenar, width=30)
            self.btn.grid(row=7, column=0, columnspan=3, pady=(5,10))

        if Pacientes(self.__cedula, self.conex).Consultar_Pacientes():
            print("Paciente encontrado")
            #try:
                #self.btnAlm.destroy()
            #except(AttributeError):
                #pass

            self.inteMsg = Label(self.wind, text="Paciente encontrado!", bg='#b7fca4', fg='#02bd02')
            self.inteMsg.grid(row=2, column=0, columnspan=3)

            aparecerCampos()

            """
            self.entryApel.insert(0, self.__apellidos)
            self.entryNom.insert(0, self.__nombres)
            self.entryDir.insert(0, self.__direccion)
            self.entryEd.insert(0, self.__edad)
            self.entryEma.insert(0, self.__email)
            self.entryPar.insert(0, self.__pariente_cercano)
            self.entryEnf.insert(0, self.__enfermedades_hereditarias)

            self.btnAct = Button(self.f, text='Actualizar', command=actualizar, width=30)
            self.btnAct.grid(row=7, column=0, columnspan=2, pady=(5,5))

            self.btnEli = Button(self.f, text='Eliminar Paciente', command=eliminar, width=30)
            self.btnEli.grid(row=8, column=0, columnspan=2, pady=(5,0))
            """
        else:
            print("No existe el registro en la base de datos")
            try:
                self.f.grid_forget()
            except(AttributeError):
                pass

            self.inteMsg = Label(self.wind, text="No existe el paciente", bg='#f56464', fg='#d92222')
            self.inteMsg.grid(row=2, column=0, columnspan=3)


class HistorialClinico:
    __cod_historial_cl = 0
    __medico = ""
    __cedula = ""
    __fecha = datetime.now().strftime('%Y-%m-%d')
    __motivo = ""
    __tratamiento = 0
    __diagnostico = 0

    def Actualizar_Historial_Clinico(self):
        self.__cedula = self.entryCed.get()

        def nuevoHC():
            def guardar():
                self.__fecha = self.entryFec.get()
                self.__medico = self.entryMed.get()
                self.__motivo = self.entryMot.get()
                self.__cedula = self.entryCed.get()

                diagnostico = self.entryDia.get("1.0", 'end-1c')
                tratamiento = self.entryTra.get("1.0", 'end-1c')

                cursor.execute("SELECT id_diagnostico FROM diagnostico WHERE descripcion = '{}'".format(str(diagnostico)))
                datoD = cursor.fetchone()
                self.__diagnostico = int(datoD[0])

                cursor.execute("SELECT id_tratamiento FROM tratamiento WHERE descripcion = '{}'".format(str(tratamiento)))
                datoT = cursor.fetchone()
                self.__tratamiento = int(datoT[0])

                try:
                    cursor.execute("INSERT INTO historial_clinico(medico, cedula, motivo, fecha, tratamiento, diagnostico) VALUES('{}', '{}', '{}', '{}', {}, {})".format(self.__medico, self.__cedula, self.__motivo, self.__fecha, str(self.__tratamiento), str(self.__diagnostico)))
                    self.conex.commit()
                except:
                    messagebox.showerror('Error', 'Ocurrió un error al almacenar los datos en la base de datos')
                else:
                    messagebox.showinfo('Guardado Exitoso!', 'Los datos han sido almacenados con exito')
                    self.btnAlm.config(state="disabled")
                    self.btnDia.config(state="disabled")
                    self.btnTra.config(state="disabled")

            cursor = self.conex.cursor()

            try:
                self.btnHC.grid_forget()
                self.regMsg.grid_forget()
            except(AttributeError):
                pass

            try:
                self.f.grid_forget()
            except(AttributeError):
                pass

            self.__diagnostico = 0
            self.__tratamiento = 0

            aparecerCampos()

            try:
                self.entryDia.config(state = "disabled")
                self.entryTra.config(state = "disabled")
            except(AttributeError):
                pass

            #Boton Guardar
            if self.entryDia.get("1.0", 'end-1c') == "" or self.entryDia.get("1.0", 'end-1c') == None and self.entryTra.get("1.0", 'end-1c') == "" or self.entryTra.get("1.0", 'end-1c') == None:
                self.btnAlm = Button(self.f, text='Guardar', state="disabled", command=guardar)
                self.btnAlm.grid(row=8, column=0, columnspan=4, pady=(5,10))
            else:
                self.btnAlm = Button(self.f, text='Guardar', state="normal", command=guardar)
                self.btnAlm.grid(row=8, column=0, columnspan=4, pady=(5,10))

        def revisarHC():
            def mostrarHC():
                def actualizar():
                    self.__fecha = datos[0]
                    self.__medico = datos[1]
                    self.__motivo = datos[2]
                    self.__diagnostico = int(datos[5])
                    self.__tratamiento = int(datos[6])
                    self.__cod_historial_cl = int(datos[7])
                    

                    try:
                        self.btnHC.grid_forget()
                        self.regMsg.grid_forget()
                    except(AttributeError):
                        pass

                    try:
                        self.f.grid_forget()
                    except(AttributeError):
                        pass

                    aparecerCampos()

                    self.entryFec.insert(0, self.__fecha)
                    self.entryMed.insert(0, self.__medico)
                    self.entryMot.insert(0, self.__motivo)

                    cursor.execute("SELECT d.descripcion, t.descripcion FROM historial_clinico as h, tratamiento as t, diagnostico as d WHERE h.tratamiento = t.id_tratamiento AND h.diagnostico = d.id_diagnostico AND h.diagnostico = {} AND h.tratamiento = {} AND h.cedula = '{}'".format(str(self.__diagnostico), str(self.__tratamiento), str(self.__cedula)))
                    datosDT = cursor.fetchone()

                    print(datosDT[0])
                    print(datosDT[1])
                    self.entryDia.insert('1.0', datosDT[0])
                    self.entryTra.insert('1.0', datosDT[1])

                    try:
                        self.entryDia.config(state = "disabled")
                        self.entryTra.config(state = "disabled")
                    except(AttributeError):
                        pass

                    def guardar():
                        self.__fecha = self.entryFec.get()
                        self.__medico = self.entryMed.get()
                        self.__motivo = self.entryMot.get()

                        try:
                            cursor.execute("UPDATE historial_clinico SET fecha = '{}', medico = '{}', motivo = '{}', tratamiento = {}, diagnostico = {} WHERE cod_historial_cl = {}".format(self.__fecha, self.__medico, self.__motivo, str(self.__tratamiento), str(self.__diagnostico), str(self.__cod_historial_cl)))
                            self.conex.commit()
                        except:
                            messagebox.showerror('Error', 'Ocurrió un error al almacenar los datos en la base de datos')
                        else:
                            messagebox.showinfo('Guardado Exitoso!', 'Los datos han sido actualizados con exito')
                            self.btnAlm.config(state="disabled")
                            self.btnDia.config(state="disabled")
                            self.btnTra.config(state="disabled")

                    #Boton Guardar
                    if self.entryDia.get("1.0", 'end-1c') == "" or self.entryDia.get("1.0", 'end-1c') == None and self.entryTra.get("1.0", 'end-1c') == "" or self.entryTra.get("1.0", 'end-1c') == None:
                        self.btnAlm = Button(self.f, text='Guardar', state="disabled", command=guardar)
                        self.btnAlm.grid(row=8, column=0, columnspan=4, pady=(5,10))
                    else:
                        self.btnAlm = Button(self.f, text='Guardar', state="normal", command=guardar)
                        self.btnAlm.grid(row=8, column=0, columnspan=4, pady=(5,10))

                    try:
                        self.wind2.destroy()
                        self.entryCed.config(state="normal")
                        self.anNue.config(state="normal")
                        self.anVer.config(state="normal")
                        self.btn.config(state="normal")
                    except(TclError):
                        pass

                cursor.execute("SELECT h.fecha, h.medico, h.motivo, d.descripcion, t.descripcion, h.diagnostico, h.tratamiento, h.cod_historial_cl FROM historial_clinico as h, tratamiento as t, diagnostico as d WHERE h.tratamiento = t.id_tratamiento AND h.diagnostico = d.id_diagnostico AND h.fecha = '{}' AND h.cedula = '{}'".format(lista.get(), self.__cedula))
                
                datos = cursor.fetchone()
                
                #LabelFrame
                self.fw2 = LabelFrame(self.wind2, text="Datos del Historial Clinico del Paciente", pady=20, padx=120)
                self.fw2.grid(row=2, column=0, columnspan=3, pady=(10,5))

                #Fecha
                Label(self.fw2, text="Fecha:", font=("Arial Bold", 10, BOLD), anchor="center").grid(row=0, column=0, pady=(0,5))
                Label(self.fw2, text="{}".format(str(datos[0])), font=("Arial Bold", 9), anchor="center").grid(row=1, column=0, pady=(5,10))

                #Medico
                Label(self.fw2, text="Medico:", font=("Arial Bold", 10, BOLD), anchor="center").grid(row=2, column=0, pady=(10,5))
                Label(self.fw2, text="{}".format(str(datos[1])), font=("Arial Bold", 9), anchor="center").grid(row=3, column=0, pady=(5,10))
        
                #Motivo
                Label(self.fw2, text="Motivo:", font=("Arial Bold", 10, BOLD), anchor="center").grid(row=4, column=0, pady=(10,5))
                Label(self.fw2, text="{}".format(str(datos[2])), font=("Arial Bold", 9), anchor="center").grid(row=5, column=0, pady=(5,10))

                #Diagnostico
                Label(self.fw2, text="Diagnostico:", font=("Arial Bold", 10, BOLD), anchor="center").grid(row=6, column=0, pady=(10,5))
                Label(self.fw2, text="{}".format(str(datos[3])), font=("Arial Bold", 9), anchor="center").grid(row=7, column=0, pady=(5,10))

                #Tratamiento
                Label(self.fw2, text="Tratamiento:", font=("Arial Bold", 10, BOLD), anchor="center").grid(row=8, column=0, pady=(10,5))
                Label(self.fw2, text="{}".format(str(datos[4])), font=("Arial Bold", 9), anchor="center").grid(row=9, column=0, pady=(5,0))

                self.btnActDtHC = Button(self.wind2, text="Actualizar Datos", command=actualizar)
                self.btnActDtHC.grid(row=3, column=0, columnspan=3, pady=(15,15))

            self.wind2 = Tk()
            self.entryCed.config(state="disabled")
            self.anNue.config(state="disabled")
            self.anVer.config(state="disabled")
            self.btn.config(state="disabled")

            def bloq():
                def entrada():
                    try:
                        self.wind2.destroy()
                        self.entryCed.config(state="normal")
                        self.anNue.config(state="normal")
                        self.anVer.config(state="normal")
                        self.btn.config(state="normal")
                    except(TclError):
                        pass
                d = entrada()
                try:
                    self.wind2.wait_window(d)
                except(TclError):
                        pass

            self.wind2.title('Historial Clinico del paciente')
            self.wind2.resizable(0, 0)
            self.wind2.geometry('600x600')

            self.wind2.protocol("WM_DELETE_WINDOW", bloq)

            Label(self.wind2, text="Historial Clinico", font = ("Arial Bold", 15, BOLD)).grid(row=0, column=0, columnspan= 3, pady=(10, 10))
            
            self.__cedula = self.entryCed.get()
            cursor = self.conex.cursor()
            cursor.execute("SELECT fecha FROM historial_clinico WHERE cedula = '{}'".format(self.__cedula))
            
            fechas = []
            fechas = cursor.fetchall()

            Label(self.wind2, text="Seleccionar fecha:").grid(row=1, column=0, pady=(10, 10), padx=(10,10))

            lista = ttk.Combobox(self.wind2, width=40, state="readonly")
            lista.grid(row=1, column=1, pady=(10, 10), padx=(10,10))

            lista['values'] = fechas

            Button(self.wind2, text="Mostrar", command=mostrarHC).grid(row=1, column=2, pady=(10,10), padx=(70,30))
            self.wind2.mainloop()
                    
                    
        
        def consultar():
            if self.Consultar_Historial_Clinico():
                print("Historial Clinico Ingresado")

                self.__cedula = self.entryCed.get()
                cursor = self.conex.cursor()
                cursor.execute("SELECT COUNT(cod_historial_cl) FROM historial_clinico WHERE cedula = '{}'".format(self.__cedula))
                reg = cursor.fetchone()

                if int(reg[0]) > 1:
                    self.regMsg = Label(self.wind, text="Se encontraron {} registros".format(str(reg[0])), fg='#a0a0a0')
                    self.regMsg.grid(row=3, column=2, pady=(15, 10), columnspan=2)
                else:
                    self.regMsg = Label(self.wind, text="Se encontro {} registro".format(str(reg[0])), fg='#a0a0a0')
                    self.regMsg.grid(row=3, column=2, pady=(15, 10), columnspan=2)
                
                self.btnHC.config(state = 'disabled')
                
                self.anNue = Button(self.wind, text='Añadir Nuevo', command=nuevoHC)
                self.anNue.grid(row=4, column=0, padx=(5,5), pady=(10,5), columnspan=2)

                self.anVer = Button(self.wind, text='Ver y Actualizar', command=revisarHC)
                self.anVer.grid(row=4, column=2, padx=(5,5), pady=(10,5), columnspan=2)
                
            else:
                messagebox.showwarning('Historial Clinico no registrado', 'El paciente ingresado no tiene historial clinico')

                self.__cedula = self.entryCed.get()
                cursor = self.conex.cursor()
                self.regMsg = Label(self.wind, text="No posee historial", fg='#a0a0a0')
                self.regMsg.grid(row=3, column=2, pady=(15, 10), columnspan=2)
                
                self.btnHC.config(state = 'disabled')
                
                self.anNue = Button(self.wind, text='Añadir Nuevo', command=nuevoHC)
                self.anNue.grid(row=4, column=0, padx=(5,5), pady=(10,5), columnspan=2)

                try:
                    self.anVer.config(state="disabled")
                except(AttributeError):
                    pass

        def abreDiagnostico():
            wDia = Tk()
            app = Diagnostico(wDia, self.conex, self.__diagnostico, self.entryDia, self.btnAlm, self.entryTra)
            def actualizacion():
                def cuadros():
                    try:
                        wDia.destroy()
                        self.entryDia.config(state="normal")
                        cursor = self.conex.cursor()
                        cursor.execute("SELECT descripcion FROM diagnostico WHERE id_diagnostico = {}".format(str(self.__diagnostico)))
                        dato = cursor.fetchone()
                        self.entryDia.delete('1.0', END)

                        try:
                            self.entryDia.insert('1.0', str(dato[0]))
                        except(TypeError):
                            self.entryDia.insert('1.0', '')

                        self.entryDia.config(state="disabled")
                        if self.entryDia.get("1.0", 'end-1c') == "" or self.entryDia.get("1.0", 'end-1c') == None and self.entryTra.get("1.0", 'end-1c') == "" or self.entryTra.get("1.0", 'end-1c') == None:
                            self.btnAlm.config(state="disabled")
                        else:
                            self.btnAlm.config(state="normal")
                    except(TclError):
                        pass

                d = cuadros()
                try:
                    wDia.wait_window(d)
                except(TclError):
                    pass

            wDia.protocol("WM_DELETE_WINDOW", actualizacion)
            wDia.mainloop()

        def abreTratamiento():
            wTra = Tk()
            app = Tratamiento(wTra, self.conex, self.__tratamiento, self.entryTra, self.entryDia, self.btnAlm)
            def actualizacion():
                def cuadros():
                    try:
                        wTra.destroy()
                        self.entryTra.config(state="normal")
                        cursor = self.conex.cursor()
                        cursor.execute("SELECT descripcion FROM tratamiento WHERE id_tratamiento = {}".format(str(self.__tratamiento)))
                        dato = cursor.fetchone()
                        self.entryTra.delete('1.0', END)

                        try:
                            self.entryTra.insert('1.0', str(dato[0]))
                        except(TypeError):
                            self.entryTra.insert('1.0', '')

                        self.entryTra.config(state="disabled")
                        if self.entryDia.get("1.0", 'end-1c') == "" or self.entryDia.get("1.0", 'end-1c') == None and self.entryTra.get("1.0", 'end-1c') == "" or self.entryTra.get("1.0", 'end-1c') == None:
                            self.btnAlm.config(state="disabled")
                        else:
                            self.btnAlm.config(state="normal")
                    except(TclError):
                        pass

                d = cuadros()
                try:
                    wTra.wait_window(d)
                except(TclError):
                    pass

            wTra.protocol("WM_DELETE_WINDOW", actualizacion)
            wTra.mainloop()

        def aparecerCampos():

            #LabelFrame
            self.f = LabelFrame(self.wind, text="Datos del Historial Clinico", pady=20, padx=20)
            self.f.grid(row=5, column=0, columnspan=4, padx=(20,20))

            #Fecha
            Label(self.f, text="Fecha: ").grid(row=0, column=0, pady=(10,5))

            self.entryFec = Entry(self.f, width=20)
            self.entryFec.grid(row=0, column=1, pady=(10,5), columnspan = 2)

            Label(self.f, text="yyyy-mm-dd", fg="grey").grid(row=0, column=3, pady=(10,5))

            #Medico
            Label(self.f, text="Medico: ").grid(row=1, column=0, pady=(5,5))

            self.entryMed = Entry(self.f, width=30)
            self.entryMed.grid(row=1, column=1, pady=(5,5), columnspan = 3)
            
            #Motivo
            Label(self.f, text="Motivo: ").grid(row=2, column=0, pady=(5,5))

            self.entryMot = Entry(self.f, width=30)
            self.entryMot.grid(row=2, column=1, pady=(5,5), columnspan = 3)

            #Diagnostico
            Label(self.f, text="Diagnostico:").grid(row=3, column=0, pady=(5,3), columnspan=4)

            self.entryDia = Text(self.f, width=40, height=8)
            self.entryDia.grid(row = 4, column=0, columnspan=4, pady=(3,5))

            #Tratamiento
            Label(self.f, text="Tratamiento:").grid(row=5, column=0, pady=(5,3), columnspan=4)

            self.entryTra = Text(self.f, width=40, height=8)
            self.entryTra.grid(row = 6, column=0, columnspan=4, pady=(3,5))
            
            #Boton Diagnostico
            self.btnDia = Button(self.f, text='Registrar Diagnostico', command = abreDiagnostico)
            self.btnDia.grid(row=7, column=0, columnspan=2, pady=(5,10))

            #Boton Tratamiento
            self.btnTra = Button(self.f, text='Registrar Tratamiento', command = abreTratamiento)
            self.btnTra.grid(row=7, column=2, columnspan=2, pady=(5,10))

            #self.btn = Button(self.f, text='Guardar', command=almacenar, width=30)
            #self.btn.grid(row=7, column=0, columnspan=3, pady=(5,10))

        if Pacientes(self.__cedula, self.conex).Consultar_Pacientes():
            print("Paciente encontrado")
            #try:
                #self.btnAlm.destroy()
            #except(AttributeError):
                #pass

            self.inteMsg = Label(self.wind, text="Paciente encontrado!", bg='#b7fca4', fg='#02bd02')
            self.inteMsg.grid(row=2, column=0, columnspan=4)

            self.btnHC = Button(self.wind, text='Buscar Historial Clinico', command=consultar)
            self.btnHC.grid(row=3, column=0, padx=(5,5), pady=(15,10), columnspan=2)

        else:
            print("No existe el registro en la base de datos")
            try:
                self.btnHC.grid_forget()
                self.regMsg.grid_forget()
                self.anNue.grid_forget()
                self.anVer.grid_forget()
            except(AttributeError):
                pass

            try:
                self.f.grid_forget()
            except(AttributeError):
                pass

            try:
                self.f.grid_forget()
            except(AttributeError):
                pass

            self.inteMsg = Label(self.wind, text="No existe el paciente", bg='#f56464', fg='#d92222')
            self.inteMsg.grid(row=2, column=0, columnspan=4)
    
    def Consultar_Historial_Clinico(self):
        self.__cedula = self.entryCed.get()
        cursor = self.conex.cursor()
        cursor.execute("SELECT cod_historial_cl, medico, fecha, motivo, tratamiento, diagnostico FROM historial_clinico WHERE cedula = '{}' GROUP BY cedula".format(self.__cedula))
        dato = cursor.fetchone()
        if not dato is None:
            #self.__cod_historial_cl = dato[0]
            #self.__medico = dato[1]
            #self.__fecha = dato[2]
            #self.__motivo = dato[3]
            #self.__tratamiento = dato[4]
            #self.__diagnostico = dato[5]
            return True
        else:
            return False

class SeguimientoTratamiento:
    __num_seguimiento = 0
    __cod_historial_cl = 0
    __cedula = ""
    __enfermero = ""
    __fecha_seguimiento = datetime.now().strftime('%Y-%m-%d')
    __descripcion_seguimiento = ""
    __observaciones = ""

    def __init__(self, stwind, conex):
        self.wind = stwind
        self.conex = conex
        self.wind.title("Registro de Seguimiento de Tratamiento")
        #self.wind.geometry('420x700')
        self.wind.geometry(str("420x700+"+str(self.wind.winfo_screenwidth()//2 - 420//2)+"+"+str(self.wind.winfo_screenheight()//2 - 700//2)))
        self.wind.resizable(0, 0)
        Label(self.wind, text="Registro de Seguimiento de Tratamiento", font = ("Arial Bold", 13, BOLD)).grid(row=0, column=0, columnspan= 4, pady=(10, 10))
        Label(self.wind, text="Cedula: ").grid(row=1, column=0, padx=(10, 30), pady=(10,10))

        self.entryCed = Entry(self.wind, width=30)
        self.entryCed.grid(row=1, column=1, padx=(10,10), pady=(10,10), columnspan=2)

        self.btn = Button(self.wind, text='Buscar', command=self.Registrar_Seguimiento_Tratamiento)
        self.btn.grid(row=1, column=3, padx=(10,10), pady=(10,10))

    def Registrar_Seguimiento_Tratamiento(self):

        self.__cedula = self.entryCed.get()

        def consultar():
            self.wind2 = Tk()

            self.wind2.title('Historial Clinico del paciente')
            self.wind2.resizable(0, 0)
            self.wind2.geometry('600x600')

            Label(self.wind2, text="Historial Clinico", font = ("Arial Bold", 15, BOLD)).grid(row=0, column=0, columnspan= 3, pady=(10, 10))

            cursor.execute("SELECT h.cod_historial_cl, h.fecha, h.medico, h.motivo, d.descripcion, t.descripcion, h.diagnostico, h.tratamiento, h.cod_historial_cl FROM historial_clinico as h, tratamiento as t, diagnostico as d WHERE h.tratamiento = t.id_tratamiento AND h.diagnostico = d.id_diagnostico AND h.cod_historial_cl = {}".format(str(lista.get())))
                
            datos = cursor.fetchone()
            
            #LabelFrame
            self.fw2 = LabelFrame(self.wind2, text="Datos del Historial Clinico del Paciente", pady=20, padx=120)
            self.fw2.grid(row=1, column=0, columnspan=3, pady=(10,5), padx=(30,30))

            #Id Historial
            Label(self.fw2, text="Codigo Historial:", font=("Arial Bold", 10, BOLD), anchor="center").grid(row=0, column=0, pady=(5,20), columnspan= 2)
            Label(self.fw2, text="{}".format(str(datos[0])), font=("Arial Bold", 9, BOLD), anchor="center").grid(row=0, column=2, pady=(5,20))

            #Fecha
            Label(self.fw2, text="Fecha:", font=("Arial Bold", 10, BOLD), anchor="center").grid(row=1, column=0, pady=(10,5), columnspan=3)
            Label(self.fw2, text="{}".format(str(datos[1])), font=("Arial Bold", 9), anchor="center").grid(row=2, column=0, pady=(5,10), columnspan=3)

            #Medico
            Label(self.fw2, text="Medico:", font=("Arial Bold", 10, BOLD), anchor="center").grid(row=3, column=0, pady=(10,5), columnspan=3)
            Label(self.fw2, text="{}".format(str(datos[2])), font=("Arial Bold", 9), anchor="center").grid(row=4, column=0, pady=(5,10), columnspan=3)
    
            #Motivo
            Label(self.fw2, text="Motivo:", font=("Arial Bold", 10, BOLD), anchor="center").grid(row=5, column=0, pady=(10,5), columnspan=3)
            Label(self.fw2, text="{}".format(str(datos[3])), font=("Arial Bold", 9), anchor="center").grid(row=6, column=0, pady=(5,10), columnspan=3)

            #Diagnostico
            Label(self.fw2, text="Diagnostico:", font=("Arial Bold", 10, BOLD), anchor="center").grid(row=7, column=0, pady=(10,5), columnspan=3)
            Label(self.fw2, text="{}".format(str(datos[4])), font=("Arial Bold", 9), anchor="center").grid(row=8, column=0, pady=(5,10), columnspan=3)

            #Tratamiento
            Label(self.fw2, text="Tratamiento:", font=("Arial Bold", 10, BOLD), anchor="center").grid(row=9, column=0, pady=(10,5), columnspan=3)
            Label(self.fw2, text="{}".format(str(datos[5])), font=("Arial Bold", 9), anchor="center").grid(row=10, column=0, pady=(5,0), columnspan=3)

            #Boton
            def cerrar():
                self.wind2.destroy()

            Button(self.fw2, text="Cerrar", command=cerrar).grid(row=11, column= 0, pady=(10,10), columnspan=3)

            self.wind2.mainloop()

        def almacenar():
            self.__cod_historial_cl = int(lista.get())
            self.__fecha_seguimiento = self.entryFec.get()
            self.__enfermero = self.entryEnf.get()
            self.__descripcion_seguimiento = self.entrySeg.get("1.0", 'end-1c')
            self.__observaciones = self.entryObs.get("1.0", 'end-1c')

            dST = [self.__cod_historial_cl, self.__cedula, self.__enfermero, self.__fecha_seguimiento, self.__descripcion_seguimiento, self.__observaciones]
            cursor = self.conex.cursor()

            try:
                cursor.execute("INSERT INTO seguimiento_tratamiento(cod_historial_cl, cedula, Enfermero, Fecha_seguimiento, descripcion_seguimiento, observaciones) VALUES(?,?,?,?,?,?)", dST)
                self.conex.commit()
            except:
                messagebox.showerror('Error', 'Ocurrió un error al almacenar los datos en la base de datos')
            else:
                messagebox.showinfo('Guardado Exitoso!', 'Los datos han sido almacenados con exito')
                self.btn.config(state='disabled')
            

        def aparecerCampos():

            #LabelFrame
            self.f = LabelFrame(self.wind, text="Datos del Seguimiento de Tratamiento", pady=20, padx=20)
            self.f.grid(row=5, column=0, columnspan=4, padx=(20,20))
 
            #Fecha de Seguimiento
            Label(self.f, text="Fecha de Seguimiento: ").grid(row=0, column=0, pady=(10,5))

            self.entryFec = Entry(self.f, width=20)
            self.entryFec.grid(row=0, column=1, pady=(10,5), columnspan = 2)

            Label(self.f, text="yyyy-mm-dd", fg="grey").grid(row=0, column=3, pady=(10,5))

            #Enfermero
            Label(self.f, text="Enfermero: ").grid(row=1, column=0, pady=(5,5))

            self.entryEnf = Entry(self.f, width=30)
            self.entryEnf.grid(row=1, column=1, pady=(5,5), columnspan = 3)

            #Descripcion Seguimiento
            Label(self.f, text="Descripcion del Seguimiento:").grid(row=2, column=0, pady=(5,3), columnspan=4)

            self.entrySeg = Text(self.f, width=40, height=8)
            self.entrySeg.grid(row = 3, column=0, columnspan=4, pady=(3,5))

            #Observaciones
            Label(self.f, text="Observaciones:").grid(row=4, column=0, pady=(5,3), columnspan=4)

            self.entryObs = Text(self.f, width=40, height=8)
            self.entryObs.grid(row = 5, column=0, columnspan=4, pady=(3,5))

            self.btn = Button(self.f, text='Guardar', command=almacenar)
            self.btn.grid(row=6, column=0, columnspan=4, pady=(5,10))

        if Pacientes(self.__cedula, self.conex).Consultar_Pacientes():
            #try:
                #self.btnAlm.destroy()
            #except(AttributeError):
                #pass

            self.inteMsg = Label(self.wind, text="Paciente encontrado!", bg='#b7fca4', fg='#02bd02')
            self.inteMsg.grid(row=2, column=0, columnspan=4)

            cursor = self.conex.cursor()
            cursor.execute("SELECT cod_historial_cl FROM historial_clinico WHERE cedula = '{}'".format(self.__cedula))
            
            ids = []
            ids = cursor.fetchall()
            

            Label(self.wind, text="Cod Historial Clinico:").grid(row=3, column=0, pady = (10,10), columnspan= 2)

            lista = ttk.Combobox(self.wind, width=20, state='readonly')
            lista.grid(row=3, column=2, pady=(10,10))

            lista['values'] = ids

            def esconder(event):
                try:
                    self.f.grid_forget()
                except(AttributeError):
                    pass

            lista.bind('<<ComboboxSelected>>', esconder)

            self.btnHC = Button(self.wind, text='Ver', command=consultar)
            self.btnHC.grid(row=3, column=3, pady=(10,10))

            self.btnST = Button(self.wind, text='Registrar Seguimiento de Tratamiento', command=aparecerCampos)
            self.btnST.grid(row=4, column=0, pady=(10,10), columnspan=4)

        else:

            try:
                self.f.grid_forget()
            except(AttributeError):
                pass

            self.inteMsg = Label(self.wind, text="No existe el paciente", bg='#f56464', fg='#d92222')
            self.inteMsg.grid(row=2, column=0, columnspan=4)

class Diagnostico:
    __id_diagnostico = 0
    __medico = ""
    __fecha = datetime.now().strftime('%Y-%m-%d')
    __descripcion = ""

    def __init__(self, diawind, conex, id, antDia, antBtn, antTra):
        self.__id_diagnostico = id
        self.antDia = antDia
        self.antBtn = antBtn
        self.antTra = antTra
        self.wind = diawind
        self.conex = conex
        self.wind.title("Registro de Diagnostico")
        #self.wind.geometry('420x700')
        self.wind.geometry(str("420x580+"+str(self.wind.winfo_screenwidth()//2 - 420//2)+"+"+str(self.wind.winfo_screenheight()//2 - 580//2)))
        self.wind.resizable(0, 0)
        Label(self.wind, text="Registro de Diagnostico", font = ("Arial Bold", 13, BOLD)).grid(row=0, column=0, columnspan= 2, pady=(10, 10))
        self.Registrar_Diagnostico()
    
    def Registrar_Diagnostico(self):

        def almacenar():
            btn.config(state="disabled")
            self.__fecha = self.entryFec.get()
            self.__medico = self.entryMed.get()
            self.__descripcion = self.entryDia.get("1.0", 'end-1c')

            cursor = self.conex.cursor()
            cursor.execute("SELECT id_diagnostico FROM diagnostico WHERE id_diagnostico = {}".format(str(self.__id_diagnostico)))
            dato = cursor.fetchone()

            if dato == None:
                cursor.execute("SELECT COUNT(id_diagnostico) FROM diagnostico")
                cant = cursor.fetchone()
                id = int(cant[0]) + 1
                try:
                    cursor.execute("INSERT INTO diagnostico VALUES({},'{}','{}','{}')".format(str(id), self.__medico, self.__fecha, self.__descripcion))
                    self.conex.commit()
                except:
                    messagebox.showerror('Error', 'Ocurrió un error al almacenar los datos en la base de datos')
                else:
                    messagebox.showinfo('Guardado Exitoso!', 'Los datos han sido actualizados con exito')
                    try:
                        #Boton Guardar
                        self.wind.destroy()
                        self.antDia.config(state="normal")
                        cursor = self.conex.cursor()
                        cursor.execute("SELECT descripcion FROM diagnostico WHERE id_diagnostico = {}".format(str(id)))
                        dato = cursor.fetchone()
                        self.antDia.delete('1.0', END)
                        self.antDia.insert('1.0', str(dato[0]))
                        self.antDia.config(state="disabled")
                        if self.antDia.get("1.0", 'end-1c') == "" or self.antDia.get("1.0", 'end-1c') == None and self.antTra.get("1.0", 'end-1c') == "" or self.antTra.get("1.0", 'end-1c') == None:
                            self.antBtn.config(state="disabled")
                        else:
                            self.antBtn.config(state="normal")
                    except(TclError):
                        pass
            else:
                try:
                    cursor.execute("UPDATE diagnostico SET medico = '{}', fecha = '{}', descripcion = '{}' WHERE id_diagnostico = {}".format(self.__medico, self.__fecha, self.__descripcion, str(self.__id_diagnostico)))
                    self.conex.commit()
                except:
                    messagebox.showerror('Error', 'Ocurrió un error al almacenar los datos en la base de datos')
                else:
                    messagebox.showinfo('Guardado Exitoso!', 'Los datos han sido actualizados con exito')
                    try:
                        self.wind.destroy()
                        self.antDia.config(state="normal")
                        cursor = self.conex.cursor()
                        cursor.execute("SELECT descripcion FROM diagnostico WHERE id_diagnostico = {}".format(str(self.__id_diagnostico)))
                        dato = cursor.fetchone()
                        self.antDia.delete('1.0', END)
                        self.antDia.insert('1.0', str(dato[0]))
                        self.antDia.config(state="disabled")
                        if self.antDia.get("1.0", 'end-1c') == "" or self.antDia.get("1.0", 'end-1c') == None and self.antTra.get("1.0", 'end-1c') == "" or self.antTra.get("1.0", 'end-1c') == None:
                            self.antBtn.config(state="disabled")
                        else:
                            self.antBtn.config(state="normal")
                    except(TclError):
                        pass

        #LabelFrame
        self.f = LabelFrame(self.wind, text="Datos del Diagnostico", pady=20, padx=20)
        self.f.grid(row=1, column=0, columnspan=2, padx=(20,20))

        #Fecha
        Label(self.f, text="Fecha:").grid(row=0, column=0, pady=(10,10), columnspan = 2)

        self.entryFec = Entry(self.f, width=20)
        self.entryFec.grid(row=1, column=0, pady=(10,20))

        Label(self.f, text="yyyy-mm-dd", fg="grey").grid(row=1, column=1, pady=(10,20))

        #Medico
        Label(self.f, text="Medico:").grid(row=2, column=0, pady=(10,10), columnspan = 2)

        self.entryMed = Entry(self.f, width=30)
        self.entryMed.grid(row=3, column=0, pady=(10,20), columnspan = 2)

        #Diagnostico
        Label(self.f, text="Descripcion:").grid(row=4, column=0, pady=(10,10), columnspan = 2)

        self.entryDia = Text(self.f, width=40, height=8)
        self.entryDia.grid(row = 5, column=0, columnspan = 2, pady=(10,10))

        cursor = self.conex.cursor()
        cursor.execute("SELECT id_diagnostico, fecha, medico, descripcion FROM diagnostico WHERE id_diagnostico = {}".format(str(self.__id_diagnostico)))
        dato = cursor.fetchone()

        if not dato == None:
            self.entryFec.insert(0, dato[1])
            self.entryMed.insert(0, dato[2])
            self.entryDia.insert('1.0', str(dato[3]))

        #Boton
        btn = Button(self.f, text="Guardar Diagnostico", command=almacenar)
        btn.grid(row=6, column=0, columnspan=2, pady=(10,20))

class Tratamiento:
    __id_tratamiento = 0
    __medico = ""
    __fecha_inicio = datetime.now().strftime('%Y-%m-%d')
    __descripcion = ""

    def __init__(self, trawind, conex, id, anTra, antDia, antBtn):
        self.__id_tratamiento = id
        self.anTra = anTra
        self.antDia = antDia
        self.antBtn = antBtn
        self.wind = trawind
        self.conex = conex
        self.wind.title("Registro de Tratamiento")
        self.wind.geometry(str("420x580+"+str(self.wind.winfo_screenwidth()//2 - 420//2)+"+"+str(self.wind.winfo_screenheight()//2 - 580//2)))
        self.wind.resizable(0, 0)
        Label(self.wind, text="Registro de Tratamiento", font = ("Arial Bold", 13, BOLD)).grid(row=0, column=0, columnspan= 2, pady=(10, 10))
        self.Registrar_Tratamiento()
    
    def Registrar_Tratamiento(self):

        def almacenar():
            btn.config(state="disabled")
            self.__fecha_inicio = self.entryFec.get()
            self.__medico = self.entryMed.get()
            self.__descripcion = self.entryTra.get("1.0", 'end-1c')

            cursor = self.conex.cursor()
            cursor.execute("SELECT id_tratamiento FROM tratamiento WHERE id_tratamiento = {}".format(str(self.__id_tratamiento)))
            dato = cursor.fetchone()

            if dato == None:
                cursor.execute("SELECT COUNT(id_tratamiento) FROM tratamiento")
                cant = cursor.fetchone()
                id = int(cant[0]) + 1
                try:
                    cursor.execute("INSERT INTO tratamiento VALUES({},'{}','{}','{}')".format(str(id), self.__medico, self.__fecha_inicio, self.__descripcion))
                    self.conex.commit()
                except:
                    messagebox.showerror('Error', 'Ocurrió un error al almacenar los datos en la base de datos')
                else:
                    messagebox.showinfo('Guardado Exitoso!', 'Los datos han sido actualizados con exito')
                    try:
                        self.wind.destroy()
                        self.anTra.config(state="normal")
                        cursor = self.conex.cursor()
                        cursor.execute("SELECT descripcion FROM tratamiento WHERE id_tratamiento = {}".format(str(id)))
                        dato = cursor.fetchone()
                        self.anTra.delete('1.0', END)
                        self.anTra.insert('1.0', str(dato[0]))
                        self.anTra.config(state="disabled")
                        if self.antDia.get("1.0", 'end-1c') == "" or self.antDia.get("1.0", 'end-1c') == None and self.anTra.get("1.0", 'end-1c') == "" or self.anTra.get("1.0", 'end-1c') == None:
                            self.antBtn.config(state="disabled")
                        else:
                            self.antBtn.config(state="normal")
                    except(TclError):
                        pass
            else:
                try:
                    cursor.execute("UPDATE tratamiento SET medico = '{}', fecha_inicio = '{}', descripcion = '{}' WHERE id_tratamiento = {}".format(self.__medico, self.__fecha_inicio, self.__descripcion, str(self.__id_tratamiento)))
                    self.conex.commit()
                except:
                    messagebox.showerror('Error', 'Ocurrió un error al almacenar los datos en la base de datos')
                else:
                    messagebox.showinfo('Guardado Exitoso!', 'Los datos han sido actualizados con exito')
                    try:
                        self.wind.destroy()
                        self.anTra.config(state="normal")
                        cursor = self.conex.cursor()
                        cursor.execute("SELECT descripcion FROM tratamiento WHERE id_tratamiento = {}".format(str(self.__id_tratamiento)))
                        dato = cursor.fetchone()
                        self.anTra.delete('1.0', END)
                        self.anTra.insert('1.0', str(dato[0]))
                        self.anTra.config(state="disabled")
                        if self.antDia.get("1.0", 'end-1c') == "" or self.antDia.get("1.0", 'end-1c') == None and self.anTra.get("1.0", 'end-1c') == "" or self.anTra.get("1.0", 'end-1c') == None:
                            self.antBtn.config(state="disabled")
                        else:
                            self.antBtn.config(state="normal")
                    except(TclError):
                        pass

        #LabelFrame
        self.f = LabelFrame(self.wind, text="Datos del Tratamiento", pady=20, padx=20)
        self.f.grid(row=1, column=0, columnspan=2, padx=(20,20))

        #Fecha
        Label(self.f, text="Fecha de Inicio:").grid(row=0, column=0, pady=(10,10), columnspan = 2)

        self.entryFec = Entry(self.f, width=20)
        self.entryFec.grid(row=1, column=0, pady=(10,20))

        Label(self.f, text="yyyy-mm-dd", fg="grey").grid(row=1, column=1, pady=(10,20))

        #Medico
        Label(self.f, text="Medico:").grid(row=2, column=0, pady=(10,10), columnspan = 2)

        self.entryMed = Entry(self.f, width=30)
        self.entryMed.grid(row=3, column=0, pady=(10,20), columnspan = 2)

        #Descripcion
        Label(self.f, text="Descripcion:").grid(row=4, column=0, pady=(10,10), columnspan = 2)

        self.entryTra = Text(self.f, width=40, height=8)
        self.entryTra.grid(row = 5, column=0, columnspan = 2, pady=(10,10))

        cursor = self.conex.cursor()
        cursor.execute("SELECT id_tratamiento, fecha_inicio, medico, descripcion FROM tratamiento WHERE id_tratamiento = {}".format(str(self.__id_tratamiento)))
        dato = cursor.fetchone()

        if not dato == None:
            self.entryFec.insert(0, dato[1])
            self.entryMed.insert(0, dato[2])
            self.entryTra.insert('1.0', str(dato[3]))

        #Boton
        btn = Button(self.f, text="Guardar Tratamiento", command=almacenar)
        btn.grid(row=6, column=0, columnspan=2, pady=(10,20))

#################################### NO TOCAR #################################################
class Enfermero(Pacientes):
    def __init__(self, pacwind, conex):
        self.wind = pacwind
        self.conex = conex
        self.wind.title("Actualizacion de Pacientes")
        self.wind.geometry('360x520')
        self.wind.resizable(0, 0)
        Label(self.wind, text="Actualizacion de Pacientes", font = ("Arial Bold", 13, BOLD)).grid(row=0, column=0, columnspan= 3, pady=(10, 10))
        Label(self.wind, text="Cedula: ").grid(row=1, column=0, padx=(10, 30), pady=(10,10))

        self.entryCed = Entry(self.wind, width=30)
        self.entryCed.grid(row=1, column=1, padx=(10,10), pady=(10,10))

        btn = Button(self.wind, text='Buscar', command=self.Actualizar_Pacientes)
        btn.grid(row=1, column=2, padx=(10,10), pady=(10,10))
###############################################################################################
class Medico(HistorialClinico):
    def __init__(self, hcwind, conex):
        self.wind = hcwind
        self.conex = conex
        self.wind.title("Actualizacion de Historial Clinico")
        #self.wind.geometry('420x700')
        self.wind.geometry(str("420x700+"+str(self.wind.winfo_screenwidth()//2 - 420//2)+"+"+str(self.wind.winfo_screenheight()//2 - 700//2)))
        self.wind.resizable(0, 0)
        Label(self.wind, text="Actualizacion de Historial Clinico", font = ("Arial Bold", 13, BOLD)).grid(row=0, column=0, columnspan= 4, pady=(10, 10))
        Label(self.wind, text="Cedula: ").grid(row=1, column=0, padx=(10, 30), pady=(10,10))

        self.entryCed = Entry(self.wind, width=30)
        self.entryCed.grid(row=1, column=1, padx=(10,10), pady=(10,10), columnspan=2)

        self.btn = Button(self.wind, text='Buscar', command=self.Actualizar_Historial_Clinico)
        self.btn.grid(row=1, column=3, padx=(10,10), pady=(10,10))

#################################### NO TOCAR #################################################
class Recepcionista(Citas):
    def __init__(self, citwind, conex):
        self.wind = citwind
        self.conex = conex
        self.wind.title("Agendamiento de Citas")
        self.wind.geometry('360x520')
        self.wind.resizable(0, 0)
        Label(self.wind, text="Agendamiento de Citas", font = ("Arial Bold", 13, BOLD)).grid(row=0, column=0, columnspan= 3, pady=(10, 10))
        Label(self.wind, text="Cedula: ").grid(row=1, column=0, padx=(10, 30), pady=(10,10))

        self.entryCed = Entry(self.wind, width=30)
        self.entryCed.grid(row=1, column=1, padx=(10,10), pady=(10,10))

        btn = Button(self.wind, text='Buscar', command=self.Agendar_Citas)
        btn.grid(row=1, column=2, padx=(10,10), pady=(10,10))
###############################################################################################

if __name__ == '__main__':
    conexion = sqlite3.connect('centro de salud.db')
    window = Tk()
    app = Login(window, conexion)
    window.mainloop()