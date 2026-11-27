+++
id = "ref/arc-rogue/vexing-dodger"
kind = "archetype"
title = "Vexing Dodger"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Vexing%20Dodger"
source_ids = ["giant-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vexing_dodger", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "giant-hunters-handbook"
page = "21"

[fields]
kind = "archetype"
features = [
  { anchor = "limb-climber", level = 1 },
  { anchor = "improved-dirty-trick", level = 2 },
  { anchor = "underfoot-agility", level = 3 },
  { anchor = "underfoot-trickster", level = 4 },
  { anchor = "distracting-climber", level = 8 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["limb-climber"] },
  { replaces = "Rogue talent gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["improved-dirty-trick"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["underfoot-agility"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["underfoot-trickster"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["distracting-climber"] },
]
+++

Vexing dodgers take advantage of their smaller size to outmaneuver larger foes such as giants.
Vexing dodgers have the following class features.

## Limb-Climber (Ex) {#limb-climber}

When adjacent to or in the space of a corporeal creature at least one size category larger than
herself, a vexing dodger can climb that creature's body with a successful [Climb](ref/skill/climb)
check against a DC equal to the target creature's CMD. Although the vexing dodger is holding on to
the creature, this action isn't a grapple; it doesn't provoke attacks of opportunity from the
creature, and neither the vexing dodger nor the creature she climbs gains the grappled condition.
While the vexing dodger is on the climbed creature, the creature takes a penalty on attack rolls
against the vexing dodger equal to the number of sneak attack dice the dodger possesses. This
ability replaces trapfinding.

## Improved Dirty Trick (Ex) {#improved-dirty-trick}

At 2nd level, a vexing dodger gains [Improved Dirty Trick](ref/feat/improved-dirty-trick) as a bonus
feat, even if she doesn't meet the prerequisites. This ability replaces the rogue talent gained at
2nd level.

## Underfoot Agility (Ex) {#underfoot-agility}

At 3rd level, a vexing dodger gains a +1 morale bonus on Acrobatics, Climb, and Escape Artist
attempts against creatures at least one size category larger than herself. This bonus increases by 1
for every 3 levels beyond 3rd. This ability replaces trap sense.

## Underfoot Trickster (Ex) {#underfoot-trickster}

At 4th level, a vexing dodger can move through the space of a creature two size categories larger
than herself without needing to attempt an Acrobatics check. She would still need to succeed at
Acrobatics checks to avoid attacks of opportunity provoked by leaving a threatened space; this
ability covers only the ability to move. Additionally, whenever the vexing dodger hits a larger foe
with a melee sneak attack, she can choose to forgo the sneak attack bonus damage and instead attempt
make a [dirty trick](ref/rule/dirty-trick) combat maneuver as a swift action. This ability replaces
uncanny dodge.

## Distracting Climber (Ex) {#distracting-climber}

At 8th level, when a vexing dodger attempts a dirty trick maneuver against a creature she's
climbing, she gets a bonus on the combat maneuver check equal to the number of sneak attack dice she
has. If she chooses to [sicken](ref/misc/sickened) the target with her dirty trick and succeeds at
her combat maneuver check, the target must succeed at a Fortitude saving throw (DC = 10 + 1/2 the
vexing dodger's level + her Intelligence modifier) or be [nauseated](ref/misc/nauseated) for 1
round. This ability replaces improved uncanny dodge.

## Rogue Talents (Ex) {#rogue-talents}

A vexing dodger can choose [uncanny dodge](ref/ability/uncanny-dodge) as a rogue talent starting at
4th level, and she can choose [improved uncanny dodge](ref/ability/improved-uncanny-dodge) as an
advanced rogue talent. The following talents complement the vexing dodger archetype: befuddling
strike, confounding blades, peerless maneuver, positioning attack, slow reactions, wall scramble.
