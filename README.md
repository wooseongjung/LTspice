# LTspice — Mixed Signal IC Design Study Notes

Self-study for analog/mixed-signal IC design, targeting Samsung DS / SK Hynix design engineer roles and KAIST EE master's preparation.

## Toolchain
Open-source analog design stack:

| Tool | Role |
|------|------|
| **LTspice** | Primary SPICE simulator (schematic + waveform viewer) |
| **ngspice** | CLI SPICE — batch sims, Monte Carlo, Python integration |
| **KiCad** | Schematic capture + PCB layout |
| **Qucs (Qucs-S)** | Alternative simulator, RF/noise analysis, ngspice backend |

Later: **Cadence Virtuoso → Quartus → Verilog HDL**

---

## Reference Courses

### Course 1 — Inflearn: Practical Analog Circuit Design (Analog IP)
Tool setup, single-stage amp simulation methodology, and the 7 core analog IPs used at Samsung/SK Hynix.

### Course 2 — Advanced Mixed-Signal (Part 3, Ch 1–8)
PLL, ADC/DAC, high-speed analog, noise/distortion, layout, PVT, test, integration project.

---

## Study Roadmap

### Part 0 — Tool Setup
| # | Topic | Status |
|---|-------|--------|
| 00 | LTspice on Mac | ⬜ |
| 01 | ngspice setup & CLI workflow | ⬜ |
| 02 | KiCad schematic capture | ⬜ |
| 03 | Qucs / Qucs-S setup | ⬜ |
| 04 | Cross-tool workflow & netlist exchange | ⬜ |

### Part 1 — Analog IP Foundations (Inflearn Sections 3–4)

Each IP (07–13) follows the same 3-step course pattern:
**(1)** Follow-along build (그대로 따라해보기) → **(2)** Improve target metric → **(3)** Design to given constraint.

| # | Topic | Improve → Final Design Target | Tool | Status |
|---|-------|-------------------------------|------|--------|
| 05 | TSMC 180nm Process Library | — | LTspice / ngspice | ⬜ |
| 06 | Single-Stage Amp + 5 Simulations | DC / DC-sweep / AC / Tran / Noise methodology | LTspice | ⬜ |
| 07 | BGR — Bandgap Reference | Low-Voltage Reference → Target VREF | LTspice + ngspice | ⬜ |
| 08 | AMP — Operational Amplifier | High-Gain → Min AREA | LTspice + ngspice | ⬜ |
| 09 | LDO — Low-Dropout Regulator | Phase-Margin → Stability | LTspice + ngspice | ⬜ |
| 10 | Level Shifter | Wide-Range + Low-Power → Low-Power + Rising-Time | LTspice | ⬜ |
| 11 | Comparator | High-Speed → Low-Offset | LTspice | ⬜ |
| 12 | Oscillator (Ring / VCO) | Noise + Jitter → Area + Power | LTspice + Qucs | ⬜ |
| 13 | Charge Pump | Power-Efficiency → Small-Area | LTspice | ⬜ |
| 14 | House-Keeping Block (Integration) | Multi-IP integration project | LTspice + KiCad | ⬜ |

### Part 2 — Advanced Mixed-Signal (Part 3 of Advanced Course)
| # | Topic | Primary Tool | Status |
|---|-------|--------------|--------|
| 15 | PLL Fundamentals & High-Speed I/F | LTspice + ngspice | ⬜ |
| 16 | ADC / DAC — Precision Data Conversion | ngspice + Python | ⬜ |
| 17 | High-Speed Analog & SI/PI | Qucs + LTspice | ⬜ |
| 18 | Noise / Distortion / Linearity | Qucs + ngspice | ⬜ |
| 19 | Analog Layout Fundamentals | KiCad | ⬜ |
| 20 | PVT & Advanced Nodes (FinFET/GAA) | ngspice (Monte Carlo) | ⬜ |
| 21 | Analog Test — ATE & Production | Conceptual + ngspice | ⬜ |
| 22 | Analog Integration Project | All tools | ⬜ |

---

## Environment
- macOS, LTspice 17.2.4
- ngspice (install via Homebrew)
- KiCad (install via official DMG)
- Qucs-S (install via Homebrew or build from source)
- TSMC 180nm library (Course 1)

## Goals
- Build portfolio of designed analog IPs (BGR, AMP, LDO, Comparator, Oscillator, Charge Pump)
- Prepare for Samsung DS / SK Hynix analog circuit design interviews
- Strengthen technical foundation for KAIST EE master's program (analog & mixed-signal IC design)
