import pyautogui as pyg, time

a = int(input("Masukkan Berapa Banyak Pesan : "))
b = input("Masukkan Pesan : ")
c = 0

while c<=a:
    pyg.write(b)
    time.sleep(1)
    pyg.press("enter")
    
    c+=1