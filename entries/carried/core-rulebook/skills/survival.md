+++
id = "ref/carried/core-rulebook/skills/survival"
kind = "skill"
title = "Survival"
source_ids = ["core-rulebook"]
section = ["Skills"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Skills/Survival", path = "core_rulebook/skill/survival.json" },
]

[fields]
kind = "none"
+++

::: statblock
Key Ability: Wis
Trained Only: Yes
Armor Check Penalty: Yes
:::

_You are skilled at surviving in the wild and at navigating in the wilderness. You also excel at
following trails and tracks left by others._

## Check {#check}

You can keep yourself and others safe and fed in the wild. The table below gives the DCs for various
tasks that require Survival checks.

### Survival DC {#survival-dc}

|Survival DC|Task|
| --- | --- |
|10|Get along in the wild. Move up to half your overland speed while hunting and foraging (no food or water supplies needed). You can provide food and water for one other person for every 2 points by which your check result exceeds 10.|
|15|Gain a +2 bonus on all Fortitude saves against severe weather while moving up to half your overland speed, or gain a +4 bonus if you remain stationary. You may grant the same bonus to one other character for every 1 point by which your Survival check result exceeds 15.|
|15|Keep from getting lost or avoid natural hazards, such as quicksand.|
|15|Predict the weather up to 24 hours in advance. For every 5 points by which your Survival check result exceeds 15, you can predict the weather for one additional day in advance.|

### Follow Tracks {#follow-tracks}

To find tracks or to follow them for 1 mile requires a successful Survival check. You must make
another Survival check every time the tracks become difficult to follow. If you are not trained in
this skill, you can make untrained checks to find tracks, but you can follow them only if the DC for
the task is 10 or lower. Alternatively, you can use the Perception skill to find a footprint or
similar sign of a creature's passage using the same DCs, but you can't use Perception to follow
tracks, even if someone else has already found them.

You move at half your normal speed while following tracks (or at your normal speed with a –5 penalty
on the check, or at up to twice your normal speed with a –20 penalty on the check). The DC depends
on the surface and the prevailing conditions, as given on the table.

#### Surface {#surface}

|Surface|Survival DC|
| --- | --- |
|Very soft ground|5|
|Soft ground|10|
|Firm ground|15|
|Hard ground|20|

### Very Soft Ground {#very-soft-ground}

Any surface (fresh snow, thick dust, wet mud) that holds deep, clear impressions of footprints.

### Soft Ground {#soft-ground}

Any surface soft enough to yield to pressure, but firmer than wet mud or fresh snow, in which a
creature leaves frequent but shallow footprints.

### Firm Ground {#firm-ground}

Most normal outdoor surfaces (such as lawns, fields, woods, and the like) or exceptionally soft or
dirty indoor surfaces (thick rugs and very dirty or dusty floors). The creature might leave some
traces (broken branches or tufts of hair), but it leaves only occasional or partial footprints.

### Hard Ground {#hard-ground}

Any surface that doesn't hold footprints at all, such as bare rock or an indoor floor. Most
streambeds fall into this category, since any footprints left behind are obscured or washed away.
The creature leaves only traces (scuff marks or displaced pebbles).

#### Condition {#condition}

::: table
head = [
  [
    { text = "Condition", header = true },
    { text = "Survival DC Modifier", header = true },
  ],
]
body = [
  [
    { text = "Every three creatures in the group being tracked" },
    { text = "–1" },
  ],
  [
    { text = "Size of creature or creatures being tracked:^1^", colspan = 2 },
  ],
  [
    { text = "Fine" },
    { text = "+8" },
  ],
  [
    { text = "Diminutive" },
    { text = "+4" },
  ],
  [
    { text = "Tiny" },
    { text = "+2" },
  ],
  [
    { text = "Small" },
    { text = "+1" },
  ],
  [
    { text = "Medium" },
    { text = "+0" },
  ],
  [
    { text = "Large" },
    { text = "–1" },
  ],
  [
    { text = "Huge" },
    { text = "–2" },
  ],
  [
    { text = "Gargantuan" },
    { text = "–4" },
  ],
  [
    { text = "Colossal" },
    { text = "–8" },
  ],
  [
    { text = "Every 24 hours since the trail was made" },
    { text = "+1" },
  ],
  [
    { text = "Every hour of rain since the trail was made" },
    { text = "+1" },
  ],
  [
    { text = "Fresh snow since the trail was made" },
    { text = "+10" },
  ],
  [
    { text = "Poor visibility:^2^", colspan = 2 },
  ],
  [
    { text = "Overcast or moonless night" },
    { text = "+6" },
  ],
  [
    { text = "Moonlight" },
    { text = "+3" },
  ],
  [
    { text = "Fog or precipitation" },
    { text = "+3" },
  ],
  [
    { text = "Tracked party hides trail (and moves at half speed)" },
    { text = "+5" },
  ],
]
foot = [
  [
    { text = "1 For a group of mixed sizes, apply only the modifier for the largest size category.", colspan = 2 },
  ],
  [
    { text = "2 Apply only the largest modifier from this category.", colspan = 2 },
  ],
]
:::

Several modifiers may apply to the Survival check, as given on the table above.

## Action {#action}

Varies. A single Survival check may represent activity over the course of hours or a full day. A
Survival check made to find tracks is at least a full-round action, and it may take even longer.

## Try Again {#try-again}

Varies. For getting along in the wild or for gaining the Fortitude save bonus noted in the first
table above, you make a Survival check once every 24 hours. The result of that check applies until
the next check is made. To avoid getting lost or avoid natural hazards, you make a Survival check
whenever the situation calls for one. Retries to avoid getting lost in a specific situation or to
avoid a specific natural hazard are not allowed. For finding tracks, you can retry a failed check
after 1 hour (outdoors) or 10 minutes (indoors) of searching.

## Special {#special}

If you are trained in Survival, you can automatically determine where true north lies in relation to
yourself.

A ranger gains a bonus on Survival checks when using this skill to find or follow the tracks of a
favored enemy.

If you have the Self-Sufficient feat, you get a bonus on Survival checks (see Feats).
