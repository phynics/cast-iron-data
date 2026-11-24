+++
id = "ref/arc-slayer/cutthroat"
kind = "archetype"
title = "Cutthroat"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Cutthroat"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cutthroat", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "advanced-class-guide"
page = "119"

[fields]
kind = "archetype"
features = [
  { anchor = "class-skills" },
  { anchor = "street-stalker", level = 1 },
  { anchor = "opportune-target", level = 2 },
  { anchor = "stab-and-grab", level = 6 },
]
trades = [
  { replaces = "Track", feature = "track", by = ["street-stalker"] },
  { replaces = "Slayer talent gained at 2nd level", feature = "slayer-talents", levels = [2], by = ["opportune-target"] },
  { replaces = "Slayer talent gained at 6th level", feature = "slayer-talents", levels = [6], by = ["stab-and-grab"] },
]
+++

Street-smart and extremely resourceful, cutthroats stalk city streets and alleyways, preying on
those unfortunate enough to catch their eye. More opportunists than careful planners, they don't
care who they rob or kill, and take advantage of whatever circumstances put them near a suitable
target.

**Gained class skills:** diplo, kno, ling

**Lost class skills:** kd, kg, sur

## Class Skills {#class-skills}

A cutthroat gains Diplomacy, Knowledge (nobility), and Linguistics as class skills, but does not
gain Knowledge (dungeoneering), Knowledge (geography), or Survival as class skills.

## Street Stalker (Ex) {#street-stalker}

At 1st level, a cutthroat selects the Acrobatics, Climb, or Knowledge (local) skill. Once selected,
this cannot be changed. When in urban environments, the cutthroat adds 1/2 his slayer level (minimum
1) to checks attempted with this skill. This ability replaces track.

## Opportune Target (Ex) {#opportune-target}

At 2nd level, a cutthroat who catches a foe by surprise can quickly study that foe to find its
weaknesses. If a cutthroat can act in the surprise round, once during that surprise round he can
study a foe as a free action (instead of a move action) and select it as his studied target. This
ability replaces the slayer talent gained at 2nd level.

## Stab and Grab (Ex) {#stab-and-grab}

At 6th level, as a swift action a cutthroat can attempt a [steal](ref/rule/steal) combat maneuver
against a dead or unconscious target or a studied target he has just confirmed a critical hit
against. A dead or unconscious opponent takes a -10 penalty to its CMD against this maneuver. This
ability replaces the slayer talent gained at 6th level.

## Slayer Talents {#slayer-talents}

The following slayer talents (and rogue talents) complement the cutthroat archetype: fast stealth,
poison use, slowing strike, surprise attack, and terrain mastery. (Those with asterisks \[\*\] are
detailed in the slayer class, starting on page 53.)

## Advanced Slayer Talents {#advanced-slayer-talents}

The following advanced slayer talents (and advanced rogue talents) complement the cutthroat
archetype: assassinate, knock-out blow, opportunist, and slayer camouflage.
