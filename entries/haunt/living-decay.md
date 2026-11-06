+++
id = "ref/haunt/living-decay"
kind = "rule"
title = "Living Decay"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "living_decay", path = "json/haunts.json" },
]

[fields]
kind = "none"
+++

Among the most frightening diseases are those that cause their victims' bodies to rot away. A living
decay haunt arises when an epidemic of such a disease devastates a population.

**Sources:** Horror Adventures pg 177

**Living Decay**

**Challenge rating:** 10

**XP** 9,600\
NE persistent haunt (50-ft. radius)\
**Caster Level** 9th

**Notice:** Perception DC 20 (to smell decaying flesh)

**Hit points:** 45

**Weakness:** [remove disease](ref/spell/remove-disease)

**Trigger:** proximity

**Reset:** 1 day

### Effect

The area fills with a potent miasma that reeks of decaying flesh. Everyone within the radius must
succeed at a DC 20 Fortitude save or contract the disease living rot, as detailed below, except they
bypass the latent/carrier state. Within the haunt's area, the disease's frequency increases to 1
round and its save DC increases to 20. Characters who succeed at this saving throw are not immune;
they must attempt a new saving throw each round they remain in the haunt's area. Reducing the haunt
to 0 hit points does not remove the disease. A character who casts
_[remove disease](ref/spell/remove-disease)_ on the living decay haunt deals it an amount of damage
equal to her caster level.

### Destruction

Casting [heal](ref/spell/heal) on each remaining body in the original victims' mass grave (or a
single casting of [mass heal](ref/spell/heal-mass)) prevents this haunt from returning.

### Living Rot

This haunt uses the [optional Unchained disease rules](ref/rule/diseases-pu).

**Type:** Disease (Disease, contact, inhaled, or injury)

**Save:** Fortitude DC 17

**Frequency:** 1/day

**Track:** physical

**Effect:** In the weakened state, the target also takes a -2 penalty on Strength- and
Dexterity-based skill checks and ability checks. In the impaired state, the target takes a 50% miss
chance on attack rolls and the target's speed is reduced by half (minimum 5 feet). All objects
touched at the impaired state and beyond can transfer the disease.

**Cure:** 2 consecutive saves, penalties from the weakened state and worse are permanent until the
victim is the target of heal or regenerate
