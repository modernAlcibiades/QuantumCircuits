import cirq

qubit = cirq.GridQubit(0,0)

circuit = cirq.Circuit(
        cirq.X(qubit)**0.5, # square root of Not gate
        cirq.measure(qubit, key='m')
        )
print('Circuit:', circuit)

simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)
print("Results :", result)
