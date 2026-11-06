+++
id = "ref/carried/core-rulebook/rules/additional-rules/exploration"
kind = "rule"
title = "Exploration"
source_ids = ["core-rulebook"]
section = ["Rules", "Additional Rules"]
parent = "ref/carried/core-rulebook/rules/additional-rules"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Rules/Additional Rules/Exploration", path = "core_rulebook/rules/additional_rules.json" },
]

[fields]
kind = "none"
+++

Few rules are as vital to the success of adventurers than those pertaining to vision, lighting, and
how to break things. Rules for each of these are explained below.

## Vision and Light {#vision-and-light}

Dwarves and half-orcs have [darkvision](ref/rule/darkvision), but the other races presented in Races
need light to see by. See Table: Light Sources and Illumination for the radius that a light source
illuminates and how long it lasts. The increased entry indicates an area outside the lit radius in
which the light level is increased by one step (from darkness to dim light, for example).

### Table: Light Sources and Illumination {#table-light-sources-and-illumination}

::: table
caption = "Table: Light Sources and Illumination"
head = [
  [
    { text = "Object", header = true },
    { text = "Normal", header = true },
    { text = "Increased", header = true },
    { text = "Duration", header = true },
  ],
  [
    { text = "Spell", header = true },
    { text = "Normal", header = true },
    { text = "Increase", header = true },
    { text = "Duration", header = true },
  ],
]
body = [
  [
    { text = "Candle" },
    { text = "n/a^1^" },
    { text = "5 ft." },
    { text = "1 hr." },
  ],
  [
    { text = "_Everburning torch_" },
    { text = "20 ft." },
    { text = "40 ft." },
    { text = "Permanent" },
  ],
  [
    { text = "Lamp, common" },
    { text = "15 ft." },
    { text = "30 ft." },
    { text = "6 hr./pint" },
  ],
  [
    { text = "Lantern, bullseye" },
    { text = "60-ft. cone" },
    { text = "120-ft. cone" },
    { text = "6 hr./pint" },
  ],
  [
    { text = "Lantern, hooded" },
    { text = "30 ft." },
    { text = "60 ft." },
    { text = "6 hr./pint" },
  ],
  [
    { text = "Sunrod" },
    { text = "30 ft." },
    { text = "60 ft." },
    { text = "6 hr." },
  ],
  [
    { text = "Torch" },
    { text = "20 ft." },
    { text = "40 ft." },
    { text = "1 hr." },
  ],
  [
    { text = "_[Continual flame](ref/spell/continual-flame)_" },
    { text = "20 ft." },
    { text = "40 ft." },
    { text = "Permanent" },
  ],
  [
    { text = "_[Dancing lights](ref/spell/dancing-lights)_ (torches)" },
    { text = "20 ft. (each)" },
    { text = "40 ft. (each)" },
    { text = "1 min." },
  ],
  [
    { text = "_[Daylight](ref/spell/daylight)_" },
    { text = "60 ft.^2^" },
    { text = "120 ft." },
    { text = "10 min./level" },
  ],
  [
    { text = "_[Light](ref/spell/light)_" },
    { text = "20 ft." },
    { text = "40 ft." },
    { text = "10 min./level" },
  ],
]
foot = [
  [
    { text = "^1^ A candle does not provide normal illumination, only dim illumination.", colspan = 4 },
  ],
  [
    { text = "^2^ The light for a daylight spell is bright light.", colspan = 4 },
  ],
]
:::

In an area of bright light, all characters can see clearly. Some creatures, such as those with light
sensitivity and light blindness, take penalties while in areas of bright light. A creature can't use
Stealth in an area of bright light unless it is invisible or has cover. Areas of bright light
include outside in direct sunshine and inside the area of a daylight spell.

Normal light functions just like bright light, but characters with light sensitivity and light
blindness do not take penalties. Areas of normal light include underneath a forest canopy during the
day, within 20 feet of a torch, and inside the area of a light spell.

In an area of dim light, a character can see somewhat. Creatures within this area have concealment
(20% miss chance in combat) from those without [darkvision](ref/rule/darkvision) or the ability to
see in darkness. A creature within an area of dim light can make a Stealth check to conceal itself.
Areas of dim light include outside at night with a moon in the sky, bright starlight, and the area
between 20 and 40 feet from a torch.

In areas of darkness, creatures without [darkvision](ref/rule/darkvision) are effectively blinded.
In addition to the obvious effects, a blinded creature has a 50% miss chance in combat (all
opponents have total concealment), loses any Dexterity bonus to AC, takes a –2 penalty to AC, and
takes a –4 penalty on Perception checks that rely on sight and most Strength- and Dexterity-based
skill checks. Areas of darkness include an unlit dungeon chamber, most caverns, and outside on a
cloudy, moonless night.

Characters with [low-light vision](ref/rule/low-light-vision) (elves, gnomes, and half-elves) can
see objects twice as far away as the given radius. Double the effective radius of bright light,
normal light, and dim light for such characters.

Characters with [darkvision](ref/rule/darkvision) (dwarves and half-orcs) can see lit areas normally
as well as dark areas within 60 feet. A creature can't hide within 60 feet of a character with
darkvision unless it is invisible or has cover.

## Breaking and Entering {#breaking-and-entering}

When attempting to break an object, you have two choices: smash it with a weapon or break it with
sheer strength.

### Table: Size and Armor Class of Objects {#table-size-and-armor-class-of-objects}

::: table
caption = "Table: Size and Armor Class of Objects"
head = [
  [
    { text = "Size", header = true },
    { text = "AC Modifier", header = true },
  ],
]
body = [
  [
    { text = "Colossal" },
    { text = "–8" },
  ],
  [
    { text = "Gargantuan" },
    { text = "–4" },
  ],
  [
    { text = "Huge" },
    { text = "–2" },
  ],
  [
    { text = "Large" },
    { text = "–1" },
  ],
  [
    { text = "Medium" },
    { text = "+0" },
  ],
  [
    { text = "Small" },
    { text = "+1" },
  ],
  [
    { text = "Tiny" },
    { text = "+2" },
  ],
  [
    { text = "Diminutive" },
    { text = "+4" },
  ],
  [
    { text = "Fine" },
    { text = "+8" },
  ],
]
:::

### Table: Substance Hardness and Hit Points {#table-substance-hardness-and-hit-points}

::: table
caption = "Table: Substance Hardness and Hit Points"
head = [
  [
    { text = "Substance", header = true },
    { text = "Hardness", header = true },
    { text = "Hit Points", header = true },
  ],
]
body = [
  [
    { text = "Glass" },
    { text = "1" },
    { text = "1/in. of thickness" },
  ],
  [
    { text = "Paper or cloth" },
    { text = "0" },
    { text = "2/in. of thickness" },
  ],
  [
    { text = "Rope" },
    { text = "0" },
    { text = "2/in. of thickness" },
  ],
  [
    { text = "Ice" },
    { text = "0" },
    { text = "3/in. of thickness" },
  ],
  [
    { text = "Leather or hide" },
    { text = "2" },
    { text = "5/in. of thickness" },
  ],
  [
    { text = "Wood" },
    { text = "5" },
    { text = "10/in. of thickness" },
  ],
  [
    { text = "Stone" },
    { text = "8" },
    { text = "15/in. of thickness" },
  ],
  [
    { text = "Iron or steel" },
    { text = "10" },
    { text = "30/in. of thickness" },
  ],
  [
    { text = "Mithral" },
    { text = "15" },
    { text = "30/in. of thickness" },
  ],
  [
    { text = "Adamantine" },
    { text = "20" },
    { text = "40/in. of thickness" },
  ],
]
:::

### Table: Object Hardness and Hit Points {#table-object-hardness-and-hit-points}

::: table
caption = "Table: Object Hardness and Hit Points"
head = [
  [
    { text = "Object", header = true },
    { text = "Hardness", header = true },
    { text = "Hit Points", header = true },
    { text = "break DC", header = true },
  ],
]
body = [
  [
    { text = "Rope (1 in. diameter)" },
    { text = "0" },
    { text = "2" },
    { text = "23" },
  ],
  [
    { text = "Simple wooden door" },
    { text = "5" },
    { text = "10" },
    { text = "13" },
  ],
  [
    { text = "Small chest" },
    { text = "5" },
    { text = "1" },
    { text = "17" },
  ],
  [
    { text = "Good wooden door" },
    { text = "5" },
    { text = "15" },
    { text = "18" },
  ],
  [
    { text = "Treasure chest" },
    { text = "5" },
    { text = "15" },
    { text = "23" },
  ],
  [
    { text = "Strong wooden door" },
    { text = "5" },
    { text = "20" },
    { text = "23" },
  ],
  [
    { text = "Masonry wall (1 ft. thick)" },
    { text = "8" },
    { text = "90" },
    { text = "35" },
  ],
  [
    { text = "Hewn stone (3 ft. thick)" },
    { text = "8" },
    { text = "540" },
    { text = "50" },
  ],
  [
    { text = "Chain" },
    { text = "10" },
    { text = "5" },
    { text = "26" },
  ],
  [
    { text = "Manacles" },
    { text = "10" },
    { text = "10" },
    { text = "26" },
  ],
  [
    { text = "Masterwork manacles" },
    { text = "10" },
    { text = "10" },
    { text = "28" },
  ],
  [
    { text = "Iron door (2 in. thick)" },
    { text = "10" },
    { text = "60" },
    { text = "28" },
  ],
]
:::

### Table: DCs to Break or Burst Items {#table-dcs-to-break-or-burst-items}

::: table
caption = "Table: DCs to Break or Burst Items"
head = [
  [
    { text = "Strength Check to:", header = true },
    { text = "DC", header = true },
  ],
]
body = [
  [
    { text = "Break down simple door" },
    { text = "13" },
  ],
  [
    { text = "Break down good door" },
    { text = "18" },
  ],
  [
    { text = "Break down strong door" },
    { text = "23" },
  ],
  [
    { text = "Burst rope bonds" },
    { text = "23" },
  ],
  [
    { text = "Bend iron bars" },
    { text = "24" },
  ],
  [
    { text = "Break down barred door" },
    { text = "25" },
  ],
  [
    { text = "Burst chain bonds" },
    { text = "26" },
  ],
  [
    { text = "Break down iron door" },
    { text = "28" },
  ],
  [
    { text = "Condition", header = true },
    { text = "DC Adjustment\\*", header = true },
  ],
  [
    { text = "Hold portal" },
    { text = "+5" },
  ],
  [
    { text = "Arcane lock" },
    { text = "+10" },
  ],
]
foot = [
  [
    { text = "\\* If both apply, use the larger number.", colspan = 2 },
  ],
]
:::

### Smashing an Object {#smashing-an-object}

Smashing a weapon or shield with a slashing or bludgeoning weapon is accomplished with the sunder
combat maneuver (see Combat). Smashing an object is like sundering a weapon or shield, except that
your combat maneuver check is opposed by the object's AC. Generally, you can smash an object only
with a bludgeoning or slashing weapon.

Armor Class: Objects are easier to hit than creatures because they don't usually move, but many are
tough enough to shrug off some damage from each blow. An object's Armor Class is equal to 10 + its
size modifier (see Table: Size and Armor Class of Objects) + its Dexterity modifier. An inanimate
object has not only a Dexterity of 0 (–5 penalty to AC), but also an additional –2 penalty to its
AC. Furthermore, if you take a full-round action to line up a shot, you get an automatic hit with a
melee weapon and a +5 bonus on attack rolls with a ranged weapon.

Hardness: Each object has [hardness](ref/umr/hardness)—a number that represents how well it resists
damage. When an object is damaged, subtract its hardness from the damage. Only damage in excess of
its hardness is deducted from the object's hit points (see Table: Common Armor, Weapon, and Shield
Hardness and Hit Points, Table: Substance Hardness and Hit Points, and Table: Object Hardness and
Hit Points).

Hit Points: An object's hit point total depends on what it is made of and how big it is (see Table:
Common Armor, Weapon, and Shield [Hardness](ref/umr/hardness) and Hit Points, Table: Substance
Hardness and Hit Points, and Table: Object Hardness and Hit Points). Objects that take damage equal
to or greater than half their total hit points gain the broken condition (see Conditions). When an
object's hit points reach 0, it's ruined.

Very large objects have separate hit point totals for different sections.

Energy Attacks: Energy attacks deal half damage to most objects. Divide the damage by 2 before
applying the object's [hardness](ref/umr/hardness). Some energy types might be particularly
effective against certain objects, subject to GM discretion. For example, fire might do full damage
against parchment, cloth, and other objects that burn easily. Sonic might do full damage against
glass and crystal objects.

Ranged Weapon Damage: Objects take half damage from ranged weapons (unless the weapon is a siege
engine or something similar). Divide the damage dealt by 2 before applying the object's
[hardness](ref/umr/hardness).

Ineffective Weapons: Certain weapons just can't effectively deal damage to certain objects. For
example, a bludgeoning weapon cannot be used to damage a rope. Likewise, most melee weapons have
little effect on stone walls and doors, unless they are designed for breaking up stone, such as a
pick or hammer.

Immunities: Objects are immune to nonlethal damage and to critical hits.

Magic Armor, Shields, and Weapons: Each +1 of enhancement bonus adds 2 to the
[hardness](ref/umr/hardness) of armor, a weapon, or a shield, and +10 to the item's hit points.

Vulnerability to Certain Attacks: Certain attacks are especially successful against some objects. In
such cases, attacks deal double their normal damage and may ignore the object's
[hardness](ref/umr/hardness).

Damaged Objects: A damaged object remains functional with the broken condition until the item's hit
points are reduced to 0, at which point it is destroyed.

Damaged (but not destroyed) objects can be repaired with the Craft skill and a number of spells.

Saving Throws: Nonmagical, unattended items never make saving throws. They are considered to have
failed their saving throws, so they are always fully affected by spells and other attacks that allow
saving throws to resist or negate. An item attended by a character (being grasped, touched, or worn)
makes saving throws as the character (that is, using the character's saving throw bonus).

Magic items always get saving throws. A magic item's Fortitude, Reflex, and Will save bonuses are
equal to 2 + half its caster level. An attended magic item either makes saving throws as its owner
or uses its own saving throw bonus, whichever is better.

Animated Objects: Animated objects count as creatures for purposes of determining their Armor Class
(do not treat them as inanimate objects).

### Breaking Items {#breaking-items}

When a character tries to break or burst something with sudden force rather than by dealing damage,
use a Strength check (rather than an attack roll and damage roll, as with the sunder special attack)
to determine whether he succeeds. Since [hardness](ref/umr/hardness) doesn't affect an object's
break DC, this value depends more on the construction of the item than on the material the item is
made of. Consult Table: DCs to Break or Burst Items for a list of common break DCs.

If an item has lost half or more of its hit points, the item gains the broken condition (see
Conditions) and the DC to break it drops by 2.

Larger and smaller creatures get size bonuses and size penalties on Strength checks to break open
doors as follows: Fine –16, Diminutive –12, Tiny –8, Small –4, Large +4, Huge +8, Gargantuan +12,
Colossal +16.

A crowbar or portable ram improves a character's chance of breaking open a door (see Equipment).

#### Table: Common Armor, Weapon, and Shield Hardness and Hit Points {#table-common-armor-weapon-and-shield-hardness-and-hit-points}

::: table
caption = "Table: Common Armor, Weapon, and Shield Hardness and Hit Points"
head = [
  [
    { text = "Weapon or Shield", header = true },
    { text = "Hardness^1^", header = true },
    { text = "Hit Points^2, 3^", header = true },
  ],
]
body = [
  [
    { text = "Light blade" },
    { text = "10" },
    { text = "2" },
  ],
  [
    { text = "One-handed blade" },
    { text = "10" },
    { text = "5" },
  ],
  [
    { text = "Two-handed blade" },
    { text = "10" },
    { text = "10" },
  ],
  [
    { text = "Light metal-hafted weapon" },
    { text = "10" },
    { text = "10" },
  ],
  [
    { text = "One-handed metal-hafted weapon" },
    { text = "10" },
    { text = "20" },
  ],
  [
    { text = "Light hafted weapon" },
    { text = "5" },
    { text = "2" },
  ],
  [
    { text = "One-handed hafted weapon" },
    { text = "5" },
    { text = "5" },
  ],
  [
    { text = "Two-handed hafted weapon" },
    { text = "5" },
    { text = "10" },
  ],
  [
    { text = "Projectile weapon" },
    { text = "5" },
    { text = "5" },
  ],
  [
    { text = "Armor" },
    { text = "special^4^" },
    { text = "armor bonus × 5" },
  ],
  [
    { text = "Buckler" },
    { text = "10" },
    { text = "5" },
  ],
  [
    { text = "Light wooden shield" },
    { text = "5" },
    { text = "7" },
  ],
  [
    { text = "Heavy wooden shield" },
    { text = "5" },
    { text = "15" },
  ],
  [
    { text = "Light steel shield" },
    { text = "10" },
    { text = "10" },
  ],
  [
    { text = "Heavy steel shield" },
    { text = "10" },
    { text = "20" },
  ],
  [
    { text = "Tower shield" },
    { text = "5" },
    { text = "20" },
  ],
]
foot = [
  [
    { text = "^1^ Add +2 for each +1 enhancement bonus of magic items.", colspan = 3 },
  ],
  [
    { text = "^2^ The hp value given is for Medium armor, weapons, and shields. Divide by 2 for each size category of the item smaller than Medium, or multiply it by 2 for each size category larger than Medium.", colspan = 3 },
  ],
  [
    { text = "^3^ Add 10 hp for each +1 enhancement bonus of magic items.", colspan = 3 },
  ],
  [
    { text = "^4^ Varies by material; see Table: Substance [Hardness](ref/umr/hardness) and Hit Points.", colspan = 3 },
  ],
]
:::
