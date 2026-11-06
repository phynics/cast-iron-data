+++
id = "ref/monster/capacitor-ooze"
kind = "creature"
title = "Capacitor Ooze"
source_ids = ["numeria-land-of-fallen-stars"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "capacitor_ooze", path = "json/monsters04.json" },
]

[fields]
kind = "creature"
creature_type = "ooze"
size = "medium"
alignment = "neutral"
ac = "5/5/5"
hp = "195~17d8+119"
fortitude = "+12"
reflex = "+0"
will = "+0"
melee = "slam +18 (2d6+9 plus 4d6 electricity and neurophagic jolt)"
special_attacks = "neurophagic jolt"
special_qualities = "compression"
abilities = ["22", "1", "24", "-", "1", "1"]
+++

_Electricity crackles and arcs from this undulating mass of orange slime._

**Capacitor Ooze**

**Challenge rating:** 11

**aura:** osmotic drain (10 ft., DC 25)

**blindsight:** 120

**Initiative:** -5

**Size:** medium

**Alignment:** Neutral

**Type:** ooze

**Perception:** -5

**source:** Numeria, Land of Fallen Stars/48

**Experience points:** 12,800

**Armor class:** 5/5/5

**Defensive abilities:** electrified

**Fort:** +12

**Hit points:** 195 (17d8+119)

**Immune:** electricity, [ooze traits](ref/umr/ooze-traits)

**Mod:** -5 Dex

**Ref:** +0

**Will:** +0

**Offense**

**Speed:** 10 ft., climb 10 ft.

**Melee:** slam +18 (2d6+9 plus 4d6 electricity and neurophagic jolt)

**Spec Att:** neurophagic jolt

**Statistics**

**Ability scores:** Str 22, Dex 1, Con 24, Int -, Wis 1, Cha 1

**Base attack bonus:** +12

**Combat maneuver bonus:** +18

**Combat maneuver defense:** 23

**Skills:** Climb +14

**Special qualities:** [compression](ref/umr/compression)

**Ecology**

**Environment:** cold deserts or plains

**Organization:** solitary

**Treasure:** None

### Special Abilities

**Electrified (Ex)** A creature that strikes a capacitor ooze with a natural weapon, unarmed strike,
or metal weapon takes 4d6 points of electricity damage. Creatures grappling a capacitor ooze take
this damage when initiating the grapple and on each round the grapple is maintained.

**Neurophagic Jolt (Ex)** When a capacitor ooze deals electricity damage to a target with its slam
attack, the jolt to the target's neurological system [stuns](ref/misc/stunned) the creature for 1
round (Fortitude DC 25 negates). A second neurophagic jolt to a stunned target sets up a destructive
resonance in the target's brain. This resonance functions like an affliction with the following
statistics:

**Type:** Affliction

**Save:** Will DC 25

**Frequency:** 1/round for 6 rounds

**Effect:** Dexterity damage 1d2 and Intelligence damage 1d2

**Cure:** 1 save

[Neutralize poison](ref/spell/neutralize-poison) does not cure this affliction, but
[heal](ref/spell/heal), [greater restoration](ref/spell/restoration-greater), and any effect that
removes insanity does. This is a mind-affecting effect. The save DC is Constitution-based.

**Osmotic Drain (Ex)** A capacitor ooze drains power from nearby electrical sources. Any creatures
within 10 feet of a capacitor ooze carrying at least one device that's powered by or generates
electricity must succeed at a DC 25 Fortitude save or lose 1 charge from a random electrical device.
Single-use items are depowered entirely; devices with renewable electrical sources are depowered
until they can recharge (in the case of a solar-powered device) or have their electrical function
suppressed for 1d4 minutes (in the case of a shock weapon). A given power source can be drained only
once per minute. For each electrical device affected by the capacitor ooze's osmotic drain, the ooze
deals an additional 1d6 points of electricity damage the next time it would deal electricity damage
to a target, and its speed increases by 30 feet for 1 round. The save DC is Constitution-based.

### Description

Created by technologists seeking to devise an organic battery, capacitor oozes escaped captivity and
now infest the hinterlands of Numeria. They find water dangerous and humidity painful, so they
gravitate toward arid climes with stable weather.

Capacitor oozes instinctively seek out sources of electricity, consuming them like other creatures
would food. Maintaining vigor and growth requires regular consumption of organic material as well. A
capacitor ooze that's denied power or food begins to starve.

Capacitor oozes grow without bound, splitting only from damage or misfortune. Capacitor oozes that
encounter others of their kind often merge if left undisturbed, a process that takes 1d4 hours and
may result in a [giant](ref/template/giant) or [advanced](ref/template/advanced) ooze. Capacitor
oozes that aren't inclined to merge disperse, as they find disharmonious electrical auras
intolerable.
