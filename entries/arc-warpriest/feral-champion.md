+++
id = "ref/arc-warpriest/feral-champion"
kind = "archetype"
title = "Feral Champion"
aon = "ArchetypeDisplay.aspx?FixedName=Warpriest%20Feral%20Champion"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feral_champion", path = "json/archetypes_warpriest.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/warpriest" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "97"

[fields]
kind = "archetype"
features = [
  { anchor = "feral-blessing" },
  { anchor = "sacred-claws" },
  { anchor = "wild-shape", level = 7 },
]
trades = [
  { replaces = "Sacred armor", feature = "sacred-armor", by = ["wild-shape"] },
  { alters = "Blessings", feature = "blessings", by = ["feral-blessing"] },
  { alters = "Sacred weapon", feature = "sacred-weapon", by = ["sacred-claws"] },
]
+++

When a warpriest devotes himself to a god of the natural world, he is sometimes blessed with
supernatural powers that allow him to evoke animalistic power and fury.

## Feral Blessing {#feral-blessing}

A feral champion must take the [Animal](ref/blessing/animal) blessing and does not gain a second
blessing.

This alters blessings.

## Sacred Claws (Su) {#sacred-claws}

Rather than empowering a physical weapon, a feral champion grows claws as primary
[natural weapons](ref/umr/natural-attacks) on each hand. These claws deal damage as a warpriest's
sacred weapon and can be enhanced as such.

This alters sacred weapon.

## Wild Shape (Su) {#wild-shape}

At 7th level, a feral champion gains wild shape, as the [druid](ref/class/druid) ability of the same
name, and treats his warpriest level - 3 as his effective druid level for the purposes of this
ability. However, a feral champion does not gain the ability to take on elemental or plant forms
with wild shape. A feral champion can use wild shape once per day at 7th level and one additional
time per day every 4 levels thereafter, for a total of four times per day at 19th level.

This replaces sacred armor.
