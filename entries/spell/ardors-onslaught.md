+++
id = "ref/spell/ardors-onslaught"
kind = "spell"
title = "Ardor's Onslaught"
aon = "SpellDisplay.aspx?ItemName=Ardor%27s%20Onslaught"
source_ids = ["planar-adventures", "champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ardors_onslaught", path = "json/spells.json" },
]
[[sources]]
publication = "planar-adventures"
page = "39"
[[sources]]
publication = "champions-of-balance"
page = "26"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "20-ft.-radius burst" },
]
duration = "instantaneous or 1d6 rounds; see text"
saving_throw = "Will partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous or 1d6 rounds; see text
Saving throw: Will partial, see text
Spell resistance: yes
Area: 20-ft.-radius burst
:::

You unleash the power of zealous conviction to smite your enemies with a burst of pulsing metallic
energy. Only creatures with a neutral alignment component are harmed by the spell.

The spell deals 1d8 points of damage per 2 caster levels (maximum 5d8) to creatures whose alignment
is neutral with no other alignment components (with the exception of neutral outsiders, who take 1d6
points of damage per caster level, maximum 10d6). Neutral outsiders are also nauseated for 1d6
rounds. A creature can attempt a Will save to halve the damage and negate the nauseated effect.

The spell deals half damage against creatures that are chaotic neutral, lawful neutral, neutral
evil, or neutral good, and such targets are not nauseated. On a successful Will save, such a
creature reduces the damage to one-quarter the damage rolled.
