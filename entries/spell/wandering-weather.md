+++
id = "ref/spell/wandering-weather"
kind = "spell"
title = "Wandering Weather"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wandering_weather", path = "json/spells12.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/control-weather" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Druid", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "10 minutes; see text"
components = "V, S"
range = "2 miles"
effects = [
  { label = "Area", value = "2-mile-radius circle, centered on you; see text" },
]
duration = "4d12 hours; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Cleric, Druid, Oracle, Shaman, Sorcerer, Witch, Wizard
Casting time: 10 minutes; see text
Components: V, S
Range: 2 miles
Duration: 4d12 hours; see text
Saving throw: none
Spell resistance: no
Area: 2-mile-radius circle, centered on you; see text
:::

## Control Weather

**Sources:** PRPG Core Rulebook pg 261

You change the weather in the local area. It takes 10 minutes to cast the spell and an additional 10
minutes for the effects to manifest. You can call forth weather appropriate to the climate and
season of the area you are in. You can also use this spell to cause the weather in the area to
become calm and normal for the season.

|Season|Possible Weather|
| --- | --- |
|Spring|Tornado, thunderstorm, sleet storm, or hot weather|
|Summer|Torrential rain, heat wave, or hailstorm|
|Autumn|Hot or cold weather, fog, or sleet|
|Winter|Frigid cold, blizzard, or thaw|
|Late winter|Hurricane-force winds or early spring|

You control the general tendencies of the weather, such as the direction and intensity of the wind.
You cannot control specific applications of the weather-where lightning strikes, for example, or the
exact path of a tornado. The weather continues as you left it for the duration, or until you use a
standard action to designate a new kind of weather (which fully manifests itself 10 minutes later).
Contradictory conditions are not possible simultaneously.

Control weather can do away with atmospheric phenomena (naturally occurring or otherwise) as well as
create them.

A druid casting this spell doubles the duration and affects a circle with a 3-mile radius.

### Mythic Control Weather

**Sources:** Mythic Adventures pg 89

The casting time changes to 1 standard action, and the duration doubles. The weather changes after a
number of rounds equal to 11 - your tier.

_Augmented (6th):_ If you expend two uses of mythic power, you can create weather of any type
regardless of the season, and the weather changes after 1 round.

### Wandering Weather

**Sources:** Ultimate Wilderness pg 237

This spell functions as [control weather](ref/spell/control-weather) except you can opt for the
weather to remain centered on you as you move.
