+++
id = "ref/arc-alchemist/oenopion-researcher"
kind = "archetype"
title = "Oenopion Researcher"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Oenopion%20Researcher"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "oenopion_researcher", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "inner-sea-magic"
page = "37"

[fields]
kind = "archetype"
features = [
  { anchor = "experimental-mutagen", level = 2 },
  { anchor = "acid-resistance", level = 3 },
]
trades = [
  { replaces = "Poison use", feature = "poison-use", by = ["experimental-mutagen"] },
  { replaces = "Swift alchemy", feature = "swift-alchemy", by = ["acid-resistance"] },
]
+++

Nex is known for its advanced magical lore, and the alchemists of Oenopion are incredibly skilled at
making potions, elixirs, and other materials crucial to the country's economy and its
monster-creating fleshforges. A Oenopion researcher has the following class features.

## Discoveries {#discoveries}

The following discoveries complement the Oenopion researcher archetype:
[acid bomb](ref/discovery/acid-bomb), [bottled ooze](ref/discovery/bottled-ooze)\*,
[feral mutagen](ref/discovery/feral-mutagen), [infuse mutagen](ref/discovery/infuse-mutagen),
[infusion](ref/discovery/infusion), [sunlight bomb](ref/discovery/sunlight-bomb)\*. An asterisk (\*)
indicates a discovery detailed in _Ultimate Magic_.

## Experimental Mutagen (Su) {#experimental-mutagen}

At 2nd level, an Oenopion researcher learns how to create an experimental mutagen that benefits
others, though not as well as his normal mutagen. The experimental mutagen works just like a
standard mutagen, except the natural armor bonus and the alchemical bonus to the ability score are
[half](ref/misc/fractions-and-rounding) normal (+1 natural armor bonus and +2 to one ability score).
The experimental mutagen has no risk of nauseating a creature who drinks it. The researcher decides
when he creates the mutagen if it is a standard mutagen (which gives no benefit if another creature
drinks it) or an experimental mutagen (which does); there is no difference in the cost, time to
create, or any other aspect of the mutagen. If the researcher has discoveries or other abilities
that alter or increase the benefits of the mutagen, these apply to the experimental mutagen (though
the drinker only gets half the numerical bonus of the mutagen). This ability replaces poison use.

## Acid Resistance (Ex) {#acid-resistance}

At 3rd level, an Oenopion researcher gains acid resistance 5. This ability replaces swift alchemy.
