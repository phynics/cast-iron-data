+++
id = "ref/spell/splinter-spell-resistance"
kind = "spell"
title = "Splinter Spell Resistance"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "splinter_spell_resistance", path = "json/spells9.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "9"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Targets", value = "melee or thrown weapon or up to 50 pieces of ammunition touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bloodrager, Magus, Occultist, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates
Spell resistance: no
Targets: melee or thrown weapon or up to 50 pieces of ammunition touched
:::

You create an aura around the target weapon that weakens a foe's magical defenses. The first time
each round the weapon damages a creature with [spell resistance](ref/rule/spell-resistance), that
creature's spell resistance is reduced by 5 for 1 round. This reduction is not cumulative for
multiple attacks within the same round, even if the target is struck by different weapons, each
affected by a different casting of splinter spell resistance. However, the same creature's spell
resistance can be reduced on multiple rounds by subsequent hits.
