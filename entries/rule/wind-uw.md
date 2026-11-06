+++
id = "ref/rule/wind-uw"
kind = "rule"
title = "Wind"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wind_uw", path = "json/rules_adv_gm04.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Wilderness pg 170

Once you've generated the day's precipitation, you'll need to establish the wind strength unless the
precipitation indicates otherwise. For example, on foggy days, no significant wind occurs, while
thunderstorms have their own rules for determining wind strength. To set the wind strength for the
day, roll d% and consult the table below.

### Table 4-28: Wind Strength

|d%|Wind Strength|Wind Speed|Ranged Weapon Penalty/Siege Weapon Penalty|Check Size|Blown Away Size|Skill Penalty|
| --- | --- | --- | --- | --- | --- | --- |
|01-50|Light|0-10 mph|-/-|-|-|-|
|51-80|Moderate|11-20 mph|-/-|-|-|-|
|81-90|Strong|21-30 mph|-2/-|Tiny|-|-2|
|91-95|Severe|31-50 mph|-4/-|Small|Tiny|-4|
|96-100|Windstorm|51+ mph|Impossible/-4|Medium|Small|-8|

**Wind Strength:** This is the category of the wind strength.

**Wind Speed:** This is the range of wind speeds that occur. Wind speed typically fluctuates between
these values through the period of the day, and for moderate or higher wind strength, there are
periods in the day when the wind speed dips below the listed range.

**Ranged Weapon Penalty/Siege Weapon Penalty:** These are the penalties that characters take when
firing ranged weapons and siege weapons in wind of the listed strength. In windstorm-strength wind,
normal ranged weapon attacks (either projectile or thrown) are impossible. This includes ranged
attacks made via spells of the conjuration school, but it does not include evocation ranged attacks.
Siege weapons include all weapons of that type and boulders thrown by giants and other creatures
with the rock throwing special attack.

**Check Size:** Creatures of the listed size or smaller are unable to move forward against the force
of the wind unless they succeed at a DC 10 Strength check (on the ground) or a DC 20 Fly check if
airborne.

**Blown Away Size:** Creatures of the listed size on the ground are knocked prone, roll 1d4×10 feet,
and take 2d6 points of nonlethal damage, unless they succeed on a DC 15 Strength check. Flying
creatures of the listed size are blown back 2d6×10 feet and take 2d6 points of nonlethal damage due
to battering and buffeting, unless they succeed at a DC 25 Fly check.

**Skill Penalty:** This is the penalty for skill checks that can be affected by the wind. These
penalties always apply on Fly checks and sound-based Perception checks, but GMs may also wish to
apply them on Acrobatics checks, Climb checks, and any other ability or skill checks that could be
adversely affected by winds.
