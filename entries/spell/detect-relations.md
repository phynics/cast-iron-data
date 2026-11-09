+++
id = "ref/spell/detect-relations"
kind = "spell"
title = "Detect Relations"
source_ids = ["quests-and-campaigns"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_relations", path = "json/spells3.json" },
]
[[sources]]
publication = "quests-and-campaigns"
page = "28"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a seed)"
range = "*The original source did not include a range line*"
effects = [
  { label = "Targets", value = "one creature per level, no two of which can be more than 30 ft. apart" },
]
duration = "concentration, up to 1 min./level (D)"
saving_throw = "Will negates, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Bard, Cleric, Inquisitor, Oracle, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, F/DF (a seed)
Range: \*The original source did not include a range line\*
Duration: concentration, up to 1 min./level (D)
Saving throw: Will negates, see text
Spell resistance: no
Targets: one creature per level, no two of which can be more than 30 ft. apart
:::

You can determine whether or not two or more creatures are related by blood. The amount of
information gleaned depends on how long you study a particular area or set of subjects.

_1st round:_ Whether or not the subjects are related by blood.

_2nd round:_ Number of related subjects and their general relation to one another (for example, this
would reveal that one subject is a descendant of the other, but it would not specify "mother" or
"grandmother").

_3rd round:_ Precise relationship between subjects in the area. A target's Will save prevents you
from determining its exact relationship with another creature, and only one subject needs to succeed
at this save to prevent you from determining its relationship with another creature. (So, for
instance, if two brothers are in the area and one succeeds at his Will save, you could tell that
they are siblings, but could not distinguish whether they are full- or half-siblings.)

Each round, you can turn to detect relations in a new area. The spell can penetrate barriers, but 6
inches of stone, 1 inch of common metal, a thin sheet of lead, or 1 foot of wood or dirt will block
it.

This spell functions by analyzing the blood and minds of creatures in the area, collectively
examining these traits and comparing them to those of others in the area while looking for patterns.
Thus, adoptive siblings and parents cannot be detected with this spell, since they share no blood.
