+++
id = "ref/arc-medium/rivethun-spirit-channeler"
kind = "archetype"
title = "Rivethun Spirit Channeler"
aon = "ArchetypeDisplay.aspx?FixedName=Medium%20Rivethun%20Spirit%20Channeler"
source_ids = ["haunted-heroes-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rivethun_spirit_channeler", path = "json/archetypes_medium.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/medium" },
]
[[sources]]
publication = "haunted-heroes-handbook"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "mind-and-soul", level = 1 },
  { anchor = "spiritual-invocation", level = 1 },
  { anchor = "spiritual-parley", level = 2 },
  { anchor = "wrangle-condition", level = 3 },
  { anchor = "haunt-channeler", level = 7 },
]
trades = [
  { replaces = "Spirit bonus", feature = "spirit-bonus", by = ["spiritual-invocation"] },
  { replaces = "spirit surge", feature = "spirit-surge", by = ["spiritual-invocation"] },
  { replaces = "Taboo", feature = "taboo", by = ["spiritual-parley"] },
  { replaces = "Connection channel", feature = "connection-channel", by = ["haunt-channeler"] },
  { alters = "Spellcasting", feature = "spells", by = ["mind-and-soul"] },
  { alters = "Spirit", feature = "spirit", by = ["spiritual-invocation"] },
]
+++

[Rivethun](ref/rule/aff-animists) spirit channelers are mediums who practice the ancient dwarven
philosophy of the rivethun, which teaches that power lies in the connection between physical bodies
and immaterial souls. Most rivethun spirit channelers are dwarven adherents of this ancient
philosophy, but mediums of other races are accepted with equal fervor, for the rivethun teachings
state that discord and heterogeneousness are the most surefire way to open one's senses to the
spiritual world. Rivethun spirit channelers act as ambassadors and negotiators between the denizens
of the natural and supernatural worlds.

## Mind and Soul (Ex) {#mind-and-soul}

A rivethun spirit channeler chooses whether she uses her Wisdom or Charisma score to determine the
effects of her medium class abilities (including this archetype's abilities). This includes (but is
not limited to) the minimum ability score needed to learn or cast a medium spell, the save DC of her
medium spells, the number of [bonus spells](ref/rule/determine-bonuses) (if any) she receives for
having a high ability score, the number of times per day she can use her medium abilities, and the
effects of her spirit's abilities. This choice is made at 1st level, and once made, it can't be
changed.

A rivethun spirit channeler knows one fewer spell of each spell level that she can cast than is
indicated on Table 1–3: Medium Spells Known (_Pathfinder RPG Occult Adventures_ 33).

This alters the medium's spellcasting.

## Spiritual Invocation (Su) {#spiritual-invocation}

Rather than channel the legend of a single spirit for 24 hours, a rivethun spirit channeler can
invite a nearby local spirit into her body for 24 hours. This functions exactly like the spirit
dance ability of the [spirit dancer](ref/arc-medium/spirit-dancer) medium archetype, except the
rivethun spirit channeler doesn't need to find an appropriate location to channel her spirits since
she invites nearby spirits into her body instead of channeling a legend.

This alters spirit and replaces spirit bonus and spirit surge.

## Spiritual Parley (Ex) {#spiritual-parley}

At 2nd level, a rivethun spirit channeler adds 1/2 her medium level to Diplomacy checks attempted
against fey, elementals, outsiders (except native outsiders), and undead creatures, as well as on
Diplomacy checks attempted as part of the wrangle condition ability (see below).

This ability replaces taboo.

## Wrangle Condition (Su) {#wrangle-condition}

At 3rd level, a rivethun spirit channeler can interact directly with unwholesome spirits of the ills
that trouble her or her allies. This functions like the [animist shaman's](ref/arc-shaman/animist)
wrangle condition ability (_Pathfinder RPG Advanced Class Guide_ 110).

## Haunt Channeler (Su) {#haunt-channeler}

A rivethun spirit channeler receives this ability at 7th level instead of at 3rd level.

This ability replaces connection channel.
