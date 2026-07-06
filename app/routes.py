from flask import Flask, render_template, request, jsonify
from app.otomata_logic.fsa import DFASimulator, NFASimulator
from app.otomata_logic.regex_logic import RegexEvaluator
from app.otomata_logic.pda_logic import PDASimulator
from app.otomata_logic.cnf_logic import CNFConverter  # Import Modul 4

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# ==========================================
# MODUL 1: SIMULATOR FSA (DFA / NFA)
# ==========================================
@app.route('/fsa', methods=['GET', 'POST'])
def fsa_module():
    if request.method == 'POST':
        data = request.get_json()
        machine_type = data.get('machine_type', 'DFA')
        
        states = data.get('states', [])
        alphabet = data.get('alphabet', [])
        transition_table = data.get('transition_table', {})
        initial_state = data.get('initial_state', '')
        final_states = data.get('final_states', [])
        input_string = data.get('input_string', '')

        if machine_type == 'DFA':
            dfa = DFASimulator(states, alphabet, transition_table, initial_state, final_states)
            is_valid, msg = dfa.validate_machine()
            if not is_valid:
                return jsonify({'status': 'error', 'message': msg})
            
            is_accepted, trace, message = dfa.check_string(input_string)
            return jsonify({'status': 'success', 'is_accepted': is_accepted, 'trace': trace, 'message': message})
            
        elif machine_type == 'NFA':
            nfa = NFASimulator(states, alphabet, transition_table, initial_state, final_states)
            dfa_equivalent = nfa.convert_to_dfa()
            dfa_sim = DFASimulator(dfa_equivalent['states'], dfa_equivalent['alphabet'], dfa_equivalent['transition_table'], dfa_equivalent['initial_state'], dfa_equivalent['final_states'])
            is_accepted, trace, message = dfa_sim.check_string(input_string)
            return jsonify({'status': 'success', 'is_accepted': is_accepted, 'trace': trace, 'message': message, 'dfa_equivalent': dfa_equivalent})

    return render_template('fsa.html')

# ==========================================
# MODUL 2: REGULAR EXPRESSION (RE)
# ==========================================
@app.route('/regex', methods=['GET', 'POST'])
def regex_module():
    if request.method == 'POST':
        data = request.get_json()
        pattern = data.get('pattern', '')
        input_string = data.get('input_string', '')

        if not pattern:
            return jsonify({'status': 'error', 'message': 'Pola Regular Expression tidak boleh kosong.'})

        evaluator = RegexEvaluator(pattern)
        is_matched, msg = evaluator.test_string(input_string)
        grammar_rules = evaluator.generate_regular_grammar()

        return jsonify({'status': 'success', 'is_matched': is_matched, 'message': msg, 'grammar_rules': grammar_rules})

    return render_template('regex.html')

# ==========================================
# MODUL 3: PUSHDOWN AUTOMATA (PDA) & CFG
# ==========================================
@app.route('/pda', methods=['GET', 'POST'])
def pda_module():
    if request.method == 'POST':
        data = request.get_json()
        input_string = data.get('input_string', '')

        pda = PDASimulator(['q0', 'q1', 'q2'], ['a', 'b'], ['A', '#'], 'q0', '#', ['q2'])
        is_accepted, trace, message = pda.simulate(input_string)

        cfg_rules = ["S -> aSb | ε", "Keterangan: Aturan ini secara rekursif memastikan jumlah 'a' seimbang dengan 'b'."]
        return jsonify({'status': 'success', 'is_accepted': is_accepted, 'trace': trace, 'message': message, 'cfg_rules': cfg_rules})

    return render_template('pda.html')

# ==========================================
# MODUL 4: CHOMSKY NORMAL FORM (CNF)
# ==========================================
@app.route('/cnf', methods=['GET', 'POST'])
def cnf_module():
    if request.method == 'POST':
        data = request.get_json()
        productions = data.get('productions', '')

        if not productions.strip():
            return jsonify({'status': 'error', 'message': 'Aturan produksi CFG tidak boleh kosong.'})

        converter = CNFConverter(productions)
        steps = converter.simplify_and_convert()

        return jsonify({
            'status': 'success',
            'steps': steps
        })

    return render_template('cnf.html')

if __name__ == '__main__':
    app.run(debug=True)