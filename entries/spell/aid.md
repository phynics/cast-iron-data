+++
id = "ref/spell/aid"
kind = "spell"
title = "Aid"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aid", path = "json/spells.json" },
]
[[sources]]
publication = "core-rulebook"
page = "239"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Adept", level = 2 },
  { class = "Alchemist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Adept, Alchemist, Cleric, Inquisitor, Investigator, Medium, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: none
Spell resistance: yes
Target: living creature touched
Subschool: Compulsion
Descriptors: mind-affecting
:::

Aid grants the target a +1 morale bonus on attack rolls and saves against fear effects, plus
temporary hit points equal to 1d8 + caster level (to a maximum of 1d8+10 temporary hit points at
caster level 10th).
