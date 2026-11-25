+++
id = "ref/arc-familiar/mauler"
kind = "archetype"
title = "Mauler"
source_ids = ["ultimate-wilderness", "familiar-folio"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mauler", path = "json/archetypes_FAMILIAR.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "212"
[[sources]]
publication = "familiar-folio"
page = "11"

[fields]
kind = "archetype"
features = [
  { anchor = "bond-forged-in-blood" },
  { anchor = "increased-strength", level = 3 },
  { anchor = "battle-form", level = 3 },
  { anchor = "damage-reduction", level = 11 },
]
trades = [
  { replaces = "Speak with master", by = ["bond-forged-in-blood"] },
  { replaces = "speak with animals of its kind", by = ["bond-forged-in-blood"] },
  { replaces = "Deliver touch spells", by = ["battle-form"] },
  { replaces = "Spell resistance", by = ["damage-reduction"] },
  { alters = "The familiar's Intelligence score advancement", by = ["increased-strength"] },
]
+++

While most familiars are scouts and assistants, the mauler familiar cares only for the thrill of
battle. A mauler often serves a bloodthirsty or martial-minded master.

## Mauler Skills {#mauler-skills}

A mauler treats Intimidate as a class skill.

## Bond Forged in Blood (Su) {#bond-forged-in-blood}

A mauler isn't impressed by fancy words—only furious battle. A mauler can't speak or communicate via
language in any way, even if it's a type of creature that normally could.

At 5th level, whenever the mauler's master drops a foe whose Hit Dice are at least half its level to
below 0 hit points, the mauler's empathic link surges with power, granting both the mauler and its
master a +2 morale bonus on attack and damage rolls for 1 round.

This replaces speak with master and speak with animals of its kind.

## Increased Strength (Ex) {#increased-strength}

At 3rd level and every 2 levels thereafter, a mauler's Strength score increases by 1. As a result of
this ability, the familiar's Intelligence score remains 6; a mauler can never have an Intelligence
score higher than 6.

This alters the familiar's Intelligence score advancement.

## Battle Form (Su) {#battle-form}

At 3rd level, a mauler gains the ability to transform into a larger, more ferocious form and back as
a standard action three times per day. In battle form, the mauler's size becomes Medium and it gains
a +2 size bonus to its Strength score. Since many familiars are Tiny or Diminutive, be sure to check
for any additional Strength and Dexterity adjustments for increasing in size from Tiny or Diminutive
to Medium. This is a polymorph effect.

This replaces deliver touch spells.

## Damage Reduction (Su) {#damage-reduction}

At 11th level, a mauler gains DR 5/magic.

This replaces [spell resistance](ref/rule/spell-resistance).
