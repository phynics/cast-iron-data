+++
id = "ref/arc-wizard/primalist"
kind = "archetype"
title = "Primalist"
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
replaces = ["Arcane bond", "5th-level bonus feat", "10th-level bonus feat"]
+++

A primalist is a wizard who has spent a considerable amount of time studying the chaos that is
[primal magic](ref/rule/primal-magic) - she seeks order in chaos, and hopes to master the raw power
of primal magic to bolster her own abilities. A primalist wizard has the following class features.

**Primal Magic (Su)**

**Gained:** At 1st Level

**Replaces:** Arcane bond

**Swift:** A primalist may attempt to channel primal magic to cast a prepared spell without losing
that spell from its spell slot. Essentially, a primalist is forcing primal magic into the world and
attempting to shape it into a specific spell effect.

To use this ability, she casts the spell as she would normally, but as the spell's effects take
place, she makes a [concentration](ref/rule/concentration) check (DC 20 + double the spell's level).
If she fails this check, she expends the spell normally as if she had cast it, but its actual
effects are replaced by a _primal magic event_ with a CR equal to her caster level and she is
[staggered](ref/misc/staggered) for 1 round per level of the spell she was attempting to cast. If
she makes this check, she casts the spell normally and it is not expended from her prepared spell
slot, allowing her to cast that spell again at a later point.

**Usage:** 1 time/day + 1 per 5 wizard levels

**Enhance Primal Magic Event (Su)**

**Gained:** At 5th Level

**Replaces:** 5th-level bonus feat

**Special:** She can choose to use this ability after she determines what _primal magic event_ she
triggers, but before she resolves the effects of that _event._

**Swift:** When a primalist triggers a _primal magic event,_ she can increase or decrease its CR
by 1. If she makes a concentration check (DC = 15 + the _primal magic event's_ CR), she can instead
increase or decrease the CR by 2. If she reduces a _primal magic event's_ CR to less than 1, the
_event_ is negated.

**Primal Surge (Su)**

**Ability:** Whenever a primalist triggers a _primal magic event,_ she rolls the percentile dice
twice to determine the _event_ that occurs and chooses which one of the two possible events occurs.

**Gained:** At 10th Level

**Passive:** She becomes resistant to the effects of _primal magic events._ Anytime an _event_ would
affect her, the GM rolls 1d20 + the _event's_ CR against a DC of 11 + her wizard level. If this roll
fails, the _event_ does not affect her, similar to a creature with
[spell resistance](ref/rule/spell-resistance) ignoring magical effects with an SR check. If the
_primal magic event_ is duplicating the effects of a spell that does not allow spell resistance
(such as [create pit](ref/spell/create-pit)), this resistance does not apply.

**Replaces:** 10th-level bonus feat
