+++
id = "ref/spell/orders-wrath"
kind = "spell"
title = "Order's Wrath"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "orders_wrath", path = "json/spells7.json" },
]
[[sources]]
publication = "core-rulebook"
page = "317"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["lawful"]
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
  { label = "Area", value = "nonlawful creatures within a burst that fills a 30-ft. cube" },
]
duration = "instantaneous (1 round); see text"
saving_throw = "Will partial; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous (1 round); see text
Saving throw: Will partial; see text
Spell resistance: yes
Area: nonlawful creatures within a burst that fills a 30-ft. cube
Descriptors: lawful
:::

You channel lawful power to smite enemies. The power takes the form of a three-dimensional grid of
energy. Only chaotic and neutral (not lawful) creatures are harmed by the spell.

The spell deals 1d8 points of damage per two caster levels (maximum 5d8) to chaotic creatures (or
1d6 points of damage per caster level, maximum 10d6, to chaotic outsiders) and causes them to be
dazed for 1 round. A successful Will save reduces the damage to half and negates the daze effect.

The spell deals only half damage to creatures who are neither chaotic nor lawful, and they are not
dazed. They can reduce the damage in half again (down to one-quarter of the roll) with a successful
Will save.
