+++
id = "ref/arc-inquisitor/sanctified-slayer"
kind = "archetype"
title = "Sanctified Slayer"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Sanctified%20Slayer"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sanctified_slayer", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "advanced-class-guide"
page = "99"

[fields]
kind = "archetype"
features = [
  { anchor = "studied-target", level = 1 },
  { anchor = "sneak-attack", level = 4 },
  { anchor = "talented-slayer" },
]
trades = [
  { replaces = "Judgment 1/day", feature = "judgment", levels = [1], by = ["studied-target"] },
  { replaces = "Later iterations of the judgment ability", by = ["sneak-attack"] },
  { replaces = "Second judgment", feature = "second-judgment", by = ["talented-slayer"] },
  { replaces = "third judgment", feature = "third-judgment", by = ["talented-slayer"] },
  { replaces = "slayer", feature = "slayer", by = ["talented-slayer"] },
  { replaces = "true judgment", feature = "true-judgment", by = ["talented-slayer"] },
]
+++

While all inquisitors root out enemies of the faith, in many orders and churches there's a select
group of these religious hunters devoted to one goal, and one goal alone - to terminate the enemies
of the faith wherever they can be found. Sometimes these sanctified slayers are given special
dispensation to commit ruthless murders for the faith's greater good. Other times, they're simply
willing to take the initiative to revel in the zeal of such grisly work.

## Studied Target (Ex) {#studied-target}

At 1st level, a sanctified slayer gains the [slayer's](ref/class/slayer) studied target class
feature. She uses her inquisitor level as her effective slayer level to determine the effects of
studied target. This ability replaces judgment 1/day.

## Sneak Attack (Ex) {#sneak-attack}

At 4th level, if a sanctified slayer catches an opponent unable to defend itself effectively from
her attack, she can strike a vital spot to deal extra damage. The sanctified slayer's attack deals
additional damage anytime her target would be denied a Dexterity bonus to AC (whether or not the
target actually has a Dexterity bonus), or when the sanctified slayer [flanks](ref/rule/flanking)
her target. This additional damage is 1d6 at 4th level, and increases by 1d6 every 3 levels
thereafter. Should a sanctified slayer score a critical hit with the sneak attack, this extra damage
is not multiplied. Ranged attacks can count as sneak attacks only if the target is within 30 feet.

With a weapon that deals nonlethal damage (such as a sap, whip, or an unarmed strike), a sanctified
slayer can make a sneak attack that deals nonlethal damage instead of lethal damage. She cannot use
a weapon that deals lethal damage to deal nonlethal damage in a sneak attack, even with the usual -4
penalty.

A sanctified slayer must be able to see the target well enough to pick out a vital spot and must be
able to reach such a spot. A sanctified slayer cannot use sneak attack while striking a creature
with [concealment](ref/rule/concealment). This ability replaces the later iterations of the judgment
ability.

## Talented Slayer (Ex) {#talented-slayer}

At 8th, 16th, 17th, and 20th levels, a sanctified slayer can gain a single slayer talent, including
those from the list of rogue talents that a slayer can take, but not an advanced slayer talent. This
ability replaces second judgment, third judgment, slayer, and true judgment.
