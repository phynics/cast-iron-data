+++
id = "ref/arc-rogue/filcher"
kind = "archetype"
title = "Filcher"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Filcher"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "filcher", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "advanced-race-guide"
page = "64"

[fields]
kind = "archetype"
features = [
  { anchor = "quicker-than-the-eye", level = 2 },
  { anchor = "rummage", level = 3 },
  { anchor = "filch", level = 4 },
  { anchor = "superior-filching", level = 8 },
]
trades = [
  { replaces = "Evasion", feature = "evasion", by = ["quicker-than-the-eye"] },
  { replaces = "Trap sense +1, +2, +3, +4, +5, and +6", feature = "trap-sense", levels = [3, 6, 9, 12, 15, 18], by = ["rummage"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["filch"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["superior-filching"] },
]
+++

A filcher steals valuables without their owners even realizing it. Whether cutting purses in the
midst of combat or replacing prized items with fakes under the noses of their owners, the filcher is
the master of the quick and quiet steal. A filcher has the following class features.

**Prerequisites:** Halfling

## Quicker than the Eye (Ex) {#quicker-than-the-eye}

At 2nd level, a filcher develops an amazingly swift and delicate touch. When she uses Sleight of
Hand, creatures take a penalty on their Perception checks to notice the attempt equal to half the
filcher's class level. The filcher also subtracts her class level from the normal -20 penalty when
attempting to make a Sleight of Hand check as a move action instead of as a standard action. Lastly,
the filcher can withdraw an object hidden on her person, including a weapon, as a move action
instead of the usual standard action. This ability replaces evasion.

## Rummage (Ex) {#rummage}

At 3rd level, a filcher learns how to assess the value of items at the quickest glance. She can even
make startlingly accurate guesses about particular items merely by observing the bulges they make in
pouches, backpacks, or similar containers. She gains a +1 bonus on Appraise checks and an additional
+1 bonus every three levels thereafter.

As a swift action, a filcher can make an Appraise check in order to determine the relative value of
each object carried by her target (DC = 10 + 1 for every object the filcher is trying to ascertain
the relative value of). Though she never learns the actual prices of items when using rummage, she
does gain enough information to list these items in order, from the most valuable to the least
valuable. She can, by taking a -20 penalty on the check, add to this assessment any items carried by
her target that she cannot see. This ability replaces trap sense +1, +2, +3, +4, +5, and +6.

## Filch (Ex) {#filch}

At 4th level, a filcher learns how pluck items off her opponents even in combat. She gains
[Improved Steal](ref/feat/improved-steal) (_Advanced Player's Guide_ 163) as a bonus feat and can
use her Sleight of Hand bonus instead of her CMB when performing a [steal](ref/rule/steal) combat
maneuver (_Advanced Player's Guide_ 322). If the filcher gains bonuses on combat maneuver checks
from any feats, spells, magic items, or similar effects, they are added to the Sleight of Hand bonus
when using the steal maneuver. This ability replaces uncanny dodge.

## Superior Filching (Ex) {#superior-filching}

At 8th level, a filcher becomes a master at separating owners from their property. She gains
[Greater Steal](ref/feat/greater-steal) as a bonus feat, and opponents do not gain a +5 bonus to
their CMD when she tries to remove items fastened to them. This ability replaces improved uncanny
dodge.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the filcher archetype: fast stealth, slow reactions (_Core
Rulebook_); fast fingers, fast getaway (_Advanced Player's Guide_); black market connections, deft
palm (_Ultimate Combat_).

## Advanced Talents {#advanced-talents}

The following advanced rogue talents complement the filcher archetype: skill mastery (_Core
Rulebook_); fast tumble (_Advanced Player's Guide_); weapon snatcher (_Ultimate Combat_).
