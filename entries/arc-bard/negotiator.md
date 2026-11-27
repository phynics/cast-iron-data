+++
id = "ref/arc-bard/negotiator"
kind = "archetype"
title = "Negotiator"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Negotiator"
source_ids = ["champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "negotiator", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "champions-of-balance"
page = "18"

[fields]
kind = "archetype"
features = [
  { anchor = "hard-bargainer", level = 1 },
  { anchor = "counterargument" },
  { anchor = "fast-talk", level = 1 },
  { anchor = "binding-contract", level = 9 },
  { anchor = "rogue-talents", level = 2 },
  { anchor = "master-of-rhetoric", level = 5 },
  { anchor = "advanced-talents", level = 10 },
]
trades = [
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["hard-bargainer"] },
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["fast-talk"] },
  { replaces = "Inspire greatness", feature = "bardic-performance", power = "inspire greatness", by = ["binding-contract"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["rogue-talents"] },
  { replaces = "Lore master", feature = "lore-master", by = ["master-of-rhetoric"] },
]
+++

Bards are experts at manipulating the emotions and perceptions of others. Negotiators are those
bards who take the skills of a performer and apply them to the realms of business and law.

## Hard Bargainer {#hard-bargainer}

A negotiator adds [half](ref/misc/fractions-and-rounding) his class level (minimum 1) on Bluff,
Diplomacy, Intimidate, Knowledge (local), and Sense Motive checks. This ability replaces bardic
knowledge.

## Bardic Performance {#bardic-performance}

A negotiator gains the following types of bardic performance.

## Counterargument (Su) {#counterargument}

This performance acts as [countersong](ref/performance/countersong), except a negotiator can use
only Perform (act, comedy, oratory, or sing) to perform a counterargument.

## Fast Talk (Su) {#fast-talk}

At 1st level, a negotiator can use performance to affect the perceptions of any number of targets
that can hear him. While the negotiator performs, these targets take a -1 penalty on saving throws
against enchantment (charm) and illusion (figment, glamer, or shadow) effects, as well as a penalty
on Appraise checks equal to half the negotiator's level (minimum -1). A target that fails its
Appraise check believes that the object in question is worth 10% more or less (negotiator's choice)
than its actual value. At 5th, 11th, and 17th levels, the saving throw penalty increases by 1 and
the shift in an object's perceived value increases by 10%. Fast talk is a language-dependent,
mind-affecting ability that uses audible components. This performance replaces inspire courage.

## Binding Contract (Sp) {#binding-contract}

At 9th level, the negotiator can bind another creature's promise to the negotiator with a geas. This
acts as _[lesser geas](ref/spell/geas-lesser)_, except the creature must have Hit Dice equal to or
less than the negotiator's level. The target can negate this effect with a successful Will save (DC
= 10 + 1/2 the negotiator's level + the negotiator's Charisma modifier). The geas is discharged if
the negotiator breaks his end of the bargain. Using this ability requires 3 rounds of continuous
performance, and the target must be able to see and hear the bard throughout the performance. At
18th level, this effect acts as _[geas/quest](ref/spell/geas-quest)_ (no HD limit, and the target
cannot attempt a saving throw). Binding contract is an enchantment (compulsion), mind-affecting,
language-dependent ability that relies on audible components. This performance replaces inspire
greatness.

## Rogue Talents {#rogue-talents}

At 2nd level, a negotiator gains a rogue talent, as the rogue class feature of the same name. At 6th
level and every 4 levels thereafter, the negotiator gains an additional rogue talent. A negotiator
cannot select a rogue talent that modifies the sneak attack ability. This ability replaces versatile
performance.

## Master of Rhetoric (Ex) {#master-of-rhetoric}

At 5th level, the negotiator can take 10 on any Bluff, Diplomacy, Intimidate, Knowledge (local), or
Sense Motive check if he has ranks in that skill. A negotiator can choose not to take 10 and can
instead roll normally. In addition, the negotiator can take 20 on one of those skill checks (without
spending any additional time). The negotiator can do this once per day at 5th level, twice per day
at 11th level, and three times per day at 17th level. This ability replaces lore master.

## Advanced Talents {#advanced-talents}

At 10th level and every 4 levels thereafter, a negotiator can select an advanced rogue talent in
place of a rogue talent. A negotiator cannot select an advanced talent that modifies the sneak
attack ability.
