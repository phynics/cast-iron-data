+++
id = "ref/spell/wilderness-soldiers"
kind = "spell"
title = "Wilderness Soldiers"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wilderness_soldiers", path = "json/spells16.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 2 },
  { class = "Hunter", level = 2 },
  { class = "Ranger", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft.-radius emanation, centered on you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Druid, Hunter, Ranger
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Area: 30-ft.-radius emanation, centered on you
:::

**Sources:** Ultimate Combat pg 249

You call on the plants nearby to aid you in combat. This spell is ineffective if no plants you can
direct are within the area. You can spend a swift action and/or a standard action on each of your
turns to direct one of the following attacks. The attack bonus or CMB for these attacks equals your
base attack bonus + your Wisdom modifier. You grant a +1 bonus per three caster levels (maximum +5)
on damage rolls due to this spell. Your wilderness soldiers never provoke attacks of opportunity,
and they do not count as allies for flanking or other purposes.

_Tree:_ A tree makes a melee attack with a 10-foot reach from its trunk. A hit deals an amount of
damage equal to 1d8 points + your Wisdom modifier. The tree can instead attempt a bull rush, drag,
or reposition combat maneuver with the same reach, but the tree cannot move itself.

_Undergrowth or Hedgerow:_ Acting as a Medium creature, one square of undergrowth or hedgerow
attempts a grapple combat maneuver against an opponent within or adjacent to that square. Heavy
undergrowth gains a +2 bonus to its CMD. Undergrowth cannot move the grapple or pin a foe, but it
can deal an amount of damage equal to 1d4 points + your Wisdom modifier by making a successful
grapple check against a foe it is grappling. The undergrowth's CMD is 5 + its CMB. If you fail to
direct the undergrowth to maintain the grapple, it releases its opponent.
