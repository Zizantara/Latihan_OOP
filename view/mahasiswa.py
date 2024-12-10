class MahasiswaList:
    def __init__(self):
        self.data = []

    def tambah_mahasiswa(self, mahasiswa):
        self.data.append(mahasiswa)

    def tampilkan_mahasiswa(self):
        for mahasiswa in self.data:
            print(f"Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Kelas: {mahasiswa.kelas}")

    def ubah_data_mahasiswa(self, nim):
        for mahasiswa in self.data:
            if mahasiswa.nim == nim:
                print(f"Data ditemukan: Nama: {mahasiswa.nama}, NIM: {mahasiswa.nim}, Kelas: {mahasiswa.kelas}")
                mahasiswa.nama = input("Masukkan nama baru: ")
                mahasiswa.kelas = input("Masukkan kelas baru: ")
                print("Data mahasiswa berhasil diubah.")
                return
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")

    def hapus_data_mahasiswa(self, nim):
        for mahasiswa in self.data:
            if mahasiswa.nim == nim:
                self.data.remove(mahasiswa)
                print("Data mahasiswa berhasil dihapus.")
                return
        print("Mahasiswa dengan NIM tersebut tidak ditemukan.")
