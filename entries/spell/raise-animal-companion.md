+++
id = "ref/spell/raise-animal-companion"
kind = "spell"
title = "Raise Animal Companion"
aon = "SpellDisplay.aspx?ItemName=Raise%20Animal%20Companion"
source_ids = ["core-rulebook", "ultimate-magic"]
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
subschools = ["Healing"]
levels = [
  { class = "Adept", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Shaman", level = 6 },
  { class = "Spiritualist", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 6 },
]
casting_time = "1 minute"
components = "V, S, DF, M (diamond worth 5,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "dead creature touched" },
]
duration = "instantaneous"
saving_throw = "none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 5: Adept, Cleric, Oracle, Spiritualist, Warpriest\
6: Shaman, Witch
Casting time: 1 minute
Components: V, S, DF, M (diamond worth 5,000 gp)
Range: touch
Duration: instantaneous
Saving throw: none, see text
Spell resistance: yes
Target: dead creature touched
Subschool: Healing
:::

### Raise Animal Companion

This spell functions as [raise dead](ref/spell/raise-dead), but it only affects an animal companion,
familiar, or paladin's bonded mount.
