+++
id = "ref/spell/shifting-shadows"
kind = "spell"
title = "Shifting Shadows"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shifting_shadows", path = "json/spells9.json" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "31"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["darkness"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of ink)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "20-ft.-radius emanation centered on a point in space" },
]
duration = "1 round/level (D)"
saving_throw = "none, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bard, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of ink)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none, see text
Spell resistance: no
Area: 20-ft.-radius emanation centered on a point in space
Descriptors: darkness
:::

Waves of shifting shadows obscure the appearance of all creatures caught within the emanation,
making it harder to tell friends from foes.

This spell does not cause affected creatures to risk accidentally attacking their allies, but it
does require them to concentrate harder to keep track of their allies and foes. While this spell is
in effect, every creature in the area can treat any other creature in the area as an allied
threatening creature for the purpose of flanking. Further, whenever a creature in the area would
provoke an attack of opportunity from an enemy, that creatures' allies in the area must succeed at a
Reflex save or lose one attack of opportunity for that round as they suppress the instinct to attack
a vulnerable target that might be an ally. The shadows do not hinder precision-based attacks or
create areas of dim light.

Creatures under the effect of [true seeing](ref/spell/true-seeing) are not affected by this spell.
Creatures with [scent](ref/umr/scent) or [keen scent](ref/umr/keen-scent), creatures that are blind,
and creatures that operate effectively without vision (such as creatures with
[blindsight](ref/umr/blindsight) or [blindsense](ref/umr/blindsense)) are also not affected by this
spell.
