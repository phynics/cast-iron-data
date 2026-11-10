+++
id = "ref/spell/retributive-reparations"
kind = "spell"
title = "Retributive Reparations"
aon = "SpellDisplay.aspx?ItemName=Retributive%20Reparations"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "retributive_reparations", path = "json/spells8.json" },
]
[[sources]]
publication = "occult-origins"
page = "29"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["curse"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one object" },
]
duration = "1 day/level or until triggered, and permanent, see text"
saving_throw = "Will negates (object) and Will negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Antipaladin, Inquisitor, Occultist, Spiritualist\
4: Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 day/level or until triggered, and permanent, see text
Saving throw: Will negates (object) and Will negates, see text
Spell resistance: yes
Target: one object
Descriptors: curse
:::

If a creature successfully takes the item targeted by this spell while you are holding, wearing, or
wielding it, the creature must attempt a Will save. If the creature fails its save, it becomes
fatigued, and it must attempt a new saving throw at the end of its turn every round it does not
return the item to you. Failing a second saving throw causes the target to become exhausted. As long
as the victim of the curse is actively working to return the object, its exhaustion is reduced to
fatigue. The fatigue and exhaustion cannot be removed by effects that normally remove them, though
immunity to fatigue and exhaustion protect against the conditions as normal.

This curse can be ended with [remove curse](ref/spell/remove-curse) or by returning the item to you.
You can have this spell active on one item at a time.
