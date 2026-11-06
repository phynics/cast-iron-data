+++
id = "ref/spell/goodberry"
kind = "spell"
title = "Goodberry"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "goodberry", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Targets", value = "2d4 fresh berries touched" },
]
duration = "1 day/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Druid, Hunter, Shaman
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 day/level
Saving throw: none
Spell resistance: yes
Targets: 2d4 fresh berries touched
:::

**Sources:** PRPG Core Rulebook pg 291

Casting goodberry makes 2d4 freshly picked berries magical. You (as well as any other druid of 3rd
or higher level) can immediately discern which berries are affected. Each transmuted berry provides
nourishment as if it were a normal meal for a Medium creature. The berry also cures 1 point of
damage when eaten, subject to a maximum of 8 points of such curing in any 24-hour period.

### Mythic Goodberry

**Sources:** Mythic Adventures pg 96\
Each berry provides a full day's nourishment and counts as 1 hour of complete rest for the purpose
of removing exhaustion, fatigue, or nonlethal damage.

_Augmented (2nd):_ You can cast the spell to affect only one berry, imbuing into that berry any
harmless druid spell you have prepared. The spell remains stored in the berry for the duration of
the goodberry spell or until the berry is consumed. A creature that eats the berry gains the
benefits of that spell as if you had cast it upon her. The maximum level of the imbued spell is
equal to half your tier, and you must expend one use of mythic power for each spell level of the
imbued spell (in addition to the one use needed to cast mythic goodberry). Similar to imbue with
spell ability, you can't prepare a spell in that spell's slot until the berry is consumed or the
mythic goodberry spell ends.
