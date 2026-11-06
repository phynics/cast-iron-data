+++
id = "ref/spell/holy-smite"
kind = "spell"
title = "Holy Smite"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "holy_smite", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good"]
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
Area: 20-ft.-radius burst
Descriptors: good
:::

**Sources:** PRPG Core Rulebook pg 297

You draw down holy power to smite your enemies. Only evil and neutral creatures are harmed by the
spell; good creatures are unaffected.

The spell deals 1d8 points of damage per two caster levels (maximum 5d8) to each evil creature in
the area (or 1d6 points of damage per caster level, maximum 10d6, to an evil outsider) and causes it
to become blinded for 1 round. A successful Will saving throw reduces damage to half and negates the
blinded effect.

The spell deals only half damage to creatures who are neither good nor evil, and they are not
blinded. Such a creature can reduce that damage by half (down to one-quarter of the roll) with a
successful Will save.

### Mythic Holy Smite

**Sources:** Mythic Adventures pg 98\
The damage dealt to evil outsiders increases to 1d10 points of damage per caster level (maximum
10d10) and the damage dealt to other evil creatures increases to 1d12 points of damage per 2 caster
levels (maximum 5d12). The duration that creatures in the area are blinded increases to 2 rounds. On
a successful save, an evil creature is blinded for 1 round.
