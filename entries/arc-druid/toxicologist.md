+++
id = "ref/arc-druid/toxicologist"
kind = "archetype"
title = "Toxicologist"
aon = "ArchetypeDisplay.aspx?FixedName=Druid%20Toxicologist"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "toxicologist", path = "json/archetypes_druid2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/druid" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "expanded-repertoire", level = 1 },
  { anchor = "natural-poison-lore", level = 2 },
  { anchor = "expert-poisoner", level = 4 },
  { anchor = "toxic-shaper", level = 8 },
]
trades = [
  { replaces = "Spontaneous casting", feature = "spontaneous-casting", by = ["expanded-repertoire"] },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["natural-poison-lore"] },
  { replaces = "woodland stride", feature = "woodland-stride", by = ["natural-poison-lore"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["expert-poisoner"] },
  { replaces = "resist nature's lure", feature = "resist-nature-s-lure", by = ["expert-poisoner"] },
  { alters = "Spells", feature = "spells", by = ["expanded-repertoire"] },
  { alters = "Wild shape", feature = "wild-shape", by = ["toxic-shaper"] },
]
+++

Druids protect the natural environs of the world, and sometimes that requires forcibly expelling
those who would pollute, despoil, or otherwise harm such areas. Single battles may not be enough to
win the war, so some druids specialize in the stealthy application of insidious poisons to their
targets. In the verdant depths of the Mwangi Expanse or the Valashmai Jungle of Tian Xia, many
druids work to root out their enemies by means of powerful toxins, believing word of their foes'
horrifying deaths will deter others from attempting similar desecrations of the natural world.

## Expanded Repertoire (Ex) {#expanded-repertoire}

A toxicologist adds the following extracts and spells to her druid spell list as druid spells of the
listed spell level: _poisoned egg_ (1st level, _Pathfinder Campaign Setting: Inner Sea Gods_ 238),
_transmute potion to poison_ (2nd level), _stinking cloud_ (3rd level), _toxic gift_ (4th level),
and _cloudkill_ (5th level). A toxicologist can channel stored spell energy only into summoning
spells she has prepared ahead of time.

This ability alters spells and replaces spontaneous casting.

## Natural Poison Lore (Ex) {#natural-poison-lore}

A toxicologist has a deep understanding of and appreciation for poisons. At 2nd level, she cannot
accidentally poison herself when applying poison to a weapon and cannot accidentally poison an
animal companion or summoned creature when applying poison to its claws (though poison obviously
should not be applied to a creature's bite).

This ability replaces wild empathy and woodland stride.

## Expert Poisoner (Su) {#expert-poisoner}

At 4th level, a toxicologist increases the DCs of any spells she casts with the poison descriptor
by 1.

This ability replaces trackless step and resist nature's lure.

## Toxic Shaper (Su) {#toxic-shaper}

A toxicologist never gains the ability to use wild shape to transform into an elemental or plant. At
8th level, a toxicologist can transform into a Small or Medium vermin. When she takes this form, her
wild shape functions as _[vermin shape I](ref/spell/vermin-shape-1)_. At 10th level, a toxicologist
can transform into a tiny or large vermin. When she takes this form, her wild shape functions as
_[vermin shape II](ref/spell/vermin-shape-2)_.

This ability alters wild shape.
