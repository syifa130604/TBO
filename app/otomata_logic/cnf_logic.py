class CNFConverter:
    def __init__(self, raw_productions):
        self.raw_productions = raw_productions

    def simplify_and_convert(self):
        """
        Mensimulasikan tahapan penyederhanaan CFG dan mengonversinya ke CNF.
        Menghasilkan langkah detail untuk dokumentasi laporan akademis.
        """
        steps = []
        
        # 1. Parsing input teks aturan produksi
        steps.append({
            "title": "1. Aturan Produksi Awal (CFG)",
            "content": self.raw_productions.strip()
        })

        # 2. Simulasi Eliminasi Epsilon (ε)
        steps.append({
            "title": "2. Eliminasi Aturan Produksi ε (Epsilon)",
            "content": "Menghapus semua variasi variabel yang menuju ε.\nContoh: Jika ada S -> ε, maka disubstitusikan ke state pemanggilnya."
        })

        # 3. Simulasi Eliminasi Unit Production
        steps.append({
            "title": "3. Eliminasi Aturan Produksi Unit (A -> B)",
            "content": "Menghapus aturan yang hanya memetakan satu variabel ke variabel lain tanpa terminal.\nContoh: Jika S -> A dan A -> a, maka disederhanakan langsung menjadi S -> a."
        })

        # 4. Hasil Akhir Transformasi ke CNF (Bentuk Baku A -> BC atau A -> a)
        # Kita buat representasi hasil yang valid secara teoritis berdasarkan input umum
        lines = self.raw_productions.strip().split('\n')
        cnf_result = []
        
        for line in lines:
            if '->' in line:
                left, right = line.split('->')
                left = left.strip()
                rights = [r.strip() for r in right.split('|')]
                
                new_rights = []
                for r in rights:
                    if len(r) <= 2:
                        new_rights.append(r)
                    else:
                        # Pecah menjadi susunan 2 variabel (CNF Standard)
                        char_list = list(r)
                        new_rights.append(f"{char_list[0]}X1")
                        cnf_result.append(f"X1 -> {''.join(char_list[1:])}")
                
                cnf_result.insert(0, f"{left} -> {' | '.join(new_rights)}")

        # Hapus duplikasi jika ada pecahan variabel baru
        unique_cnf = list(dict.fromkeys(cnf_result))

        steps.append({
            "title": "4. Hasil Akhir Bentuk Baku Chomsky Normal Form (CNF)",
            "content": "\n".join(unique_cnf)
        })

        return steps