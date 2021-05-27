import cirq
import numpy as np

class R_m(cirq.Gate):
    def __init__(self, m):
        super(R_m, self)
        self.m = m

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        return np.array([
            [1.0,   0.0],
            [0.0,   np.exp((2.j*np.pi)/2.0**self.m)]])

    def _circuit_diagram_info_(self, args):
        return "R({})".format(self.m)


def qft_onequbit_control_ops(target, state):
    '''
    target  : Qubit to be modified
    state   : Controlled U**n  operations
    '''
    yield cirq.H(target)
    for i, q in enumerate(state):
        yield(R_m(i+1).on(target).controlled_by(q))

def qft_circuit(state, inverse=False):
    '''
    state   : The state to be transformed
    '''
    for i, q in enumerate(state):
        yield(qft_onequbit_control_ops(q, state[i+1:]))

state = cirq.LineQubit.range(4)
circuit = cirq.Circuit()
#circuit.append(cirq.X(state[2]))
circuit.append(qft_circuit(state))
print(circuit)

#for i in range(len(state)):
#    state[i] = 1
#print(state, state[-1])
simulator = cirq.Simulator()
result = simulator.simulate(circuit, qubit_order = state)#, repetitions=20)
print("Results :", result)
