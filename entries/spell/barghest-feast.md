+++
id = "ref/spell/barghest-feast"
kind = "spell"
title = "Barghest Feast"
source_ids = ["pathfinder-117-assault-on-longshadow"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "barghest_feast", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["evil"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Investigator", level = 3 },
]
casting_time = "1 standard action"
components = "S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level; see text"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Investigator
Casting time: 1 standard action
Components: S
Range: touch
Duration: 10 minutes/level; see text
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Descriptors: evil
:::

**Sources:** Pathfinder \#117: Assault on Longshadow pg 76

> _[Hobgoblin](ref/race/hobgoblin) alchemists devoted to [Hadregash](ref/faith/hadregash) have
> developed the following extract to empower themselves and their allies or to make prey easier to
> catch and enslave._

The target gains the ability to absorb power from devouring a humanoid corpse. To use this ability,
the target must feed on the corpse of one nonevil humanoid creature, a process that takes 1 full
round per Hit Die the creature had and provokes attacks of opportunity. For every 2 rounds it feeds
on the corpse in this way, the target gains a +1 profane bonus on attack rolls, saving throws, and
skill checks (to a maximum of +5).
