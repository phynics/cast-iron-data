+++
id = "ref/arc-summoner/leshy-caller"
kind = "archetype"
title = "Leshy Caller"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Leshy%20Caller"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "leshy_caller", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "94"

[fields]
kind = "archetype"
alters = ["Summon monster"]
+++

A leshy caller summons creatures from the First World and forges a bond with a leshy eidolon.

**Leshy Eidolon**

**Info:** When a leshy caller summons her eidolon, the eidolon's body is created from extraplanar
plant material and imbued with the intelligence of a leshy spirit. Its statistics are changed from
those of a standard eidolon as shown below.

**Type**

**Info:** The eidolon is still an outsider, and its statistics don't change, but it also counts as a
plant. As it isn't truly a plant, it doesn't gain the plant immunities.

;;;ab\{head title="Base Form" icon=info action=Info alter=Eidolon\}

The leshy caller chooses one of the base forms listed below for her eidolon. When the eidolon is
summoned in an environment matching one of these base forms, the leshy caller can change the
eidolon's base form to the matching form by sacrificing one daily use of her
_[summon nature's ally](ref/spell/summon-natures-ally)_ ability as a **free action**.

Plant eidolon base forms are as follows.

### Cactus (Desert)

**Size**

**Details:** Medium

**Speed**

**Details:** 30 ft.

**AC**

**Details:** +2 natural armor

**Saves**

**Details:** Fort (good), Ref (good), Will (bad)

**Attack**

**Details:** sting (1d4)

**Ability Scores**

**Details:** Str 14, Dex 14, Con 13, Int 7, Wis 10, Cha 11

**Free Evolutions**

**Details:** [limbs](ref/evolution/limbs) (arms), limbs (legs), [sting](ref/evolution/sting)

### Conifer (Forest, Mountain)

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

**Details:** Str 14, Dex 12, Con 15, Int 7, Wis 10, Cha 11

**Free Evolutions**

**Details:** [claws](ref/evolution/claws), [limbs](ref/evolution/limbs) (arms), limbs (legs)

### Fungus (Swamp, Underground)

**Size**

**Details:** Medium

**Speed**

**Details:** 30 ft.

**AC**

**Details:** +2 natural armor

**Saves**

**Details:** Fort (good), Ref (good), Will (bad)

**Attack**

**Details:** bite (1d6)

**Ability Scores**

**Details:** Str 14, Dex 14, Con 13, Int 7, Wis 10, Cha 11

**Free Evolutions**

**Details:** [bite](ref/evolution/bite), [limbs](ref/evolution/limbs) (arms), limbs (legs)

### Leaf (Forest, Jungle, Swamp)

**Size**

**Details:** Medium

**Speed**

**Details:** 30 ft.

**AC**

**Details:** +2 natural armor

**Saves**

**Details:** Fort (good), Ref (good), Will (bad)

**Attack**

**Details:** slam (1d8)

**Ability Scores**

**Details:** Str 16, Dex 12, Con 13, Int 7, Wis 10, Cha 11

**Free Evolutions**

**Details:** [limbs](ref/evolution/limbs) (arms), limbs (legs), [slam](ref/evolution/slam)

### Seaweed (Aquatic)

**Size**

**Details:** Medium

**Speed**

**Details:** 20 ft., swim 40 ft.

**AC**

**Details:** +2 natural armor

**Saves**

**Details:** Fort (good), Ref (good), Will (bad)

**Attack**

**Details:** slam (1d8)

**Ability Scores**

**Details:** Str 12, Dex 14, Con 15, Int 7, Wis 10, Cha 11

**Free Evolutions**

**Details:** [limbs](ref/evolution/limbs) (arms), [slam](ref/evolution/slam),
[swim](ref/evolution/swim) (2)

;;;

**Summon Nature's Ally (Sp)**

**Ability:** A leshy caller can cast [summon nature's ally](ref/spell/summon-natures-ally) as a
[spell-like ability](ref/umr/spell-like-abilities) a number of times per day equal to 3 + her
Charisma modifier.

**Alters:** Summon monster

**Info:** At levels where a regular summoner would gain access to a new level of
_[summon monster](ref/spell/summon-monster)_ as a
[spell-like ability](ref/umr/spell-like-abilities), the leshy caller instead gains the equivalent
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell; at 19th level, she can cast
[summon nature's ally IX](ref/spell/summon-natures-ally-9) or [gate](ref/spell/gate).

**Passive:** When a leshy caller gains a _[summon nature's ally](ref/spell/summon-natures-ally)_
spell as a [spell-like ability](ref/umr/spell-like-abilities), she adds it to her class spell list
(though she must still select it as a spell known if she wants to gain the ability to cast it as a
normal spell). She adds [leaf leshys](ref/monster/leshy-leaf-leshy),
[gourd leshys](ref/monster/leshy-gourd-leshy), [fungus leshys](ref/monster/leshy-fungus-leshy),
[seaweed leshys](ref/monster/leshy-seaweed-leshy), and [lotus leshys](ref/monster/leshy-lotus-leshy)
to her list of creatures for _summon nature's ally I, II, III, IV,_ and _V,_ respectively.
