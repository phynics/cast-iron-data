+++
id = "ref/arc-monk/menhir-guardian"
kind = "archetype"
title = "Menhir Guardian"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Menhir%20Guardian"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "menhir_guardian", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "64"

[fields]
kind = "archetype"
features = [
  { anchor = "claws", level = 1 },
  { anchor = "wild-flurry" },
  { anchor = "rebuking-strike", level = 1 },
]
trades = [
  { replaces = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Unarmed strike", feature = "unarmed-strike", by = ["claws"] },
  { replaces = "ki strike", feature = "ki-pool", power = "ki strike", by = ["claws"] },
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["rebuking-strike"] },
  { replaces = "high jump", feature = "high-jump", by = ["rebuking-strike"] },
  { replaces = "quivering palm", feature = "quivering-palm", by = ["rebuking-strike"] },
  { alters = "Alignment requirement" },
  { alters = "Ki pool", feature = "ki-pool", by = ["claws"] },
  { alters = "Furry of blows", feature = "flurry-of-blows", by = ["wild-flurry"] },
]
+++

Menhir guardians are ascetic protectors of sacred druidic sites, less concerned with structure and
maintaining internal order than they are with preserving the natural balance of the world.

## Alignment {#alignment}

A menhir guardian can be lawful neutral, neutral good, neutral evil, or neutral. While they can work
with chaotic allies, they cannot themselves be chaotic.

This alters the monk's alignment requirement.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A menhir guardian is proficient with the [club](ref/eq-weapon/club), [dagger](ref/eq-weapon/dagger),
[dart](ref/eq-weapon/dart), [quarterstaff](ref/eq-weapon/quarterstaff),
[sickle](ref/eq-weapon/sickle), [shortspear](ref/eq-weapon/shortspear),
[sling](ref/eq-weapon/sling), and [spear](ref/eq-weapon/spear). A menhir guardian can use these
weapons in conjunction with his wild flurry ability.

This replaces the monk's weapon and armor proficiency.

## Claws (Ex) {#claws}

A menhir guardian learns to draw upon natural forces to subtly change his body. He gains the
[shifter's](ref/class/shifter) shifter claws class feature and treats his monk level as his shifter
level for the purposes of this ability. The menhir guardian cannot use the ki strike aspect of ki
pool.

This replaces unarmed strike and alters ki pool.

## Wild Flurry (Ex) {#wild-flurry}

A menhir guardian gains flurry of blows. He can use this ability with the natural attacks provided
by his shifter claws ability or the weapons specified above under weapon and armor proficiency.

This alters furry of blows.

## Rebuking Strike (Ex) {#rebuking-strike}

At 1st level, a menhir guardian can channel his ki into a devastating strike that repels his
enemies. A menhir guardian must declare that he is using rebuking strike before making a
[natural attack](ref/umr/natural-attacks) with his claws. On a hit, a foe damaged by the menhir
guardian's claws must succeed at a Fortitude saving throw (DC = 10 + half the menhir guardian's
level + his Wisdom modifier) or be pushed back 5 feet directly away from the menhir guardian, plus
an additional 5 feet for every 4 levels the menhir guardian has beyond 1st. If this movement would
be blocked by a solid object, the target of rebuking strike takes 1d6 points of damage per 10 feet
moved and falls [prone](ref/rule/prone) at the end of the movement.

At 5th level, a creature that fails its save against a menhir guardian's rebuking strike also has
its speed reduced by half for a number of rounds equal to the menhir guardian's level.

At 15th level, a creature that fails its save is also affected by _[aversion](ref/spell/aversion)_,
making it avoid the menhir guardian's current location for 1 round per level the menhir guardian
has.

The menhir guardian can attempt a rebuking strike a number of times per day equal to his monk level
but only once per round.

This replaces stunning fist, high jump, and quivering palm.
