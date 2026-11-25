+++
id = "ref/arc-witch/season-witch"
kind = "archetype"
title = "Season Witch"
aon = "ArchetypeDisplay.aspx?FixedName=Witch%20Season%20Witch"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "season_witch", path = "json/archetypes_witch.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/witch" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "90"

[fields]
kind = "archetype"
features = [
  { anchor = "season-of-the-witch" },
]
trades = [
  { alters = "Patron", feature = "patron-spells", power = "patron", by = ["season-of-the-witch"] },
  { alters = "Hex gained at 1st level", feature = "hex", levels = [1], by = ["season-of-the-witch"] },
]
+++

Season witches gain their power from the cyclical and mystical exchange of energy passed from one
season of nature to another. Often, season witches carry bitter grudges against their fellow
witches, with many believing that the season prior to their chosen focus is inferior and the season
that replaces their favored time is an usurper of time, but at other times season witches work
together, understanding that all are a part of the cycle of the natural world.

## Season of the Witch (Su) {#season-of-the-witch}

A season witch observes the cycles of life through symbolic festivals and the very real passage of
time. Their covens celebrate the seasons and their impact on magic. These seasonal cycles alter
their magic and mind-set, focusing their spells and hexes on a predominant energy type and
philosophy.

A season witch makes a commitment to embody the sacred symbolism of a season year round, and learns
her spells through communion with nature, divining secrets from shapes in the clouds or the play of
leaves on the wind. At 1st level, a season witch chooses the season that defines her abilities as
her patron; this choice also provides her certain benefits.

A spring witch has dominion over the renewing spirit of life and youth. The save DCs of her spells
that deal electricity damage increase by 1. At 1st level, she gains either the
[charm](ref/hex/charm) hex or [disguise](ref/hex/disguise) hex as a bonus hex.

A summer witch has dominion over growth, the harvest, and toil. The save DCs of her spells that deal
fire damage increase by 1. At 1st level, she gains either the [fortune](ref/hex/fortune) hex or
[misfortune](ref/hex/misfortune) hex as a bonus hex.

An autumn witch has dominion over the provision of the land and the passing of life. The save DCs of
her spells that deal acid damage increase by 1. At 1st level, she gains either the
[blight](ref/hex/blight) hex or [slumber](ref/hex/slumber) hex as a bonus hex.

A winter witch has dominion over hearth and home. The save DCs of her spells that deal cold damage
increase by 1. At 1st level, she gains either the [healing](ref/hex/healing) hex or
[ward](ref/hex/ward) hex as a bonus hex.

This alters patron and the hex gained at 1st level.

## Hexes {#hexes}

The following hexes complement the season witch archetype: flight (spring), summer's heat (summer),
poison steep (autumn), no place like home (winter).

## Major Hexes {#major-hexes}

The following major hexes complement the season witch archetype: speak in dreams (spring), agony
(summer), hoarfrost (autumn), major healing (winter).

## Grand Hexes {#grand-hexes}

The following grand hexes complement the season witch archetype: forced reincarnation (spring),
natural disaster (summer), death curse (autumn), life giver (winter).
