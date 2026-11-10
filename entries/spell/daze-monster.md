+++
id = "ref/spell/daze-monster"
kind = "spell"
title = "Daze Monster"
aon = "SpellDisplay.aspx?ItemName=Daze%20Monster"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "daze_monster", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/daze" },
]
[[sources]]
publication = "core-rulebook"
page = "264"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of wool or similar substance)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature of 6 HD or less" },
]
duration = "1 round"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Summoner, Unchained Summoner\
2: Arcanist, Bloodrager, Bard, Medium, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of wool or similar substance)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round
Saving throw: Will negates
Spell resistance: yes
Target: one living creature of 6 HD or less
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell functions like [daze](ref/spell/daze), but can affect any one living creature of any
type. Creatures of 7 or more HD are not affected.
