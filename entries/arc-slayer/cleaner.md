+++
id = "ref/arc-slayer/cleaner"
kind = "archetype"
title = "Cleaner"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Cleaner"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cleaner", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "advanced-class-guide"
page = "118"

[fields]
kind = "archetype"
features = [
  { anchor = "deceitful", level = 1 },
  { anchor = "without-a-trace", level = 4 },
  { anchor = "mislead", level = 7 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["deceitful"] },
  { replaces = "Slayer talent gained at 4th level", feature = "slayer-talents", levels = [4], by = ["without-a-trace"] },
  { replaces = "Stalker", feature = "stalker", by = ["mislead"] },
]
+++

A cleaner is responsible for destroying or removing incriminating evidence from a crime scene,
disposing of corpses and eliminating witnesses to make a crime look like an accident or a mere
disappearance.

## Deceitful {#deceitful}

At 1st level, a cleaner becomes skilled at deceiving others, and gains
[Deceitful](ref/feat/deceitful) as a bonus feat. This ability replaces track.

## Without a Trace (Ex) {#without-a-trace}

At 4th level, a cleaner is able to study a location, conceal evidence, and hide in or extricate
himself quickly from that location. Studying a location takes 1 minute for each 10-foot square. Once
he has studied an area, the cleaner can attempt a Disguise check to alter evidence or a Stealth
check to conceal evidence (by doing things such as cleaning up bloodstains, obscuring footprints,
moving a dead body, and so on). Altering an area takes 1d3 � 10 minutes of work per 10-foot square.
Anyone attempting to determine what actually happened in that area must succeed at an opposed
Perception check against the result of the cleaner's Disguise or Stealth check (cleaner's choice) or
accept the altered scene as truth. The cleaner gains a +4 bonus on this check, on Sleight of Hand
checks to hide objects from that location on his person, and on Stealth checks to hide within or
escape from that location. This lasts as long as the scene remains unaltered (except by the
cleaner). This ability replaces the slayer talent gained at 4th level.

## Mislead (Sp) {#mislead}

At 7th level, a cleaner can cast _[misdirection](ref/spell/misdirection)_ on himself at will. This
lasts until the cleaner uses the ability again or ends the effect as a standard action. This ability
replaces stalker.

## Slayer Talents {#slayer-talents}

The following slayer talents (and rogue talents) complement the cleaner archetype:
[camouflage](ref/talent/camouflage), [fast stealth](ref/talent/fast-stealth), foil scrutiny\*,
[rogue crawl](ref/talent/rogue-crawl), [surprise attack](ref/talent/surprise-attack), and
[terrain mastery](ref/talent/terrain-mastery). (Those with asterisks \[\*\] are detailed in the
slayer class, starting on page 53.)

## Advanced Slayer Talents {#advanced-slayer-talents}

The following advanced slayer talents (and advanced rogue talents) complement the cleaner archetype:
assassinate\*, [knock-out blow](ref/talent/knock-out-blow),
[master of disguise](ref/talent/master-of-disguise), and slayer camouflage\*.
