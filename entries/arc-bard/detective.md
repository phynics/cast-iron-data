+++
id = "ref/arc-bard/detective"
kind = "archetype"
title = "Detective"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Detective"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detective", path = "json/archetypes_bard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "advanced-players-guide"
page = "81"

[fields]
kind = "archetype"
features = [
  { anchor = "bardic-performance" },
  { anchor = "careful-teamwork" },
  { anchor = "true-confession", level = 9 },
  { anchor = "show-yourselves", level = 15 },
  { anchor = "eye-for-detail" },
  { anchor = "arcane-insight", level = 2 },
  { anchor = "arcane-investigation" },
]
trades = [
  { replaces = "Inspire courage", feature = "bardic-performance", power = "inspire courage", by = ["careful-teamwork"] },
  { replaces = "Inspire greatness", feature = "bardic-performance", power = "inspire greatness", by = ["true-confession"] },
  { replaces = "Inspire heroics", feature = "bardic-performance", power = "inspire heroics", by = ["show-yourselves"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge", by = ["eye-for-detail"] },
  { replaces = "Well-versed", feature = "well-versed", by = ["arcane-insight"] },
  { replaces = "Versatile performance", feature = "versatile-performance", by = ["arcane-investigation"] },
]
+++

Piecing together clues and catching the guilty with sheer cleverness, the detective is skilled at
divining the truth.

## Bardic Performance {#bardic-performance}

A detective gains the following types of bardic performance.

## Careful Teamwork (Su) {#careful-teamwork}

A detective uses performance to keep allies coordinated, alert, and ready for action. All allies
within 30 feet gain a +1 bonus on Initiative checks, Perception, and Disable Device checks for 1
hour. They also gain a +1 insight bonus on Reflex saves and to AC against traps and when they are
[flat-footed](ref/rule/flat-footed). These bonuses increase by +1 at 5th level and every six levels
thereafter. Using this ability requires 3 rounds of continuous performance, and the targets must be
able to see and hear the bard throughout the performance. This ability is language-dependent and
requires visual and audible components. This performance replaces inspire courage.

## True Confession (Su) {#true-confession}

At 9th level, a detective can use performance to trick a creature into revealing its secrets. Using
this ability requires a successful Sense Motive check to see through a Bluff or notice mental
compulsion. After 3 continuous rounds of performance, the target must make a Will save (DC 10 + 1/2
the bard's level + the bard's Cha modifier). Success renders the target immune to this power for 24
hours. On a failed save, a liar inadvertently reveals the lie and the truth behind it. A creature
under a charm or compulsion reveals the nature of its enchantment and who placed it (if the creature
knows) and gains a new saving throw to break free from the enchantment. This ability is
language-dependent and requires audible components. Using this power requires only 2 rounds of
performance at 15th level, and 1 round of performance at 20th level. This performance replaces
inspire greatness.

## Show Yourselves (Ex) {#show-yourselves}

At 15th level, a detective can use performance to compel creatures to reveal themselves when hiding.
All enemies within 30 feet must make a Will save (DC 10 + 1/2 the bard's level + the bard's Cha
modifier). If they fail, they must cease using Stealth, unlock and open doors between themselves and
the detective, and dismiss, suppress, or dispel if necessary magical effects that grant
[invisibility](ref/spell/invisibility) or any other form of [concealment](ref/rule/concealment) from
the detective. As long as they can hear the performance, affected creatures may not attack or flee
until they have eliminated every such effect, though they are freed from this compulsion immediately
if attacked. Creatures in the area must make this save each round the bard continues his
performance. This ability is language-dependent and requires audible components. This performance
replaces inspire heroics.

## Eye for Detail (Ex) {#eye-for-detail}

A detective gains a bonus equal to half his level on Knowledge (local), Perception, and Sense Motive
checks, as well as Diplomacy checks to gather information (minimum +1). This ability replaces bardic
knowledge.

## Arcane Insight (Ex) {#arcane-insight}

At 2nd level, a detective can find and disable magical traps, like a rogue's
[trapfinding](ref/ability/trapfinding) ability. In addition, he gains a +4 bonus on saving throws
made against illusions and a +4 bonus on caster level checks and saving throws to see through
disguises and protections against divination (such as _[magic aura](ref/spell/magic-aura)_,
_[misdirection](ref/spell/misdirection)_, and _[nondetection](ref/spell/nondetection)_). This
ability replaces well-versed.

## Arcane Investigation {#arcane-investigation}

In addition, a detective's class spell list includes the following:
1st—_[detect chaos](ref/spell/detect-chaos)/[evil](ref/spell/detect-evil)/[law](ref/spell/detect-law)/
[good](ref/spell/detect-good)_; 2nd—_[zone of truth](ref/spell/zone-of-truth)_;
3rd—_[arcane eye](ref/spell/arcane-eye), [speak with dead](ref/spell/speak-with-dead),
[speak with plants](ref/spell/speak-with-plants)_; 4th—_[discern lies](ref/spell/discern-lies)_;
5th—_[prying eyes](ref/spell/prying-eyes), [stone tell](ref/spell/stone-tell)_;
6th—_[discern location](ref/spell/discern-location), [find the path](ref/spell/find-the-path),
[greater prying eyes](ref/spell/prying-eyes-greater),
[moment of prescience](ref/spell/moment-of-prescience)_. A detective may add one of these spells or
any divination spell on the bard spell list to his list of spells known at 2nd level and every four
levels thereafter. This ability replaces versatile performance.
