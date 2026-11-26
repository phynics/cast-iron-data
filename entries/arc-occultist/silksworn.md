+++
id = "ref/arc-occultist/silksworn"
kind = "archetype"
title = "Silksworn"
aon = "ArchetypeDisplay.aspx?FixedName=Occultist%20Silksworn"
source_ids = ["heroes-of-the-high-court"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "silksworn", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "heroes-of-the-high-court"
page = "29"

[fields]
kind = "archetype"
features = [
  { anchor = "spells" },
  { anchor = "implements" },
  { anchor = "cantrips", level = 1 },
  { anchor = "mental-focus" },
  { anchor = "devoted-mystic" },
  { anchor = "silksworn-eloquence", level = 8 },
  { anchor = "silksworn-deception", level = 12 },
  { anchor = "silksworn-arcana", level = 16 },
  { anchor = "implement-mastery", level = 20 },
]
trades = [
  { replaces = "Knacks", feature = "knacks", by = ["cantrips"] },
  { replaces = "Outside contact", feature = "outside-contact", by = ["devoted-mystic"] },
  { replaces = "Magic circles", feature = "magic-circles", by = ["silksworn-eloquence"] },
  { replaces = "Binding circles", feature = "binding-circles", by = ["silksworn-deception"] },
  { replaces = "Fast circles", feature = "fast-circles", by = ["silksworn-arcana"] },
  { alters = "Spells", feature = "spells", by = ["spells"] },
  { alters = "Implements", feature = "implements", by = ["implements", "devoted-mystic"] },
  { alters = "Mental focus", feature = "mental-focus", by = ["mental-focus"] },
  { alters = "weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies", by = ["devoted-mystic"] },
  { alters = "Implement mastery", feature = "implement-mastery", by = ["implement-mastery"] },
  { alters = "Class skills" },
]
+++

Occultists who recognize that flashy garb and fashionable accoutrements can be just as powerful as
psychically charged relics in the right situations are known as silksworn. They draw their power
from wearing luxurious garments and can be found in many noble courts throughout Golarion, though
they often keep their abilities secret. Silksworn are even found among the mystics and the magical
practitioners of Nex, each seeking the patronage of one or more of the Arclords.

## Class Skills {#class-skills}

A silksworn adds Bluff and Knowledge (nobility) to his list of class skills, instead of Knowledge
(engineering) and Knowledge (planes).

This alters the occultist's class skills.

## Spells {#spells}

A silksworn's spells are considered arcane spells, not psychic spells, and his spells use verbal and
somatic components instead of thought and emotion components.

This alters the occultist's spells.

## Implements {#implements}

When a silksworn chooses an implement school, he does not choose a specific object. Instead, a
silksworn must be wearing an ostentatious garment or magic item worth 10 gp or more of the
appropriate type and in the appropriate slot: abjuration (wrists), conjuration (shoulders),
divination (eyes), enchantment (neck), evocation (hands), illusion (head), necromancy (chest), and
transmutation (feet). A silksworn who does not meet this requirement is treated as lacking the
appropriate implement for the purpose of his class features, including spellcasting.

This alters the occultist's implements.

## Cantrips {#cantrips}

Each time he selects an implement school, a silksworn gains one cantrip, or 0-level arcane spell
(including when he selects a school that he has already learned to use). These cantrips otherwise
behave as an occultist's knacks.

This ability replaces knacks.

## Mental Focus (Su) {#mental-focus}

The silksworn's available mental focus is equal to his occultist level + his Intelligence modifier +
his Charisma modifier.

This ability alters mental focus.

## Devoted Mystic {#devoted-mystic}

A silksworn is proficient with only simple weapons and isn't proficient with any armor or shields.

At 1st level, the silksworn gains access to four implement schools instead of two. At 2nd level and
every 4 occultist levels thereafter, the silksworn gains access to an additional implement school,
to a maximum of nine schools at 18th level.

At 8th, 12th, and 16th levels, the silksworn increases the number of spells of each level he can
cast each day by one. This does not allow the silksworn to cast spells of a level he does not yet
have access to.

This ability alters implements and the occultist's weapon and armor proficiencies, and replaces
outside contact.

## Silksworn Eloquence (Ex) {#silksworn-eloquence}

At 8th level, a silksworn gains a +1 bonus on Bluff and Diplomacy checks for each magical article of
clothing occupying one of his implement schools' magic item slots.

This ability replaces magic circles.

## Silksworn Deception (Su) {#silksworn-deception}

At 12th level, a silksworn can hide his speech and gestures within his extravagant clothing.
Whenever the silksworn casts a spell, he can attempt a Bluff check opposed by Sense Motive checks
from those observing him. Those who fail are unaware of his spellcasting, unless an effect obviously
originates from the silksworn.

This ability replaces binding circles.

## Silksworn Arcana (Su) {#silksworn-arcana}

At 16th level, when a silksworn casts a spell while wearing a magic article of clothing in the
appropriate school's magic item slot, the spell's saving throw DC increases by 2.

This ability replaces fast circles.

## Implement Mastery (Su) {#implement-mastery}

At 20th level, a silksworn chooses two implement schools instead of one, and implement mastery's
effects apply to both. The silksworn gains 4 additional points of mental focus for each school's
implement.

This alters the occultist's implement mastery.
