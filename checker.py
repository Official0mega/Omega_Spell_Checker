import tkinter
from tkinter import *
from textblob import TextBlob
import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout


Builder.load_string('''
<updlbl>:
    size:500,1000
    canvas.before: 
        Color: 
            rgba: (1, 1, 1, 1) 
        Rectangle: 
            source:'background.png'
            size: root.width, root.height 
            pos: self.pos
    Label:
        id: updlbl
        text: '[b]Output[/b]:'
		font_size:"25sp"
		pos_hint:{"x":-0.3,"y":-0.03}
		color: "5d18d6"
		markup: True
	Label:
    	text:"Rgb/Hex converter"
    	pos_hint:{"y":0.46}
    	background_color: "3d3d3d"
    	font_size:"25sp"
	Label:
		text:"this is a small app by yashas :-)"
		font_size:"8sp"
	    color:(1,1,1,1)
 	   pos_hint:{"x":0,"y":-0.4}
	TextInput: 
        id: input
        hint_text:'Enter hex/rgb code:'
        pos_hint: {'x': 0.1, 'y': 0.8} 
        font_size: "20sp"
        size_hint: 0.8, 0.09
        padding: 40
    Label:
    	text:"hex format: xxxxxx   and   rgb format: xxx,xxx,xxx"
    	font_size:"10sp"
    	pos_hint:{"y":.27}
    Button:
        text: 'Convert'
		size_hint:.4,.08
		pos_hint:{"x":0.28,"y":0.6}
		border:1,1,1,1
		on_press:root.convert()
	TextInput: 
        id: output
        hint_text:'Output will be shown here'
        pos_hint: {'x': 0.1, 'y': 0.3}
        font_size: "20sp"
        size_hint: 0.8, 0.09
        padding: 40
 ''')
 
root=Tk()
root.title("Omega Spelling Checker")
root.geometry("700x400")
root.config(background="#dae6f6")



def check_spelling():
	word=enter_text.get()
	a=TextBlob(word)
	right=str(a.correct())
	
	cs=Label(root,text="Correct Spelling is :",font=("poppins",20),bg="#dae6f6",fg="#364971")
	cs.place(x=100,y=250)
	spell.config(text=right)


heading= Label(root,text= "Omega Spelling Checker",font=("Trebuchet MS",30, "bold"),bg="#dae6f6",fg="#364971")
heading.pack(pady=(50,0))



enter_text= Entry(root,justify="center",width=30,font=("poppins",25),bg="white",border=2)
enter_text.pack(pady=10)
enter_text.focus()


button=Button(root,text="Check",font=("arial",20,"bold"),fg="white",bg="red",command=check_spelling)
button.pack()


spell= Label(root,font=("poppins",20),bg="#dae6f6",fg="#364971")
spell.place(x=350,y=250)



root.mainloop()
