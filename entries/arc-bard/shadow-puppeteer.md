+++
id = "ref/arc-bard/shadow-puppeteer"
kind = "archetype"
title = "Shadow Puppeteer"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Shadow%20Puppeteer"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_puppeteer", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-race-guide"
page = "210"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance" },
  { anchor = "shadow-servant", level = 1 },
  { anchor = "shadow-puppets", level = 1 },
]
trades = [
  { replaces = "All levels of inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["bardic-performance"] },
  { replaces = "inspire competence", feature = "bardic-performance", power = "inspire competence", by = ["bardic-performance"] },
]
+++

A shadow puppeteer invokes amazing and terrifying shadow puppet shows, producing supernatural
effects by creating and manipulating shadow. A shadow puppeteer has the following class feature.

## Bardic Performance {#bardic-performance}

A shadow puppeteer gains the following types of bardic performance. The character must be able to
perform shadow puppetry in order to activate any of these abilities. Shadow puppetry uses Perform
(act), and requires a light source. These abilities replace all levels of inspire courage and
inspire competence.

## Shadow Servant (Sp) {#shadow-servant}

At 1st level, the puppeteer can create a _shadow servant_ to perform simple tasks. The shadow
servant is identical to an _[unseen servant](ref/spell/unseen-servant)_ (caster level equal to the
shadow puppeteer's bard level), except it appears as a formless shadow. Shadow servant relies on
visual components.

## Shadow Puppets (Sp) {#shadow-puppets}

At 1st level, a shadow puppeteer can use bardic performance to create one quasi-real shadowy
creature resembling a monster from the _[summon monster I](ref/spell/summon-monster-1)_ list. These
shadowy creatures otherwise work like _[shadow conjuration](ref/spell/shadow-conjuration)_, and
targets interacting with them get a Will saving throw (DC 10 + 1/2 your bard level + your Charisma
bonus) to treat them as only 20% real. At 4th level and every three levels thereafter, this ability
acts like the next higher version of _summon monster_ (_summon monster II_ at 4th level and so on).
