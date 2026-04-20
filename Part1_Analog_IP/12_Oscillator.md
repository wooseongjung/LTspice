# 12_Oscillator — Ring Oscillator / VCO

## Course Reference
Inflearn — Section 4 Lectures 25-27

## Primary Tool
LTspice (transient + FFT) + Qucs-S (cross-validation)

## Reference Topology (from course images)
Current-starved ring oscillator:
- Odd number of inverter stages (3, 5, 7)
- NMOS + PMOS current-limiting devices per stage (freq tunable via bias)
- Output buffer for load isolation
- Course shows time-domain waveform + spectrum (FFT for phase-noise / jitter)

## Course Structure (3 Steps)

### Step 1 — Follow-Along Build (그대로 따라해보기)
- [ ] Build 5-stage current-starved ring
- [ ] Transient: plot oscillation, measure f₀
- [ ] FFT of output to observe fundamental + harmonics
- [ ] Sweep control voltage → measure Kvco (Hz/V)

### Step 2 — Noise + Jitter Improvement
Goal: reduce period jitter and phase-noise skirt. Techniques:
- **Larger devices** → less 1/f noise
- **Differential delay stages** instead of single-ended → CM supply-noise rejection
- **Supply regulation** (internal LDO) to kill supply-pushing
- **More stages with smaller per-stage delay** (trade area for noise)
- [ ] Long `.tran` + FFT to measure phase noise at 1 MHz offset
- [ ] Compute cycle-to-cycle jitter

### Step 3 — Area + Power Optimization (Assignment)
Given spec (e.g., f₀ = 100 MHz, PN < −80 dBc/Hz @ 1 MHz, area < 500 μm²):
- [ ] Minimize total Σ(W·L) × N_stages
- [ ] Minimize I_bias × VDD × N_stages
- [ ] Maintain PN target — use Leeson trade-space (P, Q, Δf)
- [ ] Verify PVT

## Key Metrics
| Metric | Target |
|--------|--------|
| f₀ | course-specified |
| Kvco (VCO variant) | stable, monotonic |
| Phase noise @ 1 MHz | < −80 dBc/Hz |
| Period jitter (rms) | < 10 ps |
| Power | mW or sub-mW |
| Supply pushing | < 10 MHz/V |

## Phase Noise Basics
- **Leeson's equation**: L(Δf) ∝ (kT / P_sig) × (f₀ / Q·Δf)²
- Ring oscillators have low effective Q → high PN compared to LC VCOs
- 1/f noise upconverts to close-in phase noise via nonlinearity (1/Δf³ region)

## Interview Questions
- Ring vs LC vs crystal — trade-offs (Q, power, tunability, integration)
- Why does phase noise have a 1/f³ region close to carrier?
- How does supply noise couple into jitter?
- Leeson's equation — explain each term

## Status
- [ ] Theory read
- [ ] Step 1 — ring oscillator follow-along
- [ ] Step 2 — noise / jitter improved
- [ ] Step 3 — area + power optimized
- [ ] FFT phase-noise measurement done
