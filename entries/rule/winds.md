+++
id = "ref/rule/winds"
kind = "rule"
title = "Winds"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "winds", path = "json/rules_gm08.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 439

The wind can create a stinging spray of sand or dust, fan a large fire, keel over a small boat, and
blow gases or vapors away. If powerful enough, it can even knock characters down (see Table 13-10),
interfere with ranged attacks, or impose penalties on some skill checks.

**Light Wind:** A gentle breeze, having little or no game effect.

**Moderate Wind:** A steady wind with a 50% chance of extinguishing small, unprotected flames, such
as candles.

**Strong Wind:** Gusts that automatically extinguish unprotected flames (candles, torches, and the
like). Such gusts impose a -2 penalty on ranged attack rolls and on Perception checks.

**Severe Wind:** In addition to automatically extinguishing any unprotected flames, winds of this
magnitude cause protected flames (such as those of lanterns) to dance wildly and have a 50% chance
of extinguishing these lights. Ranged weapon attacks and Perception checks are at a -4 penalty. This
is the velocity of wind produced by a [gust of wind](ref/spell/gust-of-wind) spell.

**Windstorm:** Powerful enough to bring down branches if not whole trees, windstorms automatically
extinguish unprotected flames and have a 75% chance of blowing out protected flames, such as those
of lanterns. Ranged weapon attacks are impossible, and even siege weapons have a -4 penalty on
attack rolls. Perception checks that rely on sound are at a -8 penalty due to the howling of the
wind.

**Hurricane-Force Wind:** All flames are extinguished. Ranged attacks are impossible (except with
siege weapons, which have a -8 penalty on attack rolls). Perception checks based on sound are
impossible: all characters can hear is the roaring of the wind. Hurricane-force winds often fell
trees.

**Tornado (CR 10):** All flames are extinguished. All ranged attacks are impossible (even with siege
weapons), as are sound-based Perception checks. Instead of being blown away (see Table 13-10),
characters in close proximity to a tornado who fail their Fortitude saves are sucked toward the
tornado. Those who come in contact with the actual funnel cloud are picked up and whirled around for
1d10 rounds, taking 6d6 points of damage per round, before being violently expelled (falling damage
might apply). While a tornado's rotational speed can be as great as 300 mph, the funnel itself moves
forward at an average of 30 mph (roughly 250 feet per round). A tornado uproots trees, destroys
buildings, and causes similar forms of major destruction.

### Table 13-10: Wind Effects

|Wind Force|Wind Speed|Normal/Siege Weapons (Ranged Attacks)^[1](ref/rule/winds#footnote-1)^|Checked Size^[2](ref/rule/winds#footnote-2)^|Blown Away Size^[3](ref/rule/winds#footnote-3)^|[Fly](ref/skill/fly) Penalty|
| --- | --- | --- | --- | --- | --- |
|Light|0-10 mph|-/-|-|-|-|
|Moderate|11-20 mph|-/-|-|-|-|
|Strong|21-30 mph|-2/-|Tiny|-|-2|
|Severe|31-50 mph|-4/-|Small|Tiny|-4|
|Windstorm|51-74 mph|Impossible/-2|Medium|Small|-8|
|Hurricane|75-174 mph|Impossible/-4|Large|Medium|-12|
|Tornado|175-300 mph|Impossible/Impossible|Huge|Large|-16|

###### ^1^ {#footnote-1}

The siege weapon category includes ballista and catapult attacks as well as boulders tossed by
giants.

###### ^2^ {#footnote-2}

Creatures of this size or smaller are unable to move forward against the force of the wind unless
they succeed on a DC 10 Strength check (if on the ground) or a DC 20 Fly skill check if airborne.

###### ^3^ {#footnote-3}

Creatures on the ground are knocked [prone](ref/rule/prone) and rolled 1d4 × 10 feet, taking 1d4
points of nonlethal damage per 10 feet, unless they make a DC 15 Strength check. Flying creatures
are blown back 2d6 × 10 feet and take 2d6 points of nonlethal damage due to battering and buffeting,
unless they succeed on a DC 25 Fly skill check.
