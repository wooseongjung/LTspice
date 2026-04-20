# 10_Level_Shifter — Level Shifter

## Course Reference
Inflearn — Section 4 Lectures 19-21

## Primary Tool
LTspice (digital transient + corner sims)

## Why Level Shifters?
Modern SoCs have multiple voltage domains (core 0.8 V, IO 1.8/3.3 V, analog 1.2 V). Signals crossing domains need translation without excessive static current or delay.

## Reference Topology (from course images)
Course surveys multiple topologies side-by-side. Start with **cross-coupled PMOS (DCVS) shifter**:
- Two PMOS cross-coupled at high domain (VDDH) → latch-like
- NMOS pull-down at low domain (VDDL)
- Complementary NMOS inputs
- Rail-to-rail, zero static current

Course image also shows current-mirror and stacked variants for comparison.

## Course Structure (3 Steps)

### Step 1 — Follow-Along Build (그대로 따라해보기)
- [ ] Build DCVS cross-coupled shifter
- [ ] Transient: square wave at VDDL, verify rail-to-rail VDDH output
- [ ] Measure propagation delay tpLH, tpHL

### Step 2 — Wide-Range + Low-Power Improvement
Goal: operate over wide VDDL range (e.g., 0.4 V → 1.8 V) with minimal dynamic + static current. Techniques:
- **Current-mirror-based shifter** for sub-threshold VDDL
- **Split-gate / stacked** topologies to avoid PMOS contention at low VDDL
- **Dynamic body biasing** or feedback to speed up weak pull-up
- [ ] Sweep VDDL 0.4 V → 1.8 V, verify functional + measure delay
- [ ] Measure average current (leakage + switching)

### Step 3 — Low-Power + Rising-Time Optimization (Assignment)
Given spec (e.g., VDDL = 0.6 V, VDDH = 1.8 V, f = 100 MHz, CL = 10 fF):
- [ ] Minimize total power (dynamic + leakage)
- [ ] Minimize rising time tR (drives downstream skew / jitter)
- [ ] Balance tR / tF symmetry (duty-cycle distortion)
- [ ] Verify PVT corners

## Key Metrics
| Metric | Target |
|--------|--------|
| Propagation delay | < 1 ns |
| Rising time (10–90%) | minimize — Step 3 |
| Static current | ~0 (pure CMOS) |
| Dynamic current | minimize — Step 3 |
| Minimum VDDL | sub-threshold capable |
| Duty-cycle distortion | < 5% |

## Interview Questions
- Why does DCVS fail at very low VDDL? (PMOS pull-up can't overcome NMOS at deep sub-VT)
- PMOS-only vs NMOS-only pull-up structures — trade-offs
- How to handle signals going *from high-V to low-V* domain?

## Status
- [ ] Theory read
- [ ] Step 1 — DCVS follow-along
- [ ] Step 2 — wide-range + low-power variant
- [ ] Step 3 — tR + power optimized
- [ ] PVT verified
