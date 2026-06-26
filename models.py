import re

class EntitasAkademik:
    """Base Class (Pewarisan)"""
    def __init__(self, nama):
        self._nama = nama # Enkapsulasi (Protected)

    def to_dict(self):
        pass # Polimorfisme (Akan di-override)

class Mahasiswa(EntitasAkademik):
    """Class Anak"""
    def __init__(self, nim, nama, jurusan, ipk):
        super().__init__(nama)
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = float(ipk)

    def to_dict(self):
        """Override metode dari class induk"""
        return {
            "nim": self.nim,
            "nama": self._nama,
            "jurusan": self.jurusan,
            "ipk": self.ipk
        }

    @staticmethod
    def validasi_nim(nim):
        """Regex: NIM harus 8 angka"""
        if not re.match(r"^\d{8}$", nim):
            raise ValueError("Format tidak valid! NIM harus 8 digit angka.")