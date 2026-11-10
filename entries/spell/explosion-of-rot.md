+++
id = "ref/spell/explosion-of-rot"
kind = "spell"
title = "Explosion of Rot"
aon = "SpellDisplay.aspx?ItemName=Explosion%20of%20Rot"
source_ids = ["ultimate-wilderness", "champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "explosion_of_rot", path = "json/spells4.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "229"
[[sources]]
publication = "champions-of-balance"
page = "25"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a rotting flower)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "10-ft.-radius burst" },
]
duration = "instantaneous"
saving_throw = "Reflex half (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Druid, Hunter
Casting time: 1 standard action
Components: V, S, M (a rotting flower)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Reflex half (see text)
Spell resistance: yes
Area: 10-ft.-radius burst
:::

You call forth a burst of decay that ravages all creatures in the area. Even nonliving creatures
such as constructs and undead crumble or wither in this malignant eruption of rotting energy.
Creatures in the area of effect take 1d6 points of damage per caster level (maximum 15d6) and are
staggered for 1d4 rounds. A target that succeeds at a Reflex saving throw takes half damage and
negates the staggered effect. Plant creatures are particularly susceptible to this rotting effect; a
plant creature caught in the burst takes a -2 penalty on the saving throw and takes 1 extra point of
damage per die.
