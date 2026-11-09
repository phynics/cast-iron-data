+++
id = "ref/spell/flames-of-the-faithful"
kind = "spell"
title = "Flames of the Faithful"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flames_of_the_faithful", path = "json/spells4.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "222"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["fire"]
levels = [
  { class = "Inquisitor", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "touch"
effects = [
  { label = "Target", value = "weapon touched" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Inquisitor
Casting time: 1 standard action
Components: V
Range: touch
Duration: 1 round/level
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: weapon touched
Descriptors: fire
:::

With a touch, you cause a glowing rune to appear on a single weapon, granting that weapon the
flaming property (and allowing it to cause an extra 1d6 points of fire damage on a successful hit).
If you are using the judgment class feature, your weapon gains the flaming burst property instead.
The spell functions only for weapons that you wield. If the weapon leaves your hand for any reason,
the spell effect ends. The effects of this spell do not stack with any existing flaming or flaming
burst weapon property that the target weapon may already possess.
