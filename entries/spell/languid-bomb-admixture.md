+++
id = "ref/spell/languid-bomb-admixture"
kind = "spell"
title = "Languid Bomb Admixture"
aon = "SpellDisplay.aspx?ItemName=Languid%20Bomb%20Admixture"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "languid_bomb_admixture", path = "json/spells6.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "233"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Investigator", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "Will negates (special, see below)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Alchemist, Investigator
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: Will negates (special, see below)
Spell resistance: yes
Target: you
Subschool: Compulsion
Descriptors: mind-affecting
:::

Upon drinking an extract created with this formula, you make a significant change to your magical
reserve that modifies the nature of all bombs you create and throw during this extract's duration.
This effect on your magical reserve has no effect on any discoveries that you use to modify your
bombs, but you can only have one admixture effect (formulae with the words "bomb admixture" in their
titles) active at a time. If you drink another bomb admixture, the effects of the former bomb
admixture end and the those of the new one become active.

When you throw a bomb and hit a direct target, it affects up to four creatures - the creature the
bomb hit directly, and up to three other creatures damaged by the splash (alchemist's choice). Those
creatures must succeed at a Will saving throw or become fatigued.
