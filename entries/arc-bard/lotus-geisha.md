+++
id = "ref/arc-bard/lotus-geisha"
kind = "archetype"
title = "Lotus Geisha"
aon = "ArchetypeDisplay.aspx?FixedName=Bard%20Lotus%20Geisha"
source_ids = ["dragon-empires-primer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lotus_geisha", path = "json/archetypes_bard2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bard" },
]
[[sources]]
publication = "dragon-empires-primer"
page = "22"

[fields]
kind = "archetype"
features = [
  { anchor = "enrapturing-performance", level = 2 },
]
trades = [
  { replaces = "Well-versed", feature = "well-versed", by = ["enrapturing-performance"] },
  { replaces = "Bardic knowledge", feature = "bardic-knowledge" },
  { replaces = "lore master", feature = "lore-master" },
  { replaces = "Weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons" },
]
+++

The lotus geisha of Minkai are renowned for their powers of seduction, and tales tell of lotus
geisha disarming foes and bolstering allies. The lotus geisha is an archetype of the bard class.

## Weapon Proficiency {#weapon-proficiency}

A lotus geisha is proficient with all simple weapons, plus the
[butterfly sword](ref/eq-weapon/butterfly-sword), [fighting fan](ref/eq-weapon/fighting-fan),
[iron brush](ref/eq-weapon/iron-brush), [sai](ref/eq-weapon/sai),
[shortbow](ref/eq-weapon/shortbow), and [shuriken](ref/eq-weapon/shuriken). See _Pathfinder RPG
Ultimate Combat_ for details on these Eastern weapons. This replaces the normal bard weapon
proficiencies.

## Enrapturing Performance (Su) {#enrapturing-performance}

At 2nd level, a lotus geisha gains the ability to execute an enrapturing performance in addition to
her bardic performance ability. An enrapturing performance is exactly like a bardic performance with
the following exceptions.

A lotus geisha can use an enrapturing performance to recreate the effects of any of her known bardic
performances, but she focuses the performance on only a single target within range. While other
creatures see and hear a lotus geisha's enrapturing performance, only the target of this ability is
affected by it. A lotus geisha cannot have a bardic performance and an enrapturing performance in
effect at the same time. Every round spent engaged in an enrapturing performance counts against the
total number of rounds per day she can use her bardic performance, and she cannot use this ability
if she does not have any more rounds of bardic performance left for that day. Starting an
enrapturing performance is a standard action; at 7th level, it becomes a move action, and at 13th
level, it becomes a swift action.

A lotus geisha adds a +2 bonus to the DC of Will saves made to resist the effects of her fascinate,
frightening tune, and suggestion enrapturing performances. When a lotus geisha uses her enrapturing
performance ability to emulate inspire competence, inspire courage, inspire greatness, or
[inspire heroics](ref/performance/inspire-heroics), any bonuses to AC or on ability checks, attack
rolls, damage rolls, saving throws, and skill checks increase by +1. For example, a lotus geisha
using inspire heroics as an enrapturing performance would grant her target a +5 morale bonus on
saving throws and a +5 dodge bonus to AC, instead of the usual +4 bonuses.

This ability replaces well-versed.

## Bonus Feats {#bonus-feats}

At 1st level, a lotus geisha gains [Spell Focus](ref/feat/spell-focus) (enchantment) as a bonus
feat. At 5th level, she gains [Greater Spell Focus](ref/feat/greater-spell-focus) (enchantment) as a
bonus feat. These bonus feats replace bardic knowledge and lore master.
