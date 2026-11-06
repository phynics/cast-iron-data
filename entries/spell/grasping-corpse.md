+++
id = "ref/spell/grasping-corpse"
kind = "spell"
title = "Grasping Corpse"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grasping_corpse", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (pinch of powdered onyx worth 1 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one corpse" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Antipaladin, Arcanist, Cleric, Occultist, Oracle, Shaman, Sorcerer, Spiritualist, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (pinch of powdered onyx worth 1 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: one corpse
Descriptors: evil
:::

**Sources:** Horror Adventures pg 118

You can cause one nearby corpse to animate for a brief moment. Choose a creature within 30 feet of
the corpse (even if the creature is outside the spell's range). The corpse shambles toward the
creature and then attempts to trip or grapple it (your choice). The corpse does not provoke attacks
of opportunity.

Attempt a special combat maneuver check against the chosen creature. Your CMB for this combat
maneuver is equal to your caster level plus your Intelligence, Wisdom, or Charisma modifier,
whichever is highest. If you chose to trip the creature, it falls prone if you equal or exceed its
CMD. If you chose to grapple, the creature gains the grappled condition until it breaks free from
the corpse. Treat your save DC for a spell of this level as the CMD of the grasping corpse.
Alternatively, destroying the corpse with damage ends the grapple. The corpse has 12 hit points and
DR 5/slashing.
