+++
id = "ref/spell/righteous-blood"
kind = "spell"
title = "Righteous Blood"
source_ids = ["demon-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "righteous_blood", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["good"]
levels = [
  { class = "Inquisitor", level = 2 },
  { class = "Paladin", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "one creature of good alignment" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Inquisitor, Paladin
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature of good alignment
Descriptors: good
:::

**Sources:** Demon Hunter's Handbook pg 27

The target creature's innate goodness infuses its body with holy energy. While this energy does not
directly empower the target, it can harm embodiments of evil. Any creature that damages the target
with a slashing or piercing melee weapon is sprayed by the target's holy blood. If the attacker is a
creature with the evil subtype, it takes 1d6 points of damage from divine power each time it
successfully hits the target. If the target has the good subtype or an ability that grants it an
aura of good (like paladins or some clerics), its blood instead deals 2d6 points of damage.
Creatures that don't have the evil subtype or that are using reach weapons are not subject to this
damage.
