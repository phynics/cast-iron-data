+++
id = "ref/spell/retribution"
kind = "spell"
title = "Retribution"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "retribution", path = "json/spells8.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "239"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil", "pain"]
levels = [
  { class = "Inquisitor", level = 3 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature who has just struck you with an attack" },
]
duration = "1 round/level"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Inquisitor
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude partial
Spell resistance: yes
Target: one creature who has just struck you with an attack
Descriptors: evil, pain
:::

Retribution blasts those who have the temerity to assault your person. You may target anyone who has
just struck you with an attack within the previous round, whether with a melee, ranged, or natural
weapon, or a spell that requires an attack roll. The target is wracked with shooting pains that
impose a -4 penalty on attack rolls, skills checks, and ability checks. On a successful Fortitude
save, the penalty only lasts for 1 round. A target who worships the same god as you takes a -2
penalty on its saving throw.
