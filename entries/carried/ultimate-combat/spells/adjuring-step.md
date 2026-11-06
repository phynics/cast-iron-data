+++
id = "ref/carried/ultimate-combat/spells/adjuring-step"
kind = "spell"
title = "Adjuring Step"
source_ids = ["ultimate-combat"]
section = ["Spells"]
tags = ["abjuration", "force"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Ultimate Combat/Spells/Adjuring Step", path = "ultimate_combat/spell/adjuring_step.json" },
]

[fields]
kind = "spell"
school = "abjuration"
subschools = ["force"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a rabbit's foot)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level or until discharged"
+++

::: statblock
School: abjuration (force)
Level: 1: Alchemist, Arcanist, Bard, Investigator, Magus, Skald, Sorcerer, Wizard
Casting Time: 1 standard action
Components: V, S, M (a rabbit's foot)
Range: personal
Target: you
Duration: 1 round/level or until discharged
:::

_You can move slowly and safely and still cast spells, until you move quickly, make an attack, or
cast a harmful spell._

This spell creates a subtle and complicated force effect that is most effective when used by a still
or slow-moving spellcaster or formula user. While you are subject to this spell, you can take two
5-foot steps each round and still cast spells and use
[spell-like abilities](ref/umr/spell-like-abilities) without provoke attacks of opportunity. This
spell automatically discharges as soon as you make an attack, cast a harmful spell against another
creature, or move more than 5 feet with a single move action. If the action that discharges the
spell also provokes attacks of opportunity, that action still provokes attacks of opportunity as
normal.
