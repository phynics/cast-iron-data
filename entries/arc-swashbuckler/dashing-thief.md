+++
id = "ref/arc-swashbuckler/dashing-thief"
kind = "archetype"
title = "Dashing Thief"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Dashing%20Thief"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dashing_thief", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "adventurers-guide"
page = "51"

[fields]
kind = "archetype"
features = [
  { anchor = "bold-thief" },
  { anchor = "thief-s-confidence", level = 1 },
  { anchor = "rogue-talents", level = 4 },
  { anchor = "dazing-charm-deed", level = 3 },
  { anchor = "swaying-charm-deed", level = 15 },
]
trades = [
  { replaces = "The swashbuckler's ability to regain panache from a killing blow", by = ["thief-s-confidence"] },
  { replaces = "Bonus feats", feature = "bonus-feats", by = ["rogue-talents"] },
  { replaces = "Menacing swordplay deed", feature = "deeds", power = "menacing swordplay", by = ["dazing-charm-deed"] },
  { replaces = "Dizzying defense deed", feature = "deeds", power = "dizzying defense", by = ["swaying-charm-deed"] },
  { alters = "Derring-do", feature = "deeds", power = "derring-do", by = ["bold-thief"] },
  { alters = "Swashbuckler's edge deeds", feature = "deeds", power = "swashbuckler's edge", by = ["bold-thief"] },
  { alters = "Panache", feature = "panache", by = ["thief-s-confidence"] },
  { alters = "Class skills", by = ["bold-thief"] },
]
+++

The dashing thief relies on swift swordplay, dazzling charm, and spirited courage to commit
audacious acts of thievery. Another thief might break into a noble's house by night, leaving none
the wiser, but the dashing thief swings in through a window, charms the noble's servant into handing
over the jewelry, and then duels her way out. [Council of Thieves](ref/rule/aff-thieves) heists
often involve at least one dashing thief, as their attention-grabbing antics can provide a
distraction for subtler agents, and their combat skills can be vital in tight spots. The majority of
the Council's dashing thieves are personally trained by Sabriune Misraria—between her renounced
family's lust-fueled intrigues and their numerous enslaved succubi, the drow heretic has numerous
sources for the tricks and stunts she teaches her agents.

## Bold Thief (Ex) {#bold-thief}

A dashing thief fulfills the Council's larcenous goals with style. Her
[derring-do](ref/swashdeed/derring-do) and [swashbuckler's edge](ref/swashdeed/swashbucklers-edge)
deeds apply to Disable Device and Sleight of Hand, but not to Fly and Ride. She adds Disable Device
to her list of class skills, but does not have Fly or Ride as class skills.

This ability alters the swashbuckler's class skills and the derring-do and swashbuckler's edge
deeds.

## Thief 's Confidence (Ex) {#thief-s-confidence}

A dashing thief's panache is fueled by bold acts of thievery. Whenever a dashing thief uses the
[steal](ref/rule/steal) combat maneuver to steal an object worth at least 100 gp × her class level
from an opponent, she regains 1 panache point. She cannot regain panache in this way from a given
opponent more than once per day.

This ability alters panache and replaces the swashbuckler's ability to regain panache from a killing
blow.

## Rogue Talents {#rogue-talents}

Council training grants a dashing thief numerous opportunities to learn trade secrets from fellow
scoundrels. At 4th level and every 4 levels thereafter, a dashing thief gains a rogue talent,
treating her class level as her rogue level when determining the talents' benefits. Starting at 12th
level, the dashing thief can choose advanced rogue talents.

This ability replaces the swashbuckler's bonus feats.

## Dazing Charm Deed (Ex) {#dazing-charm-deed}

A dashing thief takes foes aback with her forwardness, shocking them into submission long enough to
rush past or stage a getaway. At 3rd level, as a free action when she successfully feints against a
foe, she can spend 1 panache point to pull the enemy into a quick kiss (or similar gesture). The
target is [dazed](ref/misc/dazed) for 1 round unless it succeeds at a Will save (DC = 10 + half the
dashing thief's class level + her Charisma modifier). A creature dazed this way is immune to that
dashing thief's dazing charm deed for 24 hours. Whether or not a creature could potentially be
affected by a dazing charm deed is ultimately subject to GM adjudication. As a general rule,
however, it works on creatures of the dashing thief's creature type, or on those of a different type
but who share significant thematic similarities (for example, a human dashing thief could use her
dazing charm deed on any humanoid, but also potentially on creatures as diverse as dryads,
tieflings, or even centaurs or sphinxes).

This ability replaces the menacing swordplay deed.

## Swaying Charm Deed (Su) {#swaying-charm-deed}

A dashing thief eventually becomes truly irresistible. At 15th level, when a dashing thief
successfully dazes a creature using her dazing charm deed, she can instead charm the target for 1
day (as per _[charm monster](ref/spell/charm-monster)_). Only one creature can be charmed this way
at a time; if the dashing thief charms another creature this way, the first charm effect immediately
ends.

This ability replaces the dizzying defense deed.
