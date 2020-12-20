import cv2
import shutil
import os
from os import path
import tkinter as tk
from tkinter import messagebox


def ResizeWithAspectRatio(image, width=None, height=None,
                          inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]
    if h <= height and w <= width:
        return image
    if h > height:
        r = height / float(h)
        dim = (int(w * r), height)
        w = int(w*r)
        h = height
    if w > width:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)


def submit():
    path1 = path1_input.get()
    path2 = path2_input.get()
    width = width_input.get()
    height = height_input.get()
    index = int(index_input.get())
    print("Source exists:"+str(path.exists(path1)))
    print("Target exists:" + str(path.exists(path2)))
    if path.exists(path1) is False:
        messagebox.showerror("Error", "Bronfolder niet gevonden")
    elif path.exists(path2) is False:
        messagebox.showerror("Error", "Doelfolder niet gevonden")
    else:
        # window.destroy()
        ext2 = ".CR2"

        extlist = ["bmp", "dib", "jpeg", "jpg", "jp2", "jpe", "png",
                   "pbm", "pgm", "ppm", "sr", "ras", "tiff", "tif"]

        listing = os.listdir(path1)
        # index = 1286
        i = listing[index]
        while i:
            i = listing[index].lower()
            print("image:", i)
            print("index=", index)
            im_split = i.split(".")
            print("length im_split:", len(im_split))
            if len(im_split) == 2:
                im_name = im_split[0]
                im_ext = im_split[1]
                if im_ext in extlist:
                    image_name = im_name
                    im = cv2.imread(path1+"/"+i)
                    # resize = ResizeWithAspectRatio(im, width=1680, height=790)  # laptop
                    resize = ResizeWithAspectRatio(im, width=int(width), height=int(height))
                    # big screen
                    cv2.imshow('Afrika', resize)
                    k = cv2.waitKey(0)
                    print("k=", k)
                    if k == 115:
                        shutil.copyfile(path1+"/"+i, path2+"/"+i)
                        try:
                            shutil.copyfile(path1+"/"+image_name+ext2, path2+"/" +
                                            image_name+ext2)
                        except Exception as e:
                            print("no kemekl")
                    if k == 45:
                        index = index - 1
                        while len(listing[index].split(".")) != 2:
                            index -= 1
                        while listing[index].split(".")[1].lower() not in extlist:
                            index = index-1
                    if k == 27:         # wait for ESC key to exit
                        file = open(path2+"/test last index.txt", "a")
                        text = "last index for " + str(path1) + " = " + str(index) + "\n"
                        index_input.delete(0)
                        index_input.insert(0, str(index))
                        file.write(text)
                        file.close()
                        cv2.destroyAllWindows()
                        break
                    elif k != 45 and k != 115:
                        index += 1
                else:
                    index += 1
            else:
                index += 1


window = tk.Tk()
window.title("Selecteer foto's en copy/paste naar andere folder")
# window.geometry("600x400")
greeting = tk.Label(window, text="Hello there")
# greeting.pack()

path1_text = tk.Label(
    window, text="vul bronadres in van foto's  - (C:/Users/.../folder fotos)", font=('calibre', 10, 'bold'))
# path1_text.pack()
path1_input = tk.Entry(window)
path1_input.insert(0, "C:/Users/.../")
# path1_input.pack()


path2_text = tk.Label(window,
                      text="vul doeladres in voor selectie foto's  - (C:/Users/.../folder gekozen fotos)",
                      font=('calibre', 10, 'bold'))
path2_input = tk.Entry(window)
path2_input.insert(0, "C:/Users/.../")


width = tk.Label(window, text="max breedte foto:")
height = tk.Label(window, text="max hoogte foto:")
width_input = tk.Entry(window)
width_input.insert(0, "800")
height_input = tk.Entry(window)
height_input.insert(0, "600")
# width_input.pack()
# height_input.pack()
sub_btn = tk.Button(window, text='Submit', command=submit)
info_text1 = tk.Label(window, text=" Enter = volgende foto")
info_text2 = tk.Label(window, text=" - = vorige foto")
info_text3 = tk.Label(window, text=" s = bewaren in doelfolder")
info_text4 = tk.Label(window, text=" Esc = sluiten foto's")

index_text = tk.Label(window, text="Start bij foto:")
index_input = tk.Entry(window)
index_input.insert(0, "0")

path1_text.grid(sticky="W", row=0, column=0)
path1_input.grid(sticky="W", row=0, column=1)
path2_text.grid(sticky="W", row=1, column=0)
path2_input.grid(sticky="W", row=1, column=1)
width.grid(sticky="W", row=2, column=0)
width_input.grid(sticky="W", row=2, column=1)
height.grid(sticky="W", row=3, column=0)
height_input.grid(sticky="W", row=3, column=1)
index_text.grid(sticky="W", row=4, column=0)
index_input.grid(sticky="W", row=4, column=1)
sub_btn.grid(sticky="n", row=5, column=0)
info_text1.grid(sticky="n", row=6, column=0)
info_text2.grid(row=7, column=0)
info_text3.grid(row=8, column=0)
info_text4.grid(row=9, column=0)

window.mainloop()


# path1 = "C:/Users/Tim/Desktop/WhatsApp Images for replacement"
# # path1 = "C:/Users/Tim/SynologyDrive/Fotos/Tim Afrika 2"
# # path2 = "C:/Users/Tim/SynologyDrive/Fotos/Afrika selectie"
# path2 = "C:/Users/Tim/Desktop/testfolder"
# ext = ".jpg"
