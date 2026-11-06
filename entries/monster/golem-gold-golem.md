+++
id = "ref/monster/golem-gold-golem"
kind = "creature"
title = "Gold Golem"
source_ids = ["bestiary-6"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "golem_gold_golem", path = "json/monsters33.json" },
]

[fields]
kind = "creature"
creature_type = "construct"
size = "large"
alignment = "neutral"
ac = "30/13/26"
hp = "156~23d10+30"
fortitude = "+7"
reflex = "+11"
will = "+7"
melee = "2 slams +34 (4d8+12 plus prismatic surge)"
special_qualities = "death throes"
abilities = ["34", "18", "-", "-", "11", "1"]
+++

_This golden statue stands proud, bearing a regal scepter in one hand. Its other arm is stretched
out, ending in an upraised fist._

**Gold Golem**

**Challenge rating:** 15

**Type:** construct

**dv:** 60

**Initiative:** +4

**Size:** large

**Sense:** Llv

**Alignment:** Neutral

**Perception:** +0

**source:** Bestiary 6/140

**Experience points:** 51,200

**Armor class:** 30/13/26

**Dr:** 15/adamantine

**Fort:** +7

**Hit points:** 156 (23d10+30)

**Immune:** [construct traits](ref/umr/construct-traits), magic

**Mod:** +4 Dex, +17 natural, -1 size

**Ref:** +11

**Will:** +7

**Offense**

**Speed:** 30 ft.

**Melee:** 2 slams +34 (4d8+12 plus prismatic surge)

**Reach:** 10

**Space:** 10

**Statistics**

**Ability scores:** Str 34, Dex 18, Con -, Int -, Wis 11, Cha 1

**Base attack bonus:** +23

**Combat maneuver bonus:** +36

**Combat maneuver defense:** 50

**Special qualities:** death throes

**Ecology**

**Environment:** any

**Organization:** solitary or procession (2-5)

**Treasure:** None

### Special Abilities

**Death Throes (Ex)** A gold golem melts into worthless slag when destroyed, releasing a
10-foot-radius cloud of fumes that deals 1d4 points of Constitution damage to all creatures within a
10-foot radius. A successful DC 21 Fortitude save negates this effect. This is a poison effect. The
save DC is Constitution-based.

**Immunity to Magic (Ex)** A gold golem is immune to any spell or
[spell-like ability](ref/umr/spell-like-abilities) that allows
[spell resistance](ref/rule/spell-resistance). In addition, certain spells and effects function
differently against the creature, as noted below.

- A magical attack that deals fire damage reduces the golem's DR to 5/adamantine but also hastens it
  for 1d6 rounds as per the spell [haste](ref/spell/haste), with no saving throw.
- A magical attack that deals cold damage slows a gold golem for 1d6 rounds as per the spell
  [slow](ref/spell/slow), with no saving throw.

**Prismatic Surge (Su)** As a swift action when it hits a foe with its slam attack, a gold golem
unleashes a ray of prismatic energy from its bejeweled scepter. It can choose to automatically hit
the foe it hit with its slam attack with this ray, or it can target another creature within 30 feet
as a +26 ranged touch attack. Roll 1d6 for any creature struck by a ray, and consult the following
table to determine the effects. The save DCs are Constitution-based.

|1d6|Beam|Color Effect|
| --- | --- | --- |
|1|Red|20 points of fire damage (Reflex DC 21 half)|
|2|Orange|40 points of acid damage (Reflex DC 21 half)|
|3|Yellow|80 points of electricity damage (Reflex DC 21 half)|
|4|Green|Poison (see below)|
|5|Blue|Petrification (as per [flesh to stone](ref/spell/flesh-to-stone), Fort DC 21 negates)|
|6|Indigo|Insanity (as per [insanity](ref/spell/insanity), Will DC 21 negates)|

- [Affliction: Prismatic Poison](ref/affliction/golem-gold-golem/prismatic-poison)

### Description

Gold golems are extravagant constructs, crafted at great expense at the command of the rich and
powerful. They're most often used to guard palaces and family vaults, but are rarely placed in areas
that are hidden away from casual observation.

Many of those who expend the funds to create a gold golem aren't the type to hide the conspicuous
display of their wealth from their visitors. A gold golem is humanoid in appearance, standing 10
feet tall and weighing 4,500 pounds.

**Family:** [Golem](ref/family/golem)

### Construction

A gold golem is built from 1,800 pounds of special lead that must be treated with rare alchemical
reagents to magically transmute the creature to gold upon its animation. These reagents and the lead
cost 25,000 gp.

**CL** 18th; **Price** 220,000 gp\
**Requirements** [Craft Construct](ref/feat/craft-construct), [geas/quest](ref/spell/geas-quest),
[limited wish](ref/spell/limited-wish), [polymorph any object](ref/spell/polymorph-any-object), and
[prismatic spray](ref/spell/prismatic-spray), creator must be at least caster level 18th; **Skill**
Craft (armor) DC 25; **Cost** 122,500 gp
