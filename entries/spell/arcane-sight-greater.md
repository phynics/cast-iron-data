+++
id = "ref/spell/arcane-sight-greater"
kind = "spell"
title = "Greater Arcane Sight"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_sight_greater", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/arcane-sight" },
]
[[sources]]
publication = "core-rulebook"
page = "244"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 7: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Target: you
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
:::

### Greater Arcane Sight

This spell functions like [arcane sight](ref/spell/arcane-sight), except that you automatically know
which spells or magical effects are active upon any individual or object you see.

Unlike arcane sight, this spell cannot be made permanent with a permanency spell.
