+++
id = "ref/spell/elemental-assessor"
kind = "spell"
title = "Elemental Assessor"
source_ids = ["chronicle-of-the-righteous"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "elemental_assessor", path = "json/spells4.json" },
]
[[sources]]
publication = "chronicle-of-the-righteous"
page = "50"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["acid", "cold", "electricity", "fire"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (four needles)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one elemental ray" },
]
duration = "1d4+1 rounds (see text)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (four needles)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1d4+1 rounds (see text)
Saving throw: none
Spell resistance: yes
Effect: one elemental ray
Descriptors: acid, cold, electricity, fire
:::

Azata champions developed this spell to deal with fiends with unknown resistances. A ray of
spiraling colors springs from your hand and streaks to its target. You must make a successful ranged
touch attack to hit your target with the ray, which deals 2d6 points of acid damage, 2d6 points of
cold damage, 2d6 points of electricity damage, and 2d6 points of fire damage. The type of energy
that does the most points of damage to the target then persists, dealing another 4d6 points of that
type of damage per round for 1d4 rounds.
