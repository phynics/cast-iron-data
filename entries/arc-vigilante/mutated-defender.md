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
replaces = ["Vigilante specialization"]
alters = ["Vigilante talent"]
replaces_features = ["vigilante-specialization"]
alters_features = ["vigilante-talent"]
+++

Occasionally a mutation takes hold of the body of a vigilante, but he learns to hide his maladies,
usually through alchemical concoctions or magical concealment. Unlike other mutants, who are usually
shunned in Alkenstar and other settlements, mutated defenders can appear in public without revealing
their mutations - though they can still use them to their full potential in secret.

**Mutant Specialization**

**Ability:** A mutated defender gains a base attack bonus equal to his vigilante level instead of
using those listed in the vigilante's class table. He adds this value as normal to any other base
attack bonus gained from other classes or racial Hit Dice.

**Choice:** He also selects one [mutant deformity](ref/template/mutant) other than _mindless_ or
_vulnerability._ This deformity magically reverts when the vigilante is in his social identity, as
do all mutations from his mutant talents, allowing him to hide his mutation entirely. Unlike with
other vigilante talents, the vigilante is entirely unable to use the benefits of his mutant talents
while in his social identity.

**Replaces:** Vigilante specialization

**Mutant Talents**

**Ability:** A mutated defender can select from the following mutant talents, in addition to the
vigilante talents normally available to him.

**Alters:** Vigilante talent

**Mutant Blast (Su)**

**Ability:** One of the mutated defender's extremities becomes elementally warped, and he can
discharge a blast of energy from this limb. This functions as the _elemental ray_ bloodline power
(from the [elemental](ref/sorcbloodline/elemental) sorcerer bloodline) and uses his vigilante level
as his sorcerer level. The mutated defender chooses the damage type (acid, cold, electricity, or
fire) of his mutant blast when selecting this talent.

**Prereq:** 9th-level vigilante

**Text from the Elemental Ray Bloodline Power:** You can unleash an elemental ray as a **standard
action**, targeting any foe within 30 feet as a ranged touch attack. This ray deals an amount of
damage of your energy type equal to 1d6 + [half](ref/misc/fractions-and-rounding) of your sorcerer
level. You can use this ability a number of times per day equal to 3 + your Charisma modifier.

**Mutant Evolution**

**Ability:** The mutated defender gains a 1-point evolution from the eidolon list other than
[climb](ref/unchevolution/climb),
[improved natural armor](ref/unchevolution/improved-natural-armor),
[mount](ref/unchevolution/mount), [skilled](ref/unchevolution/skilled), or
[swim](ref/unchevolution/swim). He must meet any prerequisites as normal, using his vigilante level
for prerequisites that require a summoner level. He can select an evolution granting a natural
attack without fulfilling the subtype requirement, though he must replace one of his hands with the
natural weapon.

**Special:** A mutated defender can select this mutant talent multiple times, choosing a different
evolution each time.

**Mutated Lobe (Sp)**

**Ability:** A mutated defender's brain is enlarged and distended, granting him psychic powers. He
can cast [detect thoughts](ref/spell/detect-thoughts) as a
[spell-like ability](ref/umr/spell-like-abilities), with a caster level equal to his vigilante
level.

**Prereq:** 4th-level vigilante

**Usage:** 1 time/day per 4 vigilante levels
