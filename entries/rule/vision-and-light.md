+++
id = "ref/rule/vision-and-light"
kind = "rule"
title = "Vision and Light"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vision_and_light", path = "json/rules_basics04.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 172

Dwarves and half-orcs have [darkvision](ref/rule/darkvision), but other races need light to see by.
See Table 7-10 for the radius that a light source illuminates and how long it lasts. The increased
entry indicates an area outside the lit radius in which the light level is increased by one step
(from darkness to dim light, for example).

In an area of **bright light** all characters can see clearly. Some creatures, such as those with
[light sensitivity](ref/umr/light-sensitivity) and [light blindness](ref/umr/light-blindness), take
penalties while in areas of bright light. A creature can't use Stealth in an area of bright light
unless it is invisible or has cover. Areas of bright light include outside in direct sunshine and
inside the area of a daylight spell.

**Normal light** functions just like bright light, but characters with light sensitivity and light
blindness do not take penalties. Areas of normal light include underneath a forest canopy during the
day, within 20 feet of a torch, and inside the area of a light spell.

In an area of **dim light** a character can see somewhat. Creatures within this area have
concealment (20% miss chance in combat) from those without [darkvision](ref/rule/darkvision) or the
ability to see in darkness. A creature within an area of dim light can make a Stealth check to
conceal itself. Areas of dim light include outside at night with a moon in the sky, bright
starlight, and the area between 20 and 40 feet from a torch.

In areas of darkness, creatures without [darkvision](ref/rule/darkvision) are effectively blinded.
In addition to the obvious effects, a blinded creature has a 50% miss chance in combat (all
opponents have [total concealment](ref/rule/concealment)), loses any Dexterity bonus to AC, takes a
-2 penalty to AC, and takes a -4 penalty on Perception checks that rely on sight and most Strength-
and Dexterity-based skill checks. Areas of darkness include an unlit dungeon chamber, most caverns,
and outside on a cloudy, moonless night.

Characters with [low-light vision](ref/rule/low-light-vision) (elves, gnomes, and half-elves) can
see objects twice as far away as the given radius. Double the effective radius of bright light,
normal light, and dim light for such characters.

Characters with [darkvision](ref/rule/darkvision) (dwarves and half-orcs) can see lit areas normally
as well as dark areas within 60 feet. A creature can't hide within 60 feet of a character with
darkvision unless it is invisible or has cover.

### Table 7-10: Light Sources and Illumination

|Object/Spell|Normal|Increased|Duration|
| --- | --- | --- | --- |
|Candle|n/a^[1](ref/rule/vision-and-light#footnote-1)^|5 ft.|1 hr.|
|Everburning torch|20 ft.|40 ft.|Permanent|
|Lamp, common|15 ft.|30 ft.|6 hr./pint|
|Lantern, bullseye|60-ft. cone|120-ft. cone|6 hr./pint|
|Lantern, hooded|30 ft.|60 ft.|6 hr./pint|
|Sunrod|30 ft.|60 ft.|6 hr.|
|Torch|20 ft.|40 ft.|1 hr.|
|[Continual flame](ref/spell/continual-flame)|20 ft.|40 ft.|Permanent|
|[Dancing lights](ref/spell/dancing-lights) (torches)|20 ft. (each)|40 ft. (each)|1 min.|
|[Daylight](ref/spell/daylight)|60 ft.^[2](ref/rule/vision-and-light#footnote-2)^|120 ft.|10 min./level|
|[Light](ref/spell/light)|20 ft.|40 ft.|10 min./level|

###### ^1^ {#footnote-1}

A candle does not provide normal illumination, only dim light.

###### ^2^ {#footnote-2}

The light for a daylight spell is bright light.
