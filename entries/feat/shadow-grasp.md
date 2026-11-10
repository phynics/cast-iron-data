+++
id = "ref/feat/shadow-grasp"
kind = "feat"
title = "Shadow Grasp"
aon = "FeatDisplay.aspx?ItemName=Shadow%20Grasp"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_grasp", path = "json/feat13.json" },
]
[[sources]]
publication = "inner-sea-magic"
page = "15"

[fields]
kind = "feat"
feat_types = ["Metamagic"]
prerequisites = "Tenebrous Spell, Umbral Spell."
prerequisite_feats = ["ref/feat/tenebrous-spell", "ref/feat/umbral-spell"]
benefit = "When you cast a spell with the darkness descriptor that affects an area, creatures in the area are entangled. If the spell allows a saving throw, a successful save negates the entangle effect. If the spell does not normally allow a save, a creature can make a Reflex save (DC = the spell's DC if it had a saving throw) to negate the effect. If the spell allows spell resistance, failing to overcome a creature's spell resistance means it is not entangled."
+++

## Shadow Grasp (Metamagic)

Your darkness spells have substance and bind your foes.\
**Prerequisites:** [Tenebrous Spell](ref/feat/tenebrous-spell),
[Umbral Spell](ref/feat/umbral-spell).\
**Benefit:** When you cast a spell with the darkness descriptor that affects an area, creatures in
the area are [entangled](ref/rule/entangled). If the spell allows a saving throw, a successful save
negates the entangle effect. If the spell does not normally allow a save, a creature can make a
Reflex save (DC = the spell's DC if it had a saving throw) to negate the effect. If the spell allows
[spell resistance](ref/rule/spell-resistance), failing to overcome a creature's spell resistance
means it is not entangled.

An entangled creature remains so as long as it is in the area of the spell and for 1 round after it
leaves. A creature that leaves and reenters the area must make a new saving throw to avoid becoming
entangled. Creatures that succeed at a save to resist being entangled do not have to make additional
saves if they stay within the darkened area.

You are never impeded by the effects of your spells modified by this feat. A Shadow Grasp spell uses
up a slot one level higher than the spell's actual level.
