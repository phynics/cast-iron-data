+++
id = "ref/spell/symbol-of-scrying"
kind = "spell"
title = "Symbol of Scrying"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_scrying", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]
[[sources]]
publication = "ultimate-magic"
page = "241"

[fields]
kind = "spell"
school = "divination"
subschools = ["Scrying"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, M (mercury and phosphorous, plus powdered diamond and opal worth a total of 1,000 gp)"
range = "0 ft.; see text"
effects = [
  { label = "Effect", value = "one symbol" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Occultist\
5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorous, plus powdered diamond and opal worth a total of 1,000 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: none
Spell resistance: no
Effect: one symbol
Subschool: Scrying
:::

This spell functions as [symbol of death](ref/spell/symbol-of-death), except that, when triggered,
it creates a scrying sensor linked to you and centered on the symbol, even if you are on a different
plane than the symbol. You are immediately aware that the symbol has been triggered if you are
conscious, and are awakened from normal sleep if sleeping. The symbol does not otherwise disturb
your concentration. You may observe the area through the symbol as if using a
[scrying](ref/spell/scrying) spell with the sensor as the target creature. Once triggered, the
symbol remains active for 10 minutes per caster level.

Unlike symbol of death, a symbol of scrying is not considered a magical trap. Symbol of scrying can
be made permanent with a [permanency](ref/spell/permanency) spell by a caster of 13th level or
higher for the cost of 10,000 gp.
