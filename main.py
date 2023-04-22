import tkinter as tk
import customtkinter as ctk
import webbrowser
import openai

openai.api_key = "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"

ctk.set_default_color_theme("theme.json")
ctk.set_appearance_mode('Dark')


#--FRAMES---

#Welcome
class WelcomeFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
             
        self.configure(fg_color="transparent")
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        def to_main():
           self.main = MainFrame(app, fg_color="transparent")
           self.main.grid(row=0,column=1,padx=20,pady=20,sticky="nsew")
        
        def start():
            self.destroy()
            to_main()
            
        self.name = ctk.CTkLabel(self, text='Welcome to Grow Bot', font=('Sans-Serif', 40, 'bold'))
        self.name.grid(row=0, column=0,padx=20, pady=(20,0))

        self.description = ctk.CTkLabel(self, font=('Sans-Serif', 18, 'italic'), wraplength=700, text='Bienvenidos a Grow Bot. Esta es una aplicación de chat bot que utiliza la inteligencia artificial para generar respuestas creativas y personalizadas. Puedes hablar conmigo sobre cualquier tema que te interese, desde el clima hasta la poesía. También puedo ayudarte con algunas tareas como escribir un código, una canción o un resumen. Estoy aquí para entretenerte y aprender de ti. ')
        self.description.grid(row=1, column=0, padx=20, pady=20)
        
        self.button_start = ctk.CTkButton(self, command=start, text='Start', font=('Sans-Serif', 18, 'bold'),width=250, height=40)
        self.button_start.grid(row=2, column=0, padx=20, pady=20)
        
        self.copyright = ctk.CTkLabel(self, text="@Todos los Derechos Reservados a | 4nd1-dev", state="disable")
        self.copyright.grid(row=3, column=0, padx=10, pady=(20,10))


#SideBar      
class SideBarFrame(ctk.CTkFrame):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        #Title
        self.title = ctk.CTkLabel(self, text='Grow-Bot', font=('Sans-Serif', 30, 'bold'))
        self.title.grid(row=0, column=0,padx=20, pady=20, sticky="nsew")
        
        #About Us
        def abrirEnlaceGit(event):
            webbrowser.open_new("https://github.com/4nd1-dev")
            
        def aboutMeEvent():
            self.about_us = ctk.CTkToplevel(app)
            self.about_us.geometry("500x500")
            self.about_us.title("GrowBot | About Me")
            self.about_us.rowconfigure(2, weight=1)
            
            self.label = ctk.CTkLabel(self.about_us, font=("Sans-Serif", 20), text="GrowBot es un Software OpenSource desarrollado en Python completamente por 4nd1-Dev, puedes encontrarlo en mi repositorio de GitHub", anchor="w", wraplength=450)
            self.label.grid(row=0, column=0, padx=20, pady=20)
            
            self.label = ctk.CTkLabel(self.about_us, font=("Sans-Serif", 18, "bold"), text="4nd1-Dev es un desarrollador Junior enfocado en el desarrollo web y en el desarrollo de Aplicaciones Móviles Multiplataformas y de Escritorio mediante el empleo de Frameworks de Python", anchor="w", wraplength=450)
            self.label.grid(row=1, column=0, padx=20, pady=20)
            
            self.enlaceGit = ctk.CTkLabel(self.about_us, text="Sígueme en GitHub", text_color=("#ffffff", "#ffffff"),font=("Sans-Serif", 18), fg_color=("#000000","#000000"), padx=10, pady=10, cursor="hand2")
            self.enlaceGit.grid(row=2, column=0, padx=20, pady=20)
            self.enlaceGit.bind("<Button-1>", abrirEnlaceGit)
            
            self.copyright = ctk.CTkLabel(self.about_us, text="@Todos los Derechos Reservados a | 4nd1-dev", state="disable")
            self.copyright.grid(row=3, column=0, padx=10, pady=(20,10))
        
        self.title = ctk.CTkButton(self, text="About Me", font=('Sans-Serif', 15, 'bold'), fg_color="transparent", hover_color=("#ee7733","#ee7700"), text_color=("#000000", "#ffffff"), command=aboutMeEvent)
        self.title.grid(row=4, column=0,padx=20, pady=20, sticky="nsew")      
        
        #Switch
        appearance_mode_switch_var= ctk.StringVar(value="on")
        
        def appearance_mode():
            if appearance_mode_switch_var.get() == "on": ctk.set_appearance_mode('Dark')
            if appearance_mode_switch_var.get() == "off": ctk.set_appearance_mode('Light')
       
        self.buttonMode = ctk.CTkSwitch(self, text='Dark Mode', font=('Sans-Serif', 18), command=appearance_mode, variable=appearance_mode_switch_var, onvalue="on", offvalue="off")
        self.buttonMode.grid(row=5, column=0, padx=20, pady=20)
        
    
        
#Main
class MainFrame(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        #title
        self.title = ctk.CTkLabel(self, font=("Sans-Serif", 25, "bold"), text="Chat")
        self.title.grid(row=0, column=0, padx=20, pady=(20, 10))
        
        #Preguntas & Respuestas
        self.scrollableFrame = ctk.CTkScrollableFrame(self, fg_color="transparent")
        self.scrollableFrame.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
        
        self.scrollableFrame.grid_rowconfigure(0, weight=1)
        self.scrollableFrame.grid_columnconfigure(0, weight=1)
        
        #Entry & Button
        self.inputFrame = ctk.CTkFrame(self)
        self.inputFrame.grid_columnconfigure(0, weight=1)
        self.inputFrame.grid(row=2, column=0, sticky="wsew")
        
        self.inputEntry= ctk.CTkEntry(self.inputFrame, font=("Sans-Serif", 18), placeholder_text="Pregunta Algo!!", height=25)
        self.inputEntry.grid(row=0, column=0, padx=20, pady=20, sticky="wsew")
        
        
        def chat_response():
             response = openai.ChatCompletion.create( model="gpt-3.5-turbo", messages=[
                 {"role": "system", "content": "Eres un modelo del lenguaje potencializado con GPT 3.5  con un amplio conocimiento sobre Programación, Ciencia, Arte, Filosofía, Tecnología, Redacción y Comprensión de Textos, Poemas y Canciones y un Asistente Personal."},
                 {"role": "user", "content": self.prompt}
             ])
             self.responseLabel = ctk.CTkLabel(self.scrollableFrame, font=("Sans-Serif", 20), wraplength=self.scrollableFrame.winfo_width(), fg_color=("transparent"), padx=10, pady=10, anchor="w", justify="left", text="GrowBot:  " + response["choices"][0]["message"]["content"])
             self.responseLabel.pack(fill=tk.X)
        
        def send_prompt():
            self.prompt = self.inputEntry.get()
            self.promptLabel = ctk.CTkLabel(self.scrollableFrame, font=("Sans-Serif", 20, "bold"), wraplength=self.scrollableFrame.winfo_width(), fg_color=("#ffffff", "#333333"), padx=10, pady=10, anchor="w", justify="left", text="Tú: " + self.prompt)
            self.promptLabel.pack(fill=tk.X)
            self.inputEntry.delete(0, "end")
            
            chat_response()
      
        self.inputButton = ctk.CTkButton(self.inputFrame, font=("Sans-Serif", 18, "bold"), text="Send", width=100, command=send_prompt)
        self.inputButton.grid(row=0, column=1, padx=20, pady=20)
       
        



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f'{1200}x{600}')
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.minsize(1000,400)
        self.title('GrowBot')

        self.welcome = WelcomeFrame(self)
        self.welcome.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        
        self.sidebar = SideBarFrame(self, width=250, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky='nsew')




            

if __name__=='__main__':
    app = App()
    app.mainloop()