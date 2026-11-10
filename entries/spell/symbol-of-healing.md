+++
id = "ref/spell/symbol-of-healing"
kind = "spell"
title = "Symbol of Healing"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_healing", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]
[[sources]]
publication = "ultimate-magic"
page = "241"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, M (mercury and phosphorous, plus powdered diamond and opal worth a total of 500 gp)"
range = "0 ft.; see text"
effects = [
  { label = "Effect", value = "one symbol" },
]
duration = "see text"
saving_throw = "Will half (harmless) (see text)"
spell_resistance = "yes (harmless) (see text)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Cleric, Occultist, Oracle, Warpriest\
4: Paladin, Witch
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorous, plus powdered diamond and opal worth a total of 500 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: Will half (harmless) (see text)
Spell resistance: yes (harmless) (see text)
Effect: one symbol
Subschool: Healing
:::

This spell functions as [symbol of death](ref/spell/symbol-of-death), except all creatures within 60
feet of the symbol of healing instead are bathed in positive energy and heal 2d8 points + 1 point of
damage per caster level (maximum +15). Undead and other creatures harmed by positive energy instead
take 2d8 points of damage + 1 point per caster level (maximum +15); a Will save reduces this damage
by half. A creature can only be healed or harmed by the symbol once in any 24-hour period. Once
triggered, the symbol remains active for 10 minutes per caster level.

Symbol of healing can be made permanent with a [permanency](ref/spell/permanency) spell by a caster
of 10th level or higher for the cost of 10,000 gp.
