import re

class RegexEvaluator:
    def __init__(self, pattern):
        self.pattern = pattern

    def test_string(self, input_string):
        """Menguji apakah string cocok dengan pola regex dari awal sampai akhir (full match)"""
        try:
            # Menggunakan fullmatch untuk memastikan string sepenuhnya memenuhi pola
            match = re.fullmatch(self.pattern, input_string)
            if match:
                return True, "String cocok dengan pola Regular Expression."
            else:
                return False, "String TIDAK cocok dengan pola Regular Expression."
        except re.error as e:
            return False, f"Pola Regex tidak valid: {str(e)}"

    def generate_regular_grammar(self):
        """
        Menghasilkan aturan produksi regular grammar sederhana 
        berdasarkan token dasar regex (contoh: a*b, ab, a|b) untuk dokumentasi ilmiah.
        """
        rules = []
        p = self.pattern.replace(" ", "")

        # Contoh Aturan Produksi Otomatis Sederhana Berdasarkan Pola Populer
        if p == "a*b":
            rules = [
                "S -> aS | b",
                "Keterangan: State S dapat menerima 'a' berulang kali, atau langsung selesai dengan 'b'."
            ]
        elif p == "a|b" or p == "(a|b)":
            rules = [
                "S -> a | b",
                "Keterangan: State S memilih transisi menghasilkan terminal 'a' atau 'b'."
            ]
        elif p == "ab":
            rules = [
                "S -> aA",
                "A -> b",
                "Keterangan: State S wajib menerima 'a' lalu pindah ke A untuk menerima 'b'."
            ]
        elif "*" in p:
            clean_char = p.replace("*", "")
            rules = [
                f"S -> {clean_char}S | ε",
                "Keterangan: Bentuk penutupan (Kleen Closure) menghasilkan loop pada variabel atau langsung string kosong."
            ]
        else:
            # Fallback umum jika polanya kustom bebas
            rules = [
                f"S -> {p} (Menerima untai terminal langsung)",
                "Catatan: Untuk visualisasi grammar kompleks, silakan rujuk diagram transisi pada Bab III laporan."
            ]
        return rules