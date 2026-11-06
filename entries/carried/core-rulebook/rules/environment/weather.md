+++
id = "ref/carried/core-rulebook/rules/environment/weather"
kind = "rule"
title = "Weather"
source_ids = ["core-rulebook"]
section = ["Rules", "Environment"]
parent = "ref/carried/core-rulebook/rules/environment"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Rules/Environment/Weather", path = "core_rulebook/rules/environment.json" },
]

[fields]
kind = "none"
+++

Weather can play an important role in an adventure.

## Table: Random Weather {#table-random-weather}

::: table
caption = "Table: Random Weather"
head = [
  [
    { text = "d%", header = true },
    { text = "Weather", header = true },
    { text = "Cold Climate", header = true },
    { text = "Temperate Climate^1^", header = true },
    { text = "Desert", header = true },
  ],
]
body = [
  [
    { text = "01–70" },
    { text = "Normal weather" },
    { text = "Cold, calm" },
    { text = "Normal for season^2^" },
    { text = "Hot, calm" },
  ],
  [
    { text = "71–80" },
    { text = "Abnormal weather" },
    { text = "Heat wave (01–30) orcold snap (31–100)" },
    { text = "Heat wave (01–50) orcold snap (51–100)" },
    { text = "Hot, windy" },
  ],
  [
    { text = "81–90" },
    { text = "Inclement weather" },
    { text = "Precipitation (snow)" },
    { text = "Precipitation (normal for season)" },
    { text = "Hot, windy" },
  ],
  [
    { text = "91–99" },
    { text = "Storm" },
    { text = "Snowstorm" },
    { text = "Thunderstorm, snowstorm" },
    { text = "Duststorm" },
  ],
  [
    { text = "100" },
    { text = "Powerful storm" },
    { text = "Blizzard" },
    { text = "Windstorm, blizzard, hurricane, tornado" },
    { text = "Downpour" },
  ],
]
foot = [
  [
    { text = "1 Temperate includes forests, hills, marshes, mountains, plains, and warm aquatic environments.", colspan = 5 },
  ],
  [
    { text = "2 Winter is cold, summer is warm, spring and autumn are temperate. Marsh regions are slightly warmer in winter.", colspan = 5 },
  ],
]
:::

Table: Random Weather can be used as a simple local weather table. Terms on that table are defined
as follows.

## Calm {#calm}

Wind speeds are light (0 to 10 mph).

## Cold {#cold}

Between 0° and 40° Fahrenheit during the day, 10 to 20 degrees colder at night.

## Cold Snap {#cold-snap}

Lowers temperature by –10° F.

## Downpour {#downpour}

Treat as rain (see Precipitation, below), but conceals as fog. Can create floods. A downpour lasts
for 2d4 hours.

## Heat Wave {#heat-wave}

Raises temperature by +10° F.

## Hot {#hot}

Between 85° and 110° Fahrenheit during the day, 10 to 20 degrees colder at night.

## Moderate {#moderate}

Between 40° and 60° Fahrenheit during the day, 10 to 20 degrees colder at night.

## Powerful Storm (Windstorm/Blizzard/Hurricane/Tornado) {#powerful-storm-windstorm-blizzard-hurricane-tornado}

Wind speeds are over 50 mph (see Table: Wind Effects). In addition, blizzards are accompanied by
heavy snow (1d3 feet), and hurricanes are accompanied by downpours. Windstorms last for 1d6 hours.
Blizzards last for 1d3 days. Hurricanes can last for up to a week, but their major impact on
characters comes in a 24-to-48-hour period when the center of the storm moves through their area.
Tornadoes are very short-lived (1d6 × 10 minutes), typically forming as part of a thunderstorm
system.

## Precipitation {#precipitation}

Roll d% to determine whether the precipitation is fog (01–30), rain/snow (31–90), or sleet/hail
(91–00). Snow and sleet occur only when the temperature is 30° Fahrenheit or below. Most
precipitation lasts for 2d4 hours. By contrast, hail lasts for only 1d20 minutes but usually
accompanies 1d4 hours of rain.

## Storm (Duststorm/Snowstorm/Thunderstorm) {#storm-duststorm-snowstorm-thunderstorm}

Wind speeds are severe (30 to 50 mph) and visibility is cut by three-quarters. Storms last for 2d4–1
hours. See Storms, below, for more details.

## Warm {#warm}

Between 60° and 85° Fahrenheit during the day, 10 to 20 degrees colder at night.

## Windy {#windy}

Wind speeds are moderate to strong (10 to 30 mph); see Table: Wind Effects.

## Rain, Snow, Sleet, and Hail {#rain-snow-sleet-and-hail}

Bad weather frequently slows or halts travel and makes it virtually impossible to navigate from one
spot to another. Torrential downpours and blizzards obscure vision as effectively as a dense fog.

Most precipitation is rain, but in cold conditions it can manifest as snow, sleet, or hail.
Precipitation of any kind followed by a cold snap in which the temperature dips from above freezing
to 30° F or below might produce ice.

### Rain {#rain}

Rain reduces visibility ranges by half, resulting in a –4 penalty on Perception checks. It has the
same effect on flames, ranged weapon attacks, and Perception checks as severe wind.

### Snow {#snow}

Falling snow has the same effects on visibility, ranged weapon attacks, and skill checks as rain,
and it costs 2 squares of movement to enter a snow-covered square. A day of snowfall leaves 1d6
inches of snow on the ground.

### Heavy Snow {#heavy-snow}

Heavy snow has the same effects as normal snowfall but also restricts visibility as fog does (see
Fog). A day of heavy snow leaves 1d4 feet of snow on the ground, and it costs 4 squares of movement
to enter a square covered with heavy snow. Heavy snow accompanied by strong or severe winds might
result in snowdrifts 1d4 × 5 feet deep, especially in and around objects big enough to deflect the
wind—a cabin or a large tent, for instance. There is a 10% chance that a heavy snowfall is
accompanied by lightning (see Thunderstorm). Snow has the same effect on flames as moderate wind.

### Sleet {#sleet}

Essentially frozen rain, sleet has the same effect as rain while falling (except that its chance to
extinguish protected flames is 75%) and the same effect as snow once on the ground.

### Hail {#hail}

Hail does not reduce visibility, but the sound of falling hail makes sound-based Perception checks
more difficult (–4 penalty). Sometimes (5% chance) hail can become large enough to deal 1 point of
lethal damage (per storm) to anything in the open. Once on the ground, hail has the same effect on
movement as snow.

## Storms {#storms}

The combined effects of precipitation (or dust) and wind that accompany all storms reduce visibility
ranges by three-quarters, imposing a –8 penalty on Perception checks. Storms make ranged weapon
attacks impossible, except for those using siege weapons, which have a –4 penalty on attack rolls.
They automatically extinguish candles, torches, and similar unprotected flames. They cause protected
flames, such as those of lanterns, to dance wildly and have a 50% chance to extinguish these lights.
See Table: Wind Effects for possible consequences to creatures caught outside without shelter during
such a storm. Storms are divided into the following three types.

### Duststorm {#duststorm}

::: statblock
Abbrev: CR 3
:::

These desert storms differ from other storms in that they have no precipitation. Instead, a
duststorm blows fine grains of sand that obscure vision, smother unprotected flames, and can even
choke protected flames (50% chance). Most duststorms are accompanied by severe winds and leave
behind a deposit of 1d6 inches of sand. There is a 10% chance for a greater duststorm to be
accompanied by windstorm-magnitude winds (see Table: Wind Effects). These greater duststorms deal
1d3 points of nonlethal damage each round to anyone caught out in the open without shelter and also
pose a choking hazard (see Drowning, except that a character with a scarf or similar protection
across her mouth and nose does not begin to choke until after a number of rounds equal to 10 + her
Constitution score). Greater duststorms leave 2d3–1 feet of fine sand in their wake.

### Snowstorm {#snowstorm}

In addition to the wind and precipitation common to other storms, snowstorms leave 1d6 inches of
snow on the ground afterward.

### Thunderstorm {#thunderstorm}

In addition to wind and precipitation (usually rain, but sometimes also hail), thunderstorms are
accompanied by lightning that can pose a hazard to characters without proper shelter (especially
those in metal armor). As a rule of thumb, assume one bolt per minute for a 1-hour period at the
center of the storm. Each bolt causes between 4d8 and 10d8 points of electricity damage. One in 10
thunderstorms is accompanied by a tornado.

### Powerful Storms {#powerful-storms}

Very high winds and torrential precipitation reduce visibility to zero, making Perception checks and
all ranged weapon attacks impossible. Unprotected flames are automatically extinguished, and
protected flames have a 75% chance of being doused. Creatures caught in the area must make a
Fortitude save or face the effects based on the size of the creature (see Table: Wind Effects).
Powerful storms are divided into the following four types.

#### Windstorm {#windstorm}

While accompanied by little or no precipitation, windstorms can cause considerable damage simply
through the force of their winds.

#### Blizzard {#blizzard}

The combination of high winds, heavy snow (typically 1d3 feet), and bitter cold make blizzards
deadly for all who are unprepared for them.

#### Hurricane {#hurricane}

In addition to very high winds and heavy rain, hurricanes are accompanied by floods. Most
adventuring activity is impossible under such conditions.

#### Tornado {#tornado}

In addition to incredibly high winds, tornadoes can severely injure and kill those that get pulled
into their funnels.

## Fog {#fog}

Whether in the form of a low-lying cloud or a mist rising from the ground, fog obscures all sight
beyond 5 feet, including [darkvision](ref/rule/darkvision). Creatures 5 feet away have concealment
(attacks by or against them have a 20% miss chance).

## Winds {#winds}

The wind can create a stinging spray of sand or dust, fan a large fire, keel over a small boat, and
blow gases or vapors away. If powerful enough, it can even knock characters down (see Table: Wind
Effects), interfere with ranged attacks, or impose penalties on some skill checks.

### Table: Wind Effects {#table-wind-effects}

::: table
caption = "Table: Wind Effects"
head = [
  [
    { text = "Wind Force", header = true },
    { text = "Wind Speed", header = true },
    { text = "Ranged Attacks Normal/Siege Weapons^1^", header = true },
    { text = "Checked Size^2^", header = true },
    { text = "Blown Away Size", header = true },
    { text = "Fly Penalty", header = true },
  ],
]
body = [
  [
    { text = "Light" },
    { text = "0–10 mph" },
    { text = "—/—" },
    { text = "—" },
    { text = "—" },
    { text = "—" },
  ],
  [
    { text = "Moderate" },
    { text = "11–20 mph" },
    { text = "—/—" },
    { text = "—" },
    { text = "—" },
    { text = "—" },
  ],
  [
    { text = "Strong" },
    { text = "21–30 mph" },
    { text = "–2/—" },
    { text = "Tiny" },
    { text = "—" },
    { text = "–2" },
  ],
  [
    { text = "Severe" },
    { text = "31–50 mph" },
    { text = "–4/—" },
    { text = "Small" },
    { text = "Tiny" },
    { text = "–4" },
  ],
  [
    { text = "Windstorm" },
    { text = "51–74 mph" },
    { text = "Impossible/–4" },
    { text = "Medium" },
    { text = "Small" },
    { text = "–8" },
  ],
  [
    { text = "Hurricane" },
    { text = "75–174 mph" },
    { text = "Impossible/–8" },
    { text = "Large" },
    { text = "Medium" },
    { text = "–12" },
  ],
  [
    { text = "Tornado" },
    { text = "175–300 mph" },
    { text = "Impossible/impossible" },
    { text = "Huge" },
    { text = "Large" },
    { text = "–16" },
  ],
]
foot = [
  [
    { text = "1 The siege weapon category includes ballista and catapult attacks as well as boulders tossed by giants.", colspan = 6 },
  ],
  [
    { text = "_2 Checked Size_: Creatures of this size or smaller are unable to move forward against the force of the wind unless they succeed on a DC 10 Strength check (if on the ground) or a DC 20 Fly skill check if airborne.", colspan = 6 },
  ],
  [
    { text = "_3 Blown Away Size_: Creatures on the ground are knocked prone and rolled 1d4 × 10 feet, taking 1d4 points of nonlethal damage per 10 feet, unless they make a DC 15 Strength check. Flying creatures are blown back 2d6 × 10 feet and take 2d6 points of nonlethal damage due to battering and buffeting, unless they succeed on a DC 25 Fly skill check.", colspan = 6 },
  ],
]
:::

### Light Wind {#light-wind}

A gentle breeze, having little or no game effect.

### Moderate Wind {#moderate-wind}

A steady wind with a 50% chance of extinguishing small, unprotected flames, such as candles.

### Strong Wind {#strong-wind}

Gusts that automatically extinguish unprotected flames (candles, torches, and the like). Such gusts
impose a –2 penalty on ranged attack rolls and on Perception checks.

### Severe Wind {#severe-wind}

In addition to automatically extinguishing any unprotected flames, winds of this magnitude cause
protected flames (such as those of lanterns) to dance wildly and have a 50% chance of extinguishing
these lights. Ranged weapon attacks and Perception checks are at a –4 penalty. This is the velocity
of wind produced by a _[gust of wind](ref/spell/gust-of-wind)_ spell.

### Windstorm {#windstorm-2}

Powerful enough to bring down branches if not whole trees, windstorms automatically extinguish
unprotected flames and have a 75% chance of blowing out protected flames, such as those of lanterns.
Ranged weapon attacks are impossible, and even siege weapons have a –4 penalty on attack rolls.
Perception checks that rely on sound are at a –8 penalty due to the howling of the wind.

### Hurricane-Force Wind {#hurricane-force-wind}

All flames are extinguished. Ranged attacks are impossible (except with siege weapons, which have a
–8 penalty on attack rolls). Perception checks based on sound are impossible: all characters can
hear is the roaring of the wind. Hurricane-force winds often fell trees.

### Tornado {#tornado-2}

::: statblock
Abbrev: CR 10
:::

All flames are extinguished. All ranged attacks are impossible (even with siege weapons), as are
sound-based Perception checks. Instead of being blown away (see Table: Wind Effects), characters in
close proximity to a tornado who fail their Fortitude saves are sucked toward the tornado. Those who
come in contact with the actual funnel cloud are picked up and whirled around for 1d10 rounds,
taking 6d6 points of damage per round, before being violently expelled (falling damage might apply).
While a tornado's rotational speed can be as great as 300 mph, the funnel itself moves forward at an
average of 30 mph (roughly 250 feet per round). A tornado uproots trees, destroys buildings, and
causes similar forms of major destruction.
