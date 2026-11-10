+++
id = "ref/spell/egorian-diplomacy"
kind = "spell"
title = "Egorian Diplomacy"
aon = "SpellDisplay.aspx?ItemName=Egorian%20Diplomacy"
source_ids = ["spymasters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "egorian_diplomacy", path = "json/spells4.json" },
]
[[sources]]
publication = "spymasters-handbook"
page = "28"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a bent coin)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instant; see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Cleric, Inquisitor, Magus, Mesmerist, Oracle, Psychic, Skald, Warpriest
Casting time: 1 standard action
Components: V, S, M (a bent coin)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instant; see text
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

As part of casting this spell, you can attempt a single Intimidate skill check to make a target act
friendly toward you. If you succeed, the target assists you normally, but Egorian diplomacy clouds
the memory of any threats or pressure you applied. The target remembers assisting you, but can't
remember why, and its attitude toward you doesn't worsen as a result of being intimidated.

Whether a creature fails or succeeds at its saving throw, it becomes immune to further castings of
Egorian diplomacy for 24 hours.
