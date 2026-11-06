+++
id = "ref/feat/staggering-critical"
kind = "feat"
title = "Staggering Critical"
source_ids = ["core-rulebook", "pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "staggering_critical", path = "json/feat15.json" },
]

[fields]
kind = "feat"
feat_types = ["Combat", "Critical"]
prerequisites = "Critical Focus, base attack bonus +13."
prerequisite_feats = ["ref/feat/critical-focus"]
benefit = "Whenever you score a critical hit, your opponent becomes staggered for 1d4+1 rounds. A successful Fortitude save reduces the duration to 1 round. The DC of this Fortitude save is equal to 10 + your base attack bonus. The effects of this feat do not stack. Additional hits instead add to the duration."
special = "You can only apply the effects of one critical feat to a given critical hit unless you possess Critical Mastery."
+++

## Staggering Critical (Combat, Critical)

**Sources:** PRPG Core Rulebook pg 134

Your critical hits cause opponents to slow down.\
**Prerequisites:** [Critical Focus](ref/feat/critical-focus), base attack bonus +13.\
**Benefit:** Whenever you score a critical hit, your opponent becomes
[staggered](ref/misc/staggered) for 1d4+1 rounds. A successful Fortitude save reduces the duration
to 1 round. The DC of this Fortitude save is equal to 10 + your base attack bonus. The effects of
this feat do not stack. Additional hits instead add to the duration.\
**Special:** You can only apply the effects of one critical feat to a given critical hit unless you
possess [Critical Mastery](ref/feat/critical-mastery).

### Stamina

**Sources:** Pathfinder Unchained pg 132\
When you score a critical hit and attempt to stagger an opponent with this feat, you can spend up to
5 stamina points to increase the DC of this feat's saving throw by an amount equal to the number of
stamina points you spent.
