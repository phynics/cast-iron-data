+++
id = "ref/rule/me-bat-swarm"
kind = "rule"
title = "Bat Swarm"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "me_bat_swarm", path = "json/rules_adv_gm03.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 243

The bat swarm is straightforward to create, but its swarm subtype is complicated and grants it
additional features that make it unlike other monsters.

**Array:** Since a bat swarm is made up of creatures with only animal intelligence, the combatant
array is the only choice for it that makes sense.

**Creature Type:** The animal type increases the bat swarm's Fortitude and Reflex bonuses each from
+3 to +5 and grants [low-light vision](ref/rule/low-light-vision), but it mandates an Intelligence
modifier of either -4 or -5. Bats are slightly more intelligent than some other animals, so they
have a -4 modifier.

**Subtype:** The swarm subtype grants the bat swarm its various immunities, vulnerability to area
effects, swarm traits, swarm attack, and distraction.

**Size:** The bat swarm is made up of many Diminutive creatures, so it gains a +4 bonus to touch and
flat-footed AC. As a swarm, it doesn't have CMB or CMD, so the size adjustments to those numbers are
ignored. It also gains Fly and Stealth as master skills.

**Options:** The bat swarm's option is a weaker variant of the bleed attack option.

**Skills:** Other than the master skills from size, the bat swarm's echolocation enhances its
ability to notice things, so it gets Perception as a master skill. That's already plenty of skills
for an animal, so the bat swarm doesn't have any good skills.

### Bat Swarm

#### CR/HD 2

**Init** +3; **Perception** +10 ([blindsense](ref/rule/blindsight-and-blindsense) 20 ft.,
[low-light vision](ref/rule/low-light-vision))\
**Size** Diminutive (10 ft.); **Speed** 5 ft., fly 40 ft. (good)

#### Defenses

**AC** 16 (touch 16, flat-footed 16); **Fort** +5, **Ref** +5, **Will** +1\
**hp** 22; **Immune** bull rush, critical hits, flanking, grapple, spells that target a specific
number of creatures, trip, weapon damage\
**Weakness** +50% damage from area effects\
**Defense Options** swarm traits

#### Attacks

**Melee** swarm (all targets in the swarm's space) always hits (1d6 plus 1 bleed)\
**Attack Options** (DC 11) distraction

#### Statistics

**Str** -4, **Dex** +3, **Con** +1, **Int** -4, **Wis** +2; Fly +10, Stealth +10\
**XP** 600; N animal (swarm)
