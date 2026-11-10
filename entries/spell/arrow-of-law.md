+++
id = "ref/spell/arrow-of-law"
kind = "spell"
title = "Arrow of Law"
aon = "SpellDisplay.aspx?ItemName=Arrow%20of%20Law"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arrow_of_law", path = "json/spells.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "207"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["lawful"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "arrow-shaped projectile of lawful energy" },
]
duration = "instantaneous (1 round); see text"
saving_throw = "Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Cleric, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous (1 round); see text
Saving throw: Will partial (see text)
Spell resistance: yes
Effect: arrow-shaped projectile of lawful energy
Descriptors: lawful
:::

You fire a shimmering arrow of pure order from your holy symbol at any one target in range as a
ranged touch attack. A chaotic creature struck by an arrow of law takes 1d8 points of damage per two
caster levels (maximum 5d8). A chaotic outsider instead takes 1d6 points of damage per caster level
(maximum 10d6) and is dazed for 1 round. A successful Will save reduces the damage to half and
negates the daze effect. This spell deals only half damage to creatures that are neither chaotic nor
lawful, and they are not dazed. The arrow has no effect on lawful creatures.
