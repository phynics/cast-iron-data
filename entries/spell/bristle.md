+++
id = "ref/spell/bristle"
kind = "spell"
title = "Bristle"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bristle", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "207"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Druid, Hunter
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes
Target: one creature
:::

You give a creature the ability to redirect a portion of its innate toughness away from its own
defense and toward the amount of damage it deals with natural attacks. Each round, as a swift action
at the start of its turn, the creature can choose to reduce some or all of its natural armor bonus
to AC and gain an enhancement bonus on all damage rolls for natural attacks equal to that amount.
The reduction to natural armor, and thus the enhancement bonus on damage rolls, cannot exceed 1
point per 3 caster levels, to a maximum penalty/bonus of -5/+5 at 15th level. A creature cannot
reduce its natural armor bonus to less than 0 with this spell. All attacks directed against the
creature use its adjusted AC until the start of its next turn, at which time it can choose to modify
its AC again or keep it at its current level. Creatures make this decision without any need for
conscious thought or reflection; even creatures with no Intelligence score can benefit from this
spell, although they always opt for the maximum possible reduction and bonus, regardless of any
tactical advantage they might lose.
