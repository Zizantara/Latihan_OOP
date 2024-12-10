from data.mahasiswa import Mahasiswa

class InputForm:
    def get_input():
        nama = input("Masukkan nama mahasiswa: ")
        nim = input("Masukkan NIM mahasiswa: ")
        kelas = input("Masukkan kelas mahasiswa: ")
        return Mahasiswa(nama, nim, kelas)