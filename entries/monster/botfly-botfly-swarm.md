+++
id = "ref/monster/botfly-botfly-swarm"
kind = "creature"
title = "Botfly Swarm"
source_ids = ["heart-of-the-jungle"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "botfly_botfly_swarm", path = "json/monsters04.json" },
]
[[sources]]
publication = "heart-of-the-jungle"
page = "59"

[fields]
kind = "creature"
cr = "4"
creature_type = "vermin"
subtypes = ["swarm"]
size = "fine"
alignment = "neutral"
ac = "18/18/18"
hp = "40~9d8"
fortitude = "+6"
reflex = "+3"
will = "+3"
melee = "swarm (2d6 plus infestation)"
special_attacks = "infestation~suffocation#S"
abilities = ["2", "11", "10", "-", "11", "2"]
+++

_Like a cloud of black dust, a swirling swarm of insects hovers in the air. From within comes the
low, droning buzz of thousands of tiny flies._

**Botfly Swarm**

**Challenge rating:** 4

**Size:** fine

**Initiative:** +0

**Alignment:** Neutral

**Perception:** +0

**Senses:** Darkvision 60 ft.

**Subtype:** Swarm

**Type:** vermin

**Experience points:** 1,200

**Armor class:** 18/18/18

**Defensive abilities:** swarm traits

**Fort:** +6

**Hit points:** 40 (9d8)

**Immune:** mind-affecting effects, weapon damage

**Mod:** +8 size

**Ref:** +3

**Weaknesses:** swarm traits

**Will:** +3

**Offense**

**Speed:** 0 ft., fly 60 ft. (good)

**Distraction:** 14

**Melee:** swarm (2d6 plus infestation)

**Reach:** 0

**Space:** 10

**Spec Att:** infestation, suffocation\#S

###### S {#footnote-s}

No description of the _[suffocation](ref/spell/suffocation)_ attack was published, and it does not
match any known swarm trait or universal monster ability.

**Statistics**

**Ability scores:** Str 2, Dex 11, Con 10, Int -, Wis 11, Cha 2

**Base attack bonus:** +6

**Combat maneuver bonus:** -

**Combat maneuver defense:** -

**Skills:** Fly +12

**Ecology**

**Environment:** warm jungles and swamps

**Organization:** solitary or colony (2-20 swarms)

**Treasure:** None

### Special Abilities

**Infestation (Ex)** A living creature injured by a botfly swarm's attack must make a DC 14
Fortitude save or be infested with the swarm's larvae. The larvae may be cut out of the host with a
DC 15 Heal check, though each attempt inflicts 1d8 points of damage whether or not it's successful.
A [remove disease](ref/spell/remove-disease) spell destroys all larvae without further harm to the
host.

- [Affliction: Botfly Larvae](ref/affliction/botfly-botfly-swarm/botfly-larvae)

### Description

Common to sweltering jungles, warm swamplands, and lazy riverbanks, these pestilent fly swarms seek
humanoid hosts for their eggs. While not as physically dangerous as their giant cousins, implanted
botfly larvae typically carry diseases that spread to the host.

### Infestations

Parasites such as botfly larvae cause [infestations](ref/rule/infestations), a type of affliction
similar to diseases. Infestations can only be cured through specific means; otherwise, no matter how
many saving throws are made, the infestation continues to afflict the target. While a
_[remove disease](ref/spell/remove-disease)_ spell (or similar effect) instantly halts an
infestation, immunity to disease offers no protection, as the infestation itself is caused by
parasites.
