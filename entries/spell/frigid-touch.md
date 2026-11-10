+++
id = "ref/spell/frigid-touch"
kind = "spell"
title = "Frigid Touch"
aon = "SpellDisplay.aspx?ItemName=Frigid%20Touch"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "frigid_touch", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "221"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Arcanist, Bloodrager, Druid, Hunter, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: creature touched
Descriptors: cold
:::

This spell causes your hand to glow with a pale blue radiance. Your melee touch attack deals 4d6
points of cold damage and causes the target to be staggered for 1 round. If the attack is a critical
hit, the target is staggered for 1 minute instead.
