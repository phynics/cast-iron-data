+++
id = "ref/feat/bleeding-critical"
kind = "feat"
title = "Bleeding Critical"
source_ids = ["core-rulebook", "pathfinder-unchained", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bleeding_critical", path = "json/feat02.json" },
]

[fields]
kind = "feat"
feat_types = ["Combat", "Critical"]
prerequisites = "Critical Focus, base attack bonus +11."
benefit = "Whenever you score a critical hit with a slashing or piercing weapon, your opponent takes 2d6 points of bleed damage each round on his turn, in addition to the damage dealt by the critical hit. Bleed damage can be stopped by a DC 15 Heal skill check or through any magical healing. The effects of this feat stack."
special = "You can only apply the effects of one critical feat to a given critical hit unless you possess Critical Mastery."
+++

## Bleeding Critical (Combat, Critical)

**Sources:** PRPG Core Rulebook pg 118

Your critical hits cause opponents to bleed profusely.\
**Prerequisites:** [Critical Focus](ref/feat/critical-focus), base attack bonus +11.\
**Benefit:** Whenever you score a critical hit with a slashing or piercing weapon, your opponent
takes 2d6 points of [bleed](ref/rule/bleed) damage each round on his turn, in addition to the damage
dealt by the critical hit. Bleed damage can be stopped by a DC 15 Heal skill check or through any
magical healing. The effects of this feat stack.\
**Special:** You can only apply the effects of one critical feat to a given critical hit unless you
possess [Critical Mastery](ref/feat/critical-mastery).

### Stamina

**Sources:** Pathfinder Unchained pg 114\
When you deal bleed damage with this feat, you can spend up to 3 stamina points to increase the
amount of bleed damage dealt by double the number of stamina points you spent.

### Mythic Bleeding Critical

**Sources:** Mythic Adventures pg 60\
Your deadliest blows unleash rivers of blood.\
**Prerequisites:** Bleeding Critical, Mythic Critical Focus.\
**Benefit:** The bleed damage dealt with Bleeding Critical increases by your tier. Stopping this
bleed damage requires a Heal check with a DC equal to 15 + 1/2 your tier. Any magical healing ends
the bleed damage normally.

You can expend one use of mythic power to deal 1 Con bleed, in addition to the hit point bleed
damage you deal with this feat. This effect increases by 1 for each additional use of mythic power
you expend.
