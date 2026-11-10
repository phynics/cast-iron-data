+++
id = "ref/spell/transfiguring-touch"
kind = "spell"
title = "Transfiguring Touch"
aon = "SpellDisplay.aspx?ItemName=Transfiguring%20Touch"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "transfiguring_touch", path = "json/spells10.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "63"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 6 },
  { class = "Investigator", level = 5 },
  { class = "Occultist", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (alchemical reagents worth 1 gp or the value of the created material, whichever is more)"
range = "touch"
effects = [
  { label = "Target", value = "object touched, up to 1 cubic foot per level" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Alchemist, Investigator\
6: Arcanist, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (alchemical reagents worth 1 gp or the value of the created material, whichever is more)
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: object touched, up to 1 cubic foot per level
:::

You create an alchemical residue on your hands that gradually converts a touched, unattended,
nonmagical object into iron, paper, or wood (your choice). The spell converts at most 1 cubic foot
of material per caster level you have; if the object is larger than the maximum volume, the
transfiguration stops once that amount of matter has been converted. If your caster level is at
least 14th, you can opt to create lead. If your caster level is at least 19th, you can opt to create
precious metals. If you create a precious metal, you must use an equivalent value of alchemical
reagents as a material component (5 sp per pound of copper, 5 gp per pound of silver, 50 gp per
pound of gold, 500 gp per pound of platinum).
