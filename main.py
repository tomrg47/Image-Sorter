from guizero import *

app = App(title="Image Sorter")


def ui():
    #app.bg()
    title_box = Box(app,width="fill",align="top")
    title_text = Text(title_box, text="Image Sorter",font="arial",size=30)


ui()
app.display()
