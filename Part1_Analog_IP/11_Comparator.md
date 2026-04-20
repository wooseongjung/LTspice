# 11_Comparator — Comparator

## Course Reference
Inflearn — Section 4 Lectures 22-24

## Primary Tool
LTspice (transient + ramp) + ngspice (offset Monte Carlo)

## Reference Topology (from course images)
Clocked comparator — **StrongARM latch** or **double-tail** latched comparator:
- Preamp / input stage (differential pair with clock)
- Regenerative latch (cross-coupled inverter pair)
- Reset devices (pre-charge to VDD on clock low)
- Full-swing rail-to-rail output

Course sim shows input ramp with multiple output transitions (sweeping common-mode or stepping differential input).

## Course Structure (3 Steps)

### Step 1 — Follow-Along Build (그대로 따라해보기)
- [ ] Build StrongARM latch per course
- [ ] Transient: ramp differential input, observe decision point
- [ ] Measure: clock-to-out delay, input-referred offset (input sweep method)

### Step 2 — High-Speed Improvement
Goal: reduce decision time (critical for high-speed ADC, SerDes). Techniques:
- **Double-tail** structure — decouples input-stage GBW from latch regeneration
- **Pre-charged latch** — both outputs start at VDD, faster regen
- **Larger latch cross-coupled devices** — faster τ_regen (trade-off: more kickback)
- [ ] Measure delay before/after
- [ ] Stress test at small ΔVIN to check metastability

### Step 3 — Low-Offset Design (Assignment)
Given spec (e.g., σ(Vos) < 1 mV, t_dec < 100 ps, VDD = 1.0 V):
- [ ] Size input pair large (W·L) → low σ(Vos)
- [ ] Consider offset-cancellation (auto-zeroing / chopper) if spec demands
- [ ] Monte Carlo (1000 runs) in ngspice to estimate σ(Vos)
- [ ] Note common-centroid layout plan for KiCad / Virtuoso step

## Key Metrics
| Metric | Typical Target |
|--------|----------------|
| Clock-to-out delay | < 100 ps (fast), < 1 ns (normal) |
| Input-referred offset | σ < 1–5 mV (MC) |
| Kickback noise | < 10 mV on reference |
| Hysteresis | 0 or controlled |
| Power | μW range |
| Metastability MTBF | P(meta) < 10⁻¹² at margin |

## Interview Questions
- Explain StrongARM operation phase-by-phase (reset / pre-amplify / regen)
- What causes input-referred offset, and how does σ scale with W·L? (Pelgrom)
- Kickback — what is it and how to reduce it?
- Metastability — what is it, and what determines the MTBF?

## Status
- [ ] Theory read
- [ ] Step 1 — StrongARM follow-along
- [ ] Step 2 — high-speed variant
- [ ] Step 3 — low-offset design + MC verified
- [ ] PVT verified
