+++
id = "ref/spell/magic-siege-engine-greater"
kind = "spell"
title = "Greater Magic Siege Engine"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_siege_engine_greater", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-siege-engine" },
]
[[sources]]
publication = "ultimate-combat"
page = "236"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 4 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (black powder)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one siege engine touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Antipaladin, Arcanist, Inquisitor, Occultist, Paladin, Red Mantis Assassin, Sorcerer, Wizard\
5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, M/DF (black powder)
Range: close (25 ft. + 5 ft./2 levels)
Target: one siege engine touched
Duration: 1 hour/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
:::

### Greater Magic Siege Engine

This spell functions like [magic siege weapon](ref/spell/magic-siege-engine), except it gives an
indirect fire siege weapon an enhancement bonus on targeting and damage rolls of +1 per four caster
levels (maximum +5). If used on a direct-fire siege weapon, this spell functions as
[greater magic weapon](ref/spell/magic-weapon-greater).
