+++
id = "ref/spell/blessing-of-the-salamander"
kind = "spell"
title = "Blessing of the Salamander"
aon = "SpellDisplay.aspx?ItemName=Blessing%20of%20the%20Salamander"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blessing_of_the_salamander", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "206"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 4 },
  { class = "Ranger", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Hunter, Ranger\
5: Druid
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 round/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Polymorph
:::

When you cast this on a creature, its skin turns slick and clammy and it is able to regenerate
damage each round. While under the effects of the spell, the creature gains
[fast healing](ref/umr/fast-healing) 5, fire resistance 20 and a +2 competence bonus to its Combat
Maneuver Defense.
