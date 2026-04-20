# 01 — ngspice Setup & CLI Workflow

## Role in Toolchain
Command-line SPICE simulator. Best for:
- Batch simulations (PVT corners, Monte Carlo)
- Python/shell scripting for automated sweeps
- Modern BSIM model support (BSIM4, BSIM-CMG for FinFET)
- Integration with KiCad netlists

## Install on macOS
```bash
brew install ngspice
ngspice --version
```

## Basic Usage
```bash
ngspice my_circuit.cir              # Interactive mode
ngspice -b my_circuit.cir           # Batch mode
ngspice -b -o output.log circuit.cir
```

## Example Netlist (Single-Stage Amp)
```spice
* Single-stage common-source amp
.include tsmc180nm.lib

M1 out in 0 0 nmos W=10u L=0.18u
R1 vdd out 10k
Vin in 0 DC 0.9 AC 1
Vdd vdd 0 1.8

.ac dec 10 1 1G
.end
```

## Python Integration (PySpice)
```bash
pip3 install PySpice
```
```python
from PySpice.Spice.Netlist import Circuit
circuit = Circuit('Amp')
# build + simulate via ngspice backend
```

## Exercise
- [ ] Install ngspice
- [ ] Run example netlist in batch mode
- [ ] Plot result with gnuplot or Python

## Status
- [ ] Completed
