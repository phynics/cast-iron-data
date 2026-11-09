+++
id = "ref/spell/primal-regression"
kind = "spell"
title = "Primal Regression"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "primal_regression", path = "json/spells14.json" },
]
[[sources]]
publication = "occult-adventures"
page = "181"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Witch", level = 7 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature/2 levels, no two of which can be more than 30 feet apart" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Mesmerist\
6: Druid, Hunter, Psychic, Shaman\
7: Witch
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature/2 levels, no two of which can be more than 30 feet apart
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell sequesters the targets' ability for higher reasoning, allowing their darker impulses to
come to the fore. An affected target becomes a ravening monster-savage, bloodthirsty, and brutish.
Until the spell ends, the targets have all of the following benefits and drawbacks.

- Targets' Intelligence and Charisma scores drop to 3 (if the scores were higher), and they are
  unable to use Intelligenceor Charisma-based skills, cast spells, understand language, or
  communicate coherently.
- Targets take a -4 penalty on Will saves.
- Targets gain a +6 enhancement bonus to Strength, a +2 natural armor bonus to AC, and 2d8 temporary
  hit points. These temporary hit points disappear at the end of the spell's duration.

When the spell ends, each affected creature must succeed at a Will saving throw or take 1d4 points
of Intelligence drain and 1d4 points of Charisma damage.
