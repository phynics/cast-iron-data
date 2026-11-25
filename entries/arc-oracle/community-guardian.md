+++
id = "ref/arc-oracle/community-guardian"
kind = "archetype"
title = "Community Guardian"
aon = "ArchetypeDisplay.aspx?FixedName=Oracle%20Community%20Guardian"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "community_guardian", path = "json/archetypes_oracle.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/oracle" },
]
[[sources]]
publication = "advanced-race-guide"
page = "63"

[fields]
kind = "archetype"
features = [
  { anchor = "spirit-of-community" },
  { anchor = "renewing-radiance" },
]
trades = [
  { replaces = "Additional class skills from her mystery", feature = "mystery", power = "class skills" },
  { replaces = "Mystery bonus spells from these levels", feature = "mystery", levels = [2, 4, 6, 10, 12], power = "bonus spells" },
]
+++

The community guardian is chosen to protect and succor the weak and innocent within her community.
Her calling also allows her to draw upon and focus the collective will in order to achieve those
goals. A community guardian has the following class features.

## Alignment {#alignment}

Any good.

## Recommended Mysteries {#recommended-mysteries}

ancestor, life, lore, nature.

## Class Skills {#class-skills}

A community guardian adds Knowledge (local), Linguistics, Perception, and Survival to her list of
class skills. These replace the additional class skills from her mystery.

## Bonus Spells {#bonus-spells}

_bless water_ (2nd), _consecrate_ (4th), _remove disease_ (6th), _hallow_ (10th), _heroes' feast_
(12th). These bonus spells replace the oracle's mystery bonus spells from these levels.

## Revelations {#revelations}

A community guardian must take the following revelations at the listed levels.

## Spirit of Community (Ex) {#spirit-of-community}

As a move action, you call upon the spirits of community. For the next round, you grant every ally
within 30 feet a +1 competence bonus on a single skill check (of the ally's choice) that it makes
before the end of this revelation's duration. Furthermore, allies within 30 feet can, as a free
action, choose to forgo this bonus, and instead grant a single ally a +1 increase to its competence
bonus granted by this ability (maximum +5). You can use this ability a number of times per day equal
to 3 + your Charisma modifier. You must take this revelation at 1st level.

## Renewing Radiance (Su) {#renewing-radiance}

Once per day you can produce a [burst](ref/misc/burst) of swirling white light that provides a
measure of protection and renewal to allies within 30 feet for 1 round. On their turn, the allies
can choose either to gain a +1 sacred bonus to AC for 1 round or to heal a number of hit points
equal to 1d6 + your Charisma bonus (their choice). If an ally is [dying](ref/misc/dying), it is
[stabilized](ref/misc/stable) instead. At 7th level, the bonus to AC increases to +2, and the
healing increases to 2d6 + your Charisma bonus hit points, and at 14th level the bonus to AC
increases to +3, and the healing increases to 3d6 + your Charisma bonus hit points. You must take
this revelation at 3rd level.
