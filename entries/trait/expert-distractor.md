+++
id = "ref/trait/expert-distractor"
kind = "trait"
title = "Expert Distractor"
aon = "TraitDisplay.aspx?ItemName=Expert%20Distractor"
source_ids = ["blood-of-the-elements"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "expert_distractor", path = "json/traits05.json" },
]

[fields]
kind = "trait"
category = "Race"
+++

**Type:** Race

**Prerequisite:** [Ifrit](ref/race/ifrit)

**Benefit:** Whenever you damage an opponent that is casting a spell with a melee attack that deals
fire damage (such as a [flaming](ref/magic-enh/flaming) weapon or a [torch](ref/eq-misc/torch)), the
DC of the [concentration](ref/rule/concentration) check for your opponent to cast the spell is equal
to 10 + the non-fire damage dealt + double the fire damage dealt + the spell's level (instead of
just 10 + the damage dealt + the spell's level).
