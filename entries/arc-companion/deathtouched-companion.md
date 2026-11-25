+++
id = "ref/arc-companion/deathtouched-companion"
kind = "archetype"
title = "Deathtouched Companion"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deathtouched_companion", path = "json/archetypes_COMPANION.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "187"

[fields]
kind = "archetype"
features = [
  { anchor = "not-quite-animal" },
  { anchor = "dead-sight" },
  { anchor = "negative-energy-affinity" },
  { anchor = "one-foot-in-the-grave", level = 6 },
]
trades = [
  { replaces = "Share Spells", by = ["dead-sight"] },
  { replaces = "Devotion", by = ["one-foot-in-the-grave"] },
]
+++

Whether the result of a partially successful attempt at revival, a strange blight, or repeated
exposure to undead, deathtouched companions are living animals with a trace of the undead, somewhat
like [dhampirs](ref/race/dhampir).

## Deathtouched Skills {#deathtouched-skills}

Deathtouched companions treat Intimidate as a class skill.

## Not Quite Animal {#not-quite-animal}

The DC to use Handle Animal on a deathtouched companion is 5 higher, as if it were a nonanimal with
an Intelligence score of 1 or 2. It doesn't count as an animal for the purpose of an undead's
unnatural aura.

## Dead Sight (Ex) {#dead-sight}

A deathtouched companion gains [darkvision](ref/rule/darkvision) to a range of 60 feet.

This replaces share spells.

## Negative Energy Affinity (Ex) {#negative-energy-affinity}

Though a living creature, a deathtouched companion reacts to positive and negative energy as if it
were undead—positive energy harms it, while negative energy heals it.

## One Foot in the Grave (Ex) {#one-foot-in-the-grave}

At 6th level, a deathtouched companion gains a +4 morale bonus on Fortitude saves against effects
that could not normally affect objects or undead, and it takes only
[half](ref/misc/fractions-and-rounding) damage from bleed effects. However, it can be affected by
attacks that specifically target undead, such as _[halt undead](ref/spell/halt-undead)_.

This replaces devotion.
