+++
id = "ref/spell/daybreak-arrow"
kind = "spell"
title = "Daybreak Arrow"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "daybreak_arrow", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "up to 50 pieces of ammunition, all of which must be together at the time of casting" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Cleric, Inquisitor, Occultist, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: up to 50 pieces of ammunition, all of which must be together at the time of casting
Descriptors: light
:::

**Sources:** Ultimate Combat pg 226

You cause ammunition, including shuriken, to exude radiant energy. Creatures that take penalties in
bright light take these penalties for 1 round after being struck by such ammunition. Undead and
creatures harmed by sunlight take an additional 1d6 points of damage from such projectiles. This
extra damage and half of any other damage you deal with an affected projectile results directly from
radiant energy and is not subject to damage resistance. Such a projectile sheds light as if it were
a sunrod for 1 round after it is fired or thrown.
