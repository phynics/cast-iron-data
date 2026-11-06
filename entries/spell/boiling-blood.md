+++
id = "ref/spell/boiling-blood"
kind = "spell"
title = "Boiling Blood"
source_ids = ["ultimate-magic", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "boiling_blood", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "one creature per three levels, no two of which may be more than 30 ft. apart" },
]
duration = "concentration+ 1 round/level (D)"
saving_throw = "Fortitude negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Bloodrager, Bard, Cleric, Oracle, Psychic, Red Mantis Assassin, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: concentration+ 1 round/level (D)
Saving throw: Fortitude negates (see text)
Spell resistance: yes
Targets: one creature per three levels, no two of which may be more than 30 ft. apart
:::

**Sources:** Ultimate Magic pg 209

The blood of the targeted creatures begins to boil. If a target fails its save, it takes 1 point of
fire damage per round. This spell has no effect on creatures that don't have blood.

If a target has the orc subtype, it doesn't take fire damage and instead gains a +2 morale bonus to
Strength.

### Mythic Boiling Blood

**Sources:** Mythic Adventures pg 87\
A target that fails its save takes 1d3 points of fire damage per round. If a target has the orc
subtype, it also gains fire resistance 5.

_Augmented:_ If you expend two uses of mythic power, you can affect allies as though they had the
orc subtype.
