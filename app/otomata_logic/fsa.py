class DFASimulator:
    def __init__(self, states, alphabet, transition_table, initial_state, final_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transition_table = transition_table
        self.initial_state = initial_state
        self.final_states = set(final_states)

    def validate_machine(self):
        if self.initial_state not in self.states:
            return False, f"State awal '{self.initial_state}' tidak ada di kumpulan State (Q)."
        for f_state in self.final_states:
            if f_state not in self.states:
                return False, f"State akhir '{f_state}' tidak ada di kumpulan State (Q)."
        return True, "Mesin valid."

    def check_string(self, input_string):
        current_state = self.initial_state
        trace = [{"step": 0, "current_state": current_state, "input_char": None, "next_state": current_state}]
        
        if input_string == "" or input_string is None:
            is_accepted = current_state in self.final_states
            return is_accepted, trace, "String kosong dievaluasi."

        for index, char in enumerate(input_string):
            if char not in self.alphabet:
                return False, trace, f"Karakter '{char}' tidak dikenali oleh alfabet mesin."

            state_transitions = self.transition_table.get(current_state, {})
            next_state = state_transitions.get(char)

            if not next_state:
                return False, trace, f"Tidak ada transisi dari state '{current_state}' dengan input '{char}'."

            trace.append({
                "step": index + 1,
                "current_state": current_state,
                "input_char": char,
                "next_state": next_state
            })
            current_state = next_state

        is_accepted = current_state in self.final_states
        return is_accepted, trace, "Proses selesai."


class NFASimulator:
    def __init__(self, states, alphabet, transition_table, initial_state, final_states):
        self.states = set(states)
        self.alphabet = set(alphabet)
        self.transition_table = transition_table
        self.initial_state = initial_state
        self.final_states = set(final_states)

    def epsilon_closure(self, state_set):
        closure = set(state_set)
        stack = list(state_set)
        while stack:
            current = stack.pop()
            epsilon_transitions = self.transition_table.get(current, {}).get('e', [])
            for next_state in epsilon_transitions:
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def convert_to_dfa(self):
        dfa_initial = tuple(sorted(self.epsilon_closure({self.initial_state})))
        dfa_states = [dfa_initial]
        dfa_transitions = {}
        dfa_final_states = []
        unmarked_states = [dfa_initial]

        while unmarked_states:
            current_dfa_state = unmarked_states.pop(0)
            current_state_name = ",".join(current_dfa_state) if current_dfa_state else "Ø"
            dfa_transitions[current_state_name] = {}

            if any(state in self.final_states for state in current_dfa_state):
                if current_state_name not in dfa_final_states:
                    dfa_final_states.append(current_state_name)

            for symbol in self.alphabet:
                if symbol == 'e':
                    continue
                
                next_set = set()
                for nfa_state in current_dfa_state:
                    next_states = self.transition_table.get(nfa_state, {}).get(symbol, [])
                    for ns in next_states:
                        next_set.add(ns)
                
                next_closure = tuple(sorted(self.epsilon_closure(next_set)))
                next_state_name = ",".join(next_closure) if next_closure else "Ø"
                dfa_transitions[current_state_name][symbol] = next_state_name

                if next_closure not in dfa_states and next_closure != ():
                    dfa_states.append(next_closure)
                    unmarked_states.append(next_closure)
                elif next_closure == () and ((),) not in dfa_states:
                    dfa_transitions[current_state_name][symbol] = "Ø"

        formatted_dfa_states = [",".join(s) if s else "Ø" for s in dfa_states]
        return {
            "states": formatted_dfa_states,
            "alphabet": list(self.alphabet - {'e'}),
            "transition_table": dfa_transitions,
            "initial_state": ",".join(dfa_initial),
            "final_states": dfa_final_states
        }