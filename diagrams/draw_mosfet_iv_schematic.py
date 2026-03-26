"""
Generate MOSFET I-V curve test circuit schematic using schemdraw.
Circuit: NMOS with Vgs and Vds sources for DC sweep characterisation.
"""

import schemdraw
import schemdraw.elements as elm

with schemdraw.Drawing(show=False) as d:
    d.config(fontsize=13, unit=3)

    # --- Vgs source (left column) ---
    # Start at bottom-left GND, go up through Vgs to gate level
    d.add(elm.Ground().at((0, 0)))
    vgs = d.add(elm.SourceV().up().at((0, 0.3)).label('Vgs', loc='left'))

    # --- Wire from Vgs top to Gate ---
    d.add(elm.Line().right(2).at(vgs.end))

    # --- NMOS transistor ---
    mosfet = d.add(elm.NMos().anchor('gate')
                   .label('M1', loc='right', ofst=0.2))

    # --- Wire from Drain up, then left, then down through Vds to GND ---
    drain_pos = mosfet.drain
    d.add(elm.Line().up(0.5).at(drain_pos))
    d.add(elm.Line().left(4.5))
    vds = d.add(elm.SourceV().down().reverse().label('Vds', loc='left'))
    d.add(elm.Line().down(0.3))
    d.add(elm.Ground())

    # --- Source to GND ---
    d.add(elm.Line().at(mosfet.source).down(0.5))
    d.add(elm.Ground())

    # --- SPICE directives annotation ---
    d.add(elm.Annotate().at((5, 1)).delta(0, 0)
          .label('.model MyNMOS NMOS\n  (Level=1 Vto=0.5 Kp=200u)\n\n'
                 '.dc Vds 0 3.3 0.01\n     Vgs 0 3.3 0.5',
                 halign='left', valign='top'))

    d.save('mosfet_iv_schematic.png', dpi=200)
    d.save('mosfet_iv_schematic.svg')

print("Saved: mosfet_iv_schematic.png and .svg")
