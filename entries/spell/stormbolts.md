+++
id = "ref/spell/stormbolts"
kind = "spell"
title = "Stormbolts"
aon = "SpellDisplay.aspx?ItemName=Stormbolts"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stormbolts", path = "json/spells9.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "247"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["electricity"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Shaman", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a copper rod)"
range = "30 ft."
effects = [
  { label = "Area", value = "a 30-ft.-radius spread, centered on you" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 8: Arcanist, Cleric, Druid, Oracle, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a copper rod)
Range: 30 ft.
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Area: a 30-ft.-radius spread, centered on you
Descriptors: electricity
:::

When you cast this spell, lightning spills forth from your body in all directions. The bolts do not
harm natural vegetation or creatures in the area you wish to exclude from damage. Any other
creatures within the area take 1d8 points of electricity damage per caster level (maximum 20d8) and
are stunned for 1 round. A successful saving throw halves the damage and negates the stun effect.
