import cv2
import numpy as np

# Fungsi untuk mendeteksi warna dominan
def detect_dominant_color(frame):
    # Ubah frame menjadi format HSV (opsional, jika ingin lebih akurat)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Tentukan rentang warna (contoh: merah, hijau, biru)
    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])
    lower_green = np.array([36, 25, 25])
    upper_green = np.array([86, 255, 255])
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    # Buat mask untuk setiap warna
    mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)
    mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv_frame, lower_blue, upper_blue)

    # Hitung jumlah piksel untuk setiap warna
    red_pixels = cv2.countNonZero(mask_red)
    green_pixels = cv2.countNonZero(mask_green)
    blue_pixels = cv2.countNonZero(mask_blue)

    # Tentukan warna dominan
    colors = {
        "Red": red_pixels,
        "Green": green_pixels,
        "Blue": blue_pixels
    }
    dominant_color = max(colors, key=colors.get)

    return dominant_color

# Inisialisasi kamera
cap = cv2.VideoCapture(0)

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()
    if not ret:
        break

    # Deteksi warna dominan
    dominant_color = detect_dominant_color(frame)

    # Tampilkan hasil di layar
    cv2.putText(frame, f"Dominant Color: {dominant_color}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Tampilkan frame
    cv2.imshow("Color Detection", frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bebaskan kamera dan tutup semua jendela
cap.release()
cv2.destroyAllWindows()