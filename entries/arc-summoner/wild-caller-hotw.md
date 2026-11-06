+++
id = "ref/arc-summoner/wild-caller-hotw"
kind = "archetype"
title = "Wild Caller (HotW)"
source_ids = ["heroes-of-the-wild"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_caller_hotw", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]

[fields]
kind = "none"
+++

**Sources:** Heroes of the Wild pg 25\
A wild caller summons creatures from the First World and forges a bond with an eidolon with a plant
body.

**Plant Eidolon**

**Info:** When a wild caller summons his eidolon, the eidolon's body is created from extraplanar
plant material and imbued with the intelligence of a being from the First World. Its statistics are
changed from a standard eidolon as shown below.

**Type**

**Info:** The eidolon has the [plant](ref/type/plant) creature type and
[extraplanar](ref/subtype/extraplanar) subtype. Unlike other plant creatures, the eidolon is not
immune to mind-affecting or polymorph effects, though it does gain immunity to paralysis, poison,
sleep effects, and stunning.

;;;ab\{head title="Base Form" icon=info action=Info alter=Eidolon\}

The wild caller chooses one of the base forms listed below for his plant eidolon. When the eidolon
is summoned in an environment matching one of these base forms, the wild caller can choose to change
the eidolon's base form to the matching form by sacrificing one daily use of his
_[summon nature's ally](ref/spell/summon-natures-ally)_ ability as a **free action**.

Plant eidolon base forms are as follows.

### Cactus (desert)

**Size**

**Details:** Medium

**Speed**

**Details:** 30 ft.

**AC**

**Details:** +2 natural armor

**Saves**

**Details:** Fort (good), Ref (good), Will (bad)

**Attack**

**Details:** slam (1d8), sting (1d4)

**Ability Scores**

**Details:** Str 14, Dex 14, Con 13, Int 7, Wis 10, Cha 11

**Free Evolutions**

**Details:** [limbs](ref/evolution/limbs) (arms), limbs (legs), [sting](ref/evolution/sting),
[tail](ref/evolution/tail)

### Conifer (forest, mountain)

**Size**

**Details:** Medium

**Speed**

**Details:** 30 ft.

**AC**

**Details:** +2 natural armor

**Saves**

**Details:** Fort (good), Ref (bad), Will (good)

**Attack**

**Details:** 2 claws (1d4)

**Ability Scores**

**Details:** Str 14, Dex 12, Con 15, Int 7, Wis 10, Cha 11; Resist cold 10

**Free Evolutions**

**Details:** [claws](ref/evolution/claws), [limbs](ref/evolution/limbs) (arms), limbs (legs),
[resistance](ref/evolution/resistance) (cold)

### Mushroom (swamp, underground)

**Size**

**Details:** Medium

**Speed**

**Details:** 20 ft.

**AC**

**Details:** +2 natural armor

**Saves**

**Details:** Fort (good), Ref (good), Will (bad)

**Attack**

**Details:** bite (1d6) plus poison

**Ability Scores**

**Details:** Str 14, Dex 14, Con 13, Int 7, Wis 10, Cha 11

**Free Evolutions**

**Details:** [bite](ref/evolution/bite), [limbs](ref/evolution/limbs) (arms), limbs (legs),
[poison](ref/evolution/poison)

### Tree (forest, jungle, swamp)

**Size**

**Details:** Medium

**Speed**

**Details:** 20 ft.

**AC**

**Details:** +4 natural armor

**Saves**

**Details:** Fort (good), Ref (good), Will (bad)

**Attack**

**Details:** 2 slams (1d8)

**Ability Scores**

**Details:** Str 16, Dex 12, Con 13, Int 7, Wis 10, Cha 11

**Free Evolutions**

**Details:** [improved natural armor](ref/evolution/improved-natural-armor),
[limbs](ref/evolution/limbs) (arms), limbs (legs), [slam](ref/evolution/slam) &times&2

;;;

**Summon Nature's Ally (Sp)**

**Ability:** A wild caller can cast [summon nature's ally](ref/spell/summon-natures-ally) as a
[spell-like ability](ref/umr/spell-like-abilities) a number of times per day equal to 3 + his
Charisma modifier.

**Alters:** Summon monster

**Info:** At levels where a regular summoner would gain access to a new level of
_[summon monster](ref/spell/summon-monster)_ as a
[spell-like ability](ref/umr/spell-like-abilities), the wild caller instead gains the equivalent
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell; at 19th level, he can use
[summon nature's ally IX](ref/spell/summon-natures-ally-9) or [gate](ref/spell/gate).

**Passive:** When a wild caller gains a _[summon nature's ally](ref/spell/summon-natures-ally)_
spell as a [spell-like ability](ref/umr/spell-like-abilities), he adds it to his class spell list
(though he must still select it as a spell known if he wants to gain the ability to cast it as a
normal spell).

**Fey Friend (Ex)**

**Gained:** At 10th Level

**Passive:** The wild caller gains a +4 bonus on Bluff, Diplomacy, and Sense Motive checks against
fey.

**Replaces:** Aspect

**Aspect**

**Gained:** At 18th Level

**Passive:** The wild caller gains the _aspect_ ability of a normal summoner.

**Replaces:** Greater aspect
