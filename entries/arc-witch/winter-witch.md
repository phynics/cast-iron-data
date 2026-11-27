+++
id = "ref/arc-witch/winter-witch"
kind = "archetype"
title = "Winter Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Winter%20Witch"
source_ids = ["reign-of-winter-players-guide", "inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "winter_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "reign-of-winter-players-guide"
page = "11"
[[sources]]
publication = "inner-sea-magic"
page = "43"

[fields]
kind = "archetype"
features = [
  { anchor = "familiar" },
  { anchor = "cantrips" },
  { anchor = "patron" },
  { anchor = "ice-magic" },
  { anchor = "cold-flesh", level = 1 },
  { anchor = "frostfoot" },
  { anchor = "frozen-caress" },
]
trades = [
  { replaces = "4th-level hex", feature = "hex", levels = [4], by = ["cold-flesh"] },
]
+++

The descendents of Baba Yaga rule the frozen realm of Irrisen, and possess a unique power stemming
from their otherworldly origin and their ties to cold magic. This power is partly magical, partly
political, and partly cultural. Known as winter witches, these scions of Baba Yaga have not bothered
to hide their secrets from outsiders, for they understand that those who see winter witches not
native to Irrisen working their frozen magic will simply assume the witches are agents of Irrisen.
By opening up their traditions to those who have no direct blood connection to Baba Yaga or the
ruling families of Irrisen, they spread the notoriety and infamy of their wintry magic far beyond
what they could accomplish on their own. While winter witches are most commonly encountered in
Irrisen, they could be encountered in any part of the Inner Sea region, where they work to increase
Irrisen's notoriety with each frozen spell and manipulative hex they cast. A winter witch has the
following class features.

## Familiar {#familiar}

Winter witches must choose a [familiar](ref/ability/familiars) that is native to the frozen north,
even if they themselves operate in other regions. Traditionally, this limits winter witch familiar
choices to bat, cat, fox, hawk, owl, rat, raven, or weasel. A winter witch who gains the
[Improved Familiar](ref/feat/improved-familiar) feat can select any familiar she desires, save for
familiars with the fire subtype.

## Cantrips {#cantrips}

A winter witch adds _[ray of frost](ref/spell/ray-of-frost)_ to her spell list, but does not
automatically learn this cantrip.

## Patron {#patron}

A winter witch must choose her patron from one of the following patron themes:
[ancestors](ref/patron/ancestors)\*, [deception](ref/patron/deception),
[enchantment](ref/patron/enchantment)\*, [endurance](ref/patron/endurance),
[moon](ref/patron/moon)\*, [occult](ref/patron/occult)\*, [portents](ref/patron/portents)\*,
[stars](ref/patron/stars)\*, [transformation](ref/patron/transformation),
[trickery](ref/patron/trickery), [vengeance](ref/patron/vengeance)\*, [water](ref/patron/water),
[winter](ref/patron/winter)\*, or [wisdom](ref/patron/wisdom). An asterisk (\*) indicates that the
patron theme is detailed in _Ultimate Magic_.

## Ice Magic {#ice-magic}

When a winter witch casts a spell with the cold descriptor, the save DC of the spell increases by 1.
A winter witch cannot learn or cast spells with the fire descriptor at all.

## Cold Flesh (Ex) {#cold-flesh}

At 1st level, a winter witch gains _[endure elements](ref/spell/endure-elements)_ as a constant
[spell-like ability](ref/umr/spell-like-abilities), but only against cold temperatures. At 4th
level, she gains cold resistance 5, making her comfortable in near-freezing temperatures. At
9th-level, this increases to cold resistance 10, and at 14th level, it becomes immunity to cold.
This replaces the witch's 4th-level hex.

## Hexes {#hexes}

The following hexes complement the winter witch archetype: beast eye\*, blight, cook people\*, evil
eye, feral speech\*, hag's eye, hoarfrost\*, ice tomb\*, witch's hut.\* An asterisk (\*) indicates
that the hex is detailed in _Ultimate Magic_.

A winter witch can select the following hexes:

## Frostfoot (Su) {#frostfoot}

This ability works like the _[spider climb](ref/spell/spider-climb)_ spell, but the surfaces the
witch climbs must be icy. The witch can move across icy surfaces without penalty and does not need
to make [Acrobatics](ref/skill/acrobatics) checks to run or charge on ice. She can move across
regular [snow](ref/rule/rain-snow-sleet-and-hail) without penalty, and heavy snow costs her only 2
squares of movement instead of 4.

## Frozen Caress (Su) {#frozen-caress}

Whenever the winter witch casts a touch spell, she can infuse the magic with
[cold](ref/spelldef/cold) as a swift action. This grants the spell the cold descriptor, and adds 1d4
points of cold damage to the spell's effect. If the touch spell allows a saving throw, a successful
save negates this additional cold damage.
