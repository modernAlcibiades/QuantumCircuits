import cirq
import numpy as np

q0 = cirq.GridQubit(1, 0)
q1 = cirq.GridQubit(0, 1)

def basic_circuit(meas=True):
    sqrt_x = cirq.X**0.5
    yield sqrt_x(q0), sqrt_x(q1)
    yield cirq.CZ(q0, q1)
    yield sqrt_x(q0), sqrt_x(q1)
    if meas:
        yield cirq.measure(q0, key='q0'), cirq.measure(q1, key='q1')

circuit = cirq.Circuit()
circuit.append(basic_circuit())

print(circuit)


simulator = cirq.Simulator()
result = simulator.simulate(circuit, qubit_order=[q0,q1])#, repetitions=20)

print("Results :", np.around(result.final_state_vector))
