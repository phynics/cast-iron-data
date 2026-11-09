+++
id = "ref/rule/precipitation"
kind = "rule"
title = "Precipitation"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "precipitation", path = "json/rules_adv_gm04.json" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "167"

[fields]
kind = "none"
+++

The next step in setting the local weather is to determine whether precipitation occurs and the
intensity of that precipitation, if any.

**Precipitation Frequency:** Precipitation frequency is organized into five levels: drought, rare,
intermittent, common, and constant. A region's baseline precipitation frequency is set by the
season, but it can be modified by the climate and other factors. A precipitation frequency can't be
reduced lower than drought or increased higher than constant. Check each day to determine whether
precipitation occurs for that day; the percentage chance of precipitation occurring is summarized on
Table 4-18: Daily Precipitation Chances.

**Precipitation Intensity:** The baseline precipitation intensity is dependent on the elevation and
can be modified by the climate. Intensity has four categories. Light precipitation is the lowest
level of intensity and generally consists of fog, a faint drizzle of rain or a few isolated flakes
of snow. Medium precipitation represents a noticeable but not distracting fall of rain or snow.
Heavy precipitation typically consists of a driving rainstorm or significant snowfall. Torrential
precipitation is the highest level of intensity and consists of a deluge of rain or snow with
conditions that can approach whiteout levels. Precipitation intensity can never be reduced below
light or increased above torrential.

### Table 4-18: Daily Precipitation Chances

|Frequency|Chance of Precipitation|
| --- | --- |
|Drought|5% (decrease precipitation intensity by 2 steps)|
|Rare|15%|
|Intermittent|30%|
|Common|60%|
|Constant|95%|

Once you establish the intensity and the temperature, you'll determine how the precipitation
manifests.

**Precipitation Form:** Precipitation can result in more than just rain. Depending upon the
intensity and temperature, precipitation can range from a light fog or a faint drizzle of rain to a
blizzard or thunderstorm. Once you know precipitation of a specific intensity is occurring, set the
time of day the precipitation event occurs by rolling 1d12 to find the starting hour of the day and
1d6 to determine whether the hour is am or pm (1-3 = am, 4-6 = pm).

Next, use the appropriate table below for the baseline precipitation intensity and whether the
temperature is above or below freezing (32° F) to generate the specific type of precipitation and
its duration. (Remember that the temperature is lower at night!) See the
[Cloud Cover](ref/rule/cloud-cover) section for the effects of precipitation on visibility for
flying creatures.

### Precipitation Forms

**Drizzle:** Drizzle reduces visibility to three-quarters of the normal range, imposing a -2 penalty
on Perception checks. It automatically extinguishes tiny unprotected flames (candles and the like,
but not torches).

**Fog, Light:** Light fog reduces visibility to three-quarters of the normal ranges, resulting in a
-2 penalty on Perception checks and a -2 penalty on ranged attacks. Light fog typically occurs early
in the day, late in the day, or sometimes at night, but the heat of the midday usually burns it
away. Light fog occurs only when there is no or light wind.

**Fog, Medium:** Medium fog reduces visibility ranges by half, resulting in a -4 penalty on
Perception checks and a -4 penalty on ranged attacks. Medium fog typically occurs early in the day,
late in the day, or sometimes at night, but the heat of the midday usually burns it away. Medium fog
occurs only when there is no or light wind.

**Fog, Heavy:** Heavy fog obscures all vision beyond 5 feet, including
[darkvision](ref/rule/darkvision). Creatures 5 feet away have [concealment](ref/rule/concealment).
Heavy fog typically occurs early in the day, late in the day, or sometimes at night, but the heat of
the midday usually burns it away. Heavy fog occurs only when there is no or light wind.

**Rain:** Rain reduces visibility ranges by half, resulting in a -4 penalty on Perception checks.
Rain automatically extinguishes unprotected flames (candles, torches, and the like) and imposes a -4
penalty on ranged attacks.

### Table 4-19: Light Unfrozen Precipitation

|d%|Precipitation|Duration|
| --- | --- | --- |
|01-20|Light fog|1d8 hours|
|21-40|Medium fog|1d6 hours|
|41-50|Drizzle|1d4 hours|
|51-75|Drizzle|2d12 hours|
|76-90|Light rain|1d4 hours|
|91-100|Light rain (sleet if below 40° F)|1 hour|

### Table 4-21: Medium Unfrozen Precipitation

|d%|Precipitation|Duration|
| --- | --- | --- |
|01-10|Medium fog|1d8 hours|
|11-20|Medium fog|1d12 hours|
|21-30|Heavy fog|1d4 hours|
|31-35|Rain|1d4 hours|
|36-70|Rain|1d8 hours|
|71-90|Rain|2d12 hours|
|91-100|Rain (sleet if below 40° F)|1d4 hours|

**Rain, Heavy:** Heavy rain reduces visibility to one-quarter of the normal range, resulting in a -6
penalty on Perception checks. Heavy rain automatically extinguishes unprotected flames and imposes a
-6 penalty on ranged attacks.

### Table 4-23: Heavy Unfrozen Precipitation

|d%|Precipitation|Duration|
| --- | --- | --- |
|01-10|Heavy fog|1d8 hours|
|11-20|Heavy fog|2d6 hours|
|21-50|Heavy rain|1d12 hours|
|51-70|Heavy rain|2d12 hours|
|71-85|Heavy rain (sleet if below 40° F)|1d8 hours|
|86-90|Thunderstorm|1 hour|
|91-100|Thunderstorm|1d3 hours|

**Sleet:** Essentially frozen rain, sleet has the same effect as light snow, but any accumulation
typically doesn't last longer than 1-2 hours after the storm.

**Snow, Light:** Light snow reduces visibility to three-quarters of the normal range, resulting in a
-2 penalty on Perception checks. Light snow has a 75% chance each hour of extinguishing unprotected
flames and imposes a -2 penalty on ranged attacks. Light snow does not impede movement unless it
continues for 2 or more hours, at which point moving into a square of such snow requires 1 extra
5-foot square of movement (this stacks with difficult terrain). Every 2 hours of light snow leaves 1
inch of snow on the ground. As long as at least 2 inches of snow remain on the ground, the
requirement of an extra square of movement to enter a square of snow persists. If at least 1 foot of
snow remains on the ground, entering a snow-filled square instead requires 2 extra squares of
movement.

### Table 4-20: Light Frozen Precipitation

|d%|Precipitation|Duration|
| --- | --- | --- |
|01-20|Light fog|1d6 hours|
|21-40|Light fog|1d8 hours|
|41-50|Medium fog|1d4 hours|
|51-60|Light snow|1 hour|
|61-75|Light snow|1d4 hours|
|76-100|Light snow|2d12 hours|

**Snow, Medium:** Medium snow reduces visibility ranges by half, resulting in a -4 penalty on
Perception checks. Medium snow extinguishes unprotected flames and imposes a -4 penalty on ranged
attacks. Medium snow does not impede movement unless it continues for 1 hour, at which point moving
into a square of such snow requires 1 extra 5-foot square of movement (this stacks with difficult
terrain). Every hour of medium snow leaves 1 inch of snow on the ground. As long as at least 2
inches of snow remain on the ground, the requirement of an extra square of movement to enter a
square of snow persists. If at least 1 foot of snow remains on the ground, entering a snow-filled
square instead requires 2 extra squares of movement.

### Table 4-22: Medium Frozen Precipitation

|d%|Precipitation|Duration|
| --- | --- | --- |
|01-10|Medium fog|1d6 hours|
|11-20|Medium fog|1d8 hours|
|21-30|Heavy fog|1d4 hours|
|31-50|Medium snow|1d4 hours|
|51-90|Medium snow|1d8 hours|
|91-100|Medium snow|2d12 hours|

**Snow, Heavy:** Heavy snow reduces visibility ranges to one-quarter of the normal range, resulting
in a -6 penalty on Perception checks. It extinguishes unprotected flames and imposes a -6 penalty on
ranged attacks. Heavy snow impedes movement even before it begins to stick. Moving into a square
during a heavy snowstorm requires 1 extra 5-foot square of movement (this stacks with difficult
terrain). Every hour of heavy snow leaves 1d4 inches of snow on the ground. As long as at least 2
inches of snow remain on the ground, the requirement of an extra square of movement to enter a
square of snow persists. If at least 1 foot of snow remains on the ground, 2 extra squares of
movement are required to enter a snow-filled square instead. A heavy snowstorm has a 10% chance of
generating [thundersnow](ref/rule/severe-events) and has a 40% chance of becoming a blizzard if the
wind speed is severe or stronger.

### Table 4-24: Heavy Frozen Precipitation

|d%|Precipitation|Duration|
| --- | --- | --- |
|01-10|Medium fog|1d8 hours|
|11-20|Heavy fog|2d6 hours|
|21-60|Light snow|2d12 hours|
|61-90|Medium snow|1d8 hours|
|91-100|Heavy snow|1d6 hours|

**Thunderstorm:** Thunderstorms feature [powerful winds](ref/rule/winds) and heavy rain. To
determine the type of wind associated with the thunderstorm, roll on Table 4-27: Thunderstorm Winds.

In addition, there is a 40% chance that a thunderstorm features [hail](ref/rule/severe-events)
either up to an hour before or during the storm. An even greater danger presented by a thunderstorm
is the lightning that occurs during the storm. These electrical discharges, generated by the roiling
clouds, can pose a hazard to creatures that do not have proper shelters, especially creatures clad
in metal armor. Every 10 minutes during a thunderstorm, a bolt of lightning strikes an unsheltered
creature at random (though this can strike wildlife as easily as PCs). A creature struck by this
lightning must succeed a DC 18 Reflex saving throw or take 10d8 points of electricity damage (a
successful saving throw halves the damage). Creatures in metal armor take a -4 penalty on the Reflex
saving throw.

There is a 10% chance that a thunderstorm with winds of windstorm strength also generates a
[tornado](ref/rule/severe-events), while thunderstorms with windstorm-strength winds in temperatures
higher than 85° F also have a 20% chance of being a precursor to a
[hurricane](ref/rule/severe-events). There is a 20% chance that a thunderstorm of any strength in
the desert also generates a [haboob](ref/rule/severe-events).

### Table 4-25: Torrential Unfrozen Precipitation

|d%|Precipitation|Duration|
| --- | --- | --- |
|01-05|Heavy fog|1d8 hours|
|06-10|Heavy fog|2d6 hours|
|11-30|Heavy rain|2d6 hours|
|31-60|Heavy rain|2d12 hours|
|61-80|Heavy rain (sleet if below 40° F)|2d6 hours|
|81-95|Thunderstorm|1d3 hours|
|96-100|Thunderstorm|1d6 hours|

### Table 4-26: Torrential Frozen Precipitation

|d%|Precipitation|Duration|
| --- | --- | --- |
|01-05|Heavy fog|1d8 hours|
|06-10|Heavy fog|2d6 hours|
|11-50|Heavy snow|1d4 hours|
|51-90|Heavy snow|1d8 hours|
|91-100|Heavy snow|2d12 hours|

### Table 4-27: Thunderstorm Winds

|d%|Thunderstorm Wind Strength|
| --- | --- |
|01-50|Strong winds|
|51-90|Severe winds|
|91-100|Windstorm|

### Deserts

Deserts are found in places where the weather must pass over mountains, causing a rain shadow, and
in very cold environments. The baseline precipitation frequency in a desert is usually drought, but
can be rare for a few weeks per year.
