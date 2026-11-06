+++
id = "ref/spell/spirit-bonds"
kind = "spell"
title = "Spirit Bonds"
source_ids = ["divine-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_bonds", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "divination"
descriptors = ["meditative"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 hour"
components = "V, M (soothing incense worth 300 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "24 hours or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Arcanist, Cleric, Shaman, Warpriest, Witch, Wizard
Casting time: 1 hour
Components: V, M (soothing incense worth 300 gp)
Range: personal
Duration: 24 hours or until discharged
Saving throw: none
Spell resistance: no
Target: you
Descriptors: meditative
:::

**Sources:** Divine Anthology pg 13

You heighten your awareness of up to one willing creature or object per 3 caster levels, each of
which must be within 30 feet of you during the entire hour you spend preparing spells and casting
spirit bonds. By concentrating on one of these creatures or objects as a full-round action, you can
learn its direction and relative distance from your location, provided that it is on the same plane.
In the case of a creature, you can also learn the state of its emotion or health
[aura](ref/rule/auras) as a full-round action. In the case of an object, you can also get a sense of
how damaged it is, similar to reading the health aura of a creature, or, in the case of a magic item
that must be activated, you can learn when it was last activated (a full-round action in either
case).

Additionally, at any time during the spell's duration, you can deliver a single message to any of
the creatures that participated in the spell. This message is delivered telepathically regardless of
range and can be up to 25 words in length. Delivering a message in this way severs your connection
with that character, and you can no longer learn information about that creature through this spell,
but doing so does not impact the remaining duration you have linked to other creatures or objects.
