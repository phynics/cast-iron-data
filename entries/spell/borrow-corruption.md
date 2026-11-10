+++
id = "ref/spell/borrow-corruption"
kind = "spell"
title = "Borrow Corruption"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "borrow_corruption", path = "json/spells2.json" },
]
[[sources]]
publication = "horror-adventures"
page = "111"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a dirty scrap of a good priest's raiment)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Antipaladin, Medium\
3: Occultist\
4: Cleric, Druid, Hunter, Oracle, Psychic, Ranger, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M (a dirty scrap of a good priest's raiment)
Range: touch
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: creature touched
Descriptors: evil
:::

You touch a creature with at least one manifestation from a [corruption](ref/rule/corruption). You
temporarily gain any stains and gifts that corruption grants to the creature, and the creature
retains them. If the gifts have limited uses, you count as having no uses remaining. You take 1d3
points of Wisdom drain whenever you cast this spell.

If your campaign uses [the sanity system](ref/rule/sanity), your sanity score decreases by 2 (and
thus your sanity edge decreases by 1) each time you cast this spell, instead of you taking Wisdom
drain. Only [greater restoration](ref/spell/restoration-greater), [miracle](ref/spell/miracle), or
[wish](ref/spell/wish) can remove this decrease. A single casting of greater restoration removes one
decrease of sanity from casting [borrow corruption](ref/spell/borrow-corruption), while a casting of
miracle or wish removes them all.
