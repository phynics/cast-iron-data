+++
id = "ref/spell/knock-mass"
kind = "spell"
title = "Mass Knock"
source_ids = ["core-rulebook", "mythic-adventures", "inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "knock_mass", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/knock" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one means of closure/level, no two of which can be more than 30 feet apart" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Arcanist, Cleric, Inquisitor, Mesmerist, Occultist, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Target: one means of closure/level, no two of which can be more than 30 feet apart
Duration: instantaneous
Saving throw: none
Spell resistance: no
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

Also known as "unshackle," this spell functions as [knock](ref/spell/knock), but works on multiple
means of closure at once.
