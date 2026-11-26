+++
id = "ref/arc-cleric/varisian-pilgrim"
kind = "archetype"
title = "Varisian Pilgrim"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Varisian%20Pilgrim"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "varisian_pilgrim", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "inner-sea-magic"
page = "42"

[fields]
kind = "archetype"
features = [
  { anchor = "fortunate-road", level = 1 },
  { anchor = "caravan-bond", level = 1 },
  { anchor = "blessing-of-the-harrow", level = 8 },
]
trades = [
  { replaces = "Domains", feature = "domains", by = ["fortunate-road"] },
  { replaces = "Proficiency with medium armor", feature = "weapon-and-armor-proficiencies", power = "medium armor", by = ["caravan-bond"] },
  { replaces = "shields - she retains proficiency with light armor only", feature = "weapon-and-armor-proficiencies", power = "shields", by = ["caravan-bond"] },
  { replaces = "An 8th-level domain power of the Varisian pilgrim's choice", feature = "domains", levels = [8], power = "domain power", by = ["blessing-of-the-harrow"] },
]
+++

While most clerics are associated with a particular temple, adventuring clerics spend much of their
time away from their favored place of worship, and there are those who worship primarily on the road
and during the journey. These clerics see the act of travel and the arrival at sites sacred to their
religion as valuable, and perhaps more so than time spent sequestered inside a church. Relatively
common in Varisia, these pilgrims love to travel, typically on foot or with caravans. While the
archetype is called the "Varisian pilgrim," this archetype can be selected by any cleric who prefers
to worship while on the move. Whether or not they are Varisian, these clerics learn a little about
fortune-telling and a lot about people.

A Varisian pilgrim has the following class features.

## Fortunate Road {#fortunate-road}

At 1st level, a Varisian pilgrim must select the Chaos, Community, Liberation,
[Luck](ref/domain/luck), [Travel](ref/domain/travel), or [Weather](ref/domain/weather) domain (or
the [Exploration](ref/domain/travel), [Fate](ref/domain/luck), Freedom, [Trade](ref/domain/travel),
or [Seasons](ref/domain/weather) subdomains from the _Advanced Player's Guide_, if available in the
campaign) as one of her domains. If the cleric worships a deity that doesn't normally grant one of
these domains, she gains access to this domain but can only pick this one domain—she effectively
loses the option to pick a second domain. As a result, very few clerics who worship deities who
don't grant access to one of the domains or subdomains listed above opt to become Varisian pilgrims.
In all other respects, this works like and replaces the standard cleric's domain ability.

## Caravan Bond (Su) {#caravan-bond}

At 1st level, by leading a group prayer for 1 minute, a Varisian pilgrim can select a number of
traveling companions equal to her cleric level + her Wisdom bonus. She may use her domain-granted
powers on any of these traveling companions as if they were her. She can use these abilities on her
traveling companions at a range of up to 30 feet, even if the ability normally requires her touch.
This ability replaces the cleric's proficiency with medium armor and shields—she retains proficiency
with light armor only.

## Blessing of the Harrow (Su) {#blessing-of-the-harrow}

At 8th level, once per day the pilgrim may perform a harrowing for herself or another creature. This
is otherwise identical to the blessing of the harrow from the
[harrower prestige class](ref/pclass/harrower). This replaces an 8th-level domain power of the
Varisian pilgrim's choice.
