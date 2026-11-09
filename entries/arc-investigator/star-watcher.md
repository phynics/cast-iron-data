+++
id = "ref/arc-investigator/star-watcher"
kind = "archetype"
title = "Star Watcher"
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
replaces = ["Trapfinding", "trap sense", "Swift alchemy"]
alters = ["Weapon and armor proficiency", "Alchemy", "Investigator talents"]
+++

Star watchers study the movements and positions of the sun, the moon, and the stars, searching for
secrets written in the sky. They use a combination of scientific study and esoteric arts to measure,
record, and predict astronomical cycles and their effects on nature, such as the moon's influence on
tides and rivers. Some star watchers also use these observations to predict fate and significant
events, such as natural disasters.

**Weapon and Armor Proficiency**

**Ability:** A star watcher gains proficiency with the [starknife](ref/eq-weapon/starknife), but not
with the rapier.

**Alters:** Weapon and armor proficiency

**Astrology (Su)**

**Action:** Ability

**Alters:** Alchemy

**Special:** A star watcher doesn't gain a competence bonus on Craft (alchemy) checks to create
alchemical items, and he cannot identify potions with that skill. Furthermore, a star watcher cannot
select alchemist discoveries as investigator talents. A star watcher can study a
[wizard's](ref/class/wizard) spellbook or [alchemist's](ref/class/alchemist) formula book to learn
formulae, but a star watcher's formula book is too esoteric for anyone except another star watcher
to learn spells from.

A star watcher studies a symbolic language of the heavens known as _astrology._ Equal parts art form
and science, _astrology_ can be used to read the future and affect it in subtle ways. Much like an
alchemist or investigator, a star watcher collects formulae in a formula book. However, the formulae
resemble star charts, and unlike alchemists or normal investigators, he uses these formulae along
with personal details and astronomical measurements to make horoscopes - magical calculations stored
much like scrolls - in which he can store spells. In many ways, the star watcher's horoscopes
function like extracts, with the following exceptions.

A star watcher's horoscope is always keyed to a specific creature that must be willing and present
when the star watcher prepares the horoscope. Only the creature to which a horoscope is keyed can
activate it and be affected by it. A horoscope is "cast" by reading it as a **standard action**,
though a star watcher can draw and read a horoscope as a single **standard action**.

**Starfinding (Ex)**

**Ability:** A star watcher adds half his level (minimum 1) as a bonus on Knowledge (geography)
checks. He can also use astrological methods to read people. By checking his star charts, he can use
Knowledge (geography) in place of Sense Motive checks.

**Replaces:** Trapfinding, trap sense

**Investigator Talents**

**Ability:** A star watcher can select the following talents, in addition to general investigator
talents.

**Alters:** Investigator talents

**Replaces:** Swift alchemy

**Horoscopic Scrolls (Su)**

**Ability:** The star watcher gains [Scribe Scroll](ref/feat/scribe-scroll) as a bonus feat. He can
use the feat to create an arcane scroll of any formula he knows. Unlike horoscopes created with the
_astrology_ ability, anyone capable of using arcane scrolls can cast a spell from these scrolls.
Additionally, the star watcher can use scrolls as if he were an arcane spellcaster. He can use
Knowledge (geography) to identify scrolls as if using [detect magic](ref/spell/detect-magic). He
must hold the scroll for 1 round to attempt such a check.

**Precognition (Su)**

**Flavor:** A star watcher can glimpse into the mysterious possibilities of the future and prepare a
horoscope he knows he'll need later.

**Prereq:** 4th-level investigator

**Swift:** Once per day, a star watcher can treat an open extract slot as though he had prepared a
horoscope keyed to himself in it, choosing one formula of the appropriate level from his formula
book.

**Shooting Star (Ex)**

**Ability:** He can apply the benefits of _studied combat, studied strike,_ and investigator talents
that add effects to _studied combat_ or _studied strike_ while using a starknife as a thrown weapon.

**Flavor:** A star watcher can calculate trajectories with terrifying accuracy.

**Returning Star (Ex)**

**Ability:** Whenever the star watcher uses a starknife as a thrown weapon against a target of his
_studied combat,_ the starknife automatically returns as if it had the
[returning](ref/magic-enh/returning) property.

**Prereq:** _Shooting Star_ talent
