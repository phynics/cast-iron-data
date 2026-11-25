+++
id = "ref/arc-shaman/visionary"
kind = "archetype"
title = "Visionary"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Visionary"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "visionary", path = "json/archetypes_shaman.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shaman" },
]
[[sources]]
publication = "advanced-class-guide"
page = "112"

[fields]
kind = "archetype"
features = [
  { anchor = "bonus-feat", level = 4 },
  { anchor = "discern-magical-expertise", level = 4 },
  { anchor = "vision-spirit-magic", level = 4 },
  { anchor = "improved-divination", level = 6 },
  { anchor = "wandering-spirit", level = 12 },
]
trades = [
  { replaces = "Wandering spirit gained at 4th level", feature = "wandering-spirit", levels = [4], by = ["discern-magical-expertise"] },
  { replaces = "Spirit magic spells gained from the shaman's wandering spirit", feature = "spirit-magic", by = ["vision-spirit-magic"] },
  { replaces = "Wandering hex gained at 6th level", feature = "wandering-hex", levels = [6], by = ["improved-divination"] },
  { replaces = "Greater version of wandering spirit gained at 12th level", feature = "wandering-spirit", levels = [12], by = ["wandering-spirit"] },
  { replaces = "true version of wandering spirit gained at 20th level", feature = "wandering-spirit", levels = [20], by = ["wandering-spirit"] },
]
+++

The visionary is a master at divination, drawing upon her intimate relationship with the spirit
world to ferret out all manner of secrets and insights about the world around her and beyond.

## Bonus Feat {#bonus-feat}

At 4th level, the visionary gains [Diviner's Delving](ref/feat/diviners-delving) as a bonus feat,
even if she does not meet the prerequisites.

## Discern Magical Expertise (Ex) {#discern-magical-expertise}

At 4th level, the shaman can determine what type of spellcasting expertise a creature possesses by
studying the creature for 2 rounds with _[detect magic](ref/spell/detect-magic)_ or any of the
following spells: _[detect chaos](ref/spell/detect-chaos)_, _[detect evil](ref/spell/detect-evil)_,
_[detect good](ref/spell/detect-good)_, or _[detect law](ref/spell/detect-law)_ (if the creature
belongs to the alignment). This ability tells the visionary what bloodlines, domains, hexes,
schools, or mysteries (if any) the creature possesses. A successful Will saving throw negates this
effect (DC = 10 + 1/2 the shaman's level + the shaman's Wisdom modifier). A creature affected by
this ability cannot be affected by it again for 24 hours. This ability functions through magical
sensors as with _[clairaudience/clairvoyance](ref/spell/clairaudience-clairvoyance)_ and
_[scrying](ref/spell/scrying)_. This ability replaces wandering spirit gained at 4th level.

## Vision Spirit Magic {#vision-spirit-magic}

At 4th level, the visionary adds the following spells to the list of spells she can cast using
spirit magic: _see alignment_ (1st), _see invisibility_ (2nd), _clairaudience/clairvoyance_ (3rd),
_detect scrying_ (4th), _prying eyes_ (5th), _legend lore_ (6th), _vision_ (7th), _moment of
prescience_ (8th), _foresight_ (9th). This ability replaces the spirit magic spells gained from the
shaman's wandering spirit.

## Improved Divination (Su) {#improved-divination}

At 6th level, the visionary becomes more adept at [divination](ref/spell/divination) magic. When she
casts the _[augury](ref/spell/augury)_ spell, her chance for an accurate answer is automatically the
maximum of 90%. Likewise, when she casts _divination_, she has the maximum 90% chance of an accurate
answer.

Finally, the visionary can prepare _[scrying](ref/spell/scrying)_ as a 4th-level spell, and it
requires only 1 minute to cast. The visionary also has a 10% chance per caster level to cast the
spells listed in the _[scrying](ref/spell/scrying)_ spell description, instead of 5% per caster
level (to a maximum of 100%).

The visionary must still prepare these spells to receive these benefits. This ability replaces the
wandering hex gained at 6th level.

## Wandering Spirit (Su) {#wandering-spirit}

At 12th level, the visionary forms a temporary bond with another spirit (other than the one she
selected using her spirit class feature). This is identical to the 4th-level shaman class feature.
This adds the wandering spirit magic spells to the list of spells she can cast using spirit magic,
along with vision spirit magic and her original spirit. At 20th level, she gains the abilities
listed in the greater version of her wandering spirit. This ability replaces the greater version of
wandering spirit gained at 12th level and true version of wandering spirit gained at 20th level.
