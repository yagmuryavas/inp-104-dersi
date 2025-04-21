kelime = input("Bir sözcük girin: ")
if len(kelime) > 1:
    print(kelime[1:])
elif len(kelime) == 1:
    print("Sözcük sadece bir harf içeriyor, silindikten sonra boş kalıyor.")
else:
    print("Geçerli bir sözcük girmediniz.")