# 09_LDO_Design — Low-Dropout Regulator

## Course Reference
Inflearn — Section 4 Lectures 16-18

## Primary Tool
LTspice + ngspice

## Reference Topology (from course images)
Classic analog LDO:
- **Pass device** — PMOS pass transistor (source at VIN, drain at VOUT)
- **Error amplifier** — compares VFB to VREF, drives pass gate
- **Feedback divider** — R1/R2 sets VOUT = VREF · (1 + R1/R2)
- **Load cap** — COUT + ESR at output
- Course sim shows load transient (step 0 → full load) with overshoot/undershoot ringing

## Course Structure (3 Steps)

### Step 1 — Follow-Along Build (그대로 따라해보기)
- [ ] Recreate LDO with VREF input (use Part 07 BGR or ideal 1.2 V)
- [ ] `.op` — confirm regulation at nominal load
- [ ] `.tran` — load step response, measure overshoot / undershoot / settling
- [ ] `.ac` — loop gain, find UGB and PM

### Step 2 — Improve Phase Margin
Goal: PM > 45° across entire load range (light load is the stability worst case — output pole moves to low freq). Techniques:
- **Miller compensation** inside error amp
- **Zero injection** via R_ESR of COUT or explicit R+C
- **Dominant-pole at pass-gate node** via large C_COMP
- **Adaptive biasing** — EA bias scales with IOUT
- [ ] Plot PM vs IOUT (sweep 0 → Imax)

### Step 3 — Stability Optimization (Assignment)
Given spec (e.g., VIN = 1.8 V, VOUT = 1.2 V, IOUT = 0 → 100 mA, COUT = 1 μF):
- [ ] Size pass PMOS for dropout at Imax
- [ ] Design EA for adequate gain + PM across load
- [ ] Choose COUT and ESR range for stable operation
- [ ] Verify across PVT + load range + COUT tolerance

## Key Metrics
| Metric | Typical Target |
|--------|----------------|
| Dropout | < 200 mV @ Imax |
| Line regulation | < 1 mV/V |
| Load regulation | < 10 mV (0 → Imax) |
| PSRR @ 1 kHz | > 50 dB |
| Phase margin | > 45° across load |
| Load transient undershoot | < 100 mV |
| Quiescent current | < 50 μA |

## Pole/Zero Landscape
- **Output pole** — p_OUT = 1 / (2π · R_OUT · COUT), R_OUT = (1/gds_pass) ∥ RL — moves with load!
- **EA pole** — p_EA = 1 / (2π · R_EA · C_EA)
- **Pass-gate pole** — from C_GS of large pass device
- **ESR zero** — z_ESR = 1 / (2π · ESR · COUT) — can stabilize if placed right

## Interview Questions
- Why is stability harder at light load?
- Analog LDO vs digital LDO — trade-offs
- How does ESR affect PM, and why is ceramic (low-ESR) COUT tricky?
- PSRR — where does it roll off and why?

## Status
- [ ] Theory read
- [ ] Step 1 — follow-along built
- [ ] Step 2 — PM improved across load
- [ ] Step 3 — stability optimized per spec
- [ ] PVT + load + ESR corner verified
