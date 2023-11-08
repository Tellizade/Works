# Metin dosyasının adını belirtin
metin_dosyasi_adi = "metin_dosyasi.txt"

try:
    # Metin dosyasını okuma modunda açın
    with open(metin_dosyasi_adi, 'r', encoding='utf-8') as dosya:
        satirlar = dosya.readlines()
except FileNotFoundError:
    # Dosya bulunamazsa hata mesajı verin ve çıkış yapın
    print(f"{metin_dosyasi_adi} dosyası bulunamadı.")
    exit()

# 'ornek' kelimesiyle biten satırları saklamak için bir liste oluşturun
ornek_satirlar = []

# Her satırı inceleyerek 'ornek' kelimesiyle bitenleri bulun
for satir in satirlar:
    satir = satir.strip()
    if satir.endswith("örnek"):
        # 'ornek' kelimesiyle biten satırları ornek_satirlar listesine ekleyin
        ornek_satirlar.append(satir + '\n')

# 'ornek' kelimesiyle biten satırlar bulunduysa
if ornek_satirlar:
    # 'örnek.txt' adında yeni bir dosya oluşturun ve 'ornek' satırlarını yazın
    with open("örnek.txt", 'w', encoding='utf-8') as ornek_dosya:
        ornek_dosya.writelines(ornek_satirlar)
    # İşlem tamamlandığında bilgilendirici bir mesaj verin
    print("Cümle sonları 'örnek' olan satırlar 'örnek.txt' dosyasına yazıldı.")
else:
    # 'ornek' kelimesiyle biten satır bulunamazsa bilgilendirici bir mesaj verin
    print("Örnek satırı bulunamadı.")
