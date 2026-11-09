+++
id = "ref/spell/burn-corruption"
kind = "spell"
title = "Burn Corruption"
aon = "SpellDisplay.aspx?ItemName=Burn%20Corruption"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "burn_corruption", path = "json/spells2.json" },
]
[[sources]]
publication = "inner-sea-races"
page = "218"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire", "good"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bloodrager", level = 4 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Area", value = "10-ft. cube/level (S)" },
]
duration = "instantaneous"
saving_throw = "Reflex half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Bloodrager\
5: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: Reflex half
Spell resistance: yes
Area: 10-ft. cube/level (S)
Descriptors: fire, good
:::

> _The following spell is available to the indicated race or ethnicity: [Elf](ref/race/elf)_

This spell fills the area with violet flames that scour an area clean of life - especially of the
corrupted life of the Abyss. Creatures (and foliage) in the area take 1d8 points of fire damage per
2 caster levels you possess (maximum 7d8) unless they are outsiders with the chaotic and evil
subtypes or are otherwise tainted by demons, in which case they instead take 1d6 points of fire
damage per caster level (maximum 15d6). This fire damage ignores the fire resistance granted by the
demon subtype, but it does not penetrate any other form of fire resistance or immunity.
