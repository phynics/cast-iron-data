+++
id = "ref/spell/whispering-lore"
kind = "spell"
title = "Whispering Lore"
aon = "SpellDisplay.aspx?ItemName=Whispering%20Lore"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "whispering_lore", path = "json/spells16.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "29"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 1 },
]
casting_time = "1 full-round action"
components = "V, S, M/DF (an owl's beak)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Druid, Hunter, Medium, Psychic, Ranger, Witch\
2: Cleric, Oracle, Warpriest
Casting time: 1 full-round action
Components: V, S, M/DF (an owl's beak)
Range: personal
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

> _Most know of elven magic for its power, but those who delve deeper discover its elegance and ties
> to the natural world. The following spell is just one that the [elves](ref/race/elf) are known
> for._

Upon casting this spell, you are able to gain knowledge from the land itself. As you walk through
the terrain, it whisper information in a language you understand, though the whispering is so
rambling it is hard to distinguish useful information. This whispering grants you a +4 insight bonus
on a single Knowledge skill type appropriate to the type of terrain you are in. If you are within a
cold, desert, forest, jungle, mountain, plains, swamp, or water environment, you gain the bonus on
Knowledge (nature) checks. If you are within an underground environment, you gain the bonus on
Knowledge (dungeoneering) checks. If you are within an urban environment, you gain the bonus on
Knowledge (local) checks. If you are on a plane other than the Material Plane, you gain the bonus on
Knowledge (planes) checks. If you enter a new terrain, you lose the previous terrain's skill bonus
and gain the new bonus.
