+++
id = "ref/spell/abjuring-step"
kind = "spell"
title = "Abjuring Step"
aon = "SpellDisplay.aspx?ItemName=Abjuring%20Step"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "abjuring_step", path = "json/spells.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "221"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["force"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
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
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Alchemist, Arcanist, Bard, Investigator, Magus, Occultist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a rabbit's foot)
Range: personal
Duration: 1 round/level or until discharged
Saving throw: none
Spell resistance: no
Target: you
Descriptors: force
:::

This spell creates a subtle and complicated force effect that is most effective when used by a still
or slow-moving spellcaster or formula user. While you are subject to this spell, you can take two
5-foot steps each round and still cast spells and use
[spell-like abilities](ref/umr/spell-like-abilities) without provoking attacks of opportunity. This
spell automatically discharges as soon as you make an attack, cast a harmful spell against another
creature, or move more than 5 feet with a single move action. If the action that discharges the
spell also provokes attacks of opportunity, that action still provokes attacks of opportunity as
normal.
