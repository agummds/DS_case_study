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
1. **Perbaiki Program Retensi untuk Karyawan Muda dan Lajang**
Fokuskan program mentoring, jalur karir yang jelas, dan peluang belajar untuk karyawan muda yang cenderung keluar lebih cepat.

2. **Tinjau Ulang Struktur Gaji Pokok**
Meski ada penghasilan tambahan, gaji pokok yang rendah menjadi salah satu pemicu attrition. Lakukan benchmarking dan sesuaikan gaji pokok agar lebih kompetitif.

3. **Perbaiki Keseimbangan Kerja dan Kehidupan (Work-Life Balance)**
Identifikasi divisi dengan beban kerja berlebihan (misalnya yang sering lembur) dan terapkan kebijakan kerja fleksibel atau pengurangan jam lembur.

4. **Bangun Hubungan Atasan-Bawahan yang Lebih Sehat**
Selenggarakan pelatihan kepemimpinan untuk atasan agar menciptakan lingkungan kerja yang lebih mendukung, terutama karena ketidaknyamanan dengan atasan muncul sebagai faktor signifikan.

5. **Dorong Promosi dan Pengembangan Karir**
Karyawan yang jarang dipromosikan merasa kurang dihargai. Pastikan ada sistem penilaian performa yang adil dan jalur promosi yang transparan.

6. **Fokus pada Divisi Berisiko Tinggi**
Divisi seperti laboratorium teknisi, human resources, dan research scientist punya tingkat keluar tinggi. Selidiki lebih dalam penyebab spesifik di setiap divisi dan buat solusi yang disesuaikan.

7. **Perhatikan Latar Pendidikan Teknik dan Marketing**
Karena banyak attrition terjadi di kelompok ini, mungkin perlu peninjauan ulang terkait job fit, pelatihan tambahan, atau penyesuaian peran.

# Email dan password Metabase
*Email*: root@mail.com 
*Password*: root123

