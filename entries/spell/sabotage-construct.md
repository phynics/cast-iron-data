+++
id = "ref/spell/sabotage-construct"
kind = "spell"
title = "Sabotage Construct"
source_ids = ["people-of-the-river"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sabotage_construct", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/confusion" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Targets", value = "all constructs in a 15-ft.-radius burst" },
]
duration = "1 round/level"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Bard, Inquisitor, Skald\
6: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Will partial
Spell resistance: yes
Targets: all constructs in a 15-ft.-radius burst
:::

**Sources:** People of the River pg 27

This spell functions as [confusion](ref/spell/confusion), except that it affects only constructs.
When you are rolling for a confused construct's behavior, a result of 26-50 indicates the construct
twitches spasmodically. On a successful Will save, the construct is confused for only 1 round.
