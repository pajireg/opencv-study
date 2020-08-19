# from tkinter import*
#
# def loadImage(fname):
#     global inImage, XSIZE, YSIZE
#     fp = open(fname, 'rb')
#
#     for i in range(0,XSIZE):
#         tmpList = []
#         for k in range(0,YSIZE):
#             data = int(ord(fp.read(1)))
#             tmpList.append(data)
#         inImage.append(tmpList)
#
#     fp.close()
#
# def displayImage(image):
#     global XSIZE, YSIZE
#     rgbString = ""
#     for i in range(0, XSIZE):
#             tmpString = ""
#             for k in range(0, YSIZE):
#                 data = image[i][k]
#
#
#                 tmpString += "#%02x%02x%02x " % (data,data,data)
#             rgbString += "{" + tmpString+ "} "
#     paper.put(rgbString)

# window = None
# canvas = None
# XSIZE, YSIZE = 256,256
# inImage =[]
#
# window = Tk()
# window.title("흑백 사진 보기")
# canvas = Canvas(window, height = XSIZE, width = YSIZE)
# paper = PhotoImage(width = XSIZE, height = YSIZE)
# canvas.create_image((XSIZE/2,YSIZE/2), image = paper, state = "normal")
#
# filename = "RAW/lena.raw"
# loadImage(filename)
#
# displayImage(inImage)
#
# canvas.pack()
# window.mainloop()


from tkinter import*
from tkinter.filedialog import*
from tkinter.simpledialog import*
from PIL import Image, ImageFilter, ImageEnhance, ImageOps

def displayImage(img, width, height):
    global window, canvas, paper, photo, photo2, oriX, oriY

    window.geometry(str(width) + "x" + str(height))
    if canvas != None:
        canvas.destroy()

    canvas = Canvas(window, width = width, height = height)
    paper = PhotoImage(width = width, height = height)
    canvas.create_image((width/2, height/2), image = paper, state = "normal")
    rgbString = ""
    rgbImage = img.convert('RGB')
    for i in range(0, height):
        tmpString = ""
        for k in range(0, width):
            r,g,b = rgbImage.getpixel((k,i))
            tmpString += "#%02x%02x%02x "% (r, g, b)
        rgbString += "{" + tmpString +"} "
    paper.put(rgbString)
    canvas.pack()


def func_open():
    global window, canvas, paper, photo, photo2, oriX, oriY
    readFp = askopenfilename(parent = window, filetypes = (("모든 그림 파일", "*.jpg;*.jpeg;*.bmp;*.png;*.tif;*.gif"),("모든 파일", "*.*")))
    photo = Image.open(readFp).convert('RGB')
    oriX = photo.width
    oriY = photo.height

    photo2 = photo.copy()
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)
    # pass

def func_save():
    global window, canvas, paper, photo, photo2, oriX, oriY

    if photo2 == None:
        return
    saveFp = asksaveasfile(parent = window, mode = "w", defaultextension = ".jpg", filetypes = (("JPG파일", "*.jpg;*.jpeg"),("모든파일", "*.*")))

    photo2.save(saveFp.name)

def func_exit():
    pass

def func_zoomin():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("확대", "확대할 배율을 입력하세요", minvalue = 2, maxvalue = 4)
    photo2 = photo.copy()
    photo2 = photo2.resize((int(oriX*scale), int(oriY*scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2,newX,newY)

def func_zoomout():
    global window, canvas, paper, photo, photo2, oriX, oriY
    scale = askinteger("확대", "확대할 배율을 입력하세요", minvalue=2, maxvalue=4)
    photo2 = photo.copy()
    photo2 = photo2.resize((int(oriX / scale), int(oriY / scale)))
    newX = photo2.width
    newY = photo2.height
    displayImage(photo2, newX, newY)

def func_mirror1():
    pass

def func_mirror2():
    pass

def func_rotate():
    pass

def func_bright():
    pass

def func_dark():
    pass

def func_blur():
    pass

def func_embo():
    pass

def func_bw():
    pass

window, canvas, paper = None, None, None
photo, photo2 = None, None
oriX, oriY = 0, 0

window = Tk()
window.geometry("250x250")
window.title("미니 포토샵")

mainMenu = Menu(window)
window.config(menu = mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label = "파일", menu = fileMenu)
fileMenu.add_command(label = "파일 열기", command = func_open)
fileMenu.add_command(label = "파일 저장", command = func_save)
fileMenu.add_separator()
fileMenu.add_command(label = "프로그램 종료", command = func_exit)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지 처리(1)", menu = image1Menu)
image1Menu.add_command(label = "확대", command = func_zoomin)
image1Menu.add_command(label = "축소", command = func_zoomout)
image1Menu.add_separator()
image1Menu.add_command(label = "상하반전", command = func_mirror1)
image1Menu.add_command(label = "좌우반전", command = func_mirror2)
image1Menu.add_command(label = "회전", command = func_rotate)

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label = "이미지처리(2)", menu = image2Menu)
image2Menu.add_command(label = "밝게", command = func_bright)
image2Menu.add_command(label = "어둡게", command = func_dark)
image2Menu.add_separator()
image2Menu.add_command(label = "블러링", command = func_blur)
image2Menu.add_command(label = "엠보싱", command = func_embo)
image2Menu.add_separator()
image2Menu.add_command(label = "흑백이미지", command = func_bw)
window.mainloop()