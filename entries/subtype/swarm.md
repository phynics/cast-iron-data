+++
id = "ref/subtype/swarm"
kind = "rule"
title = "Swarm"
source_ids = ["bestiary-6", "bestiary", "bestiary-2", "bestiary-3", "bestiary-5"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swarm", path = "json/monster_subtypes.json" },
]
[[sources]]
publication = "bestiary-6"
[[sources]]
publication = "bestiary"
[[sources]]
publication = "bestiary-2"
[[sources]]
publication = "bestiary-3"
[[sources]]
publication = "bestiary-5"

[fields]
kind = "none"
+++

## Subtype: Swarm

A swarm is a collection of Fine, Diminutive, or Tiny creatures that acts as a single creature. A
swarm has the characteristics of its type, except as noted here. A swarm has a single pool of Hit
Dice and hit points, a single initiative modifier, a single speed, and a single Armor Class. A swarm
makes saving throws as a single creature. A single swarm occupies a square (if it is made up of
non-flying creatures) or a cube (of flying creatures) 10 feet on a side, but its reach is 0 feet,
like its component creatures. In order to attack, it moves into an opponent's space, which provokes
an attack of opportunity. It can occupy the same space as a creature of any size, since it crawls
all over its prey. A swarm can move through squares occupied by enemies and vice versa without
impediment, although the swarm provokes an attack of opportunity if it does so. A swarm can move
through cracks or holes large enough for its component creatures.

- A swarm of Tiny creatures consists of 300 non-flying creatures or 1,000 flying creatures. A swarm
  of Diminutive creatures consists of 1,500 non-flying creatures or 5,000 flying creatures. A swarm
  of Fine creatures consists of 10,000 creatures, whether they are flying or not. Swarms of
  non-flying creatures include many more creatures than could normally fit in a 10-foot square based
  on their normal space, because creatures in a swarm are packed tightly together and generally
  crawl over each other and their prey when moving or attacking. Larger swarms are represented by
  multiples of single swarms. The area occupied by a large swarm is completely shapeable, though the
  swarm usually remains in contiguous squares.
- **Swarm Traits:** A swarm has no clear front or back and no discernable anatomy, so it is not
  subject to critical hits or [flanking](ref/rule/flanking). A swarm made up of Tiny creatures takes
  half damage from slashing and piercing weapons. A swarm composed of Fine or Diminutive creatures
  is immune to all weapon damage. Reducing a swarm to 0 hit points or less causes it to break up,
  though damage taken until that point does not degrade its ability to attack or resist attack.
  Swarms are never staggered or reduced to a dying state by damage. Also, they cannot be
  [tripped](ref/rule/trip), [grappled](ref/rule/grapple), or [bull rushed](ref/rule/bull-rush), and
  they cannot grapple an opponent.
- A swarm is immune to any spell or effect that targets a specific number of creatures (including
  single-target spells such as [disintegrate](ref/spell/disintegrate)), with the exception of
  mind-affecting effects (charms, compulsions, morale effects, patterns, and phantasms) if the swarm
  has an Intelligence score and a hive mind. A swarm takes half again as much damage (+50%) from
  spells or effects that affect an area, such as splash weapons and many evocation spells.
- Swarms made up of Diminutive or Fine creatures are susceptible to high winds, such as those
  created by a [gust of wind](ref/spell/gust-of-wind) spell. For purposes of determining the effects
  of wind on a swarm, treat the swarm as a creature of the same size as its constituent creatures. A
  swarm rendered unconscious by means of nonlethal damage becomes disorganized and dispersed, and
  does not reform until its hit points exceed its nonlethal damage.
- **Swarm Attack:** Creatures with the swarm subtype don't make standard melee attacks. Instead,
  they deal automatic damage to any creature whose space they occupy at the end of their move, with
  no attack roll needed. Swarm attacks are not subject to a miss chance for
  [concealment](ref/rule/concealment) or [cover](ref/rule/cover). A swarm's statistics block has
  "swarm" in the Melee entries, with no attack bonus given. The amount of damage a swarm deals is
  based on its Hit Dice, as shown below.

|Swarm HD|Swarm Base Damage|
| --- | --- |
|1-5|1d6|
|6-10|2d6|
|11-15|3d6|
|16-20|4d6|
|21 or more|5d6|

- A swarm's attacks are nonmagical, unless the swarm's description states otherwise.
  [Damage reduction](ref/rule/damage-reduction) sufficient to reduce a swarm attack's damage to 0,
  being incorporeal, or other special abilities usually give a creature [immunity](ref/umr/immunity)
  (or at least [resistance](ref/umr/resistance)) to damage from a swarm. Some swarms also have acid,
  blood drain, poison, or other special attacks in addition to normal damage.
- Swarms do not threaten creatures, and do not make attacks of opportunity with their swarm attack.
  However, they distract foes whose squares they occupy, as described below.
- Swarms possess the [distraction](ref/umr/distraction) universal monster rule. Spellcasting or
  concentrating on spells within the area of a swarm requires a caster level check (DC 20 + spell
  level). Using skills that involve patience and concentration requires a DC 20 Will save.
