+++
id = "ref/spell/hymn-of-mercy"
kind = "spell"
title = "Hymn of Mercy"
aon = "SpellDisplay.aspx?ItemName=Hymn%20of%20Mercy"
source_ids = ["champions-of-purity"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hymn_of_mercy", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/touch-of-mercy" },
]
[[sources]]
publication = "champions-of-purity"
page = "29"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["compulsion"]
descriptors = ["good", "mind-affecting"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft.-radius burst centered on you" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Cleric, Oracle, Skald, Warpriest
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: 30-ft.-radius burst centered on you
Subschool: compulsion
Descriptors: good, mind-affecting
:::

### Hymn of Mercy

This spell functions like [touch of mercy](ref/spell/touch-of-mercy), except as noted above.
