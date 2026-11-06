+++
id = "ref/feat/gravitational-vital-strike"
kind = "feat"
title = "Gravitational Vital Strike"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gravitational_vital_strike", path = "json/feat07.json" },
]
relations = [
  { kind = "prerequisite", target = "ref/feat/heavy-gravity-acclimation", label = "or" },
  { kind = "prerequisite", target = "ref/feat/light-gravity-acclimation", label = "or" },
]

[fields]
kind = "feat"
feat_types = ["Combat"]
prerequisites = "Vital Strike; Heavy Gravity Acclimation or Light Gravity Acclimation."
prerequisite_feats = ["ref/feat/heavy-gravity-acclimation", "ref/feat/light-gravity-acclimation", "ref/feat/vital-strike"]
benefit = "When using any Vital Strike feat in an area of light or heavy gravity, roll the weapon's damage dice for the attack one additional time. For example, if using Improved Vital Strike, you would roll the weapon's damage dice for the attack four times before adding other damage bonuses, instead of three times. You must have the appropriate prerequisite feat associated with the plane's gravity trait to gain this benefit."
+++

## Gravitational Vital Strike (Combat)

**Sources:** Planar Adventures pg 28

You use unusual gravities to adjust your vital strikes.\
**Prerequisites:** [Vital Strike](ref/feat/vital-strike);
[Heavy Gravity Acclimation](ref/feat/heavy-gravity-acclimation) or
[Light Gravity Acclimation](ref/feat/light-gravity-acclimation).\
**Benefit:** When using any Vital Strike feat in an area of light or heavy
[gravity](ref/rule/gravity-traits), roll the weapon's damage dice for the attack one additional
time. For example, if using [Improved Vital Strike](ref/feat/improved-vital-strike), you would roll
the weapon's damage dice for the attack four times before adding other damage bonuses, instead of
three times. You must have the appropriate prerequisite feat associated with the plane's gravity
trait to gain this benefit.
