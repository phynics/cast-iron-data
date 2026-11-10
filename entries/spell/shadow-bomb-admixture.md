+++
id = "ref/spell/shadow-bomb-admixture"
kind = "spell"
title = "Shadow Bomb Admixture"
aon = "SpellDisplay.aspx?ItemName=Shadow%20Bomb%20Admixture"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_bomb_admixture", path = "json/spells15.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "243"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Investigator", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "special, see below"
spell_resistance = "special, see below"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Alchemist, Investigator
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level
Saving throw: special, see below
Spell resistance: special, see below
Target: you
Subschool: Creation
:::

Upon drinking an extract created with this formula, you make a significant change to your magical
reserve that modifies the nature of all bombs you create and throw during this extract's duration.
This effect on your magical reserve has no effect on any discoveries that you use to modify your
bombs, but you can only have one admixture effect (formula with the word "bomb admixture" in its
title) active at a time. If you drink another bomb admixture, the effects of the former bomb
admixture end and the new one becomes active.

When you throw a bomb and hit a direct target, a shadowy substance is released from the bomb
covering the direct target and up to three creatures that take damage from the bomb's splash
(alchemist's choice). The affected creatures must successfully make a Fortitude saving throw, or
they gain [concealment](ref/rule/concealment) but treat all other creatures as having concealment
for the duration of the shadow bomb admixture. This effect does not ignore
[spell resistance](ref/rule/spell-resistance).
