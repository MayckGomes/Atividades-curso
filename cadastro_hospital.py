import customtkinter
from time import sleep

customtkinter.set_appearance_mode("System")  
customtkinter.set_default_color_theme("blue") 

app = customtkinter.CTk()  
app.geometry("300x600")

texto = customtkinter.CTkLabel(app,text='Tela de login')
texto.place(relx=0.4, rely=0.2)


login = customtkinter.CTkEntry(app,placeholder_text='login')
login.place(relx=0.3,rely=0.3)

senha = customtkinter.CTkEntry(app,placeholder_text='senha',show='*')
senha.place(relx=0.3,rely=0.4)

def botao_command():
    if login == None and senha == None:
        text = customtkinter.CTkLabel(app,text='complete os campos!',text_color='red')
        text.place(relx=0.3, rely=0.6)

        sleep(0.5)

        text = customtkinter.CTkLabel(app,text='')
        text.place(relx=0.3, rely=0.100)
    else:
        text = customtkinter.CTkLabel(app,text='login feito com sucesso',text_color='green')
        text.place(relx=0.3, rely=0.6)

        print(login)
        print(senha)
botao = customtkinter.CTkButton(app,text='Entrar',command=botao_command)
botao.place(relx=0.3,rely=0.5)


app.mainloop()