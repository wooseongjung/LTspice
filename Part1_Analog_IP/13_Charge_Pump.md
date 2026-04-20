# 13_Charge_Pump — Charge Pump

## Course Reference
Inflearn — Section 4 Lectures 28-30

## Primary Tool
LTspice + ngspice

## Reference Topology (from course images)
Dickson charge pump (multi-stage):
- N diode-connected (or MOSFET-diode) stages in series
- Two non-overlapping clocks ϕ, ϕ̄ drive alternate flying caps
- Each stage lifts output by ~(VDD − Vth) — ideally VDD
- After N stages: VOUT ≈ (N+1)·VDD − losses
- Course sim shows multi-exponential startup ramp (one curve per stage, asymptotic to steady state)

## Course Structure (3 Steps)

### Step 1 — Follow-Along Build (그대로 따라해보기)
- [ ] Build 4-stage Dickson pump with MOSFET diodes
- [ ] Generate non-overlapping ϕ, ϕ̄ clocks
- [ ] Transient: plot output voltage rise, measure steady-state VOUT
- [ ] Compute efficiency η = (VOUT · IOUT) / (VDD · I_avg_in)

### Step 2 — Power-Efficiency Improvement
Goal: push η from ~50% baseline to > 80%. Techniques:
- **Cross-coupled (Pelliconi) pump** — full-swing, no Vth drop
- **Bootstrapped MOSFET switches** — eliminate Vth loss
- **Adiabatic clocking** (ramped clocks) to reduce CV²f switching loss
- **Optimal stage count** for a given load (too many → more switching loss)
- [ ] Measure η before/after
- [ ] Characterize η vs IOUT curve

### Step 3 — Small-Area Design (Assignment)
Given spec (e.g., VIN = 1.8 V, VOUT = 5 V @ 1 mA, η > 70%):
- [ ] Minimize total capacitor area (N × C_fly + C_out)
- [ ] Minimize switch area
- [ ] Trade: f_clk ↑ → C_fly ↓ (ripple spec) but switching losses ↑
- [ ] Verify PVT

## Key Metrics
| Metric | Target |
|--------|--------|
| Output voltage | course-specified |
| Output ripple | < 5% of VOUT |
| Efficiency | > 70% (Step 3), > 50% (Step 1) |
| Output impedance | R_out ≈ 1 / (N · f · C_fly) |
| Startup time | tens of μs typical |
| Total cap area | minimized in Step 3 |

## Design Equations
- **Ideal Dickson**: V_OUT = (N+1)·V_DD − N·V_th (MOS-diode loss)
- **Loaded**: V_OUT = (N+1)·V_DD − I_OUT / (f · C_fly)  ← R_out form
- **Ripple**: ΔV = I_OUT / (f · C_out)
- **Efficiency**: η ≈ V_OUT / V_OUT_ideal − switching_loss_fraction

## Interview Questions
- Why does a simple Dickson pump saturate below ideal (N+1)·VDD?
- Cross-coupled vs Dickson — when to use which?
- How does switching frequency affect efficiency (switching vs conduction losses)?
- Why are charge pumps used for NAND Flash programming (15–20 V from 1.8 V)?

## Status
- [ ] Theory read
- [ ] Step 1 — Dickson follow-along
- [ ] Step 2 — high-efficiency (Pelliconi / bootstrapped)
- [ ] Step 3 — small-area design
- [ ] PVT verified
