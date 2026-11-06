+++
id = "ref/rule/me-pit-fiend"
kind = "rule"
title = "Pit Fiend"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "me_pit_fiend", path = "json/rules_adv_gm03.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 243

With a diverse spread of abilities useful for both combat and spellcasting, a pit fiend remains
fairly complex to create even in the simple monster creation system. It's not really 100% a
combatant, so it requires special statistical adjustments.

**Array:** This monster mostly uses the numbers from the combatant array, but gains a large number
of spells, and therefore has the hit points of a spellcaster. As a powerful ruler in Hell, the pit
fiend's starting ability modifiers are +13, +13, +9, +9, +6, and +6.

**Creature Type:** As an outsider, the pit fiend gains [darkvision](ref/rule/darkvision) 60 feet,
increases its Fortitude from +20 to +22, and increases its attack bonuses from +30 to +32. It also
gets the elective adjustment for one additional master skill.

**Subtype:** The devil subtype graft grants the see in darkness sense, energy resistance 10 to acid
and cold, and immunity to fire and poison. It also gives the pit fiend the summon allies option and
telepathy 100 feet.

**Size:** Since it's Large, the pit fiend decreases its touch AC from 22 to 21 and increases its
flat-footed AC from 28 to 29. Its CMB goes up from +32 to +34, and its CMD goes from 42 to 43.

**Spells:** The monster gains spells as though it were a spellcaster. In addition, it can use mass
hold monster and greater teleport at will.

**Options:** For the three combat options given by its array, the pit fiend has constrict,
[damage reduction](ref/rule/damage-reduction), and improved combat maneuver (grapple), which also
gives it bonuses on CMB checks made to grapple and to CMD against grapple checks. For its one any
option, it has poison with eight advantages (two + 1/3 of the pit fiend's CR of 20). These
advantages are removing the onset, changing the frequency to 1/round for 6 rounds, increasing the
ability damage three times, increasing the cure to 2 consecutive saves, and two advantages invented
specifically for this monster: increasing the frequency to 1/round for 10 rounds, and increasing the
cure to 3 consecutive saves. As a nod to classic pit fiends, the monster can regenerate from wounds,
but the regeneration amount is so low for its level that it doesn't cost an option. Its diseased
bite is also free, since it won't matter much in high-level combat. The devil has a bonus option for
its fear aura, and doesn't spend any options for its spells, but these additions are reasonable for
a high-level villain such as the pit fiend. The Bestiary pit fiend's devil shaping ability won't
come up in combat, so it has been omitted.

**Skills:** Because of its creature type graft, the pit fiend has two master skills instead of one.

**Damage:** The number of attacks the pit fiend gains has been reduced from the number in the
Bestiary; in particular, its wing attacks have been removed to allow its remaining attacks to have
more impact. The array's two natural attacks' damage (66) is doubled to 132, then increased by 25%
to get 165, which is then divvied up between four attacks. This sets the damage value at 48 points
for each claw, 42 for the bite, and 27 for the tail slap.

### Pit Fiend

#### CR/HD 20

**Init** +9; **Perception** +35 ([darkvision](ref/rule/darkvision) 60 ft., see in darkness)\
**Aura** fear (30 ft., DC 20)\
**Size** Large (10 ft.); **Speed** 40 ft., fly 60 ft. (average); **Special Movement** greater
teleport (at will, self plus 50 lbs. of objects only)

#### Defenses

**AC** 38 (touch 21, flat-footed 29); **Fort** +22, **Ref** +20, **Will** +17; **CMD** 43 (47 vs.
grapple); **SR** 31; **Concentration** +26\
**hp** 333; regeneration 5 (good weapons, good spells); **DR** 10/good and silver; **Immune** fire,
poison; **Resist** acid 10, cold 10

#### Attacks

**Melee** 2 claws (reach 10 ft.) +32 (2d8+42), bite (reach 10 ft.) +32 (4d6+30 plus disease and
poison), tail slap (reach 10 ft.) +32 (2d8+18 plus improved combat maneuver \[grapple\])\
**Attack Spell-Like Abilities** (DC 17 + spell's level) 1/day-quickened fireball, meteor swarm; at
will-mass hold monster, wall of fire\
**Attack Options** (DC 25) constrict (2d8+60), disease (see below), poison (see below); **CMB** +34
(+38 grapple)

#### Statistics

**Utility Options** summon allies (typically barbed devil or ice devil, 60%)\
**Str** +13, **Dex** +9, **Con** +13, **Int** +6, **Wis** +9, **Cha** +6; Bluff +28, Intimidate +35,
Sense Motive +28; telepathy 100 ft.\
**XP** 307,200; LE outsider (devil, evil, extraplanar, lawful)

- [Affliction: Disease](ref/affliction/me-pit-fiend/disease)
- [Affliction: Poison](ref/affliction/me-pit-fiend/poison)
