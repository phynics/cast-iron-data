+++
id = "ref/feat/dimensional-awareness"
kind = "feat"
title = "Dimensional Awareness"
source_ids = ["monster-summoners-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dimensional_awareness", path = "json/feat04.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/arcane-strike", label = "or" },
  { kind = "prerequisite", target = "ref/feat/disruptive", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Arcane Strike or Disruptive; Banishing Critical; Combat Reflexes; Spellcraft 8 ranks; arcane pool class feature."
prerequisite_feats = ["ref/feat/arcane-strike", "ref/feat/banishing-critical", "ref/feat/combat-reflexes", "ref/feat/disruptive"]
benefit = "If a summoned or called creature materializes in a space you threaten, you can make an attack of opportunity against that creature before it acts, gaining a +2 circumstance bonus on the attack roll if you successfully identified the spell used to summon or call that creature."
normal = "A summoned or called creature appears instantly when the spell used to conjure it is completed, allowing for no attack of opportunity against the creature."
+++

## Dimensional Awareness (Combat)

**Sources:** Monster Summoner's Handbook pg 8

Your exposure to summoned creatures allows you to predict where conjured opponents will likely
appear.\
**Prerequisites:** [Arcane Strike](ref/feat/arcane-strike) or [Disruptive](ref/feat/disruptive);
[Banishing Critical](ref/feat/banishing-critical); [Combat Reflexes](ref/feat/combat-reflexes);
Spellcraft 8 ranks; arcane pool class feature.\
**Benefit:** If a summoned or called creature materializes in a space you threaten, you can make an
attack of opportunity against that creature before it acts, gaining a +2 circumstance bonus on the
attack roll if you successfully identified the spell used to summon or call that creature.\
**Normal:** A summoned or called creature appears instantly when the spell used to conjure it is
completed, allowing for no attack of opportunity against the creature.
