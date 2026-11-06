+++
id = "ref/spell/phantasmal-web"
kind = "spell"
title = "Phantasmal Web"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phantasmal_web", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature/level, no two of which may be more than 30 ft. apart" },
]
duration = "1 round/level (D)"
saving_throw = "Will disbelief, then Fortitude partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 5: Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Will disbelief, then Fortitude partial, see text
Spell resistance: yes
Target: one creature/level, no two of which may be more than 30 ft. apart
Subschool: Phantasm
Descriptors: mind-affecting
:::

**Sources:** Advanced Player's Guide pg 235

You implant within the minds of your targets the illusion that they are engulfed in tangled webs
teeming with swarms of tiny spiders. Those who fail to disbelieve the phantasmal web are treated as
if in a [web](ref/spell/web) spell, but must also make a Fortitude save at the beginning of each
turn or become nauseated for that round by the phantasmal spiders.

As the phantasmal web exists only in the minds of the targets, it cannot be burned or destroyed, and
it provides no cover (though it does provide [concealment](ref/rule/concealment)) against attacks
made by the targets. Targets cannot escape the phantasmal web by moving, even by teleportation.
[Freedom of movement](ref/spell/freedom-of-movement) allows unobstructed movement but does not
negate the concealment or nausea effects.

Targets of the spell perceive everyone else around them to be engulfed in webs and swarming spiders,
but the spell has no visible effect to other creatures (who may assist allies to disbelieve the
effect).
