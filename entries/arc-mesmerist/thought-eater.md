+++
id = "ref/arc-mesmerist/thought-eater"
kind = "archetype"
title = "Thought Eater"
aon = "ArchetypeDisplay.aspx?FixedName=Mesmerist%20Thought%20Eater"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thought_eater", path = "json/archetypes_mesmerist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/mesmerist" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "38"

[fields]
kind = "archetype"
features = [
  { anchor = "assume-identity", level = 1 },
  { anchor = "assume-morality", level = 2 },
  { anchor = "assume-knowledge", level = 3 },
  { anchor = "consume-identity", level = 20 },
]
trades = [
  { replaces = "Consummate liar", feature = "consummate-liar", by = ["assume-identity"] },
  { replaces = "Towering ego", feature = "towering-ego", by = ["assume-morality"] },
  { replaces = "Touch treatment", feature = "touch-treatment", by = ["assume-knowledge"] },
  { replaces = "Rule minds", feature = "rule-minds", by = ["consume-identity"] },
]
+++

Mesmerists that learn to pierce deep into the minds of their victims are known as thought eaters,
dangerous individuals capable of devouring thoughts and assuming the knowledge those notions
represent for themselves.

## Assume Identity (Su) {#assume-identity}

When a thought eater targets a creature with his hypnotic stare ability, the thought eater gains a
bonus on Disguise checks to appear as that creature. This bonus is equal to the thought eater's
mesmerist level, and lasts for 24 hours, or until he uses his hypnotic stare ability on a different
creature.

This ability replaces consummate liar.

## Assume Morality (Su) {#assume-morality}

At 2nd level, the thought eater's alignment matches that of the target of his assume identity
ability for the purposes of spells and effects that discern alignment. This includes any increase to
alignment aura strength from class features, such as a cleric's aura ability.

This ability replaces towering ego.

## Assume Knowledge (Su) {#assume-knowledge}

At 3rd level, the thought eater can choose one Knowledge skill possessed by the target of his
hypnotic stare. He uses the target's number of ranks in that skill, instead of his own, to calculate
his bonus (but not for other purposes, such as meeting the prerequisites of feats) to a maximum
number of ranks equal to his mesmerist level. This ability lasts for 24 hours or until he uses his
hypnotic stare ability on a different creature.

This ability replaces touch treatment.

## Consume Identity (Su) {#consume-identity}

At 20th level, when the thought eater kills a target of his hypnotic stare, he can choose to
entirely consume the creature's identity, mind, body, and soul as a free action. The target's corpse
dissolves and as long as the thought eater lives, the target of consume identity cannot be brought
back from the dead until the thought eater releases the identity (a standard action) or uses consume
identity on another target. The creature's soul can also be released by a _[wish](ref/spell/wish)_
or _[miracle](ref/spell/miracle)_ (which ends the effect of consume identity). When the thought
eater has consumed an identity, all divination spells identify him as (and consider him to be) the
creature whose identity he consumed rather than himself. This ability fools any spell short of
_[discern location](ref/spell/discern-location)_. _[Discern location](ref/spell/discern-location)_
pinpoints the thought eater's location, whenever either the thought eater or the consumed creature
is the target of that spell.

This ability replaces rule minds.
