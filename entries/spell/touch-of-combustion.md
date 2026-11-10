+++
id = "ref/spell/touch-of-combustion"
kind = "spell"
title = "Touch of Combustion"
aon = "SpellDisplay.aspx?ItemName=Touch%20of%20Combustion"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "touch_of_combustion", path = "json/spells10.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "131"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature or object touched" },
]
duration = "instantaneous"
saving_throw = "Reflex negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Arcanist, Bloodrager, Druid, Hunter, Inquisitor, Magus, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Reflex negates, see text
Spell resistance: yes
Target: creature or object touched
Descriptors: fire
:::

> _[Ifrits](ref/race/ifrit) have access to the following spell._

Your successful melee touch attack causes the target to ignite in a violent burst of flame, dealing
1d6 points of fire damage. If it fails its saving throw, the target also catches on fire. If the
target catches fire, on the first round thereafter, creatures adjacent to it (including you) must
each succeed at a Reflex save or take 1d4 points of fire damage.
