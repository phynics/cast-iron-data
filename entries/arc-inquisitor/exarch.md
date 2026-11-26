+++
id = "ref/arc-inquisitor/exarch"
kind = "archetype"
title = "Exarch"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Exarch"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "exarch", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "advanced-race-guide"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "spells" },
  { anchor = "inflexible-will", level = 1 },
  { anchor = "detect-chaos" },
  { anchor = "fearsome-jurist", level = 5 },
  { anchor = "aura-of-repetition", level = 8 },
  { anchor = "double-jeopardy", level = 12 },
  { anchor = "aura-of-reversion", level = 16 },
]
trades = [
  { replaces = "Monster lore", feature = "monster-lore", by = ["inflexible-will"] },
  { replaces = "Detect alignment", feature = "detect-alignment", by = ["detect-chaos"] },
  { replaces = "Bane", feature = "bane", by = ["fearsome-jurist"] },
  { replaces = "Second judgment", feature = "second-judgment", by = ["aura-of-repetition"] },
  { replaces = "Greater bane", feature = "greater-bane", by = ["double-jeopardy"] },
  { replaces = "Third judgment", feature = "third-judgment", by = ["aura-of-reversion"] },
  { alters = "Spellcasting", feature = "spells", by = ["spells"] },
]
+++

The gruff traditionalism of most dwarves finds its apex in those who adhere to a strict orthodoxy
rooted in ancient principles and practices and who are not amenable whatsoever to change or
innovation.

## Spells {#spells}

Exarchs cannot cast spells with the chaotic descriptor.

## Inflexible Will (Ex) {#inflexible-will}

At 1st level, an exarch gains a +2 bonus on saving throws against _[confusion](ref/spell/confusion)_
and _[insanity](ref/spell/insanity)_ effects and effects with the chaotic descriptor. This ability
replaces monster lore.

## Detect Chaos (Sp) {#detect-chaos}

At will, an exarch can use _[detect chaos](ref/spell/detect-chaos)_. This ability replaces detect
alignment.

## Fearsome Jurist (Su) {#fearsome-jurist}

At 5th level, an exarch can imbue one of her weapons with the _[jurist](ref/magic-enh/jurist)_ or
_[menacing](ref/magic-enh/menacing)_ weapon special ability as a swift action, and may switch
between these properties as a swift action. When using either special ability, her weapon's critical
threat range doubles against chaotic creatures. This does not stack with
_[keen edge](ref/spell/keen-edge),_ [Improved Critical](ref/feat/improved-critical), or similar
effects. This ability otherwise functions as and replaces [bane](ref/spell/bane).

## Aura of Repetition (Su) {#aura-of-repetition}

At 8th level, once per day while using her judgment, an exarch can project an aura of repetition, as
the Toil subdomain power (_Advanced Player's Guide_ 97). If the exarch takes Artifice (Toil) as her
domain, the save DC of her aura increases by 2 but its duration does not increase. This ability
replaces her second judgment.

## Double Jeopardy (Su) {#double-jeopardy}

At 12th level, whenever an exarch uses her fearsome jurist ability, she may choose to affect two
weapons, with one gaining the _jurist_ weapon special ability and the other the _menacing_ special
ability as above. Both special abilities may be combined in a single weapon, whose critical threat
range doubles. This does not stack with _[keen edge](ref/spell/keen-edge)_, Improved Critical, or
similar effects. This ability replaces greater bane.

## Aura of Reversion (Su) {#aura-of-reversion}

At 16th level, while using her judgment, an exarch can project a 30-foot-radius
[emanation](ref/misc/emanation) for a number of rounds per day equal to her inquisitor level. Any
creature other than the exarch that is using a transmutation effect within this aura at the
beginning of its turn becomes [sickened](ref/misc/sickened), or sickened and
[nauseated](ref/misc/nauseated) if using a polymorph effect, including the
[change shape](ref/umr/change-shape) ability (Fortitude negates; DC 10 + 1/2 the exarch's level +
her Wisdom modifier). Continuous effects from permanent magical items do not cause this effect.
Within the aura, [dispel](ref/spell/dispel-magic) checks against transmutation effects gain a +4
bonus. This ability cannot be used simultaneously with aura of repetition. This ability replaces her
third judgment.
