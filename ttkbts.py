import ttkbootstrap as tb
from ttkbootstrap import *
from ttkbootstrap.constants import *
from tkinter import *
from tkinter.messagebox import showerror
import mechanicalsoup

browser = mechanicalsoup.StatefulBrowser()
browser.open("https://www.kursna-lista.com/kursna-lista-nbs")

th = browser.page.find_all("td", attrs={"class": ""})
redovi = [i.text for i in th]

pismo = ("Time", 16, "bold")
pismo_2 = ("Time", 14)

class Konvertor:
    @staticmethod
    def kupE(e):
        return e*float(redovi[6])

    @staticmethod
    def prE(e):
        return e*float(redovi[4])

    @staticmethod
    def kupUSD(usd):
        return usd*float(redovi[97])

    @staticmethod
    def prUSD(usd):
        return usd*float(redovi[95])

    @staticmethod
    def kupSWF(swf):
        return swf*float(redovi[83])

    @staticmethod
    def prSWF(swf):
        return swf*float(redovi[81])

    @staticmethod
    def kupGBP(p):
        return p*float(redovi[90])

    @staticmethod
    def prGBP(p):
        return p*float(redovi[88])

class SampleApp(tb.Window):
    def __init__(self):
        tb.Window.__init__(self)

        self.geometry("400x400")
        self.resizable(0,0)
        self.title("Menjačnica")
        self._frame = None
        self.switch_frame(Pocetna)

        tb.Label(self, text="Izvor: https://www.kursna-lista.com/kursna-lista-nbs").place(relx=0.14, rely=0.8)

        tb.Button(self, text="EXIT", width=7, bootstyle="primary",command=self.destroy).place(relx=0.4, rely=0.9) 

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class Pocetna(tb.Frame):
    def __init__(ps, master):
        tb.Frame.__init__(ps, master)

        tb.Style("solar") 
        
        ps.frame_1 = tb.Frame(ps)
        ps.frame_1.pack(fill="x")

        tb.Label(ps.frame_1, text="POČETNA STRANA", font = pismo).pack(padx = (45,20), pady=(5, 5), side="top", expand=True)
        
        ps.eu = tk.Frame(ps)
        ps.eu.pack()
        
        tb.Label(ps.eu, text="Konvertor Eura", 
                 font = pismo_2).pack(padx=(5,0), pady=(50,2.5), side="left",expand=True)
        tb.Button(ps.eu, text="NASTAVI",
                command=lambda: master.switch_frame(KupovinaE)).pack(padx=(85,15), pady=(50,2.5), side="right",expand=True)
        
        ps.usd = tb.Frame(ps)
        ps.usd.pack()
        
        tb.Label(ps.usd, text="Konvertor US Dolara", 
                 font = pismo_2).pack(padx=(5,0), pady=(5,2.5), side="left",expand=True)
        tb.Button(ps.usd, text="NASTAVI",
                command=lambda: master.switch_frame(KupovinaUSD)).pack(padx=(40,15), pady=(5,2.5), side="right",expand=True)

        ps.swf = tb.Frame(ps)
        ps.swf.pack()
        
        tb.Label(ps.swf, text="Konvertor SW Franaka", 
                 font = pismo_2).pack(padx=(5,0), pady=(2.5,0), side="left",expand=True)
        tb.Button(ps.swf, text="NASTAVI",
                command=lambda: master.switch_frame(KupovinaSWF)).pack(padx=(22,15), pady=(5,2.5), side="right",expand=True)

        ps.gbp = tb.Frame(ps)
        ps.gbp.pack()
        
        tb.Label(ps.gbp, text="Konvertor Funte", 
                 font = pismo_2).pack(padx=(5,0) ,pady=(2.5,0), side="left",expand=True)
        tb.Button(ps.gbp, text="NASTAVI",
                command=lambda: master.switch_frame(KupovinaGBP)).pack(padx=(78,15), pady=(5,2.5), side="right",expand=True)
         

# Euro
class KupovinaE(tb.Frame):
    def __init__(eu, master):
        tb.Frame.__init__(eu, master)

        tb.Label(eu, text="Kupovina EURA", font=("Time", 16, "bold")).pack(side="top", fill="x", padx=5, pady=10)

        eu.ram_1 = tb.Frame(eu)
        eu.ram_1.pack(fill=X)

        tb.Label(eu.ram_1, text="Unesite vrednost Eura", font=("Time",10, "bold")).pack()

        eu.euro = StringVar()
        eu.entri_eu= tb.Entry(eu.ram_1, textvariable=eu.euro, font=("Time", 12, "bold"))
        eu.entri_eu.pack(side="left",pady=10)

        eu.con = tb.Button(eu.ram_1, text="KONVERTUJ", command=eu.kupovina_e)
        eu.con.pack(side="left")

        eu.result_label = tb.Label(eu, font=("Time", 12, "bold"), border=0.5)
        eu.result_label.pack(padx=5, pady=15)

        eu.ram_2 = tb.Frame(eu, height=200)
        eu.ram_2.pack(fill=X, pady=15)

        tb.Button(eu.ram_2, text="Prodaja €", width=12, 
                  command=lambda: master.switch_frame(ProdajaE)).place(relx=0.3, rely=0.15)

        tb.Button(eu.ram_2, text="POČETNI MENI",
                  command=lambda: master.switch_frame(Pocetna)).place(relx=0.65, rely=0.15)

        tb.Label(eu.ram_2, text=f"Prodajni kurs:\n{redovi[6]:.8} dinara", font=("Time",16, "bold")).place(relx=0.25, rely=0.5)

    def kupovina_e(eu):
        try:
            e = float(eu.euro.get())
            c = Konvertor.kupE(e)
            result = f'{e} Eura je {c:.2f} Dinara'
            eu.result_label.config(text=result)
            eu.entri_eu.delete(0, END)
        except ValueError as error:
            showerror(title='Error', message=error)

class ProdajaE(tb.Frame):
    def __init__(eu, master):
        tb.Frame.__init__(eu, master)
        

        tb.Label(eu, text="Prodaja Eura", font=("Time", 16, "bold")).pack(side="top", fill="x", padx=5, pady=10)

        eu.ram_1 = tb.Frame(eu)
        eu.ram_1.pack(fill=X)

        tb.Label(eu.ram_1, text="Unesite vrednost Eura", font=("Time",10, "bold")).pack()

        eu.euro = StringVar()
        eu.entri_eu= tb.Entry(eu.ram_1, textvariable=eu.euro, font=("Time", 12, "bold"))
        eu.entri_eu.pack(side="left", pady=10)

        eu.con = tb.Button(eu.ram_1, text="KONVERTUJ", command=eu.prodaja_e)
        eu.con.pack(side="left")

        eu.result_label = tb.Label(eu, font=("Time", 12, "bold"), border=0.5)
        eu.result_label.pack(padx=5, pady=15)

        eu.ram_2 = tb.Frame(eu, height=200)
        eu.ram_2.pack(fill=X, pady=15)

        tb.Button(eu.ram_2, text="Kupovina €", width=12, 
                  command=lambda: master.switch_frame(KupovinaE)).place(relx=0.3, rely=0.15)

        tb.Button(eu.ram_2, text="POČETNI MENI",
                  command=lambda: master.switch_frame(Pocetna)).place(relx=0.65, rely=0.15)

        tb.Label(eu.ram_2, text=f"Kupovni kurs:\n{redovi[4]:.8} dinara", font=("Time",16, "bold")).place(relx=0.25, rely=0.5)

    def prodaja_e(eu):
        try:
            e = float(eu.euro.get())
            c = Konvertor.prE(e)
            result = f'{e} Eura je {c:.2f} Dinara'
            eu.result_label.config(text=result)
            eu.entri_eu.delete(0, END)
        except ValueError as error:
            showerror(title='Error', message=error)


# -----------------------------------------------------------------------------------------------------------------------------------------------------
# US Dolar
class KupovinaUSD(tb.Frame):
    def __init__(usd, master):
        tb.Frame.__init__(usd, master)
        

        tb.Label(usd, text="Kupovina USD", font=("Time", 16, "bold")).pack(side="top", fill="x", pady=10)

        usd.ram_1 = tb.Frame(usd)
        usd.ram_1.pack(fill=X)

        tb.Label(usd.ram_1, text="Unesite vrednost US Dolara", font=("Time",10, "bold")).pack()

        usd.dolar = StringVar()
        usd.entri_usd= tb.Entry(usd.ram_1, textvariable=usd.dolar, font=("Time", 12, "bold"))
        usd.entri_usd.pack(side="left", pady=10)

        usd.con = tb.Button(usd.ram_1, text="KONVERTUJ", command=usd.kupovina_USD)
        usd.con.pack(side="left")

        usd.result_label = tb.Label(usd, font=("Time", 12, "bold"), border=0.5)
        usd.result_label.pack(padx=5, pady=10)

        usd.ram_2 = tb.Frame(usd, height=200)
        usd.ram_2.pack(fill=X, pady=15)

        tb.Button(usd.ram_2, text="Prodaja $", width=12,
                  command=lambda: master.switch_frame(ProdajaUSD)).place(relx=0.3, rely=0.15)

        tb.Button(usd.ram_2, text="POČETNI MENI",
                  command=lambda: master.switch_frame(Pocetna)).place(relx=0.65, rely=0.15)

        tb.Label(usd.ram_2, text=f"Prodajni kurs:\n{redovi[97]:.8} dinara", font=("Time",16, "bold")).place(relx=0.25, rely=0.5)

    def kupovina_USD(usd):
        try:
            us = float(usd.dolar.get())
            c = Konvertor.kupUSD(us)
            result = f'{us} US Dolara je {c:.2f} Dinara'
            usd.result_label.config(text=result)
            usd.entri_usd.delete(0, END)
        except ValueError as error:
            showerror(title='Error', message=error)

class ProdajaUSD(tk.Frame):
    def __init__(usd, master):
        tb.Frame.__init__(usd, master)
        

        tb.Label(usd, text="Prodaja USD", font=("Time", 16, "bold")).pack(side="top", fill="x", pady=10)

        usd.ram_1 = tb.Frame(usd)
        usd.ram_1.pack(fill=X)

        tb.Label(usd.ram_1, text="Unesite vrednost US Dolara", font=("Time",10, "bold")).pack()

        usd.us_dolar = StringVar()
        usd.entri_us= tb.Entry(usd.ram_1, textvariable=usd.us_dolar, font=("Time", 12, "bold"))
        usd.entri_us.pack(side="left", pady=10)

        usd.con = tb.Button(usd.ram_1, text="KONVERTUJ", command=usd.prodaja_USD)
        usd.con.pack(side="left")

        usd.result_label = tb.Label(usd, font=("Time", 12, "bold"), border=0.5)
        usd.result_label.pack(padx=5, pady=10)

        usd.ram_2 = tb.Frame(usd, height=200)
        usd.ram_2.pack(fill=X, pady=15)

        tb.Button(usd.ram_2, text="Kupovina $", width=12,
                  command=lambda: master.switch_frame(KupovinaUSD)).place(relx=0.3, rely=0.15)

        tb.Button(usd.ram_2, text="POČETNI MENI",
                  command=lambda: master.switch_frame(Pocetna)).place(relx=0.65, rely=0.15)

        tb.Label(usd.ram_2, text=f"Kupovni kurs:\n{redovi[95]:.8} dinara", font=("Time",16, "bold")).place(relx=0.25, rely=0.5)


    def prodaja_USD(usd):
        try:
            us = float(usd.us_dolar.get())
            c = Konvertor.prUSD(us)
            result = f'{us} US Dolara je {c:.2f} Dinara'
            usd.result_label.config(text=result)
            usd.entri_us.delete(0, END)
        except ValueError as error:
            showerror(title='Error', message=error)

#-------------------------------------------------------------------------------------------------------------------
# Švajcarski franak

class KupovinaSWF(tk.Frame):
    def __init__(sw, master):
        tb.Frame.__init__(sw, master)
        
        tb.Label(sw, text="Kupovina SW Franaka", font=("Time", 16, "bold")).pack(side="top", fill="x", padx=5, pady=10)

        sw.ram_1 = tb.Frame(sw)
        sw.ram_1.pack(fill=X)

        tb.Label(sw.ram_1, text="Unesite vrednost SW Franaka", font=("Time",10, "bold")).pack()

        sw.franak = StringVar()
        sw.entri_sw= tb.Entry(sw.ram_1, textvariable=sw.franak, font=("Time", 12, "bold"))
        sw.entri_sw.pack(side="left", pady=10)

        sw.con = tb.Button(sw.ram_1, text="KONVERTUJ", command=sw.kupovina_SWF)
        sw.con.pack(side="left")

        sw.result_label = tb.Label(sw, font=("Time", 12, "bold"), border=0.5)
        sw.result_label.pack(padx=5, pady=15)

        sw.ram_2 = tb.Frame(sw, height=200)
        sw.ram_2.pack(fill=X, pady=15)

        tb.Button(sw.ram_2, text="Prodaja CHF", width=12,
                  command=lambda: master.switch_frame(ProdajaSWF)).place(relx=0.3, rely=0.15)

        tb.Button(sw.ram_2, text="POČETNI MENI",
                  command=lambda: master.switch_frame(Pocetna)).place(relx=0.65, rely=0.15)

        tb.Label(sw.ram_2, text=f"Prodajni kurs:\n{redovi[83]:.8} dinara", font=("Time",16, "bold")).place(relx=0.25, rely=0.5)

    def kupovina_SWF(sw):
        try:
            swf = float(sw.franak.get())
            c = Konvertor.kupSWF(swf)
            result = f'{swf} Franaka je {c:.2f} Dinara'
            sw.result_label.config(text=result)
            sw.entri_sw.delete(0, END)
        except ValueError as error:
            showerror(title='Error', message=error)

class ProdajaSWF(tk.Frame):
    def __init__(sw, master):
        tb.Frame.__init__(sw, master)  

        tb.Label(sw, text="Prodaja SW Franaka", font=("Time", 16, "bold")).pack(side="top", fill="x", padx=5, pady=10)

        sw.ram_1 = tb.Frame(sw)
        sw.ram_1.pack(fill=X)

        tb.Label(sw.ram_1, text="Unesite vrednost SW Franaka", font=("Time",10, "bold")).pack()

        sw.franak = StringVar()
        sw.entri_swf= tb.Entry(sw.ram_1, textvariable=sw.franak, font=("Time", 12, "bold"))
        sw.entri_swf.pack(side="left", pady=10)

        sw.con = tb.Button(sw.ram_1, text="KONVERTUJ", command=sw.swf_rs)
        sw.con.pack(side="left")

        sw.result_label = tb.Label(sw, font=("Time", 12, "bold"), border=0.5)
        sw.result_label.pack(padx=5, pady=15)

        sw.ram_2 = tb.Frame(sw, height=200)
        sw.ram_2.pack(fill=X, pady=15)

        tb.Button(sw.ram_2, text="Kupovina CHF", width=12,
                  command=lambda: master.switch_frame(KupovinaSWF)).place(relx=0.3, rely=0.15)

        tb.Button(sw.ram_2, text="POČETNI MENI",
                  command=lambda: master.switch_frame(Pocetna)).place(relx=0.65, rely=0.15)

        tb.Label(sw.ram_2, text=f"Kupovni kurs:\n{redovi[81]:.8} dinara", font=("Time",16, "bold")).place(relx=0.25, rely=0.5)

    def swf_rs(sw):
        try:
            swf = float(sw.franak.get())
            c = Konvertor.prSWF(swf)
            result = f'{swf} Franaka je {c:.2f} Dinara'
            sw.result_label.config(text=result)
            sw.entri_swf.delete(0, END)
        except ValueError as error:
            showerror(title='Error', message=error)
# -------------------------------------------------------------------------------------------------------------------
# Funta

class KupovinaGBP(tk.Frame):
    def __init__(gb, master):
        tb.Frame.__init__(gb, master)
        

        tb.Label(gb, text="Kupovina Funte", font=("Time", 16, "bold")).pack(side="top", fill="x", pady=10)

        gb.ram_1 = tb.Frame(gb)
        gb.ram_1.pack(fill=X)

        tb.Label(gb.ram_1, text="Unesite vrednost Funte", font=("Time",10, "bold")).pack()

        gb.funta = StringVar()
        gb.entri_p= tb.Entry(gb.ram_1, textvariable=gb.funta, font=("Time", 12, "bold"))
        gb.entri_p.pack(side="left", pady=10)

        gb.con = tb.Button(gb.ram_1, text="KONVERTUJ", command=gb.kupovina_GBP)
        gb.con.pack(side="left")

        gb.result_label = tb.Label(gb, font=("Time", 12, "bold"), border=0.5)
        gb.result_label.pack(padx=5, pady=10)

        gb.ram_2 = tb.Frame(gb, height=200)
        gb.ram_2.pack(fill=X, pady=15)

        tb.Button(gb.ram_2, text="Prodaja £", width=12,
                  command=lambda: master.switch_frame(ProdajaGBR)).place(relx=0.3, rely=0.15)

        tb.Button(gb.ram_2, text="POČETNI MENI",
                  command=lambda: master.switch_frame(Pocetna)).place(relx=0.65, rely=0.15)

        tb.Label(gb.ram_2, text=f"Prodajni kurs:\n{redovi[90]:.6} dinara", font=("Time",16, "bold")).place(relx=0.25, rely=0.5)

    def kupovina_GBP(gb):
        try:
            p = float(gb.funta.get())
            c = Konvertor.kupGBP(p)
            result = f'{p} Funti je {c:.2f} Dinara'
            gb.result_label.config(text=result)
            gb.entri_p.delete(0, END)
        except ValueError as error:
            showerror(title='Error', message=error)

class ProdajaGBR(tk.Frame):
    def __init__(gb, master):
        tb.Frame.__init__(gb, master)
        

        tb.Label(gb, text="Prodaja Funte", font=("Time", 16, "bold")).pack(side="top", fill="x", pady=10)

        gb.ram_1 = tb.Frame(gb)
        gb.ram_1.pack(fill=X)

        tb.Label(gb.ram_1, text="Unesite vrednost Funte", font=("Time",10, "bold")).pack()

        gb.gb_funta = StringVar()
        gb.entri_gbp= tb.Entry(gb.ram_1, textvariable=gb.gb_funta, font=("Time", 12, "bold"))
        gb.entri_gbp.pack(side="left", pady=10)

        gb.con = tb.Button(gb.ram_1, text="KONVERTUJ", command=gb.prodaja_GBP)
        gb.con.pack(side="left")

        gb.result_label = tb.Label(gb, font=("Time", 12, "bold"), border=0.5)
        gb.result_label.pack(padx=5, pady=10)

        gb.ram_2 = tb.Frame(gb, height=200)
        gb.ram_2.pack(fill=X, pady=15)

        tb.Button(gb.ram_2, text="Kupovina £", width=12,
                  command=lambda: master.switch_frame(KupovinaGBP)).place(relx=0.3, rely=0.15)

        tb.Button(gb.ram_2, text="POČETNI MENI",
                  command=lambda: master.switch_frame(Pocetna)).place(relx=0.65, rely=0.15)

        tb.Label(gb.ram_2, text=f"Kupovni kurs:\n{redovi[88]:.6} dinara", font=("Time",16, "bold")).place(relx=0.25, rely=0.5)

    def prodaja_GBP(gb):
        try:
            funta = float(gb.gb_funta.get())
            c = Konvertor.prGBP(funta)
            result = f'{funta} Funti je {c:.2f} Dinara'
            gb.result_label.config(text=result)
            gb.entri_gbp.delete(0, END)
        except ValueError as error:
            showerror(title='Error', message=error)

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()