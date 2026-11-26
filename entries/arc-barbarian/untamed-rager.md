+++
id = "ref/arc-barbarian/untamed-rager"
kind = "archetype"
title = "Untamed Rager"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Untamed%20Rager"
source_ids = ["dirty-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "untamed_rager", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "dirty-tactics-toolbox"
page = "15"

[fields]
kind = "archetype"
features = [
  { anchor = "despicable-tactics", level = 2 },
  { anchor = "feral-appearance", level = 3 },
  { anchor = "deplorable-tactics", level = 5 },
  { anchor = "dishonorable", level = 7 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["despicable-tactics"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["feral-appearance"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["deplorable-tactics"] },
  { replaces = "Damage reduction", feature = "damage-reduction", by = ["dishonorable"] },
]
+++

There are no rules in the wild. Some barbarians enter combat with only victory in mind and do
anything in their power to achieve it.

## Despicable Tactics {#despicable-tactics}

At 2nd level, the untamed rager gains [Improved Dirty Trick](ref/feat/improved-dirty-trick) as a
bonus feat. This ability replaces uncanny dodge.

## Feral Appearance (Ex) {#feral-appearance}

At 3rd level, the untamed rager gains a +1 bonus on Intimidate checks. This bonus increases by 1
every 3 barbarian levels thereafter. This ability replaces trap sense.

## Deplorable Tactics {#deplorable-tactics}

At 5th level, the untamed rager gains [Greater Dirty Trick](ref/feat/greater-dirty-trick) as a bonus
feat. This ability replaces improved uncanny dodge.

## Dishonorable (Ex) {#dishonorable}

At 7th level and every 3 barbarian levels thereafter, the untamed rager gains a +1 bonus on combat
maneuver checks when performing dirty tricks and to her CMD to resist others' dirty tricks. This
ability replaces [damage reduction](ref/rule/damage-reduction).
