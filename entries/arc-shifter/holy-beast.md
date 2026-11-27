+++
id = "ref/arc-shifter/holy-beast"
kind = "archetype"
title = "Holy Beast"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Holy%20Beast"
source_ids = ["heroes-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "holy_beast", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "heroes-of-golarion"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "blessed-claws", level = 1 },
  { anchor = "divine-fury", level = 1 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["divine-fury"] },
  { replaces = "track", feature = "track", by = ["divine-fury"] },
  { replaces = "woodland stride", feature = "woodland-stride", by = ["divine-fury"] },
  { replaces = "trackless step", feature = "trackless-step", by = ["divine-fury"] },
  { alters = "Shifter claws", feature = "shifter-claws", by = ["blessed-claws"] },
]
+++

Thousands of gods are venerated in Vudra, and devoted followers might have personal relationships
with their chosen deities. Holy beast shifters pledge to hunt down their deity's enemies to earn
that deity's blessing. These shifters tend to take on the aspect of their deity's sacred animal, and
many of them seek to destroy [rakshasas](ref/family/rakshasa).

## Beast's Blessing {#beast-s-blessing}

A holy beast must worship a deity.

## Blessed Claws (Su) {#blessed-claws}

This ability functions as the shifter's claws class feature, except the holy beast shifter's default
claws are long and thin, dealing piercing damage. At 3rd level, her claws are treated as one type of
aligned weapon (chaotic, evil, good, or lawful) within one step of her deity's alignment in addition
to ignoring DR/cold iron, DR/magic, and DR/silver. If multiple alignment components are available to
the holy beast, she selects one; this choice cannot be changed later.

This alters shifter claws.

## Divine Fury (Su) {#divine-fury}

A holy beast shifter focuses entirely on hunting down specific outsiders on behalf of her deity. She
gains the ranger's [favored enemy](ref/ability/favored-enemy) class feature, except she can select
only an outsider type from the favored enemy table. The bonus against her favored enemy
automatically increases by 1 at 5th level and every 5 levels thereafter. At 5th level and every 5
levels thereafter, she can forgo gaining an additional shifter aspect to instead gain an additional
outsider type as her favored enemy. Her bonuses from the favored enemy feature against new outsider
types chosen in this way are equal to the bonus for the type chosen at 1st level.

This replaces wild empathy, track, woodland stride, and trackless step.
