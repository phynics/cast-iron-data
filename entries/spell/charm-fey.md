+++
id = "ref/spell/charm-fey"
kind = "spell"
title = "Charm Fey"
aon = "SpellDisplay.aspx?ItemName=Charm%20Fey"
source_ids = ["the-first-world-realm-of-the-fey"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charm_fey", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/charm-person" },
]
[[sources]]
publication = "the-first-world-realm-of-the-fey"
page = "12"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one fey creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Target: one fey creature
Subschool: charm
Descriptors: mind-affecting
:::

### Charm Fey

This spell functions as [charm person](ref/spell/charm-person), except it affects a fey instead of a
humanoid.
