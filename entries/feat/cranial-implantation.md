+++
id = "ref/feat/cranial-implantation"
kind = "feat"
title = "Cranial Implantation"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cranial_implantation", path = "json/feat03.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/self-sufficient", label = "or" },
  { kind = "prerequisite", target = "ref/feat/trepanation", label = "or" },
]
[[sources]]
publication = "occult-origins"
page = "24"

[fields]
kind = "feat"
prerequisites = "Self-Sufficient or Trepanation, Heal 7 ranks."
prerequisite_feats = ["ref/feat/self-sufficient", "ref/feat/trepanation"]
benefit = "You can perform the phrenology occult skill unlock, though you must use needles or similar sharp implements rather than your fingertips, dealing 1d3 points of damage to the subject. If you can cast psychic spells or have the Psychic Sensitivity feat, you can use phrenology one additional time per day."
+++

You turn the science of phrenology inward, driving needles and nails into your or another's brain to
grant focus through the pathways of pain.\
**Prerequisites:** [Self-Sufficient](ref/feat/self-sufficient) or
[Trepanation](ref/feat/trepanation), Heal 7 ranks.\
**Benefit:** You can perform the [phrenology](ref/skill/knowledge-arcana) occult skill unlock,
though you must use needles or similar sharp implements rather than your fingertips, dealing 1d3
points of damage to the subject. If you can cast psychic spells or have the
[Psychic Sensitivity](ref/feat/psychic-sensitivity) feat, you can use phrenology one additional time
per day.

In addition, you can insert needles into a creature's brain to help center its thoughts and
emotions. Doing so requires a successful Heal check (DC = 25 + the target's Hit Dice). Creatures
with implanted needles gain a +1 bonus on saving throws against spells with the emotion or fear
descriptor (or similar effects), but take a -1 penalty on saving throws against spells with the
electricity or pain descriptors. Implanting needles deals 1d6 points of damage to the patient, which
can't be healed by any means until the needles are removed (which requires a second successful Heal
check at the same DC, or a [restoration](ref/spell/restoration) or
[regenerate](ref/spell/regenerate) spell).

If you have implanted needles into your own cranium, you can probe them as a swift action while
casting a spell, dealing an amount of damage to yourself equal to 1 + the spell's level. The pain
from this probing stimulates your powers of focus, granting you a bonus of +1d6 on any
[concentration](ref/rule/concentration) check you must attempt as part of casting that spell. This
damage doesn't force you to attempt a concentration check.
