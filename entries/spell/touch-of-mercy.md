+++
id = "ref/spell/touch-of-mercy"
kind = "spell"
title = "Touch of Mercy"
aon = "SpellDisplay.aspx?ItemName=Touch%20of%20Mercy"
source_ids = ["champions-of-purity"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "touch_of_mercy", path = "json/spells10.json" },
]
[[sources]]
publication = "champions-of-purity"
page = "29"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["good", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Arcanist, Bard, Cleric, Oracle, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: good, mind-affecting
:::

The target creature deals only nonlethal damage with all of its weapon attacks. Damage taken by
creatures or objects that are not subject to nonlethal damage is not converted to nonlethal and
remains lethal damage. The weapon retains all of its other normal properties.
