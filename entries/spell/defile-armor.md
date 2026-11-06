+++
id = "ref/spell/defile-armor"
kind = "spell"
title = "Defile Armor"
source_ids = ["advanced-players-guide", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "defile_armor", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Inquisitor", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "armor touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 3: Antipaladin\
4: Inquisitor
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: armor touched
Descriptors: evil
:::

**Sources:** Advanced Player's Guide pg 215

As sanctify armor, except you gain DR 5/good when using your judgment or smite ability.

### Mythic Defile Armor

**Sources:** Mythic Adventures pg 90\
You gain DR 5/good while wearing the target armor. While using your judgment or smite ability, this
improves to DR 10/good.

_Augmented (3rd):_ If you expend two uses of mythic power, while you use your judgment or smite, add
half your tier to your AC as a profane bonus.
