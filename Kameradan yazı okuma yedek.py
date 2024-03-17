import cv2
import pytesseract

# Tesseract OCR'yi başlatma
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract' # Tesseract'in dizinini doğru şekilde belirtin

# Kamera başlatılıyor
cap = cv2.VideoCapture(0)

# Kamera çözünürlüğünü ayarlama (isteğe bağlı)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

# Fotoğraf çekme ve metin okuma fonksiyonu
def take_photo_and_read_text():
    # Kameradan bir kare al
    ret, frame = cap.read()

    # Görüntüyü siyah-beyaz yap
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Tesseract ile metni oku
    text = pytesseract.image_to_string(gray)

    # Metni ekrana yazdır
    print("Okunan Metin: ", text)

# Ana döngü
while True:
    # Kameradan görüntüyü al
    ret, frame = cap.read()

    # Görüntüyü ekrana göster
    cv2.imshow('Kamera', frame)

    # Klavyeden bir tuşa basıldığında
    key = cv2.waitKey(1)
    if key == ord('q'):  # 'q' tuşuna basıldığında çık
        break
    elif key == ord('c'):  # 'c' tuşuna basıldığında fotoğraf çek ve metni oku
        take_photo_and_read_text()

# Kamerayı kapat
cap.release()

# Pencereyi kapat
cv2.destroyAllWindows()
