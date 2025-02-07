Algoritma Deteksi Warna Dominan

1. Inisialisasi
Tujuan : Menyiapkan kamera dan lingkungan untuk pemrosesan gambar.
        Langkah-langkah :
        a. Aktifkan kamera menggunakan cv2.VideoCapture(0).
        b. Siapkan jendela untuk menampilkan hasil deteksi warna.

2. Pembacaan Frame
Tujuan : Mengambil frame dari kamera secara real-time.
        Langkah-langkah :
        a. Baca frame dari kamera menggunakan cap.read().
        b. Periksa apakah frame berhasil dibaca (ret).
        c. Jika frame tidak valid, hentikan proses.

3. Konversi Ruang Warna
Tujuan : Mengonversi frame dari ruang warna BGR (default OpenCV) ke HSV untuk mempermudah segmentasi warna.
        Langkah-langkah :
        a. Gunakan cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) untuk mengonversi frame ke ruang warna HSV.
        b. HSV lebih cocok untuk segmentasi warna karena komponen Hue (warna), Saturation (kecerahan), dan Value (intensitas) lebih intuitif daripada RGB.

4. Segmentasi Berbasis Warna
Tujuan : Membuat mask untuk setiap warna target (misalnya merah, hijau, biru) berdasarkan rentang nilai HSV.
        Langkah-langkah :
        a. Tentukan rentang warna untuk setiap warna target:
        Misalnya, untuk merah: lower_red = [0, 120, 70], upper_red = [10, 255, 255].
        Untuk hijau: lower_green = [36, 25, 25], upper_green = [86, 255, 255].
        Untuk biru: lower_blue = [100, 150, 0], upper_blue = [140, 255, 255].
        b. Buat mask untuk setiap warna menggunakan cv2.inRange(hsv_frame, lower_bound, upper_bound).
        Mask adalah citra biner (hitam-putih) yang menunjukkan area dengan warna tertentu.
        c. Hitung jumlah piksel non-zero di setiap mask menggunakan cv2.countNonZero(mask).

5. Penentuan Warna Dominan
Tujuan : Menentukan warna yang paling dominan berdasarkan jumlah piksel.
        Langkah-langkah :
        a. Bandingkan jumlah piksel untuk setiap warna:
        Misalnya, jika jumlah piksel merah > hijau dan merah > biru, maka warna dominan adalah merah.
        b. Gunakan struktur data seperti dictionary untuk menyimpan jumlah piksel per warna:
        python
        Copy
        1
        colors = {"Red": red_pixels, "Green": green_pixels, "Blue": blue_pixels}
        c. Temukan warna dengan jumlah piksel maksimum menggunakan max(colors, key=colors.get).

6. Tampilan Hasil
Tujuan : Menampilkan warna dominan pada layar.
        Langkah-langkah :
        a. Tambahkan teks yang menunjukkan warna dominan ke frame menggunakan cv2.putText().
        b. Tampilkan frame yang telah diperbarui menggunakan cv2.imshow().

7. Loop Real-Time
Tujuan : Memproses frame secara kontinu hingga pengguna memutuskan untuk keluar.
        Langkah-langkah :
        a. Ulangi langkah 2–6 untuk setiap frame yang dibaca dari kamera.
        b. Berikan opsi untuk keluar dari loop dengan menekan tombol 'q' (cv2.waitKey(1) & 0xFF == ord('q')).

8. Pembebasan Sumber Daya
Tujuan : Membersihkan sumber daya setelah aplikasi selesai.
        Langkah-langkah :
        a. Hentikan kamera menggunakan cap.release().
        b. Tutup semua jendela OpenCV menggunakan cv2.destroyAllWindows().
