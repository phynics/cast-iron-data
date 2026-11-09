+++
id = "ref/spell/mind-over-matter"
kind = "spell"
title = "Mind Over Matter"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mind_over_matter", path = "json/spells14.json" },
]
[[sources]]
publication = "occult-origins"
page = "30"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Spiritualist", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Mesmerist, Psychic, Spiritualist
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
:::

You blur the lines between mind and body, reassigning ability damage or drain your target has taken
to a corresponding ability score, as per the following table.

|Physical Ability Score|Mental Ability Score|
| --- | --- |
|Strength|Intelligence|
|Dexterity|Wisdom|
|Constitution|Charisma|

The transfer of damage can go either way-you can convert Intelligence damage to Strength damage and
vice versa. You can transfer any number of points of damage or drain in a single casting, though
only from one ability score to the corresponding ability score. You cannot transfer enough ability
damage or drain to reduce an ability score to 0.
