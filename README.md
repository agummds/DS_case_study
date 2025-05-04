# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Maju
# Business Understanding
Perusahaan Jaya Jaya Maju menghadapi masalah tingginya tingkat keluarnya karyawan. Hal ini tentunya akan berimbas tingginya attrition rate (rasio jumlah karyawan yang keluar dengan total karyawan keseluruhan) hingga lebih dari 10%. Oleh karena itu, perlu dianalisis faktor-faktor yang mempengaruhi tingkat keluarnya karyawan untuk membantu departemen HR dalam mengurangi tingkat attrition.

# Permasalahan Bisnis
Perusahaan menghadapi masalah signifikan terkait attrition (tingkat keluar-masuk karyawan). Berdasarkan dataset hasil akhir, ada berbagai faktor internal yang berkaitan dengan keputusan karyawan untuk keluar, seperti:

- Jarak dari rumah ke kantor (DistanceFromHome)
- Frekuensi perjalanan bisnis (BusinessTravel)
- Kepuasan kerja (JobSatisfaction, EnvironmentSatisfaction)
- Jam kerja lembur (OverTime)
- Penghasilan bulanan (MonthlyIncome)
- Jumlah tahun bekerja dan promosi terakhir (YearsAtCompany, YearsSinceLastPromotion)

# Cakupan Proyek
- Mengumpulkan dan memproses data terkait karyawan.
- Menganalisis data untuk mengidentifikasi pola serta faktor-faktor yang memengaruhi keputusan karyawan.
- Membangun model prediktif menggunakan algoritma Decision Tree.
- Mengembangkan dashboard bisnis untuk memvisualisasikan temuan dan hasil prediksi.
- Menyusun rekomendasi tindakan strategis berdasarkan hasil analisis.

# Persiapan
Berikut adalah tahapan untuk menyiapkannya:

sumber data: https://github.com/dicodingacademy/dicoding_dataset/tree/main/employee

Di sini untuk melakukan proses saya sepenuhnya menggunakan Google Colab. Baru kemudian pada bagian visualisasi menggunakan Metadata menggunakan Docker.. Tapi jika ingin menjalankan proyek di local, dapat dilakukan dengan cara berikut:
1. Buka terminal di VSCODE.
2. Jalankan perintah berikut.
```
 conda create --name submissionds python==3.12.4
```
3. Jalankan perintah kedua
```
conda activate submissionds
```
4. Instal semua library yang dibutuhkan menggunakan perintah berikut.(KARENA SEMUA IBRARY ADA DI FILE "requirements.txt), MAKA
```
pip isntall -r requirements.txt
```
5. Jika ingin melakukan prediksi langsung, maka tinggal ke file predictive.py dan lihat apa hal yg ingin diubah dari parameter dalam Dataframe
6. Untuk menjalankan hasil, tinggal jalankan perintah
```
python predictive.py
```
# Business Dashboard
Dashboard bisnis dikembangkan untuk memvisualisasikan informasi terkait data karyawan, tingkat attrition, serta faktor-faktor utama yang berkontribusi pada tingginya angka keluar-masuk karyawan. Dashboard ini menyajikan berbagai aspek, termasuk faktor demografi dan penghasilan, aspek pekerjaan dan kepuasan, keseimbangan antara kerja dan kehidupan, serta elemen lain yang berperan dalam meningkatkan risiko attrition.

# Conculussion
Data menunjukkan bahwa karyawan yang keluar tersebar di berbagai rentang EmployeeID, dengan puncak attrition tertinggi berada di tengah kelompok karyawan. Selain itu, distribusi usia berdasarkan tingkat pendidikan memperlihatkan bahwa kelompok dengan tingkat pendidikan sedang (misalnya tingkat 3) menyumbang jumlah usia tertinggi, yang kemungkinan juga berkorelasi dengan kelompok umur muda yang lebih rentan keluar.

Faktor-faktor yang memengaruhi tingginya attrition mencakup distribusi demografis (usia dan pendidikan), posisi pekerjaan, tingkat penghasilan, keseimbangan kerja dan kehidupan, serta kenyamanan lingkungan kerja. Temuan ini menunjukkan bahwa strategi retensi perlu difokuskan tidak hanya pada satu kelompok, tetapi harus mempertimbangkan berbagai lapisan karyawan di seluruh organisasi.

# Rekomendasi Action Items
Berdasarkan hasil analisis visual data attrition pada dashboard, berikut adalah rekomendasi strategis yang dapat diambil perusahaan untuk mencapai target penurunan tingkat keluar masuknya karyawan (**attrition rate**).


## ✅ Rekomendasi Utama

### 1. Fokus pada Departemen dengan Attrition Tinggi
- Identifikasi akar masalah di departemen seperti **Customer Service** dan **Marketing**
- Implementasikan program retensi khusus per divisi
- Tetapkan target penurunan attrition per departemen

### 2. Perkuat Retensi Karyawan Baru (< 1 Tahun)
- Tingkatkan efektivitas program onboarding
- Terapkan sistem mentoring atau buddy system
- Evaluasi ulang proses rekrutmen awal

### 3. Tinjau Lokasi dengan Tingkat Turnover Tinggi
- Audit fasilitas dan kepuasan kerja per lokasi
- Lakukan rotasi/relokasi untuk mengurangi beban lokasi tertentu
- Perbaiki komunikasi antar lokasi dan kantor pusat

### 4. Optimalkan Peran Supervisor dan Middle Manager
- Berikan pelatihan leadership dan coaching
- Terapkan 360-degree feedback untuk supervisor
- Monitor hubungan manajemen langsung dengan tingkat resign

### 5. Intervensi Intensif untuk Job Level 1
- Tinjau kembali proses onboarding, pelatihan awal, dan ekspektasi kerja di level ini.
- Evaluasi apakah beban kerja, gaji, dan prospek karier sesuai.
- Terapkan program *early engagement* selama 3–6 bulan pertama kerja.

### 6. Retensi Gender-Sensitif
- Buat inisiatif dukungan kerja yang ramah gender seperti fleksibilitas kerja, cuti, dan layanan kesehatan tambahan.
- Lakukan *exit interview* untuk menggali alasan resign yang mungkin berbeda antara pria dan wanita.


# Email dan password Metabase
*Email*: root@mail.com 
*Password*: root123

