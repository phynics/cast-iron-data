+++
id = "ref/spell/irriseni-mirror-sight"
kind = "spell"
title = "Irriseni Mirror Sight"
source_ids = ["pathfinder-67-the-snows-of-summer", "cities-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "irriseni_mirror_sight", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/scrying" },
]

[fields]
kind = "spell"
school = "divination"
subschools = ["Scrying"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S, F (a mirror)"
range = "see text"
effects = [
  { label = "Effect", value = "magical sensor" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, F (a mirror)
Range: see text
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Effect: magical sensor
Subschool: Scrying
:::

**Sources:** Pathfinder \#67: The Snows of Summer pg 73, Cities of Golarion pg 63

This spell lets you look into a mirror near you and see an image that is reflected in another
specific mirror (chosen by you) or an individual reflected in any other mirror. This works like a
[scrying](ref/spell/scrying) spell, except you can only view creatures on the same plane as you.
Each time you cast the spell, you can choose to see one of three types of reflections in your
mirror.

_Known Mirror:_ The current reflection in another mirror with which you are familiar.

_Known Person:_ The current reflection of a person you know well, assuming that person is near a
mirror.

_Known Place:_ The current reflection of a place you know well, assuming the location is being
reflected in a mirror.

You receive only visual information through this ability. You can choose to transmit information
both ways so that a person reflected in the remote mirror can view whatever appears in the mirror
you are using.

For example, Urion Petresky knows that Queen Elvanna keeps a mirror in a hall near her throne room.
He can look through his own handheld mirror and see into this hall, even if the queen is not there.
Alternatively, he can attempt to find the queen (wherever she is) by looking into his mirror; if, at
that moment, the queen is near any mirror at all, he can see her. He may instead cast the spell and
try to see into her throne room, hoping that someone has brought a mirror there. If any of these
conditions fails, Urion sees nothing but his own reflection.

This spell works with intentionally fabricated mirrors only; it is not effective with other
reflective surfaces, such as still pools or polished metal shields. Effects that block scrying block
this spell.
