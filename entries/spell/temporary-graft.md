+++
id = "ref/spell/temporary-graft"
kind = "spell"
title = "Temporary Graft"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "temporary_graft", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 4 },
  { class = "Occultist", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F (a dismembered body part)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Bloodrager, Investigator, Occultist\
4: Arcanist, Magus, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a dismembered body part)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Horror Adventures pg 129

You temporarily graft a dismembered body part onto yourself. You must have the body part in your
possession or the spell has no effect. The graft must come from a creature the same size category as
you. You can have only one graft active at a time. Grafting on a new body part immediately ends the
effects of the older casting and causes that body part to fall off. The effect of the graft depends
on the type of body part you choose to graft to yourself, as follows.

_Fins:_ The fins grant you a 40 foot swim speed.

_Head:_ The head grants you all-around vision. If the head came from a creature that had
[darkvision](ref/rule/darkvision), [low-light vision](ref/rule/low-light-vision), or scent, you gain
the appropriate senses at half the normal range. You can speak through either head, but not both
simultaneously. You don't receive any additional special abilities the head might have had (like a
medusa's petrifying gaze ability).

_Leg:_ The leg increases your base movement speed by 5 feet and grants you a +2 bonus to CMD against
overrun and trip combat maneuvers (the usual bonus for having an extra leg).

_Wings:_ The wings grant you a 40-foot fly speed (poor maneuverability).
