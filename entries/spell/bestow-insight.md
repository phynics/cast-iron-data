+++
id = "ref/spell/bestow-insight"
kind = "spell"
title = "Bestow Insight"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bestow_insight", path = "json/spells12.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "79"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one creature touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Arcanist, Bard, Inquisitor, Medium, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard\
3: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature touched
Subschool: Compulsion
:::

> _[Humans](ref/race/human) have access to the following spells._

When casting this spell, choose a single skill that you have at least one rank in. The target gains
a +2 insight bonus on skill checks with this skill and is considered trained in that skill. The
insight bonus increases by 1 for every four levels of the caster (maximum +6). Furthermore, once
before the spell's duration, the target can choose to roll two checks and take the greater result.
Doing so ends the spell's other effects.
