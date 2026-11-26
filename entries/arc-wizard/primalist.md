+++
id = "ref/arc-wizard/primalist"
kind = "archetype"
title = "Primalist"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Primalist"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "primalist", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "inner-sea-magic"
page = "37"

[fields]
kind = "archetype"
features = [
  { anchor = "primal-magic", level = 1 },
  { anchor = "enhance-primal-magic-event", level = 5 },
  { anchor = "primal-surge", level = 10 },
]
trades = [
  { replaces = "Arcane bond", feature = "arcane-bond", by = ["primal-magic"] },
  { replaces = "Wizard bonus feat acquired at 5th level", feature = "bonus-feats", levels = [5], by = ["enhance-primal-magic-event"] },
  { replaces = "Wizard bonus feat acquired at 10th level", feature = "bonus-feats", levels = [10], by = ["primal-surge"] },
]
+++

A primalist is a wizard who has spent a considerable amount of time studying the chaos that is
[primal magic](ref/rule/primal-magic)—she seeks order in chaos, and hopes to master the raw power of
primal magic to bolster her own abilities. A primalist wizard has the following class features.

## Primal Magic (Su) {#primal-magic}

At 1st level, a primalist may attempt to channel primal magic as a swift action to cast a prepared
spell without losing that spell from its spell slot. Essentially, a primalist is forcing primal
magic into the world and attempting to shape it into a specific spell effect. To use this ability,
she casts the spell as she would normally, but as the spell's effects take place, she makes a
[concentration](ref/rule/concentration) check (DC 20 + double the spell's level). If she fails this
check, she expends the spell normally as if she had cast it, but its actual effects are replaced by
a primal magic event with a CR equal to her caster level and she is [staggered](ref/misc/staggered)
for 1 round per level of the spell she was attempting to cast. If she makes this check, she casts
the spell normally and it is not expended from her prepared spell slot, allowing her to cast that
spell again at a later point.

You may use primal magic in this manner once per day. This ability replaces arcane bond. At 5th,
10th, 15th, and 20th level, you can use it an additional time per day.

## Enhance Primal Magic Event (Su) {#enhance-primal-magic-event}

At 5th level, when a primalist triggers a primal magic event, as a swift action she can increase or
decrease its CR by 1. If she makes a concentration check (DC = 15 + the primal magic event's CR),
she can instead increase or decrease the CR by 2. If she reduces a primal magic event's CR to less
than 1, the event is negated. She can choose to use this ability after she determines what primal
magic event she triggers, but before she resolves the effects of that event. This ability replaces
the wizard bonus feat acquired at 5th level.

## Primal Surge (Su) {#primal-surge}

At 10th level, whenever a primalist triggers a primal magic event, she rolls the percentile dice
twice to determine the event that occurs and chooses which one of the two possible events occurs.
She becomes resistant to the effects of primal magic events. Anytime an event would affect her, the
GM rolls 1d20 + the event's CR against a DC of 11 + her wizard level. If this roll fails, the event
does not affect her, similar to a creature with [spell resistance](ref/rule/spell-resistance)
ignoring magical effects with an SR check. If the primal magic event is duplicating the effects of a
spell that does not allow spell resistance (such as _[create pit](ref/spell/create-pit)_), this
resistance does not apply. This ability replaces the wizard bonus feat acquired at 10th level.
