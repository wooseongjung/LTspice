# 04 — Cross-Tool Workflow & Netlist Exchange

## The Unified Flow

## Netlist Portability
- SPICE netlist format is mostly cross-compatible
- LTspice-specific: `.lib`, `.tran 0 tstop startup`, some model variants
- ngspice-specific: `.control` / `.endc` blocks for scripting
- KiCad exports standard SPICE netlist

## Recommended Study Flow for Each Block
1. Sketch schematic in LTspice → fast iteration
2. Verify key metrics in ngspice (batch) with PVT corners
3. Optional: cross-check in Qucs-S
4. When mature: redraw in KiCad for portfolio documentation

## Python-Based Automation Example
```python
# Run 1000 Monte Carlo samples via ngspice
import subprocess, random
for i in range(1000):
    # generate netlist with randomized params
    # run ngspice, parse output
    pass
```

## Status
- [ ] Completed
