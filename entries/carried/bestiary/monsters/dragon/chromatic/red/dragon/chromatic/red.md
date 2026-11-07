+++
id = "ref/carried/bestiary/monsters/dragon/chromatic/red/dragon/chromatic/red"
kind = "creature"
title = "Dragon, Chromatic, Red"
source_ids = ["bestiary"]
section = ["Monsters", "Dragon", "Chromatic", "Red"]
tags = ["dragon", "fire", "small"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Bestiary/Monsters/Dragon/Chromatic/Red/Dragon/Chromatic/Red", path = "bestiary/creature/dragon_chromatic_red.json" },
]

[fields]
kind = "creature"
cr = "6"
creature_type = "dragon"
subtypes = ["fire"]
size = "Small"
alignment = "CE"
abilities = ["17", "14", "15", "10", "11", "10"]
+++

::: statblock
CR: 6
Alignment: CE
Size: Small
Type: dragon (fire)
Hit Dice: 7d12
Speed: 40 ft.
Ability Scores: Str 17, Dex 14, Con 15, Int 10, Wis 11, Cha 10
Environment: warm mountains
Organization: solitary
Treasure: triple
Natural Armor: +6
Breath Weapon: cone, 2d10 fire
:::

## Special Abilities {#special-abilities}

### Fire Aura {#fire-aura}

::: statblock
Ability Type: Supernatural
:::

An adult red dragon is surrounded by an aura of intense heat. All creatures within 5 feet take 1d6
points of fire damage at the beginning of the dragon's turn. An old dragon's aura extends to 10
feet. An ancient dragon's damage increases to 2d6.

### Incinerate {#incinerate}

::: statblock
Ability Type: Supernatural
:::

A great wyrm red dragon can incinerate creatures in its fiery breath. A creature reduced to fewer
than 0 hit points by its breath weapon must make a Fortitude save (using the breath weapon's DC).
Failure indicates that the creature is reduced to ash. Creatures destroyed in this way can only be
restored to life through true resurrection or similar magic.

### Manipulate Flames {#manipulate-flames}

::: statblock
Ability Type: Supernatural
:::

An old or older red dragon can control any fire spell within 10 feet per age category of the dragon
as a standard action. This ability allows it to move any fire effect in the area, as if it were the
caster. This ability also allows it to reposition a stationary fire effect, although the new
placement must be one allowed by the spell. Finally, for 1 round following the use of this ability,
the dragon can control any new fire spell cast within its area of control, as if it were the caster.
It can make all decisions allowed to the caster, including canceling the spell if it so desires.

### Melt Stone {#melt-stone}

::: statblock
Ability Type: Supernatural
:::

An ancient or older red dragon can use its breath weapon to melt rock at a range of 100 feet,
affecting a 5-foot-radius area per age category. The area becomes lava to a depth of 1 foot. Any
creature in contact with the lava takes 20d6 points of fire damage on the first round, 10d6 on the
second, and none thereafter as the lava hardens and cools. If used on a wall or ceiling, treat this
ability as an avalanche that deals fire damage.

### Smoke Vision {#smoke-vision}

::: statblock
Ability Type: Extraordinary
:::

A very young red dragon can see perfectly in smoky conditions (such as those created by
pyrotechnics).

### Spell-Like Abilities {#spell-like-abilities}

::: statblock
Ability Type: Spell-Like
:::

A red dragon gains the following [spell-like abilities](ref/umr/spell-like-abilities), usable at
will upon reaching the listed age category. Young—detect magic; Juvenile—pyrotechnics;
Adult—suggestion; Old—wall of fire; Ancient—find the path; Great wyrm—discern location.

## Age Category {#age-category}

|Age Category|Special Abilities|Caster Level|
| --- | --- | --- |
|Wyrmling|Fire subtype|—|
|Very young|Smoke vision|—|
|Young|_[Detect magic](ref/spell/detect-magic)_|1st|
|Juvenile|Frightful presence, _[pyrotechnics](ref/spell/pyrotechnics)_|3rd|
|Young adult|DR 5/magic, [spell resistance](ref/rule/spell-resistance)|5th|
|Adult|Fire aura, _[suggestion](ref/spell/suggestion)_|7th|
|Mature adult|DR 10/magic|9th|
|Old|Manipulate flames, _[wall of fire](ref/spell/wall-of-fire)_|11th|
|Very old|DR 15/magic|13th|
|Ancient|Melt stone, _[find the path](ref/spell/find-the-path)_|15th|
|Wyrm|DR 20/magic|17th|
|Great wyrm|Incinerate, _[discern location](ref/spell/discern-location)_|19th|
