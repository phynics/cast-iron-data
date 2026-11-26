+++
id = "ref/arc-alchemist/blightseeker"
kind = "archetype"
title = "Blightseeker"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Blightseeker"
source_ids = ["heroes-of-the-darklands"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blightseeker", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "heroes-of-the-darklands"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "spore-bomb", level = 1 },
  { anchor = "blights", level = 1 },
  { anchor = "blight-engineering", level = 14 },
]
trades = [
  { replaces = "Discoveries gained at 6th, 12th, and 18th levels", feature = "discovery", levels = [6, 12, 18], by = ["blights"] },
  { replaces = "Persistent mutagen", feature = "persistent-mutagen", by = ["blight-engineering"] },
  { alters = "Bombs", feature = "bomb", by = ["spore-bomb"] },
]
+++

Blightseekers are alchemists devoted to the study of fungi native to the Darklands. While diverse
fungi exist on the surface world, the unique combination of environmental conditions found in the
Darklands fosters the growth of unpredictable and otherworldly fungal growths.

## Spore Bomb (Su) {#spore-bomb}

At 1st level, a blightseeker creates a special kind of alchemist bomb that delivers a payload of
alchemically engineered fungal spores. These bombs infest their target with a virulent blight (see
below). The blightseeker's bombs deal 1d4 points of damage (instead of 1d6), plus 1d4 points of
damage for every 2 alchemist levels beyond 1st.

A creature that takes a direct hit from a spore bomb must succeed at a Fortitude save (DC = 10 +
[half](ref/misc/fractions-and-rounding) the blightseeker's level + his Intelligence modifier) or
suffer the associated blight effects. Creatures that take splash damage from the bomb are not
affected by the blight.

This ability alters bombs.

## Blights (Ex) {#blights}

At 1st level, a blightseeker gains the blights from the list below. When he prepares bombs at the
start of the day, a blightseeker chooses which blight to apply to each bomb. If a blight has no
duration listed, it lasts a number of rounds equal to the blightseeker's Intelligence modifier.

At 1st level, a blightseeker gains the following blights.

- Impairing: The target's base land speed decreases by 10 feet, to a minimum of 10 feet. This effect
  doesn't stack with itself.

- Minor Sickening: The target is [sickened](ref/misc/sickened), but it takes only a -1 penalty on
  affected rolls.

At 6th level, a blightseeker adds the following blights to the list of those that can be applied to
his bombs.

- Fatiguing: The target is [fatigued](ref/misc/fatigued).

- Fear-Inducing: The target is [shaken](ref/misc/shaken).

- Sickening: The target is sickened.

At 12th level, a blightseeker adds the following blights to the list of those blights that can be
applied to his bombs.

- Confusing: The target is [confused](ref/misc/confused).

- Exhausting: The target is [exhausted](ref/misc/exhausted).

- Nauseating: The target is [nauseated](ref/misc/nauseated) for 1 round.

- Staggering: The target becomes [staggered](ref/misc/staggered) for 1 round.

At 18th level, a blightseeker adds the following blights to the list of those that can be selected.

- Blinding: The target is [blinded](ref/misc/blinded).

- Deafening: The target is [deafened](ref/misc/deafened).

- Stunning: The target is [stunned](ref/misc/stunned) for 1 round.

This ability replaces the discoveries gained at 6th, 12th, and 18th levels.

## Blight Engineering (Ex) {#blight-engineering}

At 14th level, a blightseeker can apply two blights that he knows to each spore bomb he creates.

This ability replaces persistent mutagen.
