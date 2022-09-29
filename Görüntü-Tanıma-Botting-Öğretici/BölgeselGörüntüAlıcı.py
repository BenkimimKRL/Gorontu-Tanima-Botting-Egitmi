#Bu komut dosyası 660,350,600,400 bölgesinin görüntüsünü "C:\Users\KRL\Desktop\***\savedimage.png" yolunda saveimage.png olarak kaydeder
#Daha açık konuşma gerekirse örnegin (660,350,600,400) Bölgesindeki görüntüye veya bi bakımdan pencereye sadece işlem yapmak istiyorsun işte bu kodlama tam sana göre
#aşagıdaki(660,350,600,400))içindeki alan kodlarını degiştirerek test yapa bilirsiniz zaten direk görüntü bulundugu klasöre gelicektir

import pyautogui

im1 = pyautogui.screenshot(region=(660,350,600,400))
im1.save(r"./stickman.png")
