+++
id = "ref/spell/disrupting-weapon"
kind = "spell"
title = "Disrupting Weapon"
aon = "SpellDisplay.aspx?ItemName=Disrupting%20Weapon"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "disrupting_weapon", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "273"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Targets", value = "one melee weapon" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless, object); see text"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Cleric, Inquisitor, Oracle, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level
Saving throw: Will negates (harmless, object); see text
Spell resistance: yes (object)
Targets: one melee weapon
:::

This spell makes a melee weapon deadly to undead. Any undead creature with HD equal to or less than
your caster level must succeed on a Will save or be destroyed utterly if struck in combat with this
weapon. [Spell resistance](ref/rule/spell-resistance) does not apply against the destruction effect.
