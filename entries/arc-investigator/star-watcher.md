+++
id = "ref/arc-investigator/star-watcher"
kind = "archetype"
title = "Star Watcher"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Star%20Watcher"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "star_watcher", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "57"

[fields]
kind = "archetype"
features = [
  { anchor = "astrology" },
  { anchor = "starfinding", level = 1 },
  { anchor = "investigator-talents" },
  { anchor = "horoscopic-scrolls" },
  { anchor = "precognition" },
  { anchor = "returning-star" },
  { anchor = "shooting-star" },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["starfinding"] },
  { replaces = "trap sense", feature = "trap-sense", by = ["starfinding"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["investigator-talents"] },
  { alters = "Weapon and armor proficiency", feature = "weapon-and-armor-proficiencies" },
  { alters = "Alchemy", feature = "alchemy", by = ["astrology"] },
  { alters = "Investigator talents", feature = "investigator-talent", by = ["investigator-talents"] },
]
+++

Star watchers study the movements and positions of the sun, the moon, and the stars, searching for
secrets written in the sky. They use a combination of scientific study and esoteric arts to measure,
record, and predict astronomical cycles and their effects on nature, such as the moon's influence on
tides and rivers. Some star watchers also use these observations to predict fate and significant
events, such as natural disasters.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A star watcher gains proficiency with the [starknife](ref/eq-weapon/starknife), but not with the
rapier.

This alters the investigator's weapon and armor proficiency.

## Astrology (Su) {#astrology}

A star watcher studies a symbolic language of the heavens known as astrology. Equal parts art form
and science, astrology can be used to read the future and affect it in subtle ways. Much like an
alchemist or investigator, a star watcher collects formulae in a formula book. However, the formulae
resemble star charts, and unlike alchemists or normal investigators, he uses these formulae along
with personal details and astronomical measurements to make horoscopes—magical calculations stored
much like scrolls—in which he can store spells. In many ways, the star watcher's horoscopes function
like extracts, with the following exceptions.

A star watcher's horoscope is always keyed to a specific creature that must be willing and present
when the star watcher prepares the horoscope. Only the creature to which a horoscope is keyed can
activate it and be affected by it. A horoscope is "cast" by reading it as a standard action, though
a star watcher can draw and read a horoscope as a single standard action.

A star watcher doesn't gain a competence bonus on Craft (alchemy) checks to create alchemical items,
and he cannot identify potions with that skill. Furthermore, a star watcher cannot select alchemist
discoveries as investigator talents. A star watcher can study a [wizard's](ref/class/wizard)
spellbook or [alchemist's](ref/class/alchemist) formula book to learn formulae, but a star watcher's
formula book is too esoteric for anyone except another star watcher to learn spells from.

This alters alchemy.

## Starfinding (Ex) {#starfinding}

A star watcher adds half his level (minimum 1) as a bonus on Knowledge (geography) checks. He can
also use astrological methods to read people. By checking his star charts, he can use Knowledge
(geography) in place of Sense Motive checks.

This replaces trapfinding and trap sense.

## Investigator Talents {#investigator-talents}

A star watcher can select the following talents, in addition to general investigator talents.

## Horoscopic Scrolls (Su) {#horoscopic-scrolls}

The star watcher gains [Scribe Scroll](ref/feat/scribe-scroll) as a bonus feat. He can use the feat
to create an arcane scroll of any formula he knows. Unlike horoscopes created with the astrology
ability, anyone capable of using arcane scrolls can cast a spell from these scrolls. Additionally,
the star watcher can use scrolls as if he were an arcane spellcaster. He can use Knowledge
(geography) to identify scrolls as if using _[detect magic](ref/spell/detect-magic)_. He must hold
the scroll for 1 round to attempt such a check.

## Precognition (Su) {#precognition}

A star watcher can glimpse into the mysterious possibilities of the future and prepare a horoscope
he knows he'll need later. Once per day as a swift action, a star watcher can treat an open extract
slot as though he had prepared a horoscope keyed to himself in it, choosing one formula of the
appropriate level from his formula book. A star watcher must be at least 4th level to select this
talent.

## Returning Star (Ex) {#returning-star}

Whenever the star watcher uses a starknife as a thrown weapon against a target of his studied
combat, the starknife automatically returns as if it had the _[returning](ref/magic-enh/returning)_
property. The star watcher must have the shooting star investigator talent to select this talent.

## Shooting Star (Ex) {#shooting-star}

A star watcher can calculate trajectories with terrifying accuracy. He can apply the benefits of
studied combat, studied strike, and investigator talents that add effects to studied combat or
studied strike while using a starknife as a thrown weapon.

Access to these additional talents replaces swift alchemy.
