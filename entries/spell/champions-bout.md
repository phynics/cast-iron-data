+++
id = "ref/spell/champions-bout"
kind = "spell"
title = "Champion's Bout"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "champions_bout", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 round"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Targets", value = "two creatures" },
]
duration = "1 round/level"
saving_throw = "Will negates (see text)"
spell_resistance = "yes (see text)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Cleric, Oracle, Skald, Warpriest
Casting time: 1 round
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level
Saving throw: Will negates (see text)
Spell resistance: yes (see text)
Targets: two creatures
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** Inner Sea Races pg 218

> _The following spell is available to the indicated race or ethnicity: Shoanti_

You allow two chosen champions to fight without interference. The two creatures must be willing in
order for the spell to work. After you cast this spell, any creature attempting to aid or hinder
either of the two targets in any way must succeed at a Will save or lose its action instead
([spell resistance](ref/rule/spell-resistance) applies). A creature that fails its Will save against
champion's bout cannot attempt to interfere again. If a creature successfully interferes with the
bout, the spell ends immediately.
