+++
id = "ref/spell/raise-animal-companion"
kind = "spell"
title = "Raise Animal Companion"
aon = "SpellDisplay.aspx?ItemName=Raise%20Animal%20Companion"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "raise_animal_companion", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/raise-dead" },
]
[[sources]]
publication = "ultimate-magic"
page = "233"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["healing"]
levels = [
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 4 },
  { class = "Paladin", level = 4 },
  { class = "Ranger", level = 4 },
]
casting_time = "1 minute"
components = "V, S, M (a diamond worth 1,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "dead animal companion or bonded mount" },
]
duration = "instantaneous"
saving_throw = "none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Hunter, Paladin, Ranger\
5: Druid
Casting time: 1 minute
Components: V, S, M (a diamond worth 1,000 gp)
Range: touch
Duration: instantaneous
Saving throw: none, see text
Spell resistance: yes
Target: dead animal companion or bonded mount
Subschool: healing
:::

### Raise Animal Companion

This spell functions as [raise dead](ref/spell/raise-dead), but it only affects an animal companion,
familiar, or paladin's bonded mount.
