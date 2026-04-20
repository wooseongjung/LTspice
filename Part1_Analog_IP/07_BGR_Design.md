# 07_BGR_Design — BGR (Band-Gap Reference)

## Course Reference
Inflearn — Section 4 Lectures 10-12

## Primary Tool
LTspice (interactive) + ngspice (PVT sweeps, Monte Carlo)

## What is a BGR?
A bandgap reference generates a voltage nearly independent of temperature and supply by summing:
- **CTAT** (Complementary To Absolute T) — VBE of a forward-biased BJT, slope ≈ −2 mV/°C
- **PTAT** (Proportional To Absolute T) — ΔVBE between BJTs at different current density, slope ≈ +0.087 mV/°C × ln(N)

VREF = VBE + K·ΔVBE → canonical ~1.2 V (silicon bandgap extrapolated to 0 K).

## Reference Topology (from course images)
- PMOS current mirror at top (3 legs from VDD)
- BJT array: Q13 (1×), Q14<7:0> (8× unit for ΔVBE), Q15 (output leg)
- R4 = 20 kΩ (PTAT resistor), R5 = {BGR_RES} (design variable)
- Output node VREF
- Course sim shows temperature sweep −40°C → +120°C (multi-color overlay = corner sweep)

## Course Structure (3 Steps)

### Step 1 — Follow-Along Build (그대로 따라해보기)
- [ ] Recreate schematic in LTspice exactly as lecture shows
- [ ] `.op` — confirm VREF ≈ 1.2 V at 27°C
- [ ] `.dc temp -40 120 1` — plot VREF vs T
- [ ] Compute TC (ppm/°C) from curve slope; target < 50 ppm/°C

### Step 2 — Improve Low-Voltage Reference Operation
Goal: operate from sub-1.2 V supply. Techniques:
- **Current-mode (Banba) topology** — sum PTAT + CTAT currents through a resistor → VREF can be below VBE
- **Fractional VBE** via resistor divider before the summing node
- **Curvature correction** for 2nd-order TC cancellation
- [ ] Re-draw with current-mode summing, re-simulate
- [ ] Sweep VDD, find minimum operating supply

### Step 3 — Design to Target VREF (Assignment)
Given target VREF (e.g., 0.6 V or 1.0 V):
- [ ] Choose BJT area ratio N (typically 8 or 16)
- [ ] Compute R ratio for PTAT scaling: K = (R2/R1) · ln(N)
- [ ] Size PMOS mirror for matching (L ≥ 2·Lmin)
- [ ] Verify across PVT: TT/SS/FF × (−40/27/125°C) × (VDDmin/typ/max)
- [ ] Monte Carlo (100 runs) for mismatch — measure σ(VREF)/VREF

## Key Metrics
| Metric | Typical Target | Analysis |
|--------|----------------|----------|
| VREF @ 27°C | course-specified | `.op` |
| Temperature coefficient | < 50 ppm/°C | `.dc temp` |
| PSRR @ DC | > 60 dB | `.ac` with VDD as AC source |
| Line regulation | < 1 mV/V | `.dc VDD` |
| Startup | must exit zero-current state | `.tran` with VDD ramp |
| σ(VREF)/VREF | < 1% (3σ) | Monte Carlo |

## Design Pitfalls
- Missing startup circuit → stuck at 0 V (zero-current stable state)
- PMOS mirror mismatch dominates TC variation — use large L, common-centroid layout
- R4 TC (polyR, diffR) itself limits achievable TC — choose low-TC resistor flavor
- Op-amp offset (if feedback topology) adds directly to VREF error

## Interview Questions (Samsung DS / SK Hynix)
- Derive VREF for a Brokaw-style BGR
- Why is −2 mV/°C the VBE slope? (derive from Shockley equation)
- How does a startup circuit detect and break the zero-current state?
- Compare Widlar / Brokaw / Banba topologies — when to use which?
- What limits the achievable TC in practice?

## Status
- [ ] Theory read
- [ ] Step 1 — follow-along complete
- [ ] Step 2 — low-voltage variant built
- [ ] Step 3 — target-VREF design verified across PVT
- [ ] Monte Carlo completed in ngspice
