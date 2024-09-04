from gtts import gTTS
from playsound import playsound
from customtkinter import *
import customtkinter as tk
import os
import time
from PIL import Image
import webbrowser


app = tk.CTk()
app.title("Text to Speech")
app.geometry("600x460")
tk.set_appearance_mode("Dark")

image_path1 = os.path.join("assets", "play.png")
play_image = tk.CTkImage(light_image=Image.open(image_path1), size=(30, 30))
image_path2 = os.path.join("assets", "clear.png")
clear_image = tk.CTkImage (light_image=Image.open(image_path2),size=(30,30))
image_path3 = os.path.join("assets", "git.png")
git_image = tk.CTkImage(light_image=Image.open(image_path3),size=(30,30))
image_path4 = os.path.join("assets", "web.png")
web_image = tk.CTkImage(light_image=Image.open(image_path4),size=(30,30))

def clear():
    out.delete('0','end')

def generate() :
    try :
        text = out.get()
        clear()
        out.insert('0', "Generated and saved the output inside 'speech outputs'")
        out.update()
        tts=gTTS(text=text,lang='en')
        if not (os.path.isdir("speech outputs") == True) :
           os.mkdir("speech outputs")
        os.chdir("speech outputs")
        output = f'output{time.strftime("_%H:%M:%S_%Y%m%d")}.mp3'
        tts.save(output)
        time.sleep(1)
        clear()
        out.insert(0, "Playing the audio...")
        out.update()
        time.sleep(1)
        playsound(output)
        clear()
        out.insert(0, "Type your prompt...")
        out.update()
    except :
        error = "something went wrong !! Try again"
        out.insert('0',error)

def website():
    mtmsite= "https://mtm-x.github.io/"
    webbrowser.open_new(mtmsite)

def web():
    git = "https://github.com/mtm-x"
    webbrowser.open_new(git)

    

out=tk.CTkEntry(app,
                  width=560,
                  height=100,
                  font=(('Arial', 20)),
                  corner_radius=10,
                  border_color="white",
                  border_width=2,
                  placeholder_text="Type your prompt..."
                  
                  )
out.place(x=20,y=20)



my_clear = tk.CTkButton(app,
                        text="Clear",
                        command=clear,
                        image=clear_image,
                        width=130,
                        height=60,
                        fg_color=("transparent"),
                        corner_radius=10,
                        font=('',20),
                        border_color="white",
                        border_width=2,
                        text_color="white",
                        )
my_clear.place(x=380,y=180)


convert=tk.CTkButton(app,
                         width=130,
                         height=60,
                         corner_radius=10,
                         image=play_image,
                         text="Genrate and play !",
                         command=generate,
                         border_color="white",
                         font=('',20),
                         border_width=2,
                         text_color="white",
                         fg_color=("transparent"),
                         )

convert.place(x=70,y=180)


mtm=tk.CTkButton(app,
                 text="GitHub",
                 border_color="white",
                 width=440,
                 image=git_image,
                 font=('',20),
                 height=60,
                 border_width=2,
                 text_color="white",
                 command=web,
                 fg_color=("transparent")
                )
mtm.place(x=70,y=290)

myweb=tk.CTkButton(app,
                   text="Portfolio",
                   border_color="white",
                   width=440,
                   image=web_image,
                   height=60,
                   font=('',20),
                   border_width=2,
                   text_color="white",
                   command=website,
                   fg_color=("transparent"))
myweb.place(x=70,y=370)



app.mainloop()
