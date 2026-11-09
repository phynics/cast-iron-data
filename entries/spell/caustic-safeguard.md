+++
id = "ref/spell/caustic-safeguard"
kind = "spell"
title = "Caustic Safeguard"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "caustic_safeguard", path = "json/spells2.json" },
]
[[sources]]
publication = "agents-of-evil"
page = "30"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["acid"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 round"
components = "V, S, M (a thin metal wire and a vial of acid)"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "1 hour/level (D)"
saving_throw = "Reflex half (see text)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Alchemist, Bloodrager, Investigator, Magus\
4: Arcanist, Sorcerer, Wizard
Casting time: 1 round
Components: V, S, M (a thin metal wire and a vial of acid)
Range: touch
Duration: 1 hour/level (D)
Saving throw: Reflex half (see text)
Spell resistance: no
Target: object touched
Descriptors: acid
:::

You imbue a single object with an acidic protective ward. Any creature other than you that touches
the object takes 1d6 points of acid damage per 2 caster levels (maximum 10d6; Reflex half). Each
time the spell discharges, the number of damage dice it deals is halved (rounded down); when the
spell's damage dice reach 0, the spell ends. While casting this spell, you can touch up to one
creature per 4 caster levels, which allows them to handle the warded object without triggering this
spell.
