+++
id = "ref/spell/overstimulate"
kind = "spell"
title = "Overstimulate"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "overstimulate", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (smelling salts)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Bloodrager, Bard, Cleric, Druid, Hunter, Investigator, Oracle, Psychic, Ranger, Shaman, Skald, Summoner, Unchained Summoner, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M/DF (smelling salts)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: one creature
:::

**Sources:** Inner Sea Temples pg 13

You deprive a creature of the blissful oblivion of unconsciousness, either to keep it going despite
grievous injuries or to prolong its suffering. For the duration of the spell, the target gains the
ferocity ability, allowing it to remain conscious and continue fighting even if its hit point total
is below 0. The target is still staggered and loses 1 hit point each round, and the target still
dies when its hit point total reaches a negative amount equal to its Constitution score.
