import pyautogui
import keyboard
from tkinter import *

# black = (0, 0, 0)
# X = 330
# Y = 400
# imageexist = False

while True:
    keybind = input("please enter a keybind (just number or letter): ")
    if len(keybind) == 1:
        break
    else:
        pass

def updatewindow():
    # image = pygame.image.load('data.png')
    # display_surface.blit(image, (0, 0))
    # pygame.display.update()
    # if imageexist == True:
    #     img.close()
    img = PhotoImage(file="data.png")
    canvas.create_image(0, 0, anchor=NW, image=img)
    window.update()



im = pyautogui.screenshot(region=(795, 350, 330, 400))
im.save("data.png")
# time.sleep(1)

window = Tk()
window.title("Hypixel Skyblock easy ench xp")
canvas = Canvas(window, width = 330, height = 400)
canvas.pack()
img = PhotoImage(file="data.png")
canvas.create_image(0,0, anchor=NW, image=img)
window.update()
# pygame.init()
# display_surface = pygame.display.set_mode((X, Y), pygame.RESIZABLE)
# image = pygame.image.load('data.png')
# display_surface.fill(black)
# display_surface.blit(image, (0, 0))
# pygame.display.update()


while True:
    if keyboard.is_pressed(keybind):
        print('KEY pressed')
        im = pyautogui.screenshot(region=(795, 350, 330, 400))
        im.save("data.png")
        # time.sleep(1)
    updatewindow()











