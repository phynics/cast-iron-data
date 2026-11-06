+++
id = "ref/disease/pallid-gift"
kind = "rule"
title = "Pallid Gift"
source_ids = ["villain-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pallid_gift", path = "json/diseases.json" },
]

[fields]
kind = "none"
+++

**Sources:** Villain Codex

**Type:** Disease (Injury)

**Save:** Fortitude 10 + 1/2 the pallid vector's HD + its Con modifier

**Onset:** immediate

**Frequency:** 1/day

**Effect:** Constitution damage 1d6, Wisdom damage 1d6, and the infected creature is fatigued; the
ability damage can't be healed, and the fatigue can't be removed while the creature is infected

**Cure:** 2 consecutive saves

This infection is mainly spread by [pallid vectors](ref/template/pallid-vector). A non-humanoid
infected creature that dies rises as a [plague zombie](ref/template/zombie) in 2d6 hours, and
spreads pallid gift instead of zombie rot. A humanoid infected creature that dies rises as an undead
according to its HD.

|Hit Dice|Monster|
| --- | --- |
|1-3|Plague zombie|
|4-5|[Ghast](ref/monster/ghoul)|
|6-7|[Wight](ref/monster/wight)|
|8+|[Vampire](ref/template/vampire)|
