+++
id = "ref/spell/corrosive-consumption"
kind = "spell"
title = "Corrosive Consumption"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "corrosive_consumption", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["acid"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "3 rounds"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 3 rounds
Saving throw: none
Spell resistance: yes
Target: creature touched
Subschool: Creation
Descriptors: acid
:::

**Sources:** Ultimate Magic pg 212

With a touch, this spell causes a small, rapidly growing patch of corrosive acid to appear on the
target. On the first round, the acid deals 1 point of acid damage per caster level (maximum 15). On
the second round, the acid patch grows and deals 1d4 points of acid damage per caster level (maximum
15d4). On the third and final round, the acid patch covers the entire creature and deals 1d6 points
of acid damage per caster level (maximum 15d6). The target can spend a full-round action to scrape
off the acid, or can wash it off with at least 1 gallon of liquid to halve the damage for that round
and negate the remaining rounds of the spell.
