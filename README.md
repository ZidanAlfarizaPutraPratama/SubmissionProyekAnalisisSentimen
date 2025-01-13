---

# Analisis Sentimen pada Ulasan Play Store

Proyek ini bertujuan untuk melakukan analisis sentimen pada ulasan aplikasi di Play Store dengan menggunakan teknik machine learning dan deep learning. Tiga percobaan pelatihan dilakukan dengan berbagai kombinasi algoritma, ekstraksi fitur, dan pembagian data untuk mengevaluasi akurasi model pada data uji.

## Langkah-langkah Utama

1. **Persiapan Data**: Dataset ulasan aplikasi yang sudah diambil dari proses scraping digunakan sebagai sumber data untuk analisis.
2. **Pelabelan Sentimen**: Ulasan diberi label berdasarkan rating yang diberikan (Rating 5 untuk sentimen positif, Rating 1 untuk sentimen negatif, dan Rating lainnya untuk sentimen netral).
3. **Tokenisasi dan Pembagian Data**: Teks ulasan di-tokenisasi dan data dibagi menjadi set pelatihan dan pengujian.
4. **Percobaan Pelatihan**: Tiga skema pelatihan diterapkan dengan menggunakan LSTM, Random Forest, dan SVM.
5. **Evaluasi**: Akurasi model dievaluasi pada data uji.

## Struktur Proyek

```
/playstore-sentiment-analysis
│
├── data/
│   └── playstore_reviews_indonesia.csv    # Dataset ulasan aplikasi
│
├── models/
│   ├── lstm_model.py                     # Kode model LSTM
│   ├── random_forest_model.py            # Kode model Random Forest
│   └── lstm_w2v_model.py                 # Kode model LSTM dengan Word2Vec
│
├── notebooks/
│   └── sentiment_analysis.ipynb          # Notebook utama yang berisi langkah-langkah analisis
│
├── scraping/
│   └── scraping.py                       # Script untuk scraping ulasan aplikasi dari Play Store
│
└── requirements.txt                      # Daftar dependensi yang diperlukan
```

## Instalasi

Untuk menjalankan proyek ini di lingkungan lokal Anda, pastikan Anda memiliki Python 3.x terinstal, lalu ikuti langkah-langkah berikut:

1. **Clone Repositori**
   ```bash
   git clone https://github.com/username/playstore-sentiment-analysis.git
   cd playstore-sentiment-analysis
   ```

2. **Instalasi Dependensi**
   Anda dapat menginstal semua dependensi yang diperlukan dengan menjalankan perintah berikut:
   ```bash
   pip install -r requirements.txt
   ```

3. **Unduh Dataset**
   Pastikan Anda memiliki dataset ulasan aplikasi `playstore_reviews_indonesia.csv` di folder `data/`. Anda dapat mengambilnya dengan scraping menggunakan script yang telah disediakan atau menggunakan dataset yang sudah ada.

### Menggunakan Script Scraping

Jika Anda ingin mengumpulkan data ulasan aplikasi secara langsung dari Play Store, Anda dapat menjalankan script `scraping/scraping.py`. Script ini akan mengunduh ulasan aplikasi yang ditentukan dan menyimpannya dalam format CSV. Berikut adalah langkah-langkah untuk menjalankannya:

1. **Menjalankan Script Scraping**
   Untuk menjalankan script `scraping.py`, pastikan Anda sudah menginstal semua dependensi terlebih dahulu, lalu jalankan script dengan perintah berikut:
   ```bash
   python scraping/scraping.py
   ```

2. **Menentukan Aplikasi untuk Scraping**
   Script ini memungkinkan Anda untuk menentukan ID aplikasi yang ingin Anda ambil ulasannya. Anda dapat menyesuaikan pengaturan atau menambahkan lebih banyak aplikasi untuk dikumpulkan.

## Langkah-langkah Analisis Sentimen

### Langkah 1: Persiapan Data
Dataset ulasan pengguna dimuat ke dalam DataFrame menggunakan `pandas`, dan ulasan diberi label sentimen berdasarkan rating.

### Langkah 2: Pelabelan Sentimen
Sentimen dari ulasan diberi label sebagai `positive`, `negative`, atau `neutral` berdasarkan rating yang diberikan (Rating 5 untuk positif, Rating 1 untuk negatif, dan rating lainnya untuk netral).

### Langkah 3: Tokenisasi dan Pembagian Data
Teks ulasan di-tokenisasi menjadi urutan angka menggunakan `Tokenizer` dari `keras`, dan data dibagi menjadi data latih dan data uji menggunakan `train_test_split` dari `sklearn`.

### Langkah 4: Percobaan 1 - LSTM dengan Tokenisasi dan Padding
Model pertama menggunakan LSTM (Long Short-Term Memory) untuk klasifikasi sentimen dengan tokenisasi dan padding. Model ini dilatih menggunakan data latih dan dievaluasi menggunakan data uji.

### Langkah 5: Percobaan 2 - Random Forest dengan TF-IDF
Model kedua menggunakan algoritma Random Forest untuk klasifikasi sentimen dengan ekstraksi fitur TF-IDF. Model ini dilatih pada data TF-IDF dan dievaluasi menggunakan data uji.

### Langkah 6: Percobaan 3 - LSTM dengan Word2Vec
Model ketiga menggunakan LSTM dengan representasi kata yang diperoleh dari Word2Vec untuk klasifikasi sentimen. Model ini dilatih pada vektor kata yang dihasilkan oleh Word2Vec dan dievaluasi menggunakan data uji.

## Evaluasi Model

Setiap model dievaluasi berdasarkan akurasi pada data uji. Berikut adalah hasil evaluasi dari tiga model yang digunakan:

- **LSTM dengan Tokenisasi dan Padding**: 100% akurasi
- **Random Forest dengan TF-IDF**: 100% akurasi
- **LSTM dengan Word2Vec**: 100% akurasi

Semua model memberikan hasil yang sangat baik dengan akurasi 100% pada data uji.

## Dependensi

Berikut adalah daftar dependensi yang digunakan dalam proyek ini:

- pandas
- numpy
- matplotlib
- scikit-learn
- tensorflow
- gensim

Untuk menginstal dependensi, jalankan perintah berikut:

```bash
pip install -r requirements.txt
```

## Kontribusi

Jika Anda tertarik untuk berkontribusi pada proyek ini, Anda dapat membuat **pull request** atau mengajukan **issue** jika menemukan masalah. Pastikan untuk mengikuti pedoman pengembangan yang baik dan menulis dokumentasi dengan jelas.

## Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).

---
