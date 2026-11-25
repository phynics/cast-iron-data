+++
id = "ref/arc-rogue/snoop"
kind = "archetype"
title = "Snoop"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Snoop"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "snoop", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "47"

[fields]
kind = "archetype"
features = [
  { anchor = "inspiration", level = 1 },
  { anchor = "investigator-talents", level = 2 },
  { anchor = "uncanny-snoop", level = 4 },
  { anchor = "master-of-whispers", level = 8 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["inspiration"] },
  { replaces = "evasion", feature = "evasion", by = ["inspiration"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["uncanny-snoop"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["uncanny-snoop"] },
  { replaces = "Rogue talent gained at 8th level", feature = "rogue-talents", levels = [8], by = ["master-of-whispers"] },
]
+++

Snoops are the underworld's version of detectives. They often act as information peddlers,
specializing in gathering secrets through investigation, subterfuge, and coercion, and selling or
trading those secrets for personal gain.

## Inspiration (Ex) {#inspiration}

At 1st level, a snoop gains an ability similar to the [investigator's](ref/class/investigator)
inspiration class ability. The snoop begins with an inspiration pool equal to
[half](ref/misc/fractions-and-rounding) her rogue level plus her Intelligence modifier (minimum of
1). Unlike an investigator, a snoop can only use inspiration on skill checks, not on attack rolls or
saving throws. This ability is otherwise identical to the investigator class ability of the same
name.

This ability replaces trapfinding and evasion.

## Investigator Talents (Ex) {#investigator-talents}

Beginning at 2nd level, and each time she selects a new rogue talent, a snoop can instead select one
of the following investigator talents (_Advanced Class Guide_ 32–33):
[eidetic recollection](ref/invtalent/eidetic-recollection), [empathy](ref/invtalent/empathy),
[hidden agendas](ref/invtalent/hidden-agendas),
[inspired alertness](ref/invtalent/inspired-alertness),
[inspired intimidator](ref/invtalent/inspired-intimidator), [item lore](ref/invtalent/item-lore), or
[underworld inspiration](ref/invtalent/underworld-inspiration). Her effective investigator level for
the purpose of these talents is equal to her rogue level. She still can't use inspiration on attack
rolls or saving throws (so, for instance, she can't use the second part of hidden agendas).

## Uncanny Snoop (Ex) {#uncanny-snoop}

At 4th level, a snoop gains a +2 bonus on Intimidate checks when trying to force an opponent to give
her information (or Bluff and Diplomacy checks for the same purpose if she has the
[coax information](ref/talent/coax-information) rogue talent). She also gains a +2 bonus on Sense
Motive checks to tell if someone's information is false. At 8th level, these bonuses increase to +4.

This ability replaces uncanny dodge and improved uncanny dodge.

## Master of Whispers (Ex) {#master-of-whispers}

At 8th level, a snoop receives the [rumormonger](ref/talent/rumormonger) advanced rogue talent.

This ability replaces the rogue talent gained at 8th level.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the snoop archetype: black market connections, coax
information, fast stealth, follow clues, and strong impression (as well as certainty for an
unchained rogue).

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the snoop archetype: hard minded, hidden mind, skill
mastery, and thoughtful re-examining (as well as cutting edge for an unchained rogue).
