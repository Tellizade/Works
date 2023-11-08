# Veri seti dosyasının adını belirtin
dosya_adi = "veriseti.txt"

try:
    # Dosyayı okuma modunda açın ve satırları satirlar listesine okuyun
    with open(dosya_adi, 'r', encoding='utf-8') as dosya:
        satirlar = dosya.readlines()
except FileNotFoundError:
    # Dosya bulunamazsa hata mesajı verin ve çıkış yapın
    print(f"{dosya_adi} dosyası bulunamadı.")
    exit()

# Farklı kategorilere ait satırları saklamak için boş listeler oluşturun
benign_satirlar = []
phishing_satirlar = []
malware_satirlar = []
defacement_satirlar = []
artiklar_dosyasi = []

# Her satırı inceleyerek kategoriye göre ayırın
for satir in satirlar:
    satir = satir.strip()
    if satir.endswith("benign"):
        benign_satirlar.append(satir + '\n')
    elif satir.endswith("phishing"):
        phishing_satirlar.append(satir + '\n')
    elif satir.endswith("malware"):
        malware_satirlar.append(satir + '\n')
    elif satir.endswith("defacement"):
        defacement_satirlar.append(satir + '\n')
    else:
        artiklar_dosyasi.append(satir + '\n')

# 'benign' kategorisine ait satırlar varsa
if benign_satirlar:
    # 'benign_satirlar.txt' adında yeni bir dosya oluşturun ve bu satırları yazın
    with open("benign_satirlar.txt", 'w', encoding='utf-8') as benign_dosya:
        benign_dosya.writelines(benign_satirlar)
    # İşlem tamamlandığında bilgilendirici bir mesaj verin
    print("Cümle sonları 'benign' olan satırlar 'benign_satirlar.txt' dosyasına yazıldı.")
else:
    # 'benign' kategorisine ait satır bulunamazsa bilgilendirici bir mesaj verin
    print("Benign satır bulunamadı.")

# Aynı işlemi 'phishing', 'malware' ve 'defacement' kategorileri için yapın (aynı mantık)
# 'artiklar_dosyasi' listesi artık satırları içerir
# Her bir kategoriye uygun dosyaları oluşturun ve ilgili satırları yazın

if phishing_satirlar:
    with open("phishing_satirlari.txt", 'w', encoding='utf-8') as phishing_dosya:
        phishing_dosya.writelines(phishing_satirlar)
    print("Cümle sonları 'phishing' olan satırlar 'phishing_satirlari.txt' dosyasına yazıldı.")
else:
    print("Phishing satırı bulunamadı.")

if malware_satirlar:
    with open("malware_dosyasi.txt", 'w', encoding='utf-8') as malware_dosya:
        malware_dosya.writelines(malware_satirlar)
    print("Cümle sonları 'malware' olan satırlar 'malware_dosyasi.txt' dosyasına yazıldı.")
else:
    print("Malware satırı bulunamadı.")

if defacement_satirlar:
    with open("defacement_dosyasi.txt", 'w', encoding='utf-8') as defacement_dosya:
        defacement_dosya.writelines(defacement_satirlar)
    print("Cümle sonları 'defacement' olan satırlar 'defacement_dosyasi.txt' dosyasına yazıldı.")
else:
    print("Defacement satırı bulunamadı.")

# 'artiklar_dosyasi' listesi, bu kategorilere uymayan artık satırları içerir
# Bu satırları 'artiklar_dosyasi.txt' dosyasına yazın

if artiklar_dosyasi:
    with open("artiklar_dosyasi.txt", 'w', encoding='utf-8') as artiklar_dosya:
        artiklar_dosya.writelines(artiklar_dosyasi)
    print("Geride kalan satırlar 'artiklar_dosyasi.txt' dosyasına yazıldı.")
else:
    print("Artık satır bulunamadı.")
