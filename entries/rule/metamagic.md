+++
id = "ref/rule/metamagic"
kind = "rule"
title = "Metamagic"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "metamagic", path = "json/rules_opt_magic01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 145

When using a metamagic feat to modify a spell cast from a spell pool, the caster is treated as if he
were a spontaneous caster (increasing the casting time to a full-round action if applicable). The
spell must still fall under the level he can cast with his pool. Otherwise, he must still expend one
of his spell slots to prepare it.

For instance, our example 13th-level necromancer could cast an [enlarged](ref/feat/enlarge-spell)
[fireball](ref/spell/fireball) as a full-round action using his spell pool, but to cast an
[empowered](ref/feat/empower-spell) _[fireball](ref/spell/fireball),_ he would have to expend a
5th-level spell slot to prepare it, since 5th-level spells aren't part of his pool.
