+++
id = "ref/spell/produce-flame"
kind = "spell"
title = "Produce Flame"
source_ids = ["core-rulebook", "heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "produce_flame", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "flame in your palm" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S
Range: 0 ft.
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: yes
Effect: flame in your palm
Descriptors: fire
:::

**Sources:** PRPG Core Rulebook pg 326

Flames as bright as a torch appear in your open hand. The flames harm neither you nor your
equipment.

In addition to providing illumination, the flames can be hurled or used to touch enemies. You can
strike an opponent with a melee touch attack, dealing fire damage equal to 1d6 + 1 point per caster
level (maximum +5). Alternatively, you can hurl the flames up to 120 feet as a thrown weapon. When
doing so, you attack with a ranged touch attack (with no range penalty) and deal the same damage as
with the melee attack. No sooner do you hurl the flames than a new set appears in your hand. Each
attack you make reduces the remaining duration by 1 minute. If an attack reduces the remaining
duration to 0 minutes or less, the spell ends after the attack resolves.

This spell does not function underwater.
