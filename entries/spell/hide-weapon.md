+++
id = "ref/spell/hide-weapon"
kind = "spell"
title = "Hide Weapon"
aon = "SpellDisplay.aspx?ItemName=Hide%20Weapon"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hide_weapon", path = "json/spells5.json" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "30"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Antipaladin, Arcanist, Bloodrager, Hunter, Inquisitor, Magus, Ranger, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

Upon casting this spell, a light or one-handed melee weapon in your hand melds with your flesh,
accompanied by a disgusting sucking sound. The weapon disappears completely inside your arm, and
thereafter for the duration of the spell, you can extend and retract the weapon as a move action.

While extended, the weapon remains partially melded with your hand and arm, providing a +5 bonus to
your CMD against disarm combat maneuvers. While the weapon is retracted, its shape adjusts to fit
inside your arm, and you retain the use of your hand. Spotting the weapon on casual inspection is
impossible, but anyone frisking you can attempt a DC 25 Perception check to notice a light weapon or
a DC 20 Perception check to notice a one-handed weapon hidden inside your arm. If the weapon grants
a bonus on Sleight of Hand checks to hide it (as does a dagger), the bonus is added to the DC to
find the item. Anyone who sees you casting this spell doesn't need to succeed at a Perception check
to know you have the hidden weapon.

If you cast this spell a second time, you can hide another weapon inside your other arm. You can
extend and retract both weapons as part of the same action.
