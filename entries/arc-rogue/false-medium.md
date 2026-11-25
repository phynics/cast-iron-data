+++
id = "ref/arc-rogue/false-medium"
kind = "archetype"
title = "False Medium"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20False%20Medium"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_medium", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "occult-adventures"
page = "123"

[fields]
kind = "archetype"
features = [
  { anchor = "dim-the-lights", level = 1 },
  { anchor = "false-sensitivity", level = 2 },
  { anchor = "haunting-presences", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["dim-the-lights"] },
  { replaces = "2nd-level rogue talent", feature = "rogue-talents", levels = [2], by = ["false-sensitivity"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["haunting-presences"] },
]
+++

The false medium is a master of pretending to have occult powers in order to manipulate the emotions
and atmosphere of the people and places around him, often reaping a healthy reward from the
bereaved, who find solace in his comforting lies.

## Dim the Lights (Ex) {#dim-the-lights}

At 1st level, while in [dim light](ref/rule/vision-and-light) or darkness, a false medium adds 1/2
his rogue level as a bonus on Bluff, Disguise, and Sleight of Hand checks, and creatures without
[low-light vision](ref/rule/low-light-vision) or [darkvision](ref/rule/darkvision) take an equal
penalty on skill checks to oppose the false medium's Bluff, Disguise, and Sleight of Hand checks.
This ability replaces trapfinding.

## False Sensitivity (Ex) {#false-sensitivity}

At 2nd level, a charlatan can convincingly fake the ability to use occult skill unlocks such as
[automatic writing](ref/skill/linguistics) and [dowsing](ref/skill/survival). An untrained onlooker
can't tell the difference between the false medium's scams and a true use of occult skill unlocks.
An onlooker capable of using the particular occult skill unlock that the false medium is faking can
attempt the appropriate skill check for that unlock, opposed by the false medium's Bluff check, to
detect the fraud. In any case, any results of the false medium's charades are fabricated (for
instance, the false medium might ask leading questions to elicit false memories while pretending to
use hypnotism). This ability replaces the 2nd-level rogue talent.

## Haunting Presences (Ex) {#haunting-presences}

At 3rd level, the false medium exploits his natural talent for deception to convince others of the
presence of false supernatural entities. As long as the false medium is in conditions of dim light
or darkness, he can use Bluff skill checks to emulate the effects of
_[dancing lights](ref/spell/dancing-lights)_, _[ghost sound](ref/spell/ghost-sound)_,
_[silent image](ref/spell/silent-image)_, or _[ventriloquism](ref/spell/ventriloquism)_ by throwing
his voice, subtly misdirecting or convincing subjects, or manipulating light and shadows. The range
of these effects is 10 feet from the false medium, plus an additional 5 feet for every 3 rogue
levels he possesses beyond 3rd. The effects last for 1 round, though they can be maintained with
additional checks. Only one of these effects can be created or maintained in a given round.
Observers can attempt either a Perception or Sense Motive check (whichever of their bonuses is
higher) to oppose this Bluff check; the GM should roll these checks secretly. This is an
extraordinary ability and not an illusion, so if the false medium succeeds at the opposed check,
even powerful effects like _[true seeing](ref/spell/true-seeing)_ don't detect the fakery.

This ability replaces trap sense.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the false medium rogue archetype: esoteric scholar, fast
fingers, honeyed words, major magic, minor magic, and quick trapsmith.

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the false medium rogue archetype: feat, master of
disguise, and skill mastery.
