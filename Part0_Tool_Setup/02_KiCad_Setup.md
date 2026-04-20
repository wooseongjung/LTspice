# 02 — KiCad Schematic Capture

## Role in Toolchain
Schematic capture + PCB layout tool. Best for:
- Professional schematic drawing (better than LTspice for documentation)
- Exporting SPICE netlists to ngspice
- Eventually moving designs to PCB for bench verification

## Install on macOS
Download KiCad 8.x from kicad.org → install DMG.

## Schematic → ngspice Flow
1. Create schematic in KiCad Eeschema
2. Assign SPICE models to components (Properties → Simulation Model)
3. Tools → Simulator (built-in ngspice)
4. Or export netlist: File → Export → Netlist → SPICE

## Key Features for Analog Design
- Hierarchical schematics (for multi-block designs like House-Keeping Block)
- Symbol libraries for MOSFETs, op-amps, passives
- ERC (Electrical Rules Check)
- Built-in ngspice simulation tab

## Exercise
- [ ] Install KiCad
- [ ] Create a simple RC low-pass filter schematic
- [ ] Run AC sweep using built-in simulator

## Status
- [ ] Completed
