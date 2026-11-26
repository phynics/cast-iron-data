+++
id = "ref/arc-alchemist/tinkerer"
kind = "archetype"
title = "Tinkerer"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Tinkerer"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tinkerer", path = "json/archetypes_alchemist2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "46"

[fields]
kind = "archetype"
features = [
  { anchor = "clockwork-bond", level = 1 },
  { anchor = "tinkering", level = 2 },
  { anchor = "clockwork-familiar", level = 6 },
  { anchor = "greater-tinkering", level = 8 },
  { anchor = "clockwork-upgrade", level = 10 },
  { anchor = "clockwork-mimicries", level = 14 },
]
trades = [
  { replaces = "Mutagen", feature = "mutagen", by = ["clockwork-bond"] },
  { replaces = "Poison resistance +2", feature = "poison-resistance", levels = [2], by = ["tinkering"] },
  { replaces = "poison use", feature = "poison-use", by = ["tinkering"] },
  { replaces = "poison resistance +4", feature = "poison-resistance", levels = [5], by = ["tinkering"] },
  { replaces = "Swift poisoning", feature = "swift-poisoning", by = ["clockwork-familiar"] },
  { replaces = "Poison resistance +6", feature = "poison-resistance", levels = [8], by = ["greater-tinkering"] },
  { replaces = "Poison immunity", feature = "poison-resistance", levels = [10], by = ["clockwork-upgrade"] },
  { replaces = "Persistent mutagen", feature = "persistent-mutagen", by = ["clockwork-mimicries"] },
]
+++

Tinkerers constantly dabble in clockworking, creating special familiars that they regularly upgrade
and with which they form bizarre bonds. Many worship [Brigh](ref/faith/brigh) and can be found
throughout Golarion, especially in dwarven and gnome communities.

## Clockwork Bond (Ex) {#clockwork-bond}

At 1st level, a tinkerer forms a bond with one of her creations, and begins play with it at no cost.
This functions as the [familiar](ref/ability/familiars) option of the wizard's arcane bond class
feature, with the tinkerer's effective wizard level equal to her alchemist level. If a tinkerer
would gain a [familiar](ref/sidekick/familiar) through another class, those levels stack for
purposes of determining the familiar's abilities.

A tinkerer's familiar can take any shape the tinkerer wishes, but its statistics and abilities are
identical to a [clockwork spy](ref/monster/clockwork-clockwork-spy) with the normal adjustments and
abilities for a familiar applied, and it is a [construct](ref/type/construct) with the
[clockwork](ref/subtype/clockwork) subtype. At 3rd level, if the tinkerer has the
[infusion](ref/discovery/infusion) discovery, a clockwork spy familiar can deliver the tinkerer's
extracts with a range of touch for her. At 7th level, a clockwork spy can communicate with
constructs with the clockwork subtype. Unlike most familiars, a clockwork spy does not grant special
abilities to its master.

With 1 minute of work and a successful DC 15 Heal check, a tinkerer can restore 1d4 hit points to
her clockwork spy familiar. At 4th level, a tinkerer can restore 1d6 hit points to her familiar in
this same way. This amount increases to an additional 1d6 hit points every 4 levels thereafter (2d6
at 8th level, 3d6 at 12th level, 4d6 at 16th level, and 5d6 at 20th level).

This ability replaces mutagen. A tinkerer cannot choose the cognatogen or mutagen discoveries.

## Tinkering (Ex) {#tinkering}

At 2nd level, a tinkerer can spend 1 hour working on her clockwork spy familiar to enhance it with
one of the options from the following list. At 5th level, the tinkerer can choose a second option
from the list. The same option cannot be chosen twice.

A tinkerer can change the enhancements applied to her familiar, but doing so takes 1 hour of work
per enhancement she wishes to change.

- The clockwork spy familiar gains DR 2/adamantine.

- The clockwork spy familiar gains resist cold 5.

- The clockwork spy familiar gains resist fire 5.

- The clockwork spy's slam attack deals 1d3 points of damage.

- The clockwork spy gains a +5 alchemical bonus on Stealth checks.

- The clockwork spy gains [darkvision](ref/rule/darkvision) 120 feet.

- The clockwork spy gains a +2 resistance bonus on Reflex saving throws.

- The clockwork spy gains a +2 resistance bonus on Will saving throws.

- The clockwork spy gains a +2 natural armor bonus.

- The clockwork familiar's maneuverability is average.

This ability replaces poison resistance +2, poison use, and poison resistance +4.

## Clockwork Familiar (Ex) {#clockwork-familiar}

At 6th level, the tinkerer turns her familiar into a
[clockwork familiar](ref/monster/clockwork-clockwork-familiar) that takes any form she wishes. She
must choose which type of item is installed in the clockwork familiar. She gains the clockwork
familiar at no cost, as if she were a 7th-level spellcaster with the
[Improved Familiar](ref/feat/improved-familiar) feat.

This ability replaces swift poisoning.

## Greater Tinkering (Ex) {#greater-tinkering}

At 8th level, a tinkerer can spend 1 hour working on her familiar to enhance it with one of the
options from the following list. A tinkerer can change the enhancement applied to her familiar, but
doing so takes 1 hour.

- The clockwork familiar's bite attack deals 1d4 points of damage.

- The clockwork familiar gains DR 10/adamantine.

- The clockwork familiar gains any feat for which it qualifies as a bonus feat.

- The clockwork familiar gains a +10 alchemical bonus on Stealth checks.

This ability replaces poison resistance +6.

## Clockwork Upgrade (Ex) {#clockwork-upgrade}

At 10th level, a tinkerer has learned how to change the type of magic item her clockwork familiar
can carry. This requires 1 hour of uninterrupted work. A tinkerer can change the type of item her
clockwork familiar carries only once every 24 hours. Additionally, a tinkerer can remove a spent
item and install a new one as a move action.

This ability replaces poison immunity.

## Clockwork Mimicries (Ex) {#clockwork-mimicries}

At 14th level, a tinkerer can use her mechanical mastery to create clockwork mimicries of powerful
magic items. Doing so takes 1 hour of uninterrupted work, and allows the tinkerer to create a
wondrous item that functions for a number of hours per day equal to her alchemist level. When
creating such a clockwork item, the tinkerer must use materials worth an amount equal to the
wondrous item's construction cost. She need not meet any of the item's other creation requirements.
A tinkerer cannot create a mimicry of a consumable wondrous item or a wondrous item with finite
charges, and she can have only one mimicry at a time. The clockwork item never functions as a
wondrous item for any other creature.

The tinkerer can spend 1 hour disassembling a clockwork mimicry and reassembling it into a mimicry
of a different wondrous item. When she disassembles a clockwork mimicry, she can salvage parts worth
[half](ref/misc/fractions-and-rounding) of the mimicry's creation cost. She still must pay the full
creation cost for the new mimicry. This resets the duration the mimicry functions per day.

This replaces persistent mutagen.

## Discoveries {#discoveries}

The following discoveries complement the tinkerer archetype: combine extract,
[dilution](ref/discovery/dilution), [elixir of life](ref/discovery/elixir-of-life),
[enhance potion](ref/discovery/enhance-potion), [eternal potion](ref/discovery/eternal-potion),
[extend potion](ref/discovery/extend-potion), [infusion](ref/discovery/infusion), and
[promethean disciple](ref/discovery/promethean-disciple).
