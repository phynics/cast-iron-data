+++
id = "ref/spell/daggermarks-exchange"
kind = "spell"
title = "Daggermark's Exchange"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "daggermarks_exchange", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["poison"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a dose of poison)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Druid, Hunter, Investigator\
3: Arcanist, Cleric, Occultist, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M (a dose of poison)
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
Descriptors: poison
:::

**Sources:** Inner Sea Intrigue pg 59

You swallow a dose of poison with no effect and regurgitate a dose of a different poison (your
choice) into the old container (or another you have on hand). Attempt a Craft (alchemy) check
against the new poison's DC. If you succeed, you create a dose of your chosen poison. If you fail,
the poison you regurgitate is inert. If you roll a natural 1, you expose yourself to the original
poison (although you remain immune to that poison if you have venom immunity or a similar class
feature or ability). The new poison's price must be the same as or less than the original poison's
price.
