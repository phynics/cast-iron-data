+++
id = "ref/arc-monk/soul-shepherd"
kind = "archetype"
title = "Soul Shepherd"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Soul%20Shepherd"
source_ids = ["pathfinder-139-the-dead-road"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soul_shepherd", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "pathfinder-139-the-dead-road"
page = "65"

[fields]
kind = "archetype"
features = [
  { anchor = "calming-strike", level = 1 },
  { anchor = "otherworldly-resilience", level = 2 },
  { anchor = "spirit-sense", level = 12 },
  { anchor = "yamaraj-s-judgment", level = 15 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["calming-strike"] },
  { replaces = "Evasion", feature = "evasion", by = ["otherworldly-resilience"] },
  { replaces = "improved evasion", feature = "improved-evasion", by = ["otherworldly-resilience"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["spirit-sense"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["yamaraj-s-judgment"] },
]
+++

Whether studying at the feet of psychopomps or merely imitating the creatures' philosophy and
methods, soul shepherds believe in safeguarding the Cycle of Souls.

## Calming Strike (Su) {#calming-strike}

As an immediate action after hitting an incorporeal undead creature with an unarmed strike, a soul
shepherd can attempt to calm the creature, encouraging it to move peacefully to the next stage of
its metaphysical journey. The target must succeed at a Will save (DC = 10 + half soul shepherd's
level + the soul shepherd's Wisdom modifier) or be calmed, as
_[calm spirit](ref/spell/calm-spirit)_, for 1 minute.

The soul shepherd can use this ability against a haunt by making a touch attack against an AC of
10 + the haunt's CR. A haunt does not receive a saving throw against this ability, but the ability's
duration changes to concentration + 1 round, up to 1 round per level. A soul shepherd can use this
ability a number of times per day equal to his soul shepherd level.

This replaces stunning fist.

## Otherworldly Resilience (Ex) {#otherworldly-resilience}

At 2nd level, a soul shepherd gains [DR](ref/rule/damage-reduction) 2/adamantine, cold resistance 5,
and electricity resistance 5. At 9th level, this improves to DR 5/adamantine, cold resistance 10,
and electricity resistance 10.

This replaces evasion and improved evasion.

## Spirit Sense (Su) {#spirit-sense}

At 12th level, a soul shepherd can spend 1 point from his ki pool as a swift action to grant himself
the ability to notice, locate, and distinguish between living and undead creatures within 30 feet,
just as if he had a [psychopomp's](ref/subtype/psychopomp) spiritsense ability (_Pathfinder RPG
Bestiary 4_ 308) for a number of rounds equal to his Wisdom modifier (minimum 1).

This replaces abundant step. (For the unchained monk from _Pathfinder Unchained_, this replaces the
ki power gained at 12th level.)

## Yamaraj's Judgment (Sp) {#yamaraj-s-judgment}

At 15th level, a soul shepherd can spend 1 point from his ki pool as a standard action to attempt to
free an enslaved soul from an effect that is imprisoning it, such as
_[soul bind](ref/spell/soul-bind)_ or _[trap the soul](ref/spell/trap-the-soul)_. This functions as
a targeted _[dispel magic](ref/spell/dispel-magic)_ spell with a caster level equal to the soul
shepherd's level. He can spend an additional ki point when he activates this ability to gain a +4
bonus on the caster level check. If the soul is held prisoner by a creature or a non-spell effect,
the soul shepherd frees it if his caster level check result is at least 11 + the creature or
effect's CR.

This replaces quivering palm. (For the unchained monk from _Pathfinder Unchained_, this ability is
gained at 16th level and replaces the ki power gained at 16th level.)
