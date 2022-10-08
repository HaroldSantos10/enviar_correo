from distutils.cmd import Command
from os import environ
from source import email
from dotenv import load_dotenv



#inica la configuración de la ventana
from tkinter import Tk,Label, Entry, Button, Text, messagebox


def save_fonc():
    correo=etDestino.get()
    nombre=etUser.get()
    print("Ingrese el email de quien recibirá el mensaje",correo,
    "Ingrese el nombre de quien recibirá el mensaje",nombre)

def clear_text(event):#limpia el contenido de los entries cada vez que el focus llega 
    event.widget.delete(0, "end")

def enviar_mensaje():#función que designa contiene y da formato al mensaje a enviar
    load_dotenv()#inicia la carga de html a enviar en el correo


    mensaje_html="""

    <!DOCYPE html>
    <html>
    <body>
    <h1>Un gusto saludarlo {}</h1>
    <p>{}</p>
    </body>
    </html>

    """
    origen="haroldsan9.9@gmail.com"
    environ["STMP_USER"]=origen
    nombre=etUser.get()
    destinatario=etDestino.get()
    mensaje=txtMensaje.get("1.0",'end-1c')
    Correo = email.Email()
    Correo.mandar_email([destinatario],"Prueba Python", message_format=mensaje_html.format(nombre,mensaje), format="html")

    messagebox.showinfo(title="Estado del mensaje", 
        message=f"¡El mensaje ha sido enviado exitosamente!")#mensaje de confirmación de que el corrreo a sido enviado correctamente



ventana = Tk()
ventana.geometry("650x500")
ventana.config(bg="#5E5958")
ventana.title("Enviar mensaje por email")



lbDestinatario = Label(ventana, text= "Enviar a:")
lbDestinatario.config(bg="#483D8B")
lbUsuario = Label(ventana, text="Usuario: ")
lbUsuario.config(bg= "#483D8B")
etDestino = Entry(ventana, fg = "#84979f")
etDestino.insert(0,"Ingrese el email de quien recibirá el mensaje")#indicación por defecto del entry para ser llenado
etUser = Entry(ventana, fg = "#84979f")
etUser.insert(0,"Ingrese el nombre de quien recibirá el mensaje")#indicación por defecto del entry para ser llenado

txtMensaje = Text(ventana, font= "Garamond")


btnEnviar = Button(ventana, text="Enviar", command = enviar_mensaje)
btnEnviar.config(bg="#483D8B")

lbDestinatario.place(x=30, y=100, width=100, height=30)
lbUsuario.place(x=30, y=170, width=100, height=30)
etDestino.place(x=150, y=100, width=300, height=30)
etUser.place(x=150, y=170, width=300, height=30)

txtMensaje.place(x=40, y=250, width=500, height=150)
btnEnviar.place(x=450, y=425, width=100, height=30)


#limpienza de los entries
etDestino.bind("<FocusIn>", clear_text)
etUser.bind("<FocusIn>", clear_text)




ventana.mainloop()



