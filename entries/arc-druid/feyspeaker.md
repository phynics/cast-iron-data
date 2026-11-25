+++
id = "ref/arc-druid/feyspeaker"
kind = "archetype"
title = "Feyspeaker"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Feyspeaker"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feyspeaker", path = "json/archetypes_druid.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "fey-magic", level = 1 },
  { anchor = "fey-speech", level = 1 },
  { anchor = "wild-mischief", level = 1 },
]
trades = [
  { replaces = "Nature sense", feature = "nature-sense", by = ["fey-speech"] },
  { replaces = "The druid's proficiency with medium armor", feature = "weapon-and-armor-proficiencies", power = "medium armor", by = ["wild-mischief"] },
  { alters = "Spellcasting", feature = "spells", by = ["fey-magic"] },
  { alters = "Base attack bonus", by = ["fey-speech"] },
  { alters = "class skills", by = ["fey-speech"] },
  { alters = "skills ranks per level", by = ["fey-speech"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["fey-magic"] },
]
+++

Some druids hear the whispers of the natural world like fey creatures do, and learn to mimic those
tantalizing murmurs in order to influence the minds of both wild beasts and civilized people. These
feyspeakers are often touched by the fey in some way, such as mortals who dared to eat the food and
drink the wine while in the hidden halls of the fey.

## Fey Magic {#fey-magic}

At 1st level, a feyspeaker allows the strange idylls of the fey to guide her magic. The feyspeaker
uses her Charisma score instead of her Wisdom score as her key spellcasting ability score (to
determine her spell DCs, [bonus spells](ref/rule/determine-bonuses) per day, concentration checks,
and so on).

At 4th, 6th, 8th, 10th, 12th, 14th, 16th, and 18th levels, a feyspeaker adds one enchantment or
illusion spell from the sorcerer/wizard spell list to her druid spell list as a spell of 1 level
higher (for instance, at 4th level, she could add _[color spray](ref/spell/color-spray)_ as a
2nd-level druid spell). In order to select a spell, she must be of a level high enough (including
the increased spell level) to cast it. Once selected, the spell cannot be changed.

A feyspeaker loses the ability to spontaneously cast
_[summon nature's ally](ref/spell/summon-natures-ally)_ spells. She gains the wild shape ability at
6th level and gains all benefits related to wild shape 2 druid levels later than usual. She can
never use wild shape to transform into an elemental.

This ability alters wild shape and spellcasting.

## Fey Speech (Ex) {#fey-speech}

At 1st level, a feyspeaker's words carry a tiny fragment of the otherworldly power of the fey's
voices. She gains [Bluff](ref/skill/bluff), [Diplomacy](ref/skill/diplomacy),
[Disguise](ref/skill/disguise), and [Sense Motive](ref/skill/sense-motive) as class skills. A
feyspeaker also learns Sylvan as a bonus language. In addition, the feyspeaker gains a number of
skill ranks at each level equal to 6 + her Intelligence modifier, instead of 4 + her Intelligence
modifier. The feyspeaker's base attack bonus from her druid levels is equal to
[half](ref/misc/fractions-and-rounding) her druid level (much like a sorcerer's base attack bonus is
calculated), rather than the usual druid base attack bonus.

This ability replaces nature sense and alters the druid's base attack bonus, class skills, and
skills ranks per level.

## Wild Mischief (Ex) {#wild-mischief}

At 1st level, a feyspeaker can fool an animal into thinking there is food, a potential mate, or a
predator nearby. This ability functions just like a Bluff check to deceive a character. To determine
the result of the wild mischief check, the feyspeaker rolls 1d20 and adds her druid level and her
Charisma modifier. As with Bluff checks, wild mischief checks are modified depending on the
believability of the false information. A typical domestic animal is not particularly suspicious of
the feyspeaker (no circumstance modifier), whereas wild animals are usually suspicious (-5 penalty
on the check).

To use wild mischief, the feyspeaker and the animal must be able to study each other, which means
they must be within 30 feet of one another under normal conditions. Generally, influencing an animal
in this way takes 1 minute, but as when influencing people, it could take more or less time. A
feyspeaker can also use this ability to influence a magical beast with an Intelligence score of 1 or
2, but she takes a -4 penalty on the check.

This ability replaces the druid's proficiency with medium armor.
