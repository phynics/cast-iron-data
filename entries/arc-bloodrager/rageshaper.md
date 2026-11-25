+++
id = "ref/arc-bloodrager/rageshaper"
kind = "archetype"
title = "Rageshaper"
aon = "ArchetypeDisplay.aspx?FixedName=Bloodrager%20Rageshaper"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rageshaper", path = "json/archetypes_bloodrager.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/bloodrager" },
]
[[sources]]
publication = "advanced-class-guide"
page = "84"

[fields]
kind = "archetype"
features = [
  { anchor = "bestial-aspect", level = 4 },
  { anchor = "furious-transformation", level = 5 },
]
trades = [
  { replaces = "Blood sanctuary", feature = "blood-sanctuary", by = ["bestial-aspect"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["furious-transformation"] },
]
+++

All bloodragers blend the unpredictable surge of arcane power with the savage fury of battle lust.
For most, their rage is a conduit for the eldritch power locked in their heritage, but for a
rageshaper, the latent magical energies in his blood bring about physical transformations and
facilitate the blending of arcana and aggression into a deadly synthesis that few other barbarians
(or even other bloodragers) can match.

## Bestial Aspect (Su) {#bestial-aspect}

At 4th level, whenever a rageshaper gains a [natural attack](ref/rule/natural-attacks) through the
use of a polymorph spell, he can increase the damage done by that attack
[by one die](ref/misc/damage-die-adjustments). If the spell grants multiple natural attacks, the
rageshaper must choose one kind of natural attack for the ability to enhance. At 9th level, if the
rageshaper's altered form grants him a new mode of movement, that movement's base speed increases by
10 feet. This is an enhancement bonus. If the rageshaper's bloodrage powers already grant natural
attacks or alternate modes of movement, then the bonuses granted by bestial aspect also apply to
these bloodrage powers. This ability replaces blood sanctuary.

## Furious Transformation (Su) {#furious-transformation}

At 5th level, a rageshaper can attempt to bolster any transmutation spell from the bloodrager spell
list with the polymorph subschool while bloodraging. The rageshaper must succeed at a
[concentration](ref/rule/concentration) check as if casting defensively to modify the spell;
otherwise, the spell is wasted. If he succeeds, the spell is treated as if the rageshaper had the
[Extend Spell](ref/feat/extend-spell) metamagic feat. The rageshaper must be the spell's intended
target or cast a spell with a range of personal to gain this effect. If the rageshaper casts a spell
that is linked to the rageshaper's own bloodline, such as a rageshaper with the
[elemental](ref/blrgbloodline/elemental) bloodline who casts
_[elemental body I](ref/spell/elemental-body-1)_, the spell is automatically extended without
forcing the concentration check, so long as the rageshaper casts it while in a bloodrage. This
ability replaces improved uncanny dodge.
