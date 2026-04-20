# 08_AMP_Design — Operational Amplifier (Two-Stage OTA)

## Course Reference
Inflearn — Section 4 Lectures 13-15

## Primary Tool
LTspice + ngspice

## Reference Topology (from course images)
Two-stage Miller-compensated OTA:
- **Stage 1** — PMOS differential pair (inputs VINP, VINN at ~1.2 V), NMOS current-mirror load
- **Stage 2** — common-source NMOS, PMOS current-source load → output VOUT_TWO
- **Compensation** — R1 = 100 kΩ (nulling resistor) + C1 = 50 pF (Miller cap) between stage-2 gate and output
- **Bias** — I2 = 5 μA
- Course sim shows Bode plot (magnitude + phase vs freq) with multi-curve overlay for corners

## Course Structure (3 Steps)

### Step 1 — Follow-Along Build (그대로 따라해보기)
- [ ] Recreate two-stage Miller-compensated OTA
- [ ] `.ac dec 10 1 1G` — open-loop Bode plot
- [ ] Measure: DC gain A₀, unity-gain bandwidth fU, phase margin PM
- [ ] Confirm PM > 60°

### Step 2 — High-Gain Improvement
Goal: push DC gain from ~60 dB baseline to 80+ dB. Techniques:
- **Cascode stage-1 output** (telescopic or folded cascode)
- **Long-L devices** in cascode for higher rₒ
- **Gain-boosting amp** in the cascode branch
- [ ] Measure A₀ before/after
- [ ] Re-check PM, UGB, settling — don't break closed-loop stability

### Step 3 — Design to Minimum AREA (Assignment)
Given spec (e.g., A₀ ≥ 70 dB, UGB ≥ 10 MHz, PM ≥ 60°, CL = 1 pF):
- [ ] Minimize total Σ(W·L) across all devices
- [ ] Trade-offs: smaller devices → more mismatch + more flicker noise
- [ ] Verify across PVT
- [ ] Monte Carlo on input-referred offset

## Key Metrics
| Metric | Measurement | Typical Target |
|--------|-------------|----------------|
| DC gain A₀ | AC @ DC | > 60 dB (Step 1), > 80 dB (Step 2) |
| UGB | AC magnitude crossing 0 dB | 10–50 MHz |
| Phase margin | phase @ UGB − (−180°) | > 60° |
| Slew rate | tran with large step input | I_tail / C_c |
| Input CMR | `.dc Vcm` | supply-dependent |
| Input-referred offset | Monte Carlo | < 5 mV (3σ) |
| Total area | Σ(W·L) | minimized in Step 3 |

## Design Flow
1. gₘ₁ from UGB × CL
2. Size M1/M2 input pair for needed gₘ with reasonable V_OV
3. Stage-2 mirror ratio for needed A₀
4. C_c ≈ 0.22 × CL for PM = 60°
5. R_z = 1/gₘ₂ to push RHP zero to infinity
6. Iterate

## Interview Questions
- Explain the RHP zero in Miller compensation and how R_z removes it
- Why does slew rate depend on I_tail / C_c?
- Trade-off: larger C_c improves PM but hurts UGB and SR
- When to use cascode vs two-stage vs folded-cascode

## Status
- [ ] Theory read
- [ ] Step 1 — basic two-stage built
- [ ] Step 2 — high-gain variant (cascode / gain-boosting)
- [ ] Step 3 — area-optimized design
- [ ] PVT + Monte Carlo verified
