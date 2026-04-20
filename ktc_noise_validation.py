import numpy as np
import matplotlib.pyplot as plt

# ── Data ──────────────────────────────────────────────────────────────────────
# Capacitor values in Farads
C = np.array([1e-12, 2e-12, 4e-12, 8e-12, 16e-12])

# LTspice integrated noise results (Vrms)
ltspice = np.array([61.059e-6, 44.356e-6, 31.778e-6, 22.616e-6, 16.043e-6])

# Theoretical kT/C noise floor
# k = Boltzmann constant, T = 300K (27°C, matching LTspice default tnom=27)
k = 1.38e-23
T = 300
theoretical = np.sqrt(k * T / C)  # Vrms

# ── Plot ──────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# --- Left plot: noise vs capacitance (linear scale) --------------------------
ax = axes[0]
ax.plot(C * 1e12, theoretical * 1e6,
        'o--', color='steelblue', label='Theoretical √(kT/C)', linewidth=1.5)
ax.plot(C * 1e12, ltspice * 1e6,
        's-', color='tomato', label='LTspice integrated noise', linewidth=1.5)
ax.set_xlabel('Sampling capacitance (pF)')
ax.set_ylabel('Noise voltage (µVrms)')
ax.set_title('kT/C noise vs sampling capacitance')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

# --- Right plot: error vs capacitance ----------------------------------------
ax2 = axes[1]
error_pct = (theoretical - ltspice) / theoretical * 100
ax2.bar(C * 1e12, error_pct, color='steelblue', alpha=0.7, width=0.8)
ax2.set_xlabel('Sampling capacitance (pF)')
ax2.set_ylabel('Underestimate error (%)')
ax2.set_title('LTspice vs theoretical — integration bandwidth error')
ax2.grid(True, linestyle='--', alpha=0.5, axis='y')

# Annotate each bar with its value
for ci, ei in zip(C * 1e12, error_pct):
    ax2.text(ci, ei + 0.05, f'{ei:.1f}%', ha='center', fontsize=9)

plt.tight_layout()
plt.savefig('ktc_noise_validation.png', dpi=150, bbox_inches='tight')
plt.show()

print("Capacitance sweep results:")
print(f"{'C (pF)':<10} {'Theoretical (µV)':<20} {'LTspice (µV)':<18} {'Error (%)'}")
print("-" * 60)
for c, th, lt in zip(C * 1e12, theoretical * 1e6, ltspice * 1e6):
    err = (th - lt) / th * 100
    print(f"{c:<10.0f} {th:<20.3f} {lt:<18.3f} {err:.1f}%")