+++
id = "ref/feat/diabolic-humiliation"
kind = "feat"
title = "Diabolic Humiliation"
aon = "FeatDisplay.aspx?ItemName=Diabolic%20Humiliation"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "diabolic_humiliation", path = "json/feat04.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/improved-unarmed-strike", label = "or" },
  { kind = "prerequisite", target = "ref/feat/weapon-focus", label = "or" },
]
[[sources]]
publication = "planar-adventures"
page = "27"

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Combat Reflexes, Diabolic Style; Vital Strike; Improved Unarmed Strike or Weapon Focus (unarmed strike); base attack bonus +8 or monk level 7th."
prerequisite_feats = ["ref/feat/combat-reflexes", "ref/feat/diabolic-style", "ref/feat/improved-unarmed-strike", "ref/feat/vital-strike", "ref/feat/weapon-focus"]
benefit = "When you successfully stagger a foe with an unarmed strike using Diabolic Style, the target becomes further humiliated. The target cannot gain the benefit of any morale bonus for 1 minute after being staggered in this way, and for the duration of that minute, any additional staggered effects it suffers from your attacks of opportunity last for 2 rounds rather than 1. The durations of multiple staggered effects administered in this way stack."
special = "A monk of at least 10th level with this feat can select Improved Vital Strike as a monk bonus feat."
+++

## Diabolic Humiliation (Combat)

Your humiliating strikes decrease a foe's morale.\
**Prerequisites:** [Combat Reflexes](ref/feat/combat-reflexes),
[Diabolic Style](ref/feat/diabolic-style); [Vital Strike](ref/feat/vital-strike);
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) or [Weapon Focus](ref/feat/weapon-focus)
(unarmed strike); base attack bonus +8 or monk level 7th.\
**Benefit:** When you successfully [stagger](ref/misc/staggered) a foe with an unarmed strike using
Diabolic Style, the target becomes further humiliated. The target cannot gain the benefit of any
morale bonus for 1 minute after being staggered in this way, and for the duration of that minute,
any additional staggered effects it suffers from your attacks of opportunity last for 2 rounds
rather than 1. The durations of multiple staggered effects administered in this way stack.\
**Special:** A monk of at least 10th level with this feat can select
[Improved Vital Strike](ref/feat/improved-vital-strike) as a monk bonus feat.
