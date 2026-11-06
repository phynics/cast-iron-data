+++
id = "ref/spell/anti-summoning-shield"
kind = "spell"
title = "Anti-Summoning Shield"
source_ids = ["demon-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "anti_summoning_shield", path = "json/spells.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "50-ft.-radius" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Arcanist, Bard, Skald, Sorcerer, Summoner, Unchained Summoner, Wizard\
3: Inquisitor
Casting time: 1 standard action
Components: V
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: 50-ft.-radius
:::

**Sources:** Demon Hunter's Handbook pg 26

Within the area of effect, this spell impedes the use of spells of the summoning subschool and other
effects that summon creatures. Any such spells,
[spell-like abilities](ref/umr/spell-like-abilities), or similar summoning effects used within the
area have a percent chance of failure equals 5% × your caster level, to a maximum 75% chance of
failure. If the summoning effect already has a percent chance of failure (as is often the case with
the summon spell-like ability of outsiders), these percentages stack. This spell does not affect
summoners attempting to summon their eidolon, but it does affect summoners casting other summoning
spells.
