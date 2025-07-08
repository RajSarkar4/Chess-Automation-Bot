import tkinter
import customtkinter

from chess import Chess

chess = Chess()
customtkinter.set_appearance_mode('system')

app = tkinter.Tk()
app.geometry('200x200')
app.title('Bot')

button_style = ('Robot',16,'bold')
browser_btn = customtkinter.CTkButton(master=app, text='Open Chess', command=chess.open_browser, text_font=button_style)
browser_btn.pack(anchor='w', padx=10,pady=(10,0))
move_btn_online = customtkinter.CTkButton(master=app, text='Run Bot Online', command=chess.run_bot_online, text_font=button_style)
move_btn_online.pack(anchor='w', padx=10, pady=(10,0))
move_btn_offline = customtkinter.CTkButton(master=app, text='Run Bot Offline', command=chess.run_bot_offline, text_font=button_style)
move_btn_offline.pack(anchor='w', padx=10, pady=(10,0))
reset_btn = customtkinter.CTkButton(master=app, text='Empty Bot', command=chess.reset, text_font=button_style)
reset_btn.pack(anchor='w', padx=10, pady=(10,0))
app.mainloop()