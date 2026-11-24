+++
id = "ref/arc-monk/nimble-guardian"
kind = "archetype"
title = "Nimble Guardian"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Nimble%20Guardian"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "nimble_guardian", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-race-guide"
page = "92"

[fields]
kind = "archetype"
features = [
  { anchor = "defensive-aid", level = 2 },
  { anchor = "nimble-reflexes", level = 3 },
  { anchor = "defensive-mastery", level = 5 },
  { anchor = "guardian-feline", level = 7 },
  { anchor = "evasion", level = 9 },
]
trades = [
  { replaces = "Evasion", feature = "evasion", by = ["defensive-aid"] },
  { replaces = "Still mind", feature = "still-mind", by = ["nimble-reflexes"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["defensive-mastery"] },
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["guardian-feline"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["evasion"] },
]
+++

Some catfolk monks dedicate their graceful prowess to the defense of others, especially those
dedicated to a similar ethos or who prove themselves as stalwart allies of the monk's cause. A
nimble guardian has the following class features.

**Prerequisites:** Catfolk

## Defensive Aid (Ex) {#defensive-aid}

At 2nd level, a number of times per day equal to his Wisdom bonus, a nimble guardian can interpose
herself between one adjacent ally and an attack or damage dealt in an area of effect. If an adjacent
ally is the target of the attack or is required to make a Reflex saving throw against a damaging
effect, as an immediate action the nimble guardian can grant that ally a +4 circumstance bonus to AC
or on the saving throw against the effect. The nimble guardian must use this ability before the
attack roll or saving throw is made. The nimble guardian can only use this ability if he is wearing
light or no armor. This ability replaces evasion.

## Nimble Reflexes (Ex) {#nimble-reflexes}

At 3rd level, a nimble guardian gains a +2 bonus on all Reflex saving throws. This ability replaces
still mind.

## Defensive Mastery (Ex) {#defensive-mastery}

At 5th level, a nimble guardian gains 3 additional uses of her defensive aid ability per day.
Furthermore, if an ally that gained the benefit of a use of defensive aid succeeds her Reflex saving
throw, and the effect still deals damage on a successful saving throw, the nimble guardian can spend
1 ki point to negate that damage. Doing so is not an action. This ability replaces purity of body.

## Guardian Feline (Su) {#guardian-feline}

At 7th level, a nimble guardian can transform himself into a feline creature by spending 2 ki
points. The effect lasts for 1 hour or until the nimble guardian changes back. Changing form (to
animal or back) is a standard action and does not provoke an attack of opportunity. The chosen form
must be some form of feline ([cheetah](ref/monster/cat-cheetah), [lion](ref/monster/lion), etc.).
This ability is otherwise identical to _[beast shape II](ref/spell/beast-shape-2)_. At 9th level,
this ability functions as _[beast shape III](ref/spell/beast-shape-3)._ This ability replaces
wholeness of body.

## Evasion (Ex) {#evasion}

At 9th level, a nimble guardian gains [evasion](ref/ability/evasion). This ability replaces improved
evasion.
