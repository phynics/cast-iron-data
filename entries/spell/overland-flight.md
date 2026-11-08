+++
id = "ref/spell/overland-flight"
kind = "spell"
title = "Overland Flight"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "overland_flight", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/fly" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Occultist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Summoner\
5: Alchemist, Arcanist, Investigator, Magus, Occultist, Psychic, Shaman, Sorcerer, Spiritualist, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: you
:::

**Sources:** PRPG Core Rulebook pg 317

This spell functions like a [fly](ref/spell/fly) spell, except you can fly at a speed of 40 feet (30
feet if wearing medium or heavy armor, or if carrying a medium or heavy load) with a bonus on Fly
skill checks equal to half your caster level. When using this spell for long-distance movement, you
can hustle without taking nonlethal damage (a forced march still requires Constitution checks). This
means you can cover 64 miles in an 8-hour period of flight (or 48 miles at a speed of 30 feet).
