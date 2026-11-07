+++
id = "ref/monster/drekavac"
kind = "creature"
title = "Drekavac"
source_ids = ["pathfinder-31-stolen-land"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "drekavac", path = "json/monsters07.json" },
]

[fields]
kind = "creature"
cr = "3"
creature_type = "undead"
size = "small"
alignment = "neutral evil"
ac = "15/12/14"
hp = "30~4d8+12"
fortitude = "+4"
reflex = "+2"
will = "+7"
melee = "chilling grasp +5 touch (1d6 cold plus disease) or shadow +5 touch (disease)"
special_attacks = "create spawn~disease~diseased shadow"
abilities = ["10", "12", "-", "9", "12", "17"]
+++

_Dressed in graveyard rags, this pitiful creature cries out like a sick child. An oversized, bestial
head perches atop its spindly, child-sized body, and its eyes are nothing but sunken pools of shadow
with no trace of life in them. A cloying mist wreathes its frail form, accompanied by the stench of
death and disease._

**Drekavac**

**Challenge rating:** 3

**aura:** [unnatural aura](ref/umr/unnatural-aura) (30 ft.)

**Initiative:** +1

**Alignment:** Neutral evil

**Perception:** +8

**Senses:** Darkvision 60 ft.

**Size:** small

**Sources:** Pathfinder \#31: Stolen Land pg 78\
**Type:** undead

**Experience points:** 800

**Armor class:** 15/12/14

**Dr:** 5/silver

**Fort:** +4

**Hit points:** 30 (4d8+12)

**Immune:** [undead traits](ref/umr/undead-traits)

**Mod:** +1 Dex, +3 natural, +1 size

**Ref:** +2

**Weaknesses:** sunlight aversion, vulnerability to magic, vulnerability to salt

**Will:** +7

**Offense**

**Speed:** 20 ft.

**Melee:** chilling grasp +5 touch (1d6 cold plus disease) or shadow +5 touch (disease)

**Spec Att:** create spawn, disease, diseased shadow

**Spell-Like Abilities**

**Caster level:** 5

**Concentration:** +8

**At will:**

- gaseous form

**Statistics**

**Ability scores:** Str 10, Dex 12, Con -, Int 9, Wis 12, Cha 17

**Base attack bonus:** +3

**Combat maneuver bonus:** +2

**Combat maneuver defense:** 13

**Feats:** Iron Will, Weapon Finesse

**Skills:** Intimidate +10, Perception +8, Stealth +12

**Languages:** Common

**Ecology**

**Environment:** any

**Organization:** solitary or pack (2-5)

**Treasure:** None

### Special Abilities

**Create Spawn (Su)** A child slain by a drekavac's disease has a 1-in-6 chance of rising as another
drekavac 3 days after death. The new drekavac is not in any way controlled by its maker, and is
immediately capable of exercising its full powers, including creating spawn of its own. It does not
possess any of the abilities it had in life.

**Disease (Su)** Drekavacs are spirits of disease and contagion. While most drekavacs carry bubonic
plague, drekavacs who died from other afflictions may carry those diseases instead. Any illness
caused by a drekavac must be potentially fatal. Other diseases commonly carried include
[demon fever](ref/disease/demon-fever), [filth fever](ref/disease/filth-fever), and
[slimy doom](ref/disease/slimy-doom). If a drekavac is reduced to 0 hit points (from weapons or
other sources, including [channeled energy](ref/ability/channel-energy)), all of the diseases it
caused are cured, although the victims must recover from any effects normally, and slain victims are
not restored.

- [Affliction: Bubonic plague](ref/affliction/drekavac/bubonic-plague)

**Diseased Shadow (Su)** Any creature touched by a drekavac's shadow is also affected by the
creature's disease ability. If there is a question about which way the drekavac's shadow falls, roll
1d8 to determine a random square around the creature. A character with a light source cannot be
touched by the drekavac's shadow, but the light causes the shadow to fall directly opposite the
character (unless there is another light source there as well). A drekavac can deliberately touch a
creature with its shadow as a standard action by making a successful touch attack.

A target missed by the drekavac's chilling grasp attack must make a DC 15 Reflex save to avoid being
touched by the creature's shadow as well. This save DC is Charisma-based.

**Sunlight Aversion (Ex)** Drekavacs hate natural sunlight and immediately flee from it. A drekavac
caught in natural sunlight is [staggered](ref/misc/staggered).

**Unnatural Aura (Su)** Animals, wild or domesticated, can sense the unnatural presence of a
drekavac at a distance of 30 feet. They do not willingly approach nearer than that and panic if
forced to do so unless a master succeeds at a DC 25 Handle Animal, Ride, or wild empathy check.
[Panicked](ref/misc/panicked) animals remain so as long as they are within 30 feet of the drekavac.

**Vulnerability to Magic (Ex)** A [remove curse](ref/spell/remove-curse) or
[remove disease](ref/spell/remove-disease) spell cast directly upon a drekavac (DC equal to the
drekavac's disease ability) immediately destroys the creature, allowing the afflicted soul to move
on. Destroying a drekavac with _[remove curse](ref/spell/remove-curse)_ or
_[remove disease](ref/spell/remove-disease)_ does not cure any of the creature's diseases.

**Vulnerability to Salt (Ex)** Drekavacs are vulnerable to salt that has been consecrated in the
same fashion as holy water, and cannot cross an unbroken line of blessed salt. A handful of blessed
salt thrown at a drekavac inflicts the same damage as a flask of
[holy water](ref/eq-weapon/holy-water).

### Description

Drekavacs are the undead remains of children who perished from disease, particularly in
plague-ridden areas where many such deaths occurred in a short period of time. Able to become as
insubstantial as the mist rising from a graveyard on a cold, dark night, drekavacs are carriers of
disease, seeking to infect the living with the afflictions that slew them. According to some
stories, drekavacs only result from young plague victims who remain unburied or died bereft of the
proper funeral rites; performing those rites may allow their spirits to rest and no longer haunt the
world of the living.
