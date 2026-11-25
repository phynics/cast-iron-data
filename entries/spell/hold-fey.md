+++
id = "ref/spell/hold-fey"
kind = "spell"
title = "Hold Fey"
aon = "SpellDisplay.aspx?ItemName=Hold%20Fey"
source_ids = ["the-first-world-realm-of-the-fey"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hold_fey", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hold-person" },
]
[[sources]]
publication = "the-first-world-realm-of-the-fey"
page = "12"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a small, straight piece of iron)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one fey creature" },
]
duration = "1 round/level (d); see text"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Cleric, Inquisitor, Oracle, Skald, Warpriest, Witch\
3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a small, straight piece of iron)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (d); see text
Saving throw: Will negates; see text
Spell resistance: yes
Target: one fey creature
Subschool: compulsion
Descriptors: mind-affecting
:::

### Hold Fey

This spell functions as per [hold person](ref/spell/hold-person), except it affects a fey instead of
a humanoid.
