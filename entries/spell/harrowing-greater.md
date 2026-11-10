+++
id = "ref/spell/harrowing-greater"
kind = "spell"
title = "Greater Harrowing"
source_ids = ["inner-sea-world-guide", "the-harrow-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "harrowing_greater", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/harrowing" },
]
[[sources]]
publication = "the-harrow-handbook"
page = "9"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "10 minutes"
components = "V, S, F (a Harrow deck)"
range = "touch"
effects = [
  { label = "Target", value = "one creature, plus one additional creature for every 3 caster levels" },
]
duration = "1 day/level or until fulfilled"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 5: Bard, Skald\
6: Arcanist, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, F (a Harrow deck)
Range: touch
Target: one creature, plus one additional creature for every 3 caster levels
Duration: 1 day/level or until fulfilled
Saving throw: none
Spell resistance: no
:::

### Greater Harrowing

This spell functions as [harrowing](ref/spell/harrowing), except it can affect an entire group of
creatures and allows its subjects some measure of control over their destiny. Subjects of a greater
harrowing spell record and spend their accumulated bonuses and penalties individually, according to
their own alignment.

Each participant in a greater harrowing can gain a special ability to seize control of fate if a
card that matches that participant's alignment is drawn. Like the bonuses and penalties granted by
the spell, the special ability can be used once before the end of the spell's duration. The exact
ability gained depends on the card's suit; if multiple cards that match a participant's alignment
are drawn, the participant can select one suit of her choice during the spell's casting.

_Hammers:_ As a standard action, you can grant yourself a +4 enhancement bonus to Strength for 1
minute. While this bonus persists, you can reroll any bull rush, grapple, or sunder combat maneuver
checks. You must use the result of this second roll, even if it is worse.

_Keys:_ As a standard action, you can grant yourself a +4 enhancement bonus to Dexterity for 1
minute. While this bonus persists, you gain [evasion](ref/ability/evasion), as the rogue class
feature. If you already possess evasion, you instead gain
[improved evasion](ref/talent/improved-evasion), as the advanced rogue talent.

_Shields:_ As a standard action, you can grant yourself a +4 enhancement bonus to Constitution for 1
minute. While this bonus persists, you gain [fast healing](ref/umr/fast-healing) 1 and don't die
until you reach a number of negative hit points equal to double your Constitution.

_Books:_ As a standard action, you can grant yourself a +4 enhancement bonus to Intelligence for 1
minute. While this bonus persists, you gain a +3 enhancement bonus on checks with all skills you
have no ranks in, and you can use those skills even if they can't normally be used untrained.

_Stars:_ As a standard action, you can grant yourself a +4 enhancement bonus to Wisdom for 1 minute.
While this bonus persists, you gain immunity to one of the following (your choice): charm and
compulsion effects, curse effects, or fear effects.

_Crowns:_ As a standard action, you can grant yourself a +4 enhancement bonus to Charisma for 1
minute. While this bonus persists, whenever you succeed at a Diplomacy or Intimidate check to
improve a non-hostile creature's attitude toward you, that creature's attitude toward you becomes
helpful for the remaining duration of the Charisma bonus, regardless of the number of steps by which
you would normally improve its attitude. The creature reverts to its original attitude after the
duration expires.

A single creature can be under the effects of only one harrowing or greater harrowing at a time. If
the subject is targeted with a second harrowing or greater harrowing spell while a previous
harrowing or greater harrowing is still affecting him, the new spell automatically fails for that
subject.
