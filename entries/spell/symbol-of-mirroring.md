+++
id = "ref/spell/symbol-of-mirroring"
kind = "spell"
title = "Symbol of Mirroring"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "symbol_of_mirroring", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/symbol-of-death" },
]
[[sources]]
publication = "ultimate-magic"
page = "241"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "10 minutes"
components = "V, S, M (mercury and phosphorous, plus powdered diamond and opal worth a total of 100 gp)"
range = "0 ft.; see text"
effects = [
  { label = "Effect", value = "one symbol" },
]
duration = "see text"
saving_throw = "Will partial (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Arcanist, Mesmerist, Occultist, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, M (mercury and phosphorous, plus powdered diamond and opal worth a total of 100 gp)
Range: 0 ft.; see text
Duration: see text
Saving throw: Will partial (harmless)
Spell resistance: yes
Effect: one symbol
Subschool: Figment
:::

This spell functions as [symbol of death](ref/spell/symbol-of-death), except it instead creates one
illusory duplicate of each creature within 60 feet of the symbol. These duplicates function as
[mirror image](ref/spell/mirror-image), moving with the original creatures and mimicking their
movements, sounds, and actions exactly. If an illusory double is destroyed, a new one appears on the
creature's turn. The images last for as long as a creature remains within 60 feet of the symbol, and
for 1 round/level thereafter. Once triggered, the symbol remains active for 10 minutes per caster
level.

Symbol of mirroring can be made permanent with a [permanency](ref/spell/permanency) spell by a
caster of 10th level or higher for the cost of 5,000 gp.
