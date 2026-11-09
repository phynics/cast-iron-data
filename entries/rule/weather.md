+++
id = "ref/rule/weather"
kind = "rule"
title = "Weather"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "weather", path = "json/rules_gm08.json" },
]
[[sources]]
publication = "core-rulebook"
page = "437"

[fields]
kind = "none"
+++

Weather can play an important role in an adventure.

Table 13-9 can be used as a simple local weather table. Terms on that table are defined as follows.

**Calm:** Wind speeds are light (0 to 10 mph).

**Cold:** Between 0° and 40° Fahrenheit during the day, 10 to 20 degrees colder at night.

**Cold Snap:** Lowers temperature by -10° F.

**Downpour:** Treat as rain (see Precipitation, below), but conceals as fog. Can create floods. A
downpour lasts for 2d4 hours.

**Heat Wave:** Raises temperature by +10° F.

**Hot:** Between 85° and 110° Fahrenheit during the day, 10 to 20 degrees colder at night.

**Moderate:** Between 40° and 60° Fahrenheit during the day, 10 to 20 degrees colder at night.

**Powerful Storm (Windstorm/Blizzard/Hurricane/Tornado):** Wind speeds are over 50 mph (see
[Table 13-10](ref/rule/winds). In addition, blizzards are accompanied by heavy snow (1d3 feet), and
hurricanes are accompanied by downpours. Windstorms last for 1d6 hours. Blizzards last for 1d3 days.
Hurricanes can last for up to a week, but their major impact on characters comes in a 24-to-48-hour
period when the center of the storm moves through their area. Tornadoes are very short-lived (1d6 ×
10 minutes), typically forming as part of a thunderstorm system.

**Precipitation:** Roll d% to determine whether the precipitation is fog (01-30), rain/snow (31-90),
or sleet/hail (91-00). Snow and sleet occur only when the temperature is 30° Fahrenheit or below.
Most precipitation lasts for 2d4 hours. By contrast, hail lasts for only 1d20 minutes but usually
accompanies 1d4 hours of rain.

**Storm (Duststorm/Snowstorm/Thunderstorm):** Wind speeds are severe (30 to 50 mph) and visibility
is cut by three-quarters. Storms last for 2d4-1 hours. See [Storms](ref/rule/storms) for more
details.

**Warm:** Between 60° and 85° Fahrenheit during the day, 10 to 20 degrees colder at night.

**Windy:** Wind speeds are moderate to strong (10 to 30 mph); see [Table 13-10](ref/rule/winds).

### Table 13-9: Random Weather

|d%|Weather|Cold Climate|Temperate Climate^[1](ref/rule/weather#footnote-1)^|Desert|
| --- | --- | --- | --- | --- |
|01-70|Normal weather|Cold, calm|Normal for season^[2](ref/rule/weather#footnote-2)^|Hot, calm|
|71-80|Abnormal weather|Heat wave (01-30) or cold snap (31-100)|Heat wave (01-50) or cold snap (51-100)|Hot, windy|
|81-90|Inclement weather|Precipitation (snow)|Precipitation (normal for season)|Hot, windy|
|91-99|Storm|Snowstorm|Thunderstorm, snowstorm|Duststorm|
|100|Powerful storm|Blizzard|Windstorm, blizzard, hurricane, tornado|Downpour|

###### ^1^ {#footnote-1}

Temperate includes forests, hills, marshes, mountains, plains, and warm aquatic environments.

###### ^2^ {#footnote-2}

Winter is cold, summer is warm, spring and autumn are temperate. Marsh regions are slightly warmer
in winter.
