+++
id = "ref/kinetic/spore-infusion"
kind = "rule"
title = "Spore Infusion"
source_ids = ["ultimate-wilderness", "psychic-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spore_infusion", path = "json/class_ability_kinetic_talents.json" },
]

[fields]
kind = "none"
+++

**Element:** wood

**Type:** substance infusion

**Level:** 5

**Burn:** 3

**Associated:** [Autumn Blast](ref/kinetic/autumn-blast), [Spring Blast](ref/kinetic/spring-blast),
[Summer Blast](ref/kinetic/summer-blast), [Verdant Blast](ref/kinetic/verdant-blast),
[Winter Blast](ref/kinetic/winter-blast), [Wood Blast](ref/kinetic/wood-blast)

**Saving throw:** Fortitude negates

**Source:** Ultimate Wilderness/60, Psychic Anthology/21

Creatures that take piercing or slashing damage from your blast are infected with spores. If a
target fails its Fortitude save, it takes 1d6 points of damage per round for 10 rounds as plants and
fungi grow out of its body. At the end of that time, the target is exposed to the _pulsing puffs_
disease.

**Pulsing Puffs**

**Type:** Disease (Blast-injury)

**Save:** Fortitude DC 18

**Onset:** 1 minute

**Frequency:** 1/day

**Effect:** Dexterity damage 1d6

**Cure:** 2 consecutive saves

This infusion is a disease effect. When using a wood kinetic blast against a creature infected by
this infusion, you gain a +2 bonus on attack rolls, to saving throw DCs, and on caster level checks
to overcome [spell resistance](ref/rule/spell-resistance).
