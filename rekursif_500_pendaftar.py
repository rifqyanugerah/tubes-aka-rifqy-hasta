import time

class Pendaftar:
    def __init__(self, nama, jalur, jarak, nilai, prestasi_non_akademik, kurang_mampu):
        self.nama = nama
        self.jalur = jalur
        self.jarak = jarak
        self.nilai = nilai
        self.prestasi_non_akademik = prestasi_non_akademik
        self.kurang_mampu = kurang_mampu

# Fungsi sorting untuk setiap jalur
def sort_zonasi(a):
    return a.jarak

def sort_prestasi(a):
    return (-a.nilai, -a.prestasi_non_akademik)

def sort_afirmasi(a):
    return (-a.nilai, -a.kurang_mampu)

# Fungsi rekursif untuk mengelompokkan data berdasarkan jalur
def filter_by_jalur(pendaftar, jalur, result=None):
    if result is None:
        result = []
    if not pendaftar:
        return result
    if pendaftar[0].jalur == jalur:
        result.append(pendaftar[0])
    return filter_by_jalur(pendaftar[1:], jalur, result)

# Fungsi rekursif untuk sorting
def recursive_sort(data, sort_key):
    if len(data) <= 1:
        return data
    pivot = data[0]
    less = recursive_sort([x for x in data[1:] if sort_key(x) <= sort_key(pivot)], sort_key)
    greater = recursive_sort([x for x in data[1:] if sort_key(x) > sort_key(pivot)], sort_key)
    return less + [pivot] + greater

# Fungsi rekursif untuk memilih data berdasarkan kuota
def select_by_quota(data, quota, result=None):
    if result is None:
        result = []
    if not data or len(result) >= quota:
        return result
    result.append(data[0])
    return select_by_quota(data[1:], quota, result)

# Data pendaftar
pendaftar = [
    Pendaftar("Ali Mulya", "Zonasi", 1.2, 85, 0, False),
    Pendaftar("Budi Doremi", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Citra Widya", "Afirmasi", 0.0, 88, 0, True),
    Pendaftar("Dina Minggu", "Zonasi", 0.8, 84, 0, False),
    Pendaftar("Eka Cepat", "Prestasi", 0.0, 90, 2, False),
    Pendaftar("Fikri Maulana", "Afirmasi", 0.0, 80, 0, True),
    Pendaftar("Gilang Putra", "Zonasi", 1.5, 87, 1, False),
    Pendaftar("Hana Ramadhan", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Intan Sari", "Afirmasi", 0.0, 85, 1, True),
    Pendaftar("Joko Susanto", "Zonasi", 0.5, 80, 2, False),
    
    Pendaftar("Kina Pratiwi", "Prestasi", 0.0, 95, 5, False),
    Pendaftar("Lia Damayanti", "Afirmasi", 0.0, 87, 0, True),
    Pendaftar("Mia Anisa", "Zonasi", 1.0, 90, 0, False),
    Pendaftar("Nando Rinaldi", "Prestasi", 0.0, 91, 3, False),
    Pendaftar("Oka Wirawan", "Afirmasi", 0.0, 82, 0, True),
    Pendaftar("Putu Ayu", "Zonasi", 0.7, 89, 1, False),
    Pendaftar("Qila Dwi", "Prestasi", 0.0, 88, 2, False),
    Pendaftar("Rina Wulandari", "Afirmasi", 0.0, 85, 1, True),
    Pendaftar("Siti Rohmah", "Zonasi", 1.3, 86, 0, False),
    Pendaftar("Taufik Hidayat", "Zonasi", 1.0, 91, 0, False),
    
    Pendaftar("Umi Salamah", "Prestasi", 0.0, 90, 2, False),
    Pendaftar("Vera Kurnia", "Afirmasi", 0.0, 89, 1, True),
    Pendaftar("Wawan Santoso", "Zonasi", 0.6, 84, 1, False),
    Pendaftar("Xena Fitria", "Prestasi", 0.0, 93, 4, False),
    Pendaftar("Yana Wiryawan", "Afirmasi", 0.0, 81, 0, True),
    Pendaftar("Zahra Imani", "Zonasi", 0.9, 88, 0, False),
    Pendaftar("Ari Prasetyo", "Prestasi", 0.0, 91, 3, False),
    Pendaftar("Bunga Sari", "Afirmasi", 0.0, 84, 2, True),
    Pendaftar("Chandra Setiawan", "Zonasi", 1.1, 85, 1, False),
    Pendaftar("Hermanus Hasta", "Prestasi", 1.2, 87, 4, False),
    
    Pendaftar("Dewi Oktaviana", "Zonasi", 1.0, 87, 0, False),
    Pendaftar("Eka Putra", "Prestasi", 0.0, 89, 2, False),
    Pendaftar("Fahmi Ramadhan", "Afirmasi", 0.0, 90, 1, True),
    Pendaftar("Gita Dewi", "Zonasi", 0.4, 85, 3, False),
    Pendaftar("Hidayat Amran", "Prestasi", 0.0, 92, 5, False),
    Pendaftar("Intan Anjani", "Afirmasi", 0.0, 86, 0, True),
    Pendaftar("Julius Victor", "Zonasi", 1.3, 82, 1, False),
    Pendaftar("Kartik Suryo", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Lia Maharani", "Afirmasi", 0.0, 88, 2, True),
    Pendaftar("Maya Lestari", "Zonasi", 0.8, 89, 1, False),
    
    Pendaftar("Nina Wulandari", "Prestasi", 0.0, 91, 4, False),
    Pendaftar("Omar Husein", "Afirmasi", 0.0, 80, 0, True),
    Pendaftar("Puja Nandita", "Zonasi", 1.2, 85, 2, False),
    Pendaftar("Qori Wijaya", "Prestasi", 0.0, 87, 3, False),
    Pendaftar("Rama Yudha", "Afirmasi", 0.0, 92, 5, True),
    Pendaftar("Sari Wijayanti", "Zonasi", 0.7, 90, 1, False),
    Pendaftar("Tina Saputra", "Prestasi", 0.0, 93, 2, False),
    Pendaftar("Ujang Satria", "Afirmasi", 0.0, 84, 0, True),
    Pendaftar("Vina Karmila", "Zonasi", 1.0, 82, 1, False),
    Pendaftar("Wendi Nando", "Prestasi", 0.0, 86, 2, False),
    
    Pendaftar("Xenia Maria", "Afirmasi", 0.0, 83, 0, True),
    Pendaftar("Yusuf Hadi", "Zonasi", 0.5, 85, 2, False),
    Pendaftar("Zaki Pratama", "Prestasi", 0.0, 91, 3, False),
    Pendaftar("Alya Safira", "Afirmasi", 0.0, 89, 1, True),
    Pendaftar("Bima Santosa", "Zonasi", 1.1, 80, 0, False),
    Pendaftar("Citra Rahayu", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Dina Puspita", "Afirmasi", 0.0, 87, 1, True),
    Pendaftar("Endah Sukma", "Zonasi", 0.6, 84, 0, False),
    Pendaftar("Ferry Wijaya", "Prestasi", 0.0, 88, 2, False),
    Pendaftar("Gina Setiawan", "Afirmasi", 0.0, 85, 0, True),
    
    Pendaftar("Herry Prabowo", "Zonasi", 1.0, 89, 1, False),
    Pendaftar("Indra Kurnia", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Jaya Sukma", "Afirmasi", 0.0, 84, 0, True),
    Pendaftar("Kaisar Firdaus", "Zonasi", 0.9, 85, 2, False),
    Pendaftar("Lina Rachmawati", "Prestasi", 0.0, 91, 4, False),
    Pendaftar("Mokhammad Rizky", "Afirmasi", 0.0, 86, 1, True),
    Pendaftar("Nadya Lestari", "Zonasi", 0.7, 83, 0, False),
    Pendaftar("Omar Fadillah", "Prestasi", 0.0, 89, 2, False),
    Pendaftar("Putri Maheswari", "Afirmasi", 0.0, 82, 1, True),
    Pendaftar("Qistina Nur", "Zonasi", 1.0, 87, 1, False),
    
    Pendaftar("Rafiq Budi", "Prestasi", 0.0, 91, 3, False),
    Pendaftar("Siska Andriani", "Afirmasi", 0.0, 84, 0, True),
    Pendaftar("Tasya Rinaldi", "Zonasi", 0.8, 88, 2, False),
    Pendaftar("Umar Suryanto", "Prestasi", 0.0, 90, 5, False),
    Pendaftar("Vita Kusuma", "Afirmasi", 0.0, 86, 1, True),
    Pendaftar("Wahyu Setiawan", "Zonasi", 1.1, 89, 0, False),
    Pendaftar("Xandra Fajri", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Yuliati Rahma", "Afirmasi", 0.0, 85, 2, True),
    Pendaftar("Zahara Siti", "Zonasi", 0.9, 83, 1, False),
    Pendaftar("Sebastian Purba", "Prestasi", 0.7, 83, 2, True),
    
    Pendaftar("Nina Pratiwi", "Zonasi", 1.1, 84, 0, False),
    Pendaftar("Oki Wirawan", "Prestasi", 0.0, 93, 4, False),
    Pendaftar("Putri Anindya", "Afirmasi", 0.0, 85, 1, True),
    Pendaftar("Rizky Fahreza", "Zonasi", 0.6, 88, 2, False),
    Pendaftar("Sari Melati", "Prestasi", 0.0, 91, 3, False),
    Pendaftar("Taufik Hidayat", "Afirmasi", 0.0, 87, 1, True),
    Pendaftar("Umi Fatimah", "Zonasi", 0.9, 83, 0, False),
    Pendaftar("Vina Anggraini", "Prestasi", 0.0, 92, 5, False),
    Pendaftar("Wawan Setiawan", "Afirmasi", 0.0, 84, 0, True),
    Pendaftar("Xena Natalia", "Zonasi", 1.4, 86, 1, False),
    
    Pendaftar("Yoga Pratama", "Prestasi", 0.0, 89, 2, False),
    Pendaftar("Zahra Aulia", "Afirmasi", 0.0, 85, 1, True),
    Pendaftar("Andi Permana", "Zonasi", 1.2, 81, 0, False),
    Pendaftar("Bunga Lestari", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Cahyo Bintang", "Afirmasi", 0.0, 82, 0, True),
    Pendaftar("Dina Puspita", "Zonasi", 0.5, 87, 1, False),
    Pendaftar("Erwin Saputra", "Prestasi", 0.0, 88, 2, False),
    Pendaftar("Farah Amalia", "Afirmasi", 0.0, 89, 2, True),
    Pendaftar("Gilang Ramadhan", "Zonasi", 0.7, 85, 0, False),
    Pendaftar("Hani Novita", "Prestasi", 0.0, 91, 4, False),
    
    #---------------- 100 ------------------------
    
    Pendaftar("Nina Pratiwi", "Zonasi", 1.1, 84, 0, False),
    Pendaftar("Oki Wirawan", "Prestasi", 0.0, 93, 4, True), 
    Pendaftar("Hani Novita", "Prestasi", 0.0, 91, 4, False),
    Pendaftar("Budi Santoso", "Zonasi", 2.0, 80, 0, True),
    Pendaftar("Siti Aminah", "Afirmasi", 0.0, 85, 2, False),
    Pendaftar("Rina Sari", "Zonasi", 1.5, 78, 0, False),
    Pendaftar("Adi Pratama", "Prestasi", 0.0, 95, 3, True),
    Pendaftar("Lina Kusuma", "Zonasi", 1.3, 82, 0, False),
    Pendaftar("Yusuf Hadi", "Afirmasi", 0.0, 88, 1, True),
    Pendaftar("Tari Putri", "Prestasi", 0.0, 90, 4, False),
    
    Pendaftar("Dian Rahma", "Zonasi", 2.0, 79, 0, True),
    Pendaftar("Rizky Agung", "Afirmasi", 0.0, 84, 2, False),
    Pendaftar("Rani Wulandari", "Prestasi", 0.0, 92, 3, True),
    Pendaftar("Benny Kurniawan", "Zonasi", 1.7, 81, 0, False),
    Pendaftar("Ayu Permata", "Prestasi", 0.0, 94, 4, True),
    Pendaftar("Farhan Hakim", "Zonasi", 1.4, 83, 0, False),
    Pendaftar("Citra Dewi", "Afirmasi", 0.0, 86, 1, True),
    Pendaftar("Hendra Prasetyo", "Prestasi", 0.0, 89, 3, False),
    Pendaftar("Winda Lestari", "Zonasi", 1.2, 80, 0, False),
    Pendaftar("Eka Susanti", "Prestasi", 0.0, 91, 4, True),
    
    Pendaftar("Fajar Ahmad", "Zonasi", 1.8, 85, 0, True),
    Pendaftar("Ika Rahayu", "Afirmasi", 0.0, 83, 2, False),
    Pendaftar("Agus Wijaya", "Prestasi", 0.0, 92, 3, True),
    Pendaftar("Reni Aprilia", "Zonasi", 1.1, 79, 0, False),
    Pendaftar("Dedi Firmansyah", "Prestasi", 0.0, 93, 4, True),
    Pendaftar("Sari Utami", "Zonasi", 1.5, 82, 0, False),
    Pendaftar("Andi Purnomo", "Afirmasi", 0.0, 87, 1, True),
    Pendaftar("Lestari Indah", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Rio Saputra", "Zonasi", 2.0, 84, 0, True),
    Pendaftar("Tina Melati", "Prestasi", 0.0, 95, 4, False),
    
    Pendaftar("Dina Rosalina", "Zonasi", 1.3, 81, 0, False),
    Pendaftar("Bayu Ramadhan", "Prestasi", 0.0, 92, 3, True),
    Pendaftar("Lia Kartika", "Zonasi", 1.6, 80, 0, False),
    Pendaftar("Joni Saputra", "Afirmasi", 0.0, 85, 2, True),
    Pendaftar("Siti Nurhaliza", "Prestasi", 0.0, 94, 4, False),
    Pendaftar("Denny Ardian", "Zonasi", 1.7, 83, 0, True),
    Pendaftar("Rika Amalia", "Prestasi", 0.0, 91, 3, False),
    Pendaftar("Ahmad Fauzan", "Afirmasi", 0.0, 88, 1, True),
    Pendaftar("Nina Kartini", "Zonasi", 1.4, 79, 0, False),
    Pendaftar("Indra Kusuma", "Prestasi", 0.0, 93, 4, True),
    
    Pendaftar("Putri Anggraini", "Zonasi", 1.5, 84, 0, False),
    Pendaftar("Vina Safitri", "Prestasi", 0.0, 90, 3, True),
    Pendaftar("Dewa Wijaya", "Zonasi", 1.1, 81, 0, False),
    Pendaftar("Dara Melani", "Prestasi", 0.0, 92, 4, True),
    Pendaftar("Heri Ramadhan", "Zonasi", 1.3, 80, 0, False),
    Pendaftar("Nisa Ayu", "Afirmasi", 0.0, 86, 2, True),
    Pendaftar("Arif Setiawan", "Prestasi", 0.0, 95, 3, False),
    Pendaftar("Sandy Maulana", "Zonasi", 1.6, 83, 0, False),
    Pendaftar("Mega Lestari", "Prestasi", 0.0, 91, 4, True),
    Pendaftar("Mila Kusuma", "Zonasi", 2.0, 84, 0, True),
    
    Pendaftar("Rudi Hidayat", "Afirmasi", 0.0, 87, 1, False),
    Pendaftar("Dewi Puspita", "Prestasi", 0.0, 94, 3, True),
    Pendaftar("Rizal Hakim", "Zonasi", 1.8, 82, 0, False),
    Pendaftar("Yulianti Sari", "Prestasi", 0.0, 92, 4, True),
    Pendaftar("Bayu Herlambang", "Zonasi", 1.7, 80, 0, False),
    Pendaftar("Maya Sari", "Afirmasi", 0.0, 85, 2, True),
    Pendaftar("Hana Putri", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Adi Saputra", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Fitri Aprilia", "Prestasi", 0.0, 93, 4, False),
    Pendaftar("Muhammad Arif", "Zonasi", 0.3, 83, 3, False),
    
    Pendaftar("Gita Prameswari", "Zonasi", 1.3, 82, 0, False),
    Pendaftar("Niko Pratama", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Santi Wulandari", "Zonasi", 1.7, 84, 0, True),
    Pendaftar("Arman Hakim", "Afirmasi", 0.0, 87, 2, False),
    Pendaftar("Dewi Kartika", "Prestasi", 0.0, 94, 4, True),
    Pendaftar("Rian Agung", "Zonasi", 1.2, 79, 0, False),
    Pendaftar("Bima Prasetyo", "Prestasi", 0.0, 92, 3, True),
    Pendaftar("Karin Melati", "Zonasi", 1.5, 80, 0, False),
    Pendaftar("Farah Ayu", "Afirmasi", 0.0, 86, 1, True),
    Pendaftar("Joko Susanto", "Prestasi", 0.0, 93, 4, False),
    
    Pendaftar("Vika Ramadhani", "Zonasi", 1.6, 83, 0, True),
    Pendaftar("Dian Puspitasari", "Prestasi", 0.0, 91, 3, False),
    Pendaftar("Satria Hidayat", "Zonasi", 1.8, 82, 0, True),
    Pendaftar("Meli Kartini", "Afirmasi", 0.0, 85, 2, False),
    Pendaftar("Andri Putra", "Prestasi", 0.0, 90, 4, True),
    Pendaftar("Nindy Amelia", "Zonasi", 1.4, 80, 0, False),
    Pendaftar("Zaki Ramadhan", "Prestasi", 0.0, 94, 3, True),
    Pendaftar("Tari Melani", "Zonasi", 1.3, 81, 0, False),
    Pendaftar("Hana Kusuma", "Prestasi", 0.0, 92, 4, True),
    Pendaftar("Bagas Santoso", "Zonasi", 1.1, 79, 0, False),
    
    Pendaftar("Reza Pratama", "Afirmasi", 0.0, 87, 1, True),
    Pendaftar("Siti Lestari", "Prestasi", 0.0, 93, 3, False),
    Pendaftar("Ahmad Ramli", "Zonasi", 1.7, 84, 0, True),
    Pendaftar("Rika Sari", "Prestasi", 0.0, 91, 4, False),
    Pendaftar("Dina Safitri", "Zonasi", 1.5, 80, 0, False),
    Pendaftar("Benny Ardian", "Prestasi", 0.0, 94, 3, True),
    Pendaftar("Putri Ayuningtyas", "Afirmasi", 0.0, 85, 2, False),
    Pendaftar("Arif Nugroho", "Zonasi", 1.3, 83, 0, True),
    Pendaftar("Indah Wati", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Citra Melati", "Zonasi", 1.4, 81, 0, False),
    
    Pendaftar("Fajar Ramadhan", "Prestasi", 0.0, 95, 3, True),
    Pendaftar("Lina Permata", "Afirmasi", 0.0, 87, 1, False),
    Pendaftar("Heri Purnomo", "Prestasi", 0.0, 93, 4, True),
    Pendaftar("Rani Hidayah", "Zonasi", 1.5, 80, 0, False),
    Pendaftar("Rudi Santoso", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Vina Putri", "Zonasi", 1.6, 84, 0, True),
    Pendaftar("Adi Firmansyah", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Mega Aprilia", "Afirmasi", 0.0, 85, 2, True),
    Pendaftar("Dwi Kusuma", "Prestasi", 0.0, 94, 3, False),
    Pendaftar("Bayu Hakim", "Zonasi", 1.3, 81, 0, True),
    
    #---------------- 200 ------------------------
    
    Pendaftar("Ali Pratama", "Zonasi", 1.1, 85, 0, False),
    Pendaftar("Budi Santoso", "Prestasi", 0.0, 92, 3, True),
    Pendaftar("Citra Dewi", "Afirmasi", 0.0, 88, 2, False),
    Pendaftar("Dian Putri", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Eka Susanto", "Prestasi", 0.0, 94, 4, False),
    Pendaftar("Fajar Rahman", "Zonasi", 1.3, 80, 0, True),
    Pendaftar("Gita Puspita", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Hadi Wibowo", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Indah Lestari", "Zonasi", 1.4, 82, 0, False),
    Pendaftar("Joko Hidayat", "Prestasi", 0.0, 93, 4, True),
    
    Pendaftar("Karin Permata", "Zonasi", 1.6, 81, 0, False),
    Pendaftar("Lina Pratiwi", "Prestasi", 0.0, 95, 3, True),
    Pendaftar("Maya Kusuma", "Afirmasi", 0.0, 87, 2, False),
    Pendaftar("Niko Ramadhan", "Zonasi", 1.2, 79, 0, True),
    Pendaftar("Oki Prasetyo", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Putri Melati", "Zonasi", 1.5, 84, 0, True),
    Pendaftar("Qori Hadi", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Rina Wulandari", "Zonasi", 1.8, 83, 0, True),
    Pendaftar("Sari Dewi", "Afirmasi", 0.0, 85, 2, False),
    Pendaftar("Tari Sari", "Prestasi", 0.0, 94, 4, True),
    
    Pendaftar("Umar Hakim", "Zonasi", 1.3, 81, 0, False),
    Pendaftar("Vina Lestari", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Winda Safitri", "Zonasi", 1.6, 80, 0, False),
    Pendaftar("Xena Aprilia", "Prestasi", 0.0, 93, 4, True),
    Pendaftar("Yusuf Santoso", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Zaki Pratama", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Adi Firmansyah", "Prestasi", 0.0, 92, 3, False),
    Pendaftar("Bayu Nugraha", "Zonasi", 1.4, 84, 0, True),
    Pendaftar("Cici Amelia", "Prestasi", 0.0, 90, 4, False),
    Pendaftar("Dewa Wijaya", "Zonasi", 1.7, 79, 0, True),
    
    Pendaftar("Ely Susanti", "Prestasi", 0.0, 94, 3, False),
    Pendaftar("Farhan Kusuma", "Afirmasi", 0.0, 85, 2, True),
    Pendaftar("Gina Ramadhani", "Prestasi", 0.0, 91, 4, False),
    Pendaftar("Hendra Purnomo", "Zonasi", 1.2, 80, 0, True),
    Pendaftar("Ika Permata", "Prestasi", 0.0, 93, 3, False),
    Pendaftar("Joni Lestari", "Zonasi", 1.6, 82, 0, True),
    Pendaftar("Kiki Pratami", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Lala Sari", "Afirmasi", 0.0, 88, 1, True),
    Pendaftar("Meli Anggraini", "Zonasi", 1.5, 84, 0, False),
    Pendaftar("Nina Kusuma", "Prestasi", 0.0, 95, 3, True),
    
    Pendaftar("Oka Wibawa", "Zonasi", 1.7, 81, 0, False),
    Pendaftar("Putra Wijaya", "Prestasi", 0.0, 91, 4, True),
    Pendaftar("Qila Sari", "Zonasi", 1.3, 83, 0, False),
    Pendaftar("Rama Hakim", "Afirmasi", 0.0, 86, 2, True),
    Pendaftar("Sinta Wulandari", "Prestasi", 0.0, 94, 3, False),
    Pendaftar("Tono Saputra", "Zonasi", 1.5, 80, 0, True),
    Pendaftar("Umi Hidayah", "Prestasi", 0.0, 93, 4, False),
    Pendaftar("Vita Ramadhani", "Zonasi", 1.4, 82, 0, True),
    Pendaftar("Wulan Indah", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Yogi Kusuma", "Zonasi", 1.8, 83, 0, True),
    
    Pendaftar("Zahra Permata", "Afirmasi", 0.0, 85, 2, False),
    Pendaftar("Aditya Pratama", "Zonasi", 1.1, 85, 0, False),
    Pendaftar("Bella Santika", "Prestasi", 0.0, 92, 3, True),
    Pendaftar("Cindy Amelia", "Afirmasi", 0.0, 88, 2, False),
    Pendaftar("Dina Pertiwi", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Eko Santoso", "Prestasi", 0.0, 94, 4, False),
    Pendaftar("Faisal Hakim", "Zonasi", 1.3, 80, 0, True),
    Pendaftar("Gilang Wibowo", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Hana Sari", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Indra Ramadhan", "Zonasi", 1.4, 82, 0, False),
    
    Pendaftar("Jamil Hidayat", "Prestasi", 0.0, 93, 4, True),
    Pendaftar("Karina Permata", "Zonasi", 1.6, 81, 0, False),
    Pendaftar("Lutfi Ramli", "Prestasi", 0.0, 95, 3, True),
    Pendaftar("Maya Pratiwi", "Afirmasi", 0.0, 87, 2, False),
    Pendaftar("Nando Santoso", "Zonasi", 1.2, 79, 0, True),
    Pendaftar("Omar Saputra", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Putri Anggraini", "Zonasi", 1.5, 84, 0, True),
    Pendaftar("Qomar Hadi", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Rani Puspita", "Zonasi", 1.8, 83, 0, True),
    Pendaftar("Sandi Permadi", "Afirmasi", 0.0, 85, 2, False),
    
    Pendaftar("Tika Melati", "Prestasi", 0.0, 94, 4, True),
    Pendaftar("Udin Ramli", "Zonasi", 1.3, 81, 0, False),
    Pendaftar("Vera Hidayah", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Widi Safitri", "Zonasi", 1.6, 80, 0, False),
    Pendaftar("Xaverio Santoso", "Prestasi", 0.0, 93, 4, True),
    Pendaftar("Yana Kartini", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Zulfan Pratama", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Ahmad Fajar", "Prestasi", 0.0, 92, 3, False),
    Pendaftar("Bagas Wibawa", "Zonasi", 1.4, 84, 0, True),
    Pendaftar("Cindy Pramesti", "Prestasi", 0.0, 90, 4, False),
    
    Pendaftar("Dio Nugraha", "Zonasi", 1.7, 79, 0, True),
    Pendaftar("Elya Sari", "Prestasi", 0.0, 94, 3, False),
    Pendaftar("Fauzan Pratama", "Afirmasi", 0.0, 85, 2, True),
    Pendaftar("Gina Anggraini", "Prestasi", 0.0, 91, 4, False),
    Pendaftar("Hendra Wijaya", "Zonasi", 1.2, 80, 0, True),
    Pendaftar("Ika Ramadhani", "Prestasi", 0.0, 93, 3, False),
    Pendaftar("Joko Permadi", "Zonasi", 1.6, 82, 0, True),
    Pendaftar("Kiki Sari", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Lala Kartini", "Afirmasi", 0.0, 88, 1, True),
    Pendaftar("Meli Pratiwi", "Zonasi", 1.5, 84, 0, False),
    
    Pendaftar("Nina Wijaya", "Prestasi", 0.0, 95, 3, True),
    Pendaftar("Oka Ramli", "Zonasi", 1.7, 81, 0, False),
    Pendaftar("Putra Kusuma", "Prestasi", 0.0, 91, 4, True),
    Pendaftar("Qila Dewi", "Zonasi", 1.3, 83, 0, False),
    Pendaftar("Rama Nugroho", "Afirmasi", 0.0, 86, 2, True),
    Pendaftar("Sinta Kartika", "Prestasi", 0.0, 94, 3, False),
    Pendaftar("Tono Ramadhan", "Zonasi", 1.5, 80, 0, True),
    Pendaftar("Umi Sari", "Prestasi", 0.0, 93, 4, False),
    Pendaftar("Vita Anggraini", "Zonasi", 1.4, 82, 0, True),
    Pendaftar("Wulan Kusuma", "Prestasi", 0.0, 90, 3, False),
    
    #---------------- 300 ------------------------
    Pendaftar("Aldi Pratama", "Zonasi", 1.1, 85, 0, False),
    Pendaftar("Bela Anggraini", "Prestasi", 0.0, 92, 3, True),
    Pendaftar("Citra Permata", "Afirmasi", 0.0, 88, 2, False),
    Pendaftar("Deni Saputra", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Eka Wijaya", "Prestasi", 0.0, 94, 4, False),
    Pendaftar("Fauzan Hakim", "Zonasi", 1.3, 80, 0, True),
    Pendaftar("Gita Melati", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Hana Lestari", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Indra Ramli", "Zonasi", 1.4, 82, 0, False),
    Pendaftar("Jamal Hidayat", "Prestasi", 0.0, 93, 4, True),
    
    Pendaftar("Karina Pertiwi", "Zonasi", 1.6, 81, 0, False),
    Pendaftar("Lutfi Ramadhan", "Prestasi", 0.0, 95, 3, True),
    Pendaftar("Maya Kusuma", "Afirmasi", 0.0, 87, 2, False),
    Pendaftar("Nando Wibowo", "Zonasi", 1.2, 79, 0, True),
    Pendaftar("Oki Saputra", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Putri Puspita", "Zonasi", 1.5, 84, 0, True),
    Pendaftar("Qomar Hakim", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Rani Permata", "Zonasi", 1.8, 83, 0, True),
    Pendaftar("Sandi Kartika", "Afirmasi", 0.0, 85, 2, False),
    Pendaftar("Tika Melani", "Prestasi", 0.0, 94, 4, True),
    
    Pendaftar("Udin Ramadhan", "Zonasi", 1.3, 81, 0, False),
    Pendaftar("Vera Anggraeni", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Widi Kartika", "Zonasi", 1.6, 80, 0, False),
    Pendaftar("Xander Pratama", "Prestasi", 0.0, 93, 4, True),
    Pendaftar("Yana Puspita", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Zulfan Hakim", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Ahmad Wibowo", "Prestasi", 0.0, 92, 3, False),
    Pendaftar("Bagas Nugraha", "Zonasi", 1.4, 84, 0, True),
    Pendaftar("Cindy Amelia", "Prestasi", 0.0, 90, 4, False),
    Pendaftar("Dio Santoso", "Zonasi", 1.7, 79, 0, True),
    
    Pendaftar("Elya Kartini", "Prestasi", 0.0, 94, 3, False),
    Pendaftar("Farhan Pratama", "Afirmasi", 0.0, 85, 2, True),
    Pendaftar("Gina Wulandari", "Prestasi", 0.0, 91, 4, False),
    Pendaftar("Hendra Wijaya", "Zonasi", 1.2, 80, 0, True),
    Pendaftar("Ika Ramadhani", "Prestasi", 0.0, 93, 3, False),
    Pendaftar("Joko Permadi", "Zonasi", 1.6, 82, 0, True),
    Pendaftar("Kiki Anggraini", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Lala Pratama", "Afirmasi", 0.0, 88, 1, True),
    Pendaftar("Meli Kartika", "Zonasi", 1.5, 84, 0, False),
    Pendaftar("Nina Wijaya", "Prestasi", 0.0, 95, 3, True),
    
    Pendaftar("Oka Ramli", "Zonasi", 1.7, 81, 0, False),
    Pendaftar("Putra Santoso", "Prestasi", 0.0, 91, 4, True),
    Pendaftar("Qila Dewi", "Zonasi", 1.3, 83, 0, False),
    Pendaftar("Rama Nugroho", "Afirmasi", 0.0, 86, 2, True),
    Pendaftar("Sinta Ramadhan", "Prestasi", 0.0, 94, 3, False),
    Pendaftar("Tono Prasetyo", "Zonasi", 1.5, 80, 0, True),
    Pendaftar("Umi Pratiwi", "Prestasi", 0.0, 93, 4, False),
    Pendaftar("Vita Anggraini", "Zonasi", 1.4, 82, 0, True),
    Pendaftar("Wulan Kusuma", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Yogi Ramadhan", "Zonasi", 1.8, 83, 0, True),
    
    Pendaftar("Adit Pratama", "Zonasi", 1.1, 85, 0, False),
    Pendaftar("Beni Santoso", "Prestasi", 0.0, 92, 3, True),
    Pendaftar("Cindy Permata", "Afirmasi", 0.0, 88, 2, False),
    Pendaftar("Dewi Kusuma", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Eko Ramadhan", "Prestasi", 0.0, 94, 4, False),
    Pendaftar("Fajar Wibowo", "Zonasi", 1.3, 80, 0, True),
    Pendaftar("Gina Puspita", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Hana Lestari", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Indra Wijaya", "Zonasi", 1.4, 82, 0, False),
    Pendaftar("Joni Hidayat", "Prestasi", 0.0, 93, 4, True),
    
    Pendaftar("Lutfi Saputra", "Prestasi", 0.0, 95, 3, True),
    Pendaftar("Maya Pratiwi", "Afirmasi", 0.0, 87, 2, False),
    Pendaftar("Nando Ramli", "Zonasi", 1.2, 79, 0, True),
    Pendaftar("Oki Hidayah", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Putri Anggraini", "Zonasi", 1.5, 84, 0, True),
    Pendaftar("Qomar Wibawa", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Rani Melati", "Zonasi", 1.8, 83, 0, True),
    Pendaftar("Sari Puspita", "Afirmasi", 0.0, 85, 2, False),
    Pendaftar("Tika Ramadhan", "Prestasi", 0.0, 94, 4, True),
    Pendaftar("Udin Prasetyo", "Zonasi", 1.3, 81, 0, False),
    
    Pendaftar("Vera Kartini", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Widi Santoso", "Zonasi", 1.6, 80, 0, False),
    Pendaftar("Xena Pratama", "Prestasi", 0.0, 93, 4, True),
    Pendaftar("Yana Kusuma", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Zulfan Hakim", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Adi Nugraha", "Prestasi", 0.0, 92, 3, False),
    Pendaftar("Bagus Wibawa", "Zonasi", 1.4, 84, 0, True),
    Pendaftar("Cici Anggraini", "Prestasi", 0.0, 90, 4, False),
    Pendaftar("Dio Ramadhan", "Zonasi", 1.7, 79, 0, True),
    Pendaftar("Elya Amelia", "Prestasi", 0.0, 94, 3, False),
    
    Pendaftar("Farhan Pratama", "Afirmasi", 0.0, 85, 2, True),
    Pendaftar("Gina Wulandari", "Prestasi", 0.0, 91, 4, False),
    Pendaftar("Hendra Wijaya", "Zonasi", 1.2, 80, 0, True),
    Pendaftar("Ika Melati", "Prestasi", 0.0, 93, 3, False),
    Pendaftar("Joko Ramli", "Zonasi", 1.6, 82, 0, True),
    Pendaftar("Kiki Pratama", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Lala Anggraini", "Afirmasi", 0.0, 88, 1, True),
    Pendaftar("Meli Kusuma", "Zonasi", 1.5, 84, 0, False),
    Pendaftar("Nina Wijaya", "Prestasi", 0.0, 95, 3, True),
    Pendaftar("Oka Ramadhan", "Zonasi", 1.7, 81, 0, False),
    
    Pendaftar("Putra Anggraini", "Prestasi", 0.0, 91, 4, True),
    Pendaftar("Qila Puspita", "Zonasi", 1.3, 83, 0, False),
    Pendaftar("Rama Hakim", "Afirmasi", 0.0, 86, 2, True),
    Pendaftar("Sinta Kartini", "Prestasi", 0.0, 94, 3, False),
    Pendaftar("Tono Wijaya", "Zonasi", 1.5, 80, 0, True),
    Pendaftar("Umi Kusuma", "Prestasi", 0.0, 93, 4, False),
    Pendaftar("Vita Anggraini", "Zonasi", 1.4, 82, 0, True),
    Pendaftar("Wulan Permata", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Yogi Ramli", "Zonasi", 1.8, 83, 0, True),
    Pendaftar("Zahra Hidayah", "Afirmasi", 0.0, 85, 2, False),

    #---------------- 400 ------------------------
    Pendaftar("Adit Saputra", "Zonasi", 1.1, 85, 0, False),
    Pendaftar("Bella Kartini", "Prestasi", 0.0, 92, 3, True),
    Pendaftar("Cindy Ramadhan", "Afirmasi", 0.0, 88, 2, False),
    Pendaftar("Dewi Kusuma", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Eko Wijaya", "Prestasi", 0.0, 94, 4, False),
    Pendaftar("Fajar Hakim", "Zonasi", 1.3, 80, 0, True),
    Pendaftar("Gita Permata", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Hana Lestari", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Indra Ramli", "Zonasi", 1.4, 82, 0, False),
    Pendaftar("Joni Hidayat", "Prestasi", 0.0, 93, 4, True),
    
    Pendaftar("Karina Sari", "Zonasi", 1.6, 81, 0, False),
    Pendaftar("Lutfi Ramadhan", "Prestasi", 0.0, 95, 3, True),
    Pendaftar("Maya Pratiwi", "Afirmasi", 0.0, 87, 2, False),
    Pendaftar("Nando Wibowo", "Zonasi", 1.2, 79, 0, True),
    Pendaftar("Oki Anggraini", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Putri Amelia", "Zonasi", 1.5, 84, 0, True),
    Pendaftar("Qomar Santoso", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Rani Puspita", "Zonasi", 1.8, 83, 0, True),
    Pendaftar("Sandi Ramli", "Afirmasi", 0.0, 85, 2, False),
    Pendaftar("Tika Melani", "Prestasi", 0.0, 94, 4, True),
    
    Pendaftar("Udin Pratama", "Zonasi", 1.3, 81, 0, False),
    Pendaftar("Vera Anggraini", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Widi Kusuma", "Zonasi", 1.6, 80, 0, False),
    Pendaftar("Xander Wibowo", "Prestasi", 0.0, 93, 4, True),
    Pendaftar("Yana Kartini", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Zulfan Hakim", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Adi Nugraha", "Prestasi", 0.0, 92, 3, False),
    Pendaftar("Bagus Wibawa", "Zonasi", 1.4, 84, 0, True),
    Pendaftar("Cici Amelia", "Prestasi", 0.0, 90, 4, False),
    Pendaftar("Dio Santoso", "Zonasi", 1.7, 79, 0, True),
    
    Pendaftar("Elya Ramadhan", "Prestasi", 0.0, 94, 3, False),
    Pendaftar("Farhan Pratama", "Afirmasi", 0.0, 85, 2, True),
    Pendaftar("Gina Wulandari", "Prestasi", 0.0, 91, 4, False),
    Pendaftar("Hendra Wijaya", "Zonasi", 1.2, 80, 0, True),
    Pendaftar("Ika Pratama", "Prestasi", 0.0, 93, 3, False),
    Pendaftar("Joko Ramli", "Zonasi", 1.6, 82, 0, True),
    Pendaftar("Kiki Melani", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Lala Anggraini", "Afirmasi", 0.0, 88, 1, True),
    Pendaftar("Meli Ramli", "Zonasi", 1.5, 84, 0, False),
    Pendaftar("Nina Wijaya", "Prestasi", 0.0, 95, 3, True),
    
    Pendaftar("Oka Ramadhan", "Zonasi", 1.7, 81, 0, False),
    Pendaftar("Putra Wibowo", "Prestasi", 0.0, 91, 4, True),
    Pendaftar("Qila Puspita", "Zonasi", 1.3, 83, 0, False),
    Pendaftar("Rama Santoso", "Afirmasi", 0.0, 86, 2, True),
    Pendaftar("Sinta Kartini", "Prestasi", 0.0, 94, 3, False),
    Pendaftar("Tono Wijaya", "Zonasi", 1.5, 80, 0, True),
    Pendaftar("Umi Kusuma", "Prestasi", 0.0, 93, 4, False),
    Pendaftar("Vita Amelia", "Zonasi", 1.4, 82, 0, True),
    Pendaftar("Wulan Pratiwi", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Yogi Ramli", "Zonasi", 1.8, 83, 0, True),
   
    Pendaftar("Adit Saputra", "Zonasi", 1.1, 85, 0, False),
    Pendaftar("Bella Kartini", "Prestasi", 0.0, 92, 3, True),
    Pendaftar("Cindy Ramadhan", "Afirmasi", 0.0, 88, 2, False),
    Pendaftar("Dewi Kusuma", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Eko Wijaya", "Prestasi", 0.0, 94, 4, False),
    Pendaftar("Fajar Hakim", "Zonasi", 1.3, 80, 0, True),
    Pendaftar("Gita Permata", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Hana Lestari", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Indra Ramli", "Zonasi", 1.4, 82, 0, False),
    Pendaftar("Joni Hidayat", "Prestasi", 0.0, 93, 4, True),
    
    Pendaftar("Karina Sari", "Zonasi", 1.6, 81, 0, False),
    Pendaftar("Lutfi Ramadhan", "Prestasi", 0.0, 95, 3, True),
    Pendaftar("Maya Pratiwi", "Afirmasi", 0.0, 87, 2, False),
    Pendaftar("Nando Wibowo", "Zonasi", 1.2, 79, 0, True),
    Pendaftar("Oki Anggraini", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Putri Amelia", "Zonasi", 1.5, 84, 0, True),
    Pendaftar("Qomar Santoso", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Rani Puspita", "Zonasi", 1.8, 83, 0, True),
    Pendaftar("Sandi Ramli", "Afirmasi", 0.0, 85, 2, False),
    Pendaftar("Tika Melani", "Prestasi", 0.0, 94, 4, True),
    
    Pendaftar("Udin Pratama", "Zonasi", 1.3, 81, 0, False),
    Pendaftar("Vera Anggraini", "Prestasi", 0.0, 91, 3, True),
    Pendaftar("Widi Kusuma", "Zonasi", 1.6, 80, 0, False),
    Pendaftar("Xander Wibowo", "Prestasi", 0.0, 93, 4, True),
    Pendaftar("Yana Kartini", "Afirmasi", 0.0, 86, 1, False),
    Pendaftar("Zulfan Hakim", "Zonasi", 1.5, 83, 0, True),
    Pendaftar("Adi Nugraha", "Prestasi", 0.0, 92, 3, False),
    Pendaftar("Bagus Wibawa", "Zonasi", 1.4, 84, 0, True),
    Pendaftar("Cici Amelia", "Prestasi", 0.0, 90, 4, False),
    Pendaftar("Dio Santoso", "Zonasi", 1.7, 79, 0, True),
    Pendaftar("Elya Ramadhan", "Prestasi", 0.0, 94, 3, False),
    
    Pendaftar("Farhan Pratama", "Afirmasi", 0.0, 85, 2, True),
    Pendaftar("Gina Wulandari", "Prestasi", 0.0, 91, 4, False),
    Pendaftar("Hendra Wijaya", "Zonasi", 1.2, 80, 0, True),
    Pendaftar("Ika Pratama", "Prestasi", 0.0, 93, 3, False),
    Pendaftar("Joko Ramli", "Zonasi", 1.6, 82, 0, True),
    Pendaftar("Kiki Melani", "Prestasi", 0.0, 92, 4, False),
    Pendaftar("Lala Anggraini", "Afirmasi", 0.0, 88, 1, True),
    Pendaftar("Meli Ramli", "Zonasi", 1.5, 84, 0, False),
    Pendaftar("Nina Wijaya", "Prestasi", 0.0, 95, 3, True),
    Pendaftar("Oka Ramadhan", "Zonasi", 1.7, 81, 0, False),
    
    Pendaftar("Putra Wibowo", "Prestasi", 0.0, 91, 4, True),
    Pendaftar("Qila Puspita", "Zonasi", 1.3, 83, 0, False),
    Pendaftar("Rama Santoso", "Afirmasi", 0.0, 86, 2, True),
    Pendaftar("Sinta Kartini", "Prestasi", 0.0, 94, 3, False),
    Pendaftar("Tono Wijaya", "Zonasi", 1.5, 80, 0, True),
    Pendaftar("Umi Kusuma", "Prestasi", 0.0, 93, 4, False),
    Pendaftar("Vita Amelia", "Zonasi", 1.4, 82, 0, True),
    Pendaftar("Wulan Pratiwi", "Prestasi", 0.0, 90, 3, False),
    Pendaftar("Yogi Ramli", "Zonasi", 1.8, 83, 0, True),
    Pendaftar("Adryan Evan", "Afirmasi", 1.3, 88, 2, True),
    
    #---------------- 500 ------------------------
]

# Mengukur waktu
start_time = time.time()

# Pisahkan data berdasarkan jalur menggunakan fungsi rekursif
zonasi = filter_by_jalur(pendaftar, "Zonasi")
prestasi = filter_by_jalur(pendaftar, "Prestasi")
afirmasi = filter_by_jalur(pendaftar, "Afirmasi")

# Sort data setiap jalur secara rekursif
zonasi = recursive_sort(zonasi, sort_zonasi)
prestasi = recursive_sort(prestasi, sort_prestasi)
afirmasi = recursive_sort(afirmasi, sort_afirmasi)

# Alokasi kuota
kuota_zonasi = 25
kuota_prestasi = 15
kuota_afirmasi = 10

# Menambahkan pendaftar yang diterima berdasarkan kuota
diterima = []
diterima.extend(select_by_quota(zonasi, kuota_zonasi))
diterima.extend(select_by_quota(prestasi, kuota_prestasi))
diterima.extend(select_by_quota(afirmasi, kuota_afirmasi))

# Output hasil
print("Daftar siswa diterima:")
for d in diterima:
    print(f"Nama: {d.nama}, Jalur: {d.jalur}")

# Mengukur waktu eksekusi
end_time = time.time()

# Menampilkan waktu eksekusi
execution_time = end_time - start_time
print(f"\nWaktu eksekusi: {execution_time:.4f} detik")
