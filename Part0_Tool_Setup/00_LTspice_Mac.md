# 00 — LTspice on Mac

## Role in Toolchain
Primary SPICE simulator for interactive circuit design. Best for:
- Fast schematic → simulation iteration
- Waveform probing and visualization
- Learning fundamentals with Level 1/3 MOSFET models

## Install
Download LTspice 17.2.4 from Analog Devices website → drag to Applications.

## LTspice on Mac — UI Basics
- Menu bar at top of screen (Mac style)
- Right-click for context menus
- Shortcuts use Ctrl (not Cmd) inside schematic editor

### Toolbar Shortcuts
| Key | Function |
|-----|----------|
| R | Resistor |
| C | Capacitor |
| L | Inductor |
| D | Diode |
| F | Component browser (MOSFETs) |
| W | Wire |
| G | GND |
| V | Voltage/current source |
| S | SPICE directive |
| F4 | Net label |
| T | Text comment |

### MOSFET Placement
- Press F → search nmos / pmos
- Pins: D (drain), G (gate), S (source), Bulk (GND for NMOS, VDD for PMOS)

### SPICE Directives (Press S)
```spice
.op                 ; DC operating point
.dc V1 0 3.3 0.01   ; DC sweep
.ac dec 10 1 1G     ; AC sweep
.tran 1n 100n       ; Transient
.noise V(out) Vin dec 10 1 1G  ; Noise
```

### Model Statement Example
```spice
.model MyNMOS NMOS (Level=1 Vto=0.5 Kp=200u)
```

## Exercise
- [ ] Install LTspice 17.2.4
- [ ] Create blank schematic
- [ ] Place 1 NMOS, voltage source, GND
- [ ] Add .op directive
- [ ] Run simulation

## Status
- [ ] Completed
