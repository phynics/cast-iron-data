+++
id = "ref/arc-skald/sunsinger"
kind = "archetype"
title = "Sunsinger"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Sunsinger"
source_ids = ["qadira-jewel-of-the-east"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sunsinger", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "qadira-jewel-of-the-east"
page = "33"

[fields]
kind = "archetype"
features = [
  { anchor = "pillar-of-light", level = 3 },
  { anchor = "channel-solar-energy", level = 5 },
]
trades = [
  { replaces = "Song of marching", feature = "song-of-marching", by = ["pillar-of-light"] },
  { replaces = "Spell kenning", feature = "spell-kenning", by = ["channel-solar-energy"] },
]
+++

Qadiran sunsingers are particularly religious skalds of [Sarenrae](ref/faith/sarenrae) who call down
their goddess's glory to fill soldiers with fire.

## Alignment {#alignment}

A sunsinger skald must be lawful good, neutral good, or neutral, and must worship Sarenrae.

## Pillar of Light (Su) {#pillar-of-light}

At 3rd level, a sunsinger skald can use her raging song to call upon her goddess to imbue her with
glory and make all who see it pay heed. A great beam of sunlight shines down upon the skald, casting
[bright light](ref/rule/vision-and-light) in a 30-foot radius, and allows the skald's raging song to
function as the [fascinate](ref/performance/fascinate) bardic performance.

This ability replaces song of marching.

## Channel Solar Energy (Su) {#channel-solar-energy}

At 5th level, a sunsinger skald can [channel energy](ref/ability/channel-energy) as a cleric once
per day to heal wounds or harm undead like a good-aligned cleric. When she does so, she fills the
area affected by the channeled energy with light, and can outline creatures in the area of effect as
per _[faerie fire](ref/spell/faerie-fire)_. The sunsinger uses her skald level as her effective
cleric level when channeling positive energy. Undead who are particularly harmed by sunlight take a
-2 penalty on saving throws against this channeled energy, and take 1 additional point of damage per
die of damage dealt by the effect.

At 11th level, a sunsinger can channel energy twice per day. At 17th level, she can use this ability
three times per day.

This ability replaces spell kenning.
