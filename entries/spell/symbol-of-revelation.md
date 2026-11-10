+++
id = "ref/spell/symbol-of-revelation"
kind = "spell"
title = "Symbol of Revelation"
aon = "SpellDisplay.aspx?ItemName=Symbol%20of%20Revelation"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_revelation", path = "json/spells10.json" },
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
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, M (mercury and phosphorous, plus powdered diamond and opal worth a total of 1,000 gp)"
range = "0 ft.; see text"
effects = [
  { label = "Effect", value = "one symbol" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Occultist\
4: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorous, plus powdered diamond and opal worth a total of 1,000 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: none
Spell resistance: yes
Effect: one symbol
:::

This spell functions as [symbol of death](ref/spell/symbol-of-death), except it is only activated by
invisible creatures, creatures affected by an illusion (glamer) effect, creatures with the
shapechanger subtype, or creatures that have magically changed their shape. These creatures are
outlined by a pale light that functions like [faerie fire](ref/spell/faerie-fire), except it lasts
for 10 minutes per caster level; the symbol does not otherwise reveal their true form. Once
triggered, a symbol of revelation remains active for 10 minutes per caster level.

Symbol of revelation can be made permanent with a [permanency](ref/spell/permanency) spell by a
caster of 12th level or higher for the cost of 10,000 gp.
