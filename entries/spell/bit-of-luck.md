+++
id = "ref/spell/bit-of-luck"
kind = "spell"
title = "Bit of Luck"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bit_of_luck", path = "json/spells12.json" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "7"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a four-leaf clover)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Bard, Skald\
4: Alchemist, Arcanist, Cleric, Investigator, Oracle, Psychic, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a four-leaf clover)
Range: personal
Duration: 10 minutes/level
Saving throw: none
Spell resistance: no
Target: you
:::

> _The following spell was created by [catfolk](ref/race/catfolk) and make use of their inherent
> luck._

For the spell's duration, the caster gains a reservoir of luck with a total number of points equal
to 1 point per 2 caster levels. During the spell's duration, the caster can spend 1 point from this
reservoir when making an attack roll or skill check to add a +1d8 luck bonus to the d20 roll's
result. This bonus can be added before or after the roll or check's result is revealed, and if this
bonus is large enough to turn a failure into a success, the roll succeeds. The spell instantly ends
when all points are expended or when it is cast on the target again.

An 8th-level caster can instead spend 4 points to add a +2d8 luck bonus, and a 16th-level caster can
spend 8 luck points to instead add a +3d8 luck bonus.
