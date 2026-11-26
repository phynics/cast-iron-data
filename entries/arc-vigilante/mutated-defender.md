+++
id = "ref/arc-vigilante/mutated-defender"
kind = "archetype"
title = "Mutated Defender"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Mutated%20Defender"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mutated_defender", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "9"

[fields]
kind = "archetype"
features = [
  { anchor = "mutant-specialization", level = 1 },
  { anchor = "mutant-talents", level = 2 },
  { anchor = "mutant-blast" },
  { anchor = "mutated-lobe" },
]
trades = [
  { replaces = "Vigilante specialization", feature = "vigilante-specialization", by = ["mutant-specialization"] },
  { alters = "Vigilante talent", feature = "vigilante-talent", by = ["mutant-talents"] },
]
+++

Occasionally a mutation takes hold of the body of a vigilante (_Pathfinder RPG Ultimate Intrigue_
9), but he learns to hide his maladies, usually through alchemical concoctions or magical
concealment. Unlike other mutants, who are usually shunned in Alkenstar and other settlements,
mutated defenders can appear in public without revealing their mutations—though they can still use
them to their full potential in secret.

## Mutant Specialization {#mutant-specialization}

A mutated defender gains a base attack bonus equal to his vigilante level instead of using those
listed in the vigilante's class table (_Ultimate Intrigue_ 10). He adds this value as normal to any
other base attack bonus gained from other classes or racial Hit Dice. He also selects one
[mutant deformity](ref/template/mutant) other than mindless or vulnerability. This deformity
magically reverts when the vigilante is in his social identity, as do all mutations from his mutant
talents, allowing him to hide his mutation entirely. Unlike with other vigilante talents, the
vigilante is entirely unable to use the benefits of his mutant talents while in his social identity.

This replaces vigilante specialization.

## Mutant Talents {#mutant-talents}

At 2nd level and every 2 vigilante levels thereafter, a mutated defender can select from the
following mutant talents, in addition to the vigilante talents normally available to him.

This alters vigilante talent.

## Mutant Blast (Su) {#mutant-blast}

One of the mutated defender's extremities becomes elementally warped, and he can discharge a blast
of energy from this limb. This functions as the [elemental](ref/sorcbloodline/elemental) ray
bloodline power and uses his vigilante level as his sorcerer level. The mutated defender chooses the
damage type (acid, cold, electricity, or fire) of his mutant blast when selecting this talent. The
mutated defender must be at least 9th level to select this talent.

### Mutant Evolution {#mutant-evolution}

The mutated defender gains a 1-point evolution from the eidolon list (_Pathfinder RPG Pathfinder
Unchained_ 35) other than [climb](ref/unchevolution/climb),
[improved natural armor](ref/unchevolution/improved-natural-armor),
[mount](ref/unchevolution/mount), [skilled](ref/unchevolution/skilled), or
[swim](ref/unchevolution/swim). He must meet any prerequisites as normal, using his vigilante level
for prerequisites that require a summoner level. He can select an evolution granting a natural
attack without fulfilling the subtype requirement, though he must replace one of his hands with the
natural weapon. A mutated defender can select this mutant talent multiple times, choosing a
different evolution each time.

## Mutated Lobe (Sp) {#mutated-lobe}

A mutated defender's brain is enlarged and distended, granting him psychic powers. He can cast
_[detect thoughts](ref/spell/detect-thoughts)_ as a
[spell-like ability](ref/umr/spell-like-abilities) once per day for every 4 vigilante levels he has,
with a caster level equal to his vigilante level. A vigilante must be at least 4th level to select
this talent.
