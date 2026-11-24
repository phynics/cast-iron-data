+++
id = "ref/arc-shaman/spirit-warden"
kind = "archetype"
title = "Spirit Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Shaman%20Spirit%20Warden"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_warden", path = "json/archetypes_shaman.json" },
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
  { anchor = "unnatural-mien", level = 1 },
  { anchor = "restless-magic" },
  { anchor = "rebuke-spirits", level = 2 },
  { anchor = "laugh-at-death", level = 10 },
]
trades = [
  { replaces = "Spirit magic spells gained from the shaman's spirit", feature = "spirit-magic", by = ["restless-magic"] },
  { replaces = "Hex gained at 2nd level", feature = "hex", levels = [2], by = ["rebuke-spirits"] },
  { replaces = "Hex gained at 10th level", feature = "hex", levels = [10], by = ["laugh-at-death"] },
]
+++

Not all spirits deserve reverence and respect. Some are twisted and despicable. It's a spirit
warden's duty to end these spirits' existence.

**Gained class skills:** intm

**Lost class skills:** diplo, ha

## Unnatural Mien (Ex) {#unnatural-mien}

At 1st level, the spirit warden's dealings with the spirit world give her an unsettling demeanor.
Diplomacy and Handle Animal are not class skills for a spirit warden. Intimidate is added as a class
skill, and she gains a +2 bonus on Intimidate checks to demoralize a foe.

## Restless Magic (Su) {#restless-magic}

The spirit warden adds the following spells to the list of spells she can cast using spirit magic:
_detect undead_ (1st), _command undead_ (2nd), _halt undead_ (3rd), _death ward_ (4th), _possess
object_ (5th), _undead to death_ (6th), _ethereal jaunt_ (7th), _control undead_ (8th), _foresight_
(9th). This ability replaces the spirit magic spells gained from the shaman's spirit.

## Rebuke Spirits (Su) {#rebuke-spirits}

At 2nd level, the spirit warden gains the ability to
[channel positive energy](ref/ability/channel-energy) as a cleric of her level. Regardless of her
alignment, she can only use this ability to harm undead creatures. The spirit warden can use this
ability a number of times per day equal to 3 + her Charisma modifier. This ability replaces the hex
gained at 2nd level.

## Laugh at Death (Su) {#laugh-at-death}

At 10th level, the spirit warden's familiarity with the dead has filled her with contempt for death
itself. She gains a +4 insight bonus on saving throws against death effects and to avoid or remove
negative levels. This ability replaces the hex gained at 10th level.
