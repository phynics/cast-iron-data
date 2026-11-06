+++
id = "ref/spell/deflection"
kind = "spell"
title = "Deflection"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deflection", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of rubber dipped in glue)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of rubber dipped in glue)
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Descriptors: force
:::

**Sources:** Advanced Player's Guide pg 215

You surround yourself in a whirling barrier of force that sends any attack that misses you hurling
back toward its source. This applies to any melee or ranged attack directed against you so long as
it uses an attack roll to determine whether or not it strikes you. If an attack misses you, the
attacker must make a second attack roll against its own Armor Class, using all of the applicable
modifiers of the original attack and if it hits, the attacker takes the attack's damage and suffers
all the other consequences of getting struck with that attack. You cannot deflect attacks that miss
you for any reason besides a failed attack roll (such as concealment). Similarly, you cannot deflect
attacks that actually do strike you but simply fail to do any harm.
