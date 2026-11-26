+++
id = "ref/arc-cavalier/constable"
kind = "archetype"
title = "Constable"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Constable"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "constable", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "17"

[fields]
kind = "archetype"
features = [
  { anchor = "apprehend", level = 1 },
  { anchor = "squad-commander", level = 3 },
  { anchor = "quick-interrogator", level = 4 },
  { anchor = "badge", level = 5 },
  { anchor = "instant-order", level = 11 },
  { anchor = "greater-badge", level = 14 },
]
trades = [
  { replaces = "Mount", feature = "mount", by = ["apprehend"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["squad-commander"] },
  { replaces = "Expert trainer", feature = "expert-trainer", by = ["quick-interrogator"] },
  { replaces = "Banner", feature = "banner", by = ["badge"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["instant-order"] },
  { replaces = "supreme charge", feature = "supreme-charge", by = ["instant-order"] },
  { replaces = "Greater banner", feature = "greater-banner", by = ["greater-badge"] },
  { alters = "Class skills" },
]
+++

Constables keep order in the narrow streets and dark alleys of settlements.

## Class Skills {#class-skills}

Perception is a class skill for constables. This alters the cavalier's class skills.

## Apprehend (Ex) {#apprehend}

A constable gains [Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus feat and
can attempt a [grapple](ref/rule/grapple) combat maneuver check in place of the attack at the end of
a [charge](ref/rule/charge). At 2nd level, the constable receives a +1 bonus on Perception checks
and combat maneuver checks to [disarm](ref/rule/disarm), grapple, or [trip](ref/rule/trip)
opponents. At 7th level and every 5 levels thereafter, this bonus improves by 1. At 4th level, the
constable does not treat [crowds](ref/rule/city-streets) as difficult terrain. This ability replaces
mount.

## Squad Commander (Ex) {#squad-commander}

At 3rd level, a constable can spend 1 minute laying out a plan to activate the tactician ability
without having it count against his number of uses per day. The ability must be triggered within 1
hour of the plan being made, and the benefits last for 1 minute per cavalier level he has. The
constable can have only one plan at a time, and if a new plan is made, any old plan is lost. This
ability replaces cavalier's charge.

## Quick Interrogator (Ex) {#quick-interrogator}

At 4th level, a constable can attempt a [Diplomacy](ref/skill/diplomacy) check to gather information
in 1d6 × 5 minutes and attempt a Diplomacy or [Intimidate](ref/skill/intimidate) check to change
someone's attitude in 5 rounds. This ability replaces expert trainer.

## Badge (Ex) {#badge}

At 5th level, a constable's badge becomes a powerful symbol of rules and authority. As long as he
wears his badge, allies within 30 feet who can see him gain a +2 morale bonus on saving throws
against charm, compulsion, and fear effects and a +1 morale bonus on attack rolls against targets
the constable has challenged. At 10th level and every 5 levels thereafter, the bonuses increase
by 1. This ability replaces banner.

## Instant Order (Ex) {#instant-order}

At 11th level, a constable can bark an order to an ally within 30 feet as a standard action. That
ally can instantly take a single move or standard action to comply with the order. Taking the action
[dazes](ref/misc/dazed) the ally for 1 round afterward. At 20th level, the constable can use this
ability as a move action, but no more than once per round. This ability replaces mighty charge and
supreme charge.

## Greater Badge (Ex) {#greater-badge}

At 14th level, a constable can hold his badge aloft as a standard action to inspire his allies to be
steadfast. All allies within 30 feet gain a number of
[temporary hit points](ref/rule/temporary-hit-points) equal to twice the constable's cavalier level
for 10 minutes. A given ally can benefit from this ability only once per day. This ability replaces
greater banner.
