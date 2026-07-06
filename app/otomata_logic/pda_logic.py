class PDASimulator:
    def __init__(self, states, alphabet, stack_alphabet, initial_state, start_stack, final_states):
        """
        Definisi Formal PDA: M = (Q, Σ, Γ, δ, q0, Z0, F)
        """
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.stack_alphabet = set(stack_alphabet)
        self.initial_state = initial_state
        self.start_stack = start_stack
        self.final_states = set(final_states)

    def simulate(self, input_string):
        """
        Mensimulasikan string masukan pada PDA untuk bahasa a^nb^n.
        Melacak state, sisa string, dan kondisi isi stack langkah demi langkah.
        """
        current_state = self.initial_state
        stack = [self.start_stack]  # Inisialisasi stack dengan simbol awal (Z0 atau #)
        trace = []
        
        # Simpan kondisi awal sebelum membaca string
        trace.append({
            "step": 0,
            "current_state": current_state,
            "input_char": "ε (Mulai)",
            "stack_content": "".join(stack)[::-1], # Tampilkan dari atas ke bawah
            "action": f"Inisialisasi stack dengan {self.start_stack}"
        })

        for index, char in enumerate(input_string):
            if char not in self.alphabet:
                return False, trace, f"Karakter '{char}' tidak ada dalam alfabet mesin."

            top_of_stack = stack[-1] if stack else None
            action = ""

            # Logika Aturan Transisi Spesifik Bahasa a^nb^n
            if current_state == "q0" and char == "a" and top_of_stack == "#":
                stack.append("A")
                action = "Push 'A'"
            elif current_state == "q0" and char == "a" and top_of_stack == "A":
                stack.append("A")
                action = "Push 'A'"
            elif current_state == "q0" and char == "b" and top_of_stack == "A":
                current_state = "q1"
                stack.pop()
                action = "Pindah ke q1, Pop 'A'"
            elif current_state == "q1" and char == "b" and top_of_stack == "A":
                stack.pop()
                action = "Pop 'A'"
            else:
                # Tidak ada transisi legal terdefinisi (Crash/Reject)
                trace.append({
                    "step": index + 1,
                    "current_state": current_state,
                    "input_char": char,
                    "stack_content": "".join(stack)[::-1] if stack else "Ø (Kosong)",
                    "action": "CRASH: Tidak ada transisi yang cocok!"
                })
                return False, trace, f"Mesin stuck di state '{current_state}' dengan input '{char}' dan top stack '{top_of_stack}'."

            trace.append({
                "step": index + 1,
                "current_state": current_state,
                "input_char": char,
                "stack_content": "".join(stack)[::-1] if stack else "Ø (Kosong)",
                "action": action
            })

        # Transisi epsilon terakhir untuk mengecek akhir stack dan mengubah ke final state
        if current_state == "q1" and stack and stack[-1] == "#":
            current_state = "q2"
            action = "Pindah ke q2 (Menerima Epsilon), Pop '#'"
            stack.pop()
            trace.append({
                "step": len(input_string) + 1,
                "current_state": current_state,
                "input_char": "ε (Selesai)",
                "stack_content": "".join(stack)[::-1] if stack else "Ø (Kosong)",
                "action": action
            })

        # Cek apakah string diterima berdasarkan final state
        is_accepted = current_state in self.final_states and len(stack) == 0
        
        if is_accepted:
            msg = "String Diterima! Jumlah 'a' dan 'b' sama besar serta berurutan secara seimbang."
        else:
            msg = "String Ditolak! Stack tidak bersih atau tidak mencapai state akhir yang valid."
            
        return is_accepted, trace, msg