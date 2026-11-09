+++
id = "ref/spell/divine-transfer"
kind = "spell"
title = "Divine Transfer"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "divine_transfer", path = "json/spells13.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "216"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Paladin", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous + 1 round/level (see text)"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Paladin
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous + 1 round/level (see text)
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Target: living creature touched
:::

With a single touch, you transfer some of your life essence to the subject, transferring your hit
points and your resolve. When you touch the subject you can transfer up to a number of hit points
equal to your Constitution score to the target. These hit points heal the subject, but cannot raise
the subject's hit points higher than its normal hit point total. In addition, the subject gains
DR/evil equal to your Charisma bonus (if any) for the duration of the spell.
