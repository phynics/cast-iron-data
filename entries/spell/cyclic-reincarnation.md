+++
id = "ref/spell/cyclic-reincarnation"
kind = "spell"
title = "Cyclic Reincarnation"
source_ids = ["core-rulebook", "inner-sea-races", "arcane-anthology", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cyclic_reincarnation", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/reincarnate" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Medium", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Witch", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (oils worth 1,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "dead creature touched" },
]
duration = "instantaneous"
saving_throw = "none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Druid, Hunter, Medium, Shaman\
5: Witch
Casting time: 10 minutes
Components: V, S, DF, M (oils worth 1,000 gp)
Range: touch
Duration: instantaneous
Saving throw: none, see text
Spell resistance: yes
Target: dead creature touched
:::

### Cyclic Reincarnation

**Sources:** Arcane Anthology pg 13

This spell allows a dead creature that died no more than 1 year before the casting of the spell to
return to life in a body that closely resembles its original body; it functions as
[reincarnate](ref/spell/reincarnate) except as noted. Cyclic reincarnation returns the dead creature
to life in a new body of the same race that the target belonged to in life, and the new body appears
physically similar to the creature's previous one, to the extent that the creature could be easily
mistaken for its own offspring or kin. If the affected creature isn't a humanoid, there is a 75%
chance that the creature returns to life as a youth of its race, gaining the young creature simple
template instead (or becomes a juvenile, in the case of dragons and other creatures whose power is
determined by their age category).

You can use cyclic reincarnation on someone who was killed by a death effect or turned into an
undead creature and then destroyed, but non-humanoids so restored always return to life with the
young creature simple template (or as a juvenile, in the case of creatures whose power is determined
by their age category).
