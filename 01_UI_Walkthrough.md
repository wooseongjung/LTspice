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
3. New schematic: **File → New Schematic** (`Cmd+N`)

---

## Toolbar Shortcuts

| Shortcut | Function |
|----------|----------|
| `F2` | Open component browser (resistor, capacitor, MOSFET, etc.) |
| `F3` | Draw wires |
| `G` | Place GND symbol |
| `S` | Type raw SPICE directive |
| `F4` | Label a net/node |
| `T` | Add comment text |
| `F5` | Delete mode |
| `F6` | Duplicate |
| `F7` | Move |
| `F8` | Drag (keeps wires attached) |

> **Note:** On Mac, there are no single-key shortcuts for placing resistors (`R`), capacitors (`C`), inductors (`L`), diodes (`D`), or voltage sources (`V`). Use `F2` to open the component browser and search by name.

---

## Key Mac Interaction Rules

### Placing a component
1. Press `F2` to open the component browser (or use `G` for GND)
2. Search for the component (e.g. "res", "nmos", "voltage")
3. Select it — component follows cursor
4. `Ctrl+R` to rotate, `Ctrl+E` to mirror before placing
5. Left-click to place
6. `Esc` to cancel

### Editing a component value
- Right-click on the component → opens properties dialog
- Set resistance, model name, etc. here

### Moving & Deleting
| Action | How |
|--------|-----|
| Move (detaches wires) | `F7` |
| Drag (keeps wires) | `F8` |
| Delete mode | `Del` or `F5` |
| Undo | `Cmd+Z` (or `F9`) |
| Redo | `Cmd+Shift+Z` (or `Shift+F9`) |
| Zoom in/out | Two-finger pinch/spread |
| Fit to window | `Space` |

---

## Placing a MOSFET
1. Press `F2` (or **Edit → Add Component**)
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
1. Press Run button (toolbar) or **Simulate → Run**
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
- [ ] Place a voltage source (`F2` → search "voltage") on gate and drain
- [ ] Place GND symbols on source and bulk
- [ ] Add `.op` SPICE directive
- [ ] Run simulation — confirm no errors

---

## Next Step
**MOSFET I-V Curves** — Plot Id vs Vds for different Vgs values using `.dc` sweep.
This teaches: DC sweep, waveform probing, and MOSFET operating regions all at once.
