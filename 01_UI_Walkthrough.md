# LTspice UI Walkthrough — Mixed Signal IC Design Study Notes

## Environment
- LTspice for macOS Version: 17.2.4
- Study goal: Junior → Master's level analog/mixed-signal IC design
- Tool progression: LTspice → Quartus → Verilog

---

## Mac vs Windows Differences
- Right-click opens context menus (enable two-finger tap on trackpad if needed)
- Keyboard shortcuts use `Cmd` in some places, but many still use `Ctrl`
- Menu bar is at the top of screen (Mac style), not inside the window

---

## Opening LTspice & Creating a Schematic
1. Open LTspice → grey workspace appears
2. Top menu: `File  Edit  View  Simulate  Tools  Window  Help`
3. New schematic: **File → New Schematic** (`Ctrl+N`)

---

## Toolbar Shortcuts

| Shortcut | Function |
|----------|----------|
| `R` | Place resistor |
| `C` | Place capacitor |
| `L` | Place inductor |
| `D` | Place diode |
| `F` | Open component browser (for MOSFETs etc.) |
| `W` | Draw wires |
| `G` | Place GND symbol |
| `V` | Place voltage/current source |
| `S` | Type raw SPICE directive |
| `F4` | Label a net/node |
| `T` | Add comment text |

---

## Key Mac Interaction Rules

### Placing a component
1. Press shortcut key (e.g. `R` for resistor)
2. Component follows cursor
3. Left-click to place
4. Right-click to rotate before placing
5. `Esc` to cancel

### Editing a component value
- Right-click on the component → opens properties dialog
- Set resistance, model name, etc. here

### Moving & Deleting
| Action | How |
|--------|-----|
| Move (detaches wires) | Hover + press `M` |
| Drag (keeps wires) | `F8` |
| Delete mode | `Del` or `F5` |
| Undo | `Ctrl+Z` |
| Zoom in/out | Scroll wheel |
| Fit to window | `Ctrl+Shift+F` or `F` |

---

## Placing a MOSFET
1. Press `F` (or **Edit → Add Component**)
2. Search `nmos` or `pmos` in the component browser
3. Select and place on canvas

### MOSFET pin reference
| Pin | Description |
|-----|-------------|
| D | Drain |
| G | Gate |
| S | Source |
| Bulk/Body | 4th terminal — connect to GND (NMOS) or VDD (PMOS) |

---

## SPICE Directives
Press `S` to open the SPICE directive box. Place these as text on the schematic canvas.
```spice
.tran 1n 100n       ; Transient: step=1ns, stop=100ns
.ac dec 10 1 1G     ; AC sweep: 10pts/decade, 1Hz to 1GHz
.dc V1 0 3.3 0.01   ; DC sweep: V1 from 0 to 3.3V, step 10mV
.op                 ; Operating point (single DC bias point)
```

---

## Running a Simulation & Viewing Waveforms
1. Press Run button (toolbar) — equivalent to `Ctrl+R`
2. Waveform viewer opens
3. Click on a wire → probes node voltage
4. Click on a component body → probes current through it
5. Right-click on waveform → add trace, cursor, FFT, etc.

---

## MOSFET Model Statements

### Option A — Ideal Level 1 model (for learning)
```spice
.model MyNMOS NMOS (Level=1 Vto=0.5 Kp=200u)
```

### Option B — Include an external process model file
```spice
.include "path/to/modelfile.lib"
```

---

## First Exercise Checklist
- [ ] Place one NMOS (`nmos` from component browser)
- [ ] Place a voltage source (`V`) on gate and drain
- [ ] Place GND symbols on source and bulk
- [ ] Add `.op` SPICE directive
- [ ] Run simulation — confirm no errors

---

## Next Step
**MOSFET I-V Curves** — Plot Id vs Vds for different Vgs values using `.dc` sweep.
This teaches: DC sweep, waveform probing, and MOSFET operating regions all at once.
