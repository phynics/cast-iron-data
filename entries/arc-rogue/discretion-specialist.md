+++
id = "ref/arc-rogue/discretion-specialist"
kind = "archetype"
title = "Discretion Specialist"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Discretion%20Specialist"
source_ids = ["antiheros-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "discretion_specialist", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "antiheros-handbook"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "fast-talker", level = 1 },
  { anchor = "obfuscation", level = 3 },
  { anchor = "evidence-disposal", level = 4 },
  { anchor = "no-loose-ends", level = 4 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["fast-talker"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["obfuscation"] },
  { replaces = "Danger sense", by = ["obfuscation"] },
  { replaces = "Rogue talents gained at 4th and 12th levels", feature = "rogue-talents", levels = [4, 12], by = ["evidence-disposal"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["no-loose-ends"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["no-loose-ends"] },
]
+++

Often brought in to handle messy situations, discretion specialists deal with bodies, inconvenient
witnesses, and other loose ends. Many organizations employ them to cover up activities that might be
unpopular—should they become known to the general populace.

This archetype is appropriate for rogues built using either the _Pathfinder RPG Core Rulebook_ or
_Pathfinder RPG Pathfinder Unchained_.

## Fast Talker (Ex) {#fast-talker}

A discretion specialist adds half her rogue level (minimum +1) as a bonus on Bluff, Diplomacy, and
Intimidate checks.

This replaces trapfinding.

## Obfuscation (Su) {#obfuscation}

A discretion specialist is highly skilled at convincing others not to trust their own senses. At 3rd
level as a full-round action, the discretion specialist can convince one living creature within 30
feet that up to 5 minutes of its memories from the past hour are unreliable. If the target fails a
Will saving throw (DC = 10 + half the discretion specialist's rogue level + her Intelligence
modifier), the target is convinced that those memories didn't happen or that it's confusing the
memories with a dream (or is otherwise hazy as to the memories' reality). Each hour after the
discretion specialist uses this ability, the target can attempt a new Will saving throw to realize
that its relevant memories have been tampered with, although not necessarily that the discretion
specialist was the originator of the tampering.

The discretion specialist can use this ability once per day, and one additional time per day for
every 5 rogue levels she has. At 6th level and every 3 levels thereafter, the discretion specialist
can obfuscate memories from an additional hour in the past (to a maximum of 6 hours at 18th level).

This replaces trap sense (for a core rogue) or danger sense (for an unchained rogue).

## Evidence Disposal (Sp) {#evidence-disposal}

A discretion specialist can cover up a corpse's cause of a death—or dispose of it entirely. At 4th
level, the discretion specialist gains the ability to cast _[dress corpse](ref/spell/dress-corpse)_
as a [spell-like ability](ref/umr/spell-like-abilities), using her rogue level as her caster level.
She can use this ability once per day, plus one additional time per day for every 5 rogue levels she
has (to a maximum of five times at 20th level).

At 12th level, she can spend two uses of this ability to disintegrate a corpse entirely as a
full-round action, leaving behind only a trace of fine dust (a disintegrated creature's equipment is
unaffected). The target cannot be an undead creature. A corpse disintegrated this way cannot be
brought back to life except by _[resurrection](ref/spell/resurrection)_ or more powerful magic,
including _[miracle](ref/spell/miracle)_ or _[wish](ref/spell/wish)_.

This replaces the rogue talents gained at 4th and 12th levels.

## No Loose Ends (Ex) {#no-loose-ends}

At 4th level, the discretion specialist can prevent opponents from escaping. Opponents damaged by
the discretion specialist's sneak attack are unable to take the [withdraw](ref/rule/withdraw) action
for 1 round, though they can still move as normal.

At 8th level, a creature damaged by the discretion specialist's sneak attack is hampered in casting
spells of the teleportation subschool (such as _[dimension door](ref/spell/dimension-door)_) as well
as using methods of magical transport such as _[shadow walk](ref/spell/shadow-walk)_. A target
attempting to cast such a spell before the end of the discretion specialist's next turn must succeed
at a [concentration](ref/rule/concentration) check (in addition to any concentration checks required
for casting while threatened or other circumstances) or lose the spell. The DC of this check is
equal to 10 + half the discretion specialist's rogue level + her Intelligence modifier.

This replaces uncanny dodge and improved uncanny dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement this archetype: camouflage, charmer, convincing lie, honeyed
words, and quick disguise.

## Advanced Talents {#advanced-talents}

The following advanced talents complement this archetype: hide in plain sight and master of
disguise.
