+++
id = "ref/rule/temperature-variations"
kind = "rule"
title = "Temperature Variations"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "temperature_variations", path = "json/rules_adv_gm04.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Wilderness pg 166

Weather is constantly changing, and a significant aspect of that change is the temperature. For the
purposes of this system, it's easiest to assume that the daily temperature remains relatively static
during daylight hours and then drops by 2d6+3 degrees during the night.

When setting a day's temperature in a terrain, you can roll on the temperature variations table
appropriate to the climate; the result determines how you should alter the adjusted baseline
temperature, and also suggests the duration of that change. You can also use the tables without
rolling for a result, consulting them as a guide to help you make decisions about variations in
temperature.

For terrain in a cold region, roll on Table 4-15: Cold Region Temperature Variations. Temperature
variations in this climate trend colder and last for a long period of time. For terrain in a
temperate region, roll on Table 4-16: Temperate Region Temperature Variations. Temperature
variations in this climate are about as likely to swing warmer or colder, and such variations tend
to last for shorter periods. If you need to establish a day's temperature for terrain in a temperate
region, you can roll on Table 4-17: Tropical Region Temperature Variations. Temperature variations
for tropical climates trend warm but for even shorter periods.

### Table 4-15: Cold Region Temperature Variations

|d%|Variation|Duration|
| --- | --- | --- |
|01-20|-3d10° F|1d4 days|
|21-40|-2d10° F|1d6+1 days|
|41-60|-1d10° F|1d6+2 days|
|61-80|No variation|1d6+2 days|
|81-95|+1d10° F|1d6+1 days|
|96-99|+2d10° F|1d4 days days|
|100|+3d10° F|1d2 days days|

### Table 4-16: Temperate Region Temperature Variations

|d%|Variation|Duration|
| --- | --- | --- |
|01-05|-3d10° F|1d2 days|
|06-15|-2d10° F|1d4 days|
|16-35|-1d10° F|1d6+1 days|
|36-65|No variation|1d6+1 days|
|66-85|+1d10° F|1d6+1 days|
|86-95|+2d10° F|1d4 days days|
|96-100|+3d10° F|1d2 days days|

### Table 4-17: Tropical Region Temperature Variations

|d%|Variation|Duration|
| --- | --- | --- |
|01-10|-2d10° F|1d2 days|
|11-25|-1d10° F|1d2 days|
|26-55|No variation|1d4 days|
|56-85|+1d10° F|1d4 days|
|86-100|+2d10° F|1d2 days days|
