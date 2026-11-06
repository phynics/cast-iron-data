+++
id = "ref/spell/what-grows-within"
kind = "spell"
title = "What Grows Within"
source_ids = ["pathfinder-113-what-grows-within"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "what_grows_within", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 swift action"
components = "V"
range = "personal"
effects = [
  { label = "Effect", value = "you" },
]
duration = "1 round/level"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Arcanist, Bard, Cleric, Druid, Hunter, Mesmerist, Oracle, Psychic, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 swift action
Components: V
Range: personal
Duration: 1 round/level
Saving throw: see text
Spell resistance: no
Effect: you
Descriptors: evil
:::

**Sources:** Pathfinder \#113: What Grows Within pg 66

> _This spell is associated with [Xhamen-Dor](ref/faith/xhamen-dor), but there are no restrictions
> on its use by others._

By speaking the name ["Xhamen-Dor,"](ref/monster/great-old-one-xhamen-dor) you infuse yourself with
the essence of the Inmost Blot and gain a +3 profane bonus on Will saving throws for the spell's
duration. When you prepare what grows within for the first time, or the first time you use it via a
spell completion or spell trigger item, you can thereafter be targeted by Xhamen-Dor's infected
dreams ability. As long as you are under the effects of what grows within, your mind-affecting
spells carry this supernatural taint within them and can infect those who succumb to those effects.
Whenever you successfully affect a creature with one of your mind-affecting spells (this requires
the target to fail its saving throw against the spell if the spell allows a save, but automatically
affects a target if the spell does not allow a saving throw), that target must also succeed at a
Fortitude saving throw against what grows within or it immediately becomes afflicted by a lesser
version of Xhamen-Dor's seeded infestation. This infestation does not expose the victim to
Xhamen-Dor's infectious dreams, but it can ultimately result in that creature's transformation into
one of the seeded. Each time you affect a creature with what grows within in this manner, the
remaining duration of what grows within is reduced by 1 round. If you affect multiple creatures in a
round, you choose the order in which they must save against the effects of what grows within, and
reduce the spell's remaining duration by 1 round each time one of them is affected by the
infestation.

**Lesser Seeded Infestation**

**Type:** Infestation

**Save:** Fortitude DC the spell's save DC

**Frequency:** 1/day

**Effect:** Constitution drain 1d4

**Cure:** None

This infestation can be cured by magic alone. A creature whose Constitution is reduced to 0 by this
infestation dies and rises from death in 1d4 rounds as a seeded creature. This is an infestation
effect.
