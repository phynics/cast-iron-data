+++
id = "ref/spell/dongun-shapers-touch"
kind = "spell"
title = "Dongun Shaper's Touch"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dongun_shapers_touch", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Investigator", level = 2 },
  { class = "Occultist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "concentration, up to 1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Investigator\
3: Arcanist, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: concentration, up to 1 round/level
Saving throw: none
Spell resistance: no
Target: object touched
:::

**Sources:** Inner Sea Intrigue pg 59

You create an alchemical residue on your hands that allows you to reshape any nonmagical, unattended
object with [hardness](ref/umr/hardness) 19 or less as though it were clay. Objects with hardness 9
or less are like soft clay, allowing you to reshape up to 1 cubic foot per round of effort. Objects
with hardness 10 or higher are harder to mold, allowing you to reshape up to 1/4 cubic foot per
round. The object retains its new shape for 24 hours before returning to its original shape. This
spell does not allow you to reshape a portion of a large object, such as a wall; you must be able to
reshape the entire target within the spell's duration or the spell fizzles and has no effect.
