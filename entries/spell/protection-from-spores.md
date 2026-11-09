+++
id = "ref/spell/protection-from-spores"
kind = "spell"
title = "Protection from Spores"
source_ids = ["pathfinder-113-what-grows-within"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "protection_from_spores", path = "json/spells15.json" },
]
[[sources]]
publication = "pathfinder-113-what-grows-within"
page = "66"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 1 },
  { class = "Investigator", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Hunter, Ranger\
2: Alchemist, Cleric, Druid, Investigator, Oracle, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates (harmless)
Spell resistance: no
Target: creature touched
:::

> _This spell is associated with [Xhamen-Dor](ref/faith/xhamen-dor), but there are no restrictions
> on its use by others._

With a touch, you bolster a creature's body to protect it from the harmful effects of spores and
similar afflictions. While under the effect of this spell, a creature is immune to the effects of
brown mold, green slime, russet mold, yellow mold, and any similar hazard, provided the hazard is CR
6 or lower. Similarly, the creature is immune to poison, disease, and infestation attacks from all
fungal creatures of CR 6 or lower, including effects such as basidirond spores, violet fungus rot,
and the like. The target is immune to fungus-based toxins, such as striped toadstool. Against
similar hazards or monsters of CR 7 or higher, the target gains a bonus on all saving throws against
the effect equal to half your caster level. Protection from spores offers no protection against
fungal infestations created by the seeded, by the spell what grows within, or by Xhamen-Dor.
