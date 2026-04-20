# 03 — Qucs / Qucs-S Setup

## Role in Toolchain
Schematic-driven simulator (Qucs-S uses ngspice/Xyce backend). Best for:
- RF / S-parameter analysis
- Cross-validation of LTspice results
- Noise analysis visualization

## Install on macOS
```bash
brew install --cask qucs-s
# or build from source if homebrew cask unavailable
```

## When to Use Qucs
- Small-signal S-parameter analysis
- Comparing LTspice results with a second simulator
- Harmonic balance simulation

## Exercise
- [ ] Install Qucs-S
- [ ] Port one LTspice schematic to Qucs
- [ ] Compare AC sweep results

## Status
- [ ] Completed
