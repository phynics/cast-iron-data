+++
id = "ref/feat/dimensional-disruption"
kind = "feat"
title = "Dimensional Disruption"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dimensional_disruption", path = "json/feat04.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/arcane-strike", label = "or" },
  { kind = "prerequisite", target = "ref/feat/disruptive", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Arcane Strike or Disruptive; Banishing Critical; Combat Reflexes; Dimensional Awareness; Spellcraft 8 ranks; arcane pool class feature."
prerequisite_feats = ["ref/feat/arcane-strike", "ref/feat/banishing-critical", "ref/feat/combat-reflexes", "ref/feat/dimensional-awareness", "ref/feat/disruptive"]
benefit = "When you use Dimensional Awareness to make an attack of opportunity against a creature being summoned or called into a square you threaten, you can additionally use an immediate action to attempt to send the creature back to its home plane. Attempt a Spellcraft check (DC = 15 + the creature's CR [minimum 1] + the spell level of the spell that summoned the creature). If you succeed, the creature does not get to act and is immediately sent back to its home plane."
normal = "A summoning or calling spell can be disrupted only by a failed concentration check or by countering the spell."
+++

## Dimensional Disruption (Combat)

**Sources:** Monster Summoner's Handbook pg 9

You've become so adept at combating summoned creatures that you can interrupt the magical energies
that summon them to your plane.\
**Prerequisites:** [Arcane Strike](ref/feat/arcane-strike) or [Disruptive](ref/feat/disruptive);
[Banishing Critical](ref/feat/banishing-critical); [Combat Reflexes](ref/feat/combat-reflexes);
[Dimensional Awareness](ref/feat/dimensional-awareness); Spellcraft 8 ranks; arcane pool class
feature.\
**Benefit:** When you use Dimensional Awareness to make an attack of opportunity against a creature
being summoned or called into a square you threaten, you can additionally use an immediate action to
attempt to send the creature back to its home plane. Attempt a Spellcraft check (DC = 15 + the
creature's CR \[minimum 1\] + the spell level of the spell that summoned the creature). If you
succeed, the creature does not get to act and is immediately sent back to its home plane.\
**Normal:** A summoning or calling spell can be disrupted only by a failed concentration check or by
countering the spell.
