"""Text-free TikZ room diagram: visit heatmap, policy, and room pictograms."""

from pathlib import Path
import xml.etree.ElementTree as ET


def export_vacuum_tikz(path, grid, mdp, dtmc, scheduler, visits, variables):
    height, width = len(grid), len(grid[0])
    icon = ET.parse(Path(__file__).parent / "assets" / "wi-thunderstorm.svg")
    storm_path = " ".join(icon.getroot().find("{http://www.w3.org/2000/svg}path").attrib["d"].split())
    bump = next(v for v in mdp.state_valuations.get_all_variables() if v.name == "bump")

    def key(values, state):
        return tuple(values.get_value(state, variables[name]) for name in ("x", "y", "started")) + (
            values.get_value(state, bump),
        )

    occupied = {key(dtmc.state_valuations, s.id) for s in dtmc.states if visits[s.id] > 0}
    arrows = {}
    for state in mdp.states:
        x, y, started, _ = key(mdp.state_valuations, state.id)
        if not started or key(mdp.state_valuations, state.id) not in occupied:
            continue
        choice = scheduler.get_choice(state).get_deterministic_choice()
        for action in state.actions[choice].labels:
            if action in ("north", "south", "east", "west"):
                arrows.setdefault((x, y), set()).add(action)

    maximum = 20

    def heat_mix(value):
        # A power-law color response gives low visiting times more contrast.
        # The legend retains numeric 0--20 positions and uses this same mapping.
        return 85 * min(max(value / maximum, 0), 1) ** .6

    def displayed_visits(x, y, time):
        # Display visits before termination: terminal locations contribute zero,
        # rather than lifetime occupancy from their absorbing self-loops.
        terminal = (y == 3 and x <= 1) or (x == 3 and y <= 1) or (x == 4 and y == 3)
        return 0 if terminal else float(time)
    lines = [r"\documentclass[border=1pt]{standalone}",
             r"\usepackage{tikz}", r"\usetikzlibrary{arrows.meta,svg.path}",
             r"\definecolor{gridcol}{RGB}{43,52,69}",
             r"\definecolor{cellcol}{RGB}{244,245,247}",
             r"\definecolor{heatcol}{RGB}{83,139,180}",
             r"\definecolor{catcol}{RGB}{239,159,39}",
             r"\definecolor{stormyellow}{RGB}{244,190,25}",
             r"\definecolor{hazardcell}{RGB}{252,235,235}",
             r"\definecolor{hazardstk}{RGB}{163,45,45}",
             r"\definecolor{goalcell}{RGB}{234,243,222}",
             r"\definecolor{goalcol}{RGB}{59,109,17}",
             r"\definecolor{optimalcol}{RGB}{72,65,55}",
             r"\definecolor{optimalslipcol}{RGB}{137,125,108}",
             r"\definecolor{causestk}{RGB}{133,79,11}",
             r"\definecolor{rovercol}{RGB}{93,202,165}",
             r"\definecolor{rovedge}{RGB}{15,110,86}",
             r"\begin{document}",
             r"\begin{tikzpicture}[x=1.15cm,y=1.05cm,line cap=round,line join=round]",
             r"% Visits before termination: 0--20 heat scale, power-law color response (gamma .6).",
             r"% Terminal cells are zero; legend colors use the identical mapping.",
             r"% Room pictograms use the vacuum model's fixed geometry; the cat is decorative."]
    for y, row in enumerate(grid):
        for x, time in enumerate(row):
            value = displayed_visits(x, y, time)
            fill = f"heatcol!{heat_mix(value):.2f}!cellcol"
            lines.append(fr"\fill[{fill}] ({x},{y}) rectangle ({x+1},{y+1});")

    # Fine grid and strong outside border, as in the reference figure.
    for x in range(width + 1):
        lines.append(fr"\draw[gridcol!25,line width=.3pt] ({x},0) -- ({x},{height});")
    for y in range(height + 1):
        lines.append(fr"\draw[gridcol!25,line width=.3pt] (0,{y}) -- ({width},{y});")
    lines.append(fr"\draw[gridcol,line width=.85pt] (0,0) rectangle ({width},{height});")

    # One large carpet across all four rug cells. Its woven border and fringe
    # identify the surface without covering the per-cell heatmap.
    lines += [r"\draw[causestk,line width=1.1pt,rounded corners=2pt] (1.08,1.08) rectangle (2.92,2.92);",
              r"\draw[causestk!70,line width=.45pt] (1.14,1.14) rectangle (2.86,2.86);",
              r"\foreach \t in {1.18,1.28,...,2.88} {\draw[causestk!80,line width=.6pt] (\t,1.01)--(\t,1.08) (\t,2.92)--(\t,2.99);}",
              r"\foreach \t in {1.18,1.28,...,2.88} {\draw[causestk!80,line width=.6pt] (1.01,\t)--(1.08,\t) (2.92,\t)--(2.99,\t);}"]

    # A single staircase spanning both upper-left cells.
    lines += [r"\begin{scope}[shift={(.08,3.06)},xscale=1.12,yscale=1.43]",
              r"\fill[hazardstk!12] (0,0)--(0,.15)--(.41,.15)--(.41,.30)--(.82,.30)--(.82,.45)--(1.23,.45)--(1.23,.60)--(1.64,.60)--(1.64,0)--cycle;",
              r"\draw[hazardstk,line width=.9pt] (0,0)--(0,.15)--(.41,.15)--(.41,.30)--(.82,.30)--(.82,.45)--(1.23,.45)--(1.23,.60)--(1.64,.60);",
              r"\draw[hazardstk!45,line width=.5pt] (.41,0)--(.41,.15) (.82,0)--(.82,.30) (1.23,0)--(1.23,.45);",
              r"\end{scope}"]

    # A two-seat sofa spanning both sofa cells, with slender outlined cushions.
    lines += [r"\begin{scope}[shift={(3.07,.12)},xscale=1.34,yscale=1.10]",
              r"\filldraw[fill=hazardstk!9,draw=hazardstk,line width=.9pt,rounded corners=3pt] (0,0) rectangle (.64,1.60);",
              r"\filldraw[fill=hazardcell,draw=hazardstk,line width=.65pt,rounded corners=2pt] (.12,.12) rectangle (.53,.77);",
              r"\filldraw[fill=hazardcell,draw=hazardstk,line width=.65pt,rounded corners=2pt] (.12,.83) rectangle (.53,1.48);",
              r"\draw[hazardstk,line width=.9pt] (.06,.08)--(.06,1.52);",
              r"\draw[hazardstk,line width=1pt] (.11,-.05)--(.11,0) (.53,-.05)--(.53,0) (.11,1.60)--(.11,1.65) (.53,1.60)--(.53,1.65);",
              r"\end{scope}"]

    # Sleeping cat on the upper cushion, in the same thin-line pictogram style.
    lines += [r"\begin{scope}[shift={(3.51,1.42)},scale=.8]",
              r"\filldraw[fill=catcol!20,draw=causestk,line width=.7pt] (0,0) ellipse (.21 and .12);",
              r"\draw[causestk,line width=.8pt] (.15,-.04) .. controls (.35,-.12) and (.39,.13) .. (.22,.12);",
              r"\filldraw[fill=catcol!20,draw=causestk,line width=.7pt] (-.20,.02)--(-.21,.22)--(-.10,.16)--(-.02,.16)--(.08,.22)--(.07,.02)--cycle;",
              r"\draw[causestk,line width=.55pt] (-.16,.08)--(-.11,.06) (-.03,.06)--(.02,.08);",
              r"\draw[causestk,line width=.4pt] (-.22,.02)--(-.30,.04) (.08,.02)--(.16,.04);",
              r"\end{scope}"]

    # Dock: green charging cradle with the actual Weather Icons Storm glyph.
    lines += [r"\begin{scope}[shift={(4.19,3.25)}]",
              r"\fill[goalcol!16] (0,0) rectangle (.62,.47);",
              r"\draw[goalcol,line width=.9pt] (0,.47)--(0,0)--(.62,0)--(.62,.47);",
              r"\draw[goalcol,line width=1pt] (.16,.08)--(.23,.08) (.39,.08)--(.46,.08);",
              r"\end{scope}",
              r"% wi-thunderstorm: Weather Icons (Lukas Bischoff / Erik Flowers), SIL OFL 1.1.",
              r"\begin{scope}[shift={(4.50,3.55)}]",
              r"\pgftransformscale{.52}\pgftransformyscale{-1}",
              r"\pgftransformshift{\pgfpoint{-15pt}{-17.7pt}}",
              fr'\fill[stormyellow] svg "{storm_path}";',
              r"\end{scope}"]

    # Three equally likely start positions; these are alternative starts,
    # not three simultaneous robots. Keep each clear of policy/slip arrows.
    for x in (0, 2, 4):
        lines += [fr"\begin{{scope}}[shift={{({x+.25},.2567)}},scale=1.5]",
                  r"\filldraw[fill=rovercol!35,draw=rovedge,line width=.75pt] (0,0) circle (.12);",
                  r"\draw[rovedge!65,line width=.5pt] (0,0) circle (.085);",
                  r"\fill[rovedge] (0,.035) circle (.022);",
                  r"\draw[rovedge,line width=.65pt] (-.065,-.055)--(.065,-.055);",
                  r"\end{scope}"]

    # Strong central arrows, retaining all choices at visited bump variants.
    lines.append(r"% Thick arrows: intended policy moves. Thin arrows: both sideways slips.")
    lines.append(r"% Slip arrows show attempted directions, including wall-blocked moves.")
    directions = {"north": (0, 1), "south": (0, -1), "east": (1, 0), "west": (-1, 0)}
    for (x, y), actions in sorted(arrows.items()):
        slips = set()
        for action in actions:
            dx, dy = directions[action]
            slips.update(((-dy, dx), (dy, -dx)))
        for dx, dy in sorted(slips):
            sx, sy = x + .5 + .12 * dx, y + .5 + .12 * dy
            ex, ey = x + .5 + .32 * dx, y + .5 + .32 * dy
            lines.append(fr"\draw[-{{Latex[length=3.4pt,width=3.4pt]}},optimalslipcol,line width=1.1pt] ({sx:.4f},{sy:.4f}) -- ({ex:.4f},{ey:.4f});")
        for action in sorted(actions):
            dx, dy = directions[action]
            sx, sy = x + .5 - .165 * dx, y + .5 - .165 * dy
            ex, ey = x + .5 + .30 * dx, y + .5 + .30 * dy
            lines.append(fr"\draw[-{{Latex[length=6.5pt,width=6.5pt]}},optimalcol,line width=2.6pt] ({sx:.4f},{sy:.4f}) -- ({ex:.4f},{ey:.4f});")
    # Render the scale with exactly the same color mixtures as the cells,
    # rather than PGF's independently interpolated shading.
    for i in range(256):
        left = .10 + 4.80 * i / 256
        right = .10 + 4.80 * (i + 1) / 256
        lines.append(fr"\fill[heatcol!{heat_mix(maximum*i/255):.2f}!cellcol] ({left:.5f},-.23) rectangle ({right:.5f},-.10);")
    lines.append(r"\draw[gridcol!40,line width=.35pt] (.10,-.23) rectangle (4.90,-.10);")
    for fraction in (0, .25, .5, .75, 1):
        x = .10 + 4.80 * fraction
        lines.append(fr"\draw[gridcol!60,line width=.4pt] ({x:.4f},-.23)--({x:.4f},-.27);")
        lines.append(fr"\node[anchor=north,inner sep=1pt,text=gridcol,font=\sffamily\scriptsize] at ({x:.4f},-.28) {{{maximum*fraction:.0f}}};")
    lines += [r"\end{tikzpicture}", r"\end{document}"]
    Path(path).write_text("\n".join(lines) + "\n")
