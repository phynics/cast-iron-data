+++
id = "ref/spell/knock-mass"
kind = "spell"
title = "Mass Knock"
source_ids = ["core-rulebook", "mythic-adventures", "inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "knock_mass", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one door, box, or chest with an area of up to 10 sq. ft./level" },
]
duration = "instantaneous; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Inquisitor, Medium, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous; see text
Saving throw: none
Spell resistance: no
Target: one door, box, or chest with an area of up to 10 sq. ft./level
:::

## Knock

**Sources:** PRPG Core Rulebook pg 303

Knock opens stuck, barred, or locked doors, as well as those subject to
[hold portal](ref/spell/hold-portal) or [arcane lock](ref/spell/arcane-lock). When you complete the
casting of this spell, make a caster level check against the DC of the lock with a +10 bonus. If
successful, knock opens up to two means of closure. This spell opens secret doors, as well as locked
or trick-opening boxes or chests. It also loosens welds, shackles, or chains (provided they serve to
hold something shut). If used to open an arcane locked door, the spell does not remove the arcane
lock but simply suspends its functioning for 10 minutes. In all other cases, the door does not
relock itself or become stuck again on its own. Knock does not raise barred gates or similar
impediments (such as a portcullis), nor does it affect ropes, vines, and the like. The effect is
limited by the area. Each casting can undo as many as two means of preventing access.

### Mythic Knock

**Sources:** Mythic Adventures pg 99

The spell unlocks up to three means of closure instead of two. The spell automatically opens locks
of simple or average quality, without requiring a caster level check to do so). If used on a door
locked with arcane lock, you can attempt a free dispel check against it as if using a targeted
[dispel magic](ref/spell/dispel-magic), adding your tier to the check.

_Augmented (3rd):_ You can expend two uses of mythic power to target one locked item per tier,
unlocking up to four means of closure on each, allowing a free dispel against an arcane lock on
each, and automatically opening locks of up to good quality (no caster level check needed).

If the door has a trap that triggers when opened, you become aware of the trap and its general
nature, and the door is unlocked but doesn't automatically open.

The spell can raise a barred gate, portcullis, or similar impediment, but each one counts as two
locked doors.

### Mass Knock

**Sources:** Inner Sea Temples pg 23

Also known as "unshackle," this spell functions as knock, but works on multiple means of closure at
once.
