# Search Engine dengan Machine Learning

## 🚀 Ringkasan Proyek

Ini adalah aplikasi search engine sederhana namun powerful yang dibangun menggunakan Python, Streamlit, dan scikit-learn. Aplikasi ini memungkinkan pengguna untuk melakukan pencarian semantik pada kumpulan data teks menggunakan vektorisasi TF-IDF dan kosinus similaritas.

## ✨ Fitur

- **Pencarian Berbasis Machine Learning**: Menggunakan vektorisasi TF-IDF untuk pencocokan dokumen yang cerdas
- **Antarmuka Web Interaktif**: Dibangun dengan Streamlit untuk interaksi pengguna yang mudah dan intuitif
- **Aplikasi Terdocker**: Mudah di-deploy di berbagai lingkungan
- **Hasil Pencarian yang Dapat Disesuaikan**: Mengembalikan 5 dokumen paling relevan dengan skor similaritas

## 🛠️ Teknologi yang Digunakan

- Python 3.9
- Streamlit
- scikit-learn
- Docker

## 📦 Struktur Proyek

```
├── app.py                  # Aplikasi web Streamlit
├── dataset
│   └── data.txt            # Kumpulan data teks untuk pencarian
├── Dockerfile              # Konfigurasi Docker
├── requirements.txt        # Dependensi Python
└── search_engine.py        # Implementasi inti search engine
```

## 🔧 Prasyarat

- Python 3.9+
- Docker (opsional)

## 💻 Instalasi Lokal

1. Clone repository
```bash
git clone <url-repository-anda>
cd search-engine-project
```

2. Install dependensi
```bash
pip install -r requirements.txt
```

3. Jalankan aplikasi
```bash
streamlit run app.py
```

## 🐳 Deploy dengan Docker

1. Bangun image Docker
```bash
docker build -t search-engine .
```

2. Jalankan kontainer Docker
```bash
docker run -p 8501:8501 search-engine
```

## 🔍 Cara Kerja

Search engine ini menggunakan teknik machine learning berikut:
- **Vektorisasi TF-IDF**: Mengubah dokumen teks menjadi vektor numerik
- **Kosinus Similaritas**: Menghitung relevansi dokumen terhadap kueri pencarian
- **Peringkat**: Mengembalikan 5 dokumen paling mirip dengan skor similaritasnya

### Proses Pencarian
1. Pengguna memasukkan kueri pencarian
2. Kueri divektorisasi menggunakan TF-IDF
3. Kosinus similaritas dihitung antara kueri dan dokumen
4. 5 dokumen paling relevan ditampilkan dengan skor similaritas
