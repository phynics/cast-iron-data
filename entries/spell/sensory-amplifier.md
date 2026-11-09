+++
id = "ref/spell/sensory-amplifier"
kind = "spell"
title = "Sensory Amplifier"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sensory_amplifier", path = "json/spells15.json" },
]
[[sources]]
publication = "occult-origins"
page = "29"

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting"]
levels = [
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "S"
range = "personal"
effects = [
  { label = "Area", value = "10-ft.-radius emanation centered on you" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Medium\
3: Mesmerist, Psychic, Witch\
4: Druid, Hunter
Casting time: 1 standard action
Components: S
Range: personal
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Area: 10-ft.-radius emanation centered on you
Descriptors: mind-affecting
:::

You open the minds of all creatures near you and enhance their sensory receptors. All living
creatures other than you in the area gain a +5 bonus on Perception checks. Sighted creatures gain
[low-light vision](ref/rule/low-light-vision), and creatures with a sense of smell gain
[scent](ref/umr/scent). In addition, the first time each round that a creature in the area takes
damage, it takes an additional 2d6 points of damage of the same type. Despite being within the area,
the caster does not take this extra damage.
