+++
id = "ref/feat/diabolic-style"
kind = "feat"
title = "Diabolic Style"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "diabolic_style", path = "json/feat04.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/improved-unarmed-strike", label = "or" },
  { kind = "prerequisite", target = "ref/feat/weapon-focus", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat", "Style"]
prerequisites = "Combat Reflexes; Improved Unarmed Strike or Weapon Focus (unarmed strike); base attack bonus +2 or monk level 1st."
prerequisite_feats = ["ref/feat/combat-reflexes", "ref/feat/improved-unarmed-strike", "ref/feat/weapon-focus"]
benefit = "While using this style, you can make an attack of opportunity with an unarmed strike to deliver a humiliating swat to the target. If you hit the target, you inflict 1 point of nonlethal damage and the target must succeed at a Will saving throw (DC = 10 + half your level + your Charisma modifier) or become staggered for 1 round."
special = "A monk of at least 6th level with this feat can select Vital Strike as a monk bonus feat."
+++

## Diabolic Style (Combat, Style)

**Sources:** Planar Adventures pg 27

You utilize combat as an opportunity to inflict humiliation upon those who provoke your attacks of
opportunity.\
**Prerequisites:** [Combat Reflexes](ref/feat/combat-reflexes);
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) or [Weapon Focus](ref/feat/weapon-focus)
(unarmed strike); base attack bonus +2 or monk level 1st.\
**Benefit:** While using this style, you can make an attack of opportunity with an unarmed strike to
deliver a humiliating swat to the target. If you hit the target, you inflict 1 point of nonlethal
damage and the target must succeed at a Will saving throw (DC = 10 + half your level + your Charisma
modifier) or become [staggered](ref/misc/staggered) for 1 round.\
**Special:** A monk of at least 6th level with this feat can select
[Vital Strike](ref/feat/vital-strike) as a monk bonus feat.
