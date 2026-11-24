+++
id = "ref/arc-arcanist/brown-fur-transmuter"
kind = "archetype"
title = "Brown-Fur Transmuter"
aon = "ArchetypeDisplay.aspx?FixedName=Arcanist%20Brown-Fur%20Transmuter"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brown_fur_transmuter", path = "json/archetypes_arcanist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/arcanist" },
]
[[sources]]
publication = "advanced-class-guide"
page = "77"

[fields]
kind = "archetype"
features = [
  { anchor = "powerful-change", level = 3 },
  { anchor = "share-transmutation", level = 9 },
  { anchor = "transmutation-supremacy", level = 20 },
]
trades = [
  { replaces = "The arcanist exploit gained at 3rd level", feature = "arcanist-exploits", levels = [3], by = ["powerful-change"] },
  { replaces = "The arcanist exploit gained at 9th level", feature = "arcanist-exploits", levels = [9], by = ["share-transmutation"] },
  { replaces = "Magical supremacy", feature = "magical-supremacy", by = ["transmutation-supremacy"] },
]
+++

Frequently called "brown-furs," these transmutation-focused arcanists are known for transforming
themselves into animals. What few realize is that these specialized arcanists excel at turning
themselves - and others - into all kinds of creatures.

## Powerful Change (Su) {#powerful-change}

At 3rd level, the brown-fur transmuter learns to harness the power of her magic to empower her
transmutations. Whenever the brown-fur transmuter casts a transmutation spell using one of her
arcanist spell slots, she can expend 1 point from her arcane reservoir as a free action to bolster
the spell. If the spell grants a bonus to an ability score, the bonus then increases by 2. If it
grants a bonus to more than one ability score, only one of the ability scores gains this bonus. The
brown-fur transmuter cannot expend more than 1 point from her arcane reservoir in this way. This
ability replaces the arcanist exploit gained at 3rd level.

## Share Transmutation (Su) {#share-transmutation}

At 9th level, the brown-fur transmuter can target others with her transmutation spells. A brown-fur
transmuter can expend 1 point from her arcane reservoir to change any transmutation spell with a
range of personal to a range of touch. Such a spell automatically fails on unwilling creatures. This
ability replaces the arcanist exploit gained at 9th level.

## Transmutation Supremacy (Su) {#transmutation-supremacy}

At 20th level, the brown-fur transmuter learns to fully master the power of transmutation. Whenever
she casts a transmutation spell, it is treated as it were affected by the
[Extend Spell](ref/feat/extend-spell) feat without altering the casting time or slot used. (She
cannot then alter its duration again with the Extend Spell feat). Whenever she uses her powerful
change ability, the bonus increases by 4 instead of 2. Her share transmutation ability can now
target a willing creature within 30 feet. This ability replaces magical supremacy.
