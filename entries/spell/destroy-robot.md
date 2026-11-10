+++
id = "ref/spell/destroy-robot"
kind = "spell"
title = "Destroy Robot"
aon = "SpellDisplay.aspx?ItemName=Destroy%20Robot"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "destroy_robot", path = "json/spells3.json" },
]
[[sources]]
publication = "technology-guide"
page = "8"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, F/DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one robot (see below)" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Druid, Hunter\
6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F/DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Target: one robot (see below)
:::

You attempt to destroy any one robot in range. When you cast this spell, your hand crackles with
electricity. You must succeed at a ranged touch attack to affect the target. The target takes 12d6
points of damage + 1 point per caster level, or 3d6 points of damage + 1 point per caster level on a
successful saving throw. A cyborg or android can be damaged by this spell, but takes half damage and
gains a +4 bonus on the saving throw to resist the spell's effects.
