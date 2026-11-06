+++
id = "ref/carried/mythic-adventures/monsters/aboleth/mythic"
kind = "creature"
title = "Aboleth, Mythic"
source_ids = ["mythic-adventures"]
section = ["Monsters", "Aboleth"]
tags = ["aberration", "aquatic", "mythic", "huge"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Mythic Adventures/Monsters/Aboleth/Mythic", path = "mythic_adventures/creature/mythic/aboleth_mythic.json" },
]

[fields]
kind = "creature"
cr = "9"
creature_type = "Aberration"
subtypes = ["aquatic", "mythic"]
size = "Huge"
alignment = "LE"
ac = "23, touch 9, flat-footed 22 (+1 Dex, +14 natural, -2 size)"
hp = "118 (9d8+78)"
fortitude = "+9"
reflex = "+6"
will = "+11"
melee = "4 tentacles +11 (1d8+5 plus slime)"
special_attacks = "mucus mist, mythic power (3/day, surge +1d6)"
special_qualities = "slime armor"
abilities = ["20", "12", "22", "15", "17", "19"]
+++

::: statblock
CR: 9
XP: 6,400
Alignment: LE
Size: Huge
Type: Aberration (aquatic, mythic)
Init: +8M
Senses: [darkvision](ref/rule/darkvision) 60 ft.; Perception +15
Aura: mucus cloud (5 feet)
AC: 23, touch 9, flat-footed 22 (+1 Dex, +14 natural, -2 size)
hp: 118 (9d8+78)
Fort: +9
Ref: +6
Will: +11
DR: 5/epic
Speed: 10 ft., swim 60 ft.
Melee: 4 tentacles +11 (1d8+5 plus slime)
Space: 15 ft.
Reach: 15 ft.
Special Attacks: mucus mist, mythic power (3/day, surge +1d6)
Spell-like abilities: (CL 16th; concentration +20)\
At will-_[hypnotic pattern](ref/spell/hypnotic-pattern)_ (DC 16), _[illusory wall](ref/spell/illusory-wall)_ (DC 18), _[mirage arcana](ref/spell/mirage-arcana)_ (DC 19), _[persistent image](ref/spell/persistent-image)_ (DC 19), _[programmed image](ref/spell/programmed-image)_ (DC 20), _[project image](ref/spell/project-image)_ (DC 21), _[veil](ref/spell/veil)_ (DC 20)\
3/day-_[dominate monster](ref/spell/dominate-monster)_ (DC 23)
Ability Scores: Str 20, Dex 12, Con 22, Int 15, Wis 17, Cha 19
Base Atk: +6
CMB: +13
CMD: 24
Feats: Combat Casting, Improved InitiativeM, Iron WillM, Lightning Reflexes, Weapon Focus (tentacle)
Skills: Bluff +13, Intimidate +16, Knowledge (any one) +14, Perception +15, Spellcraft +14, Swim +25
Languages: Aboleth, Aklo, Aquan, Undercommon
SQ: slime armor
Environment: any aquatic
Organization: solitary, pair, brood (3-6), or shoal (7-19)
Treasure: double
MR: 3
:::

_A foul mist surrounds this huge, three-eyed, tentacled fish creature, and plates of hardened slime
guard its body._

## Special Abilities {#special-abilities}

### Mucus Cloud {#mucus-cloud}

::: statblock
Ability Type: Extraordinary
:::

While underwater, an aboleth exudes a cloud of transparent slime. All creatures adjacent to an
aboleth must succeed at a DC 20 Fortitude save each round or lose the ability to breathe air (but
gain the ability to breathe water) for 3 hours. Renewed contact with an aboleth's mucus cloud and
failing another save extends the effect for another 3 hours. The save DC is Constitution-based.

### Mucus Mist {#mucus-mist}

::: statblock
Ability Type: Extraordinary
:::

When exposed to the air, a mythic aboleth can release its mucus as a fine mist. This obscures vision
like obscuring mist and has the same properties as its mucus cloud. Creatures that breathe water are
able to breathe normally while within the cloud. The mist moves with the aboleth.

### Slime {#slime}

::: statblock
Ability Type: Extraordinary
:::

A creature hit by an aboleth's tentacle must succeed at a DC 20 Fortitude save or its skin and flesh
transform into a clear, slimy membrane over the course of 1d4 rounds. The creature's new "flesh" is
soft and tender, reducing its Constitution score by 4 as long as the transformation persists. If the
creature's flesh isn't kept moist, it dries quickly and the victim takes 1d12 points of damage every
10 minutes. Remove disease and similar effects can restore an afflicted creature to normal, but
immunity to disease offers no protection from this attack. The save DC is Constitution-based.

### Slime Armor {#slime-armor}

::: statblock
Ability Type: Extraordinary
:::

A mythic aboleth can spend 1 minute to create an armorlike carapace from hardened slime. This gives
it a +4 armor bonus, reduces its swim speed to 30 feet, and increases its land speed to 30 feet. The
aboleth can dissolve the armor as a full-round action.

A mythic aboleth has exceptional magic, usually gained by staying alive long enough to see some of
its dark experiments through to fruition. Brooding and brilliant, it seeks to conquer the dry lands.
