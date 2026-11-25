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
features = [
  { anchor = "leshy-eidolon" },
  { anchor = "summon-nature-s-ally" },
]
trades = [
  { alters = "Summon monster", feature = "summon-monster-i", by = ["summon-nature-s-ally"] },
]
+++

A leshy caller summons creatures from the First World and forges a bond with a leshy eidolon.

## Leshy Eidolon {#leshy-eidolon}

When a leshy caller summons her eidolon, the eidolon's body is created from extraplanar plant
material and imbued with the intelligence of a leshy spirit. Its statistics are changed from those
of a standard eidolon as follows. An unchained summoner uses the plant eidolon subtype (see page 95)
instead of one of the subtypes listed in _Pathfinder RPG Pathfinder Unchained_.

### Type {#type}

The eidolon is still an outsider, and its statistics don't change, but it also counts as a plant. As
it isn't truly a plant, it doesn't gain the plant immunities.

### Base Form {#base-form}

The leshy caller chooses one of the base forms listed below for her eidolon. When the eidolon is
summoned in an environment matching one of these base forms, the leshy caller can change the
eidolon's base form to the matching form by sacrificing one daily use of her
_[summon nature's ally](ref/spell/summon-natures-ally)_ ability as a free action.

Plant eidolon base forms are as follows.

_Cactus (Desert):_ Size Medium; Speed 30 ft.; AC +2 natural armor; Saves Fort (good), Ref (good),
Will (bad); Attack [sting](ref/evolution/sting) (1d4); Ability Scores Str 14, Dex 14, Con 13, Int 7,
Wis 10, Cha 11; Free Evolutions [limbs](ref/evolution/limbs) (arms), limbs (legs), sting.

_Conifer (Forest, Mountain):_ Size Medium; Speed 30 ft.; AC +2 natural armor; Saves Fort (good), Ref
(bad), Will (good); Attack 2 [claws](ref/evolution/claws) (1d4); Ability Scores Str 14, Dex 12, Con
15, Int 7, Wis 10, Cha 11; Free Evolutions claws, limbs (arms), limbs (legs).

_Fungus (Swamp, Underground):_ Size Medium; Speed 30 ft.; AC +2 natural armor; Saves Fort (good),
Ref (good), Will (bad); Attack [bite](ref/evolution/bite) (1d6); Ability Scores Str 14, Dex 14, Con
13, Int 7, Wis 10, Cha 11; Free Evolutions bite, limbs (arms), limbs (legs).

_Leaf (Forest, Jungle, Swamp):_ Size Medium; Speed 30 ft.; AC +2 natural armor; Saves Fort (good),
Ref (good), Will (bad); Attack [slam](ref/evolution/slam) (1d8); Ability Scores Str 16, Dex 12, Con
13, Int 7, Wis 10, Cha 11; Free Evolutions limbs (arms), limbs (legs), slam.

_Seaweed (Aquatic):_ Size Medium; Speed 20 ft., [swim](ref/evolution/swim) 40 ft.; AC +2 natural
armor; Saves Fort (good), Ref (good), Will (bad); Attack slam (1d8); Ability Scores Str 12, Dex 14,
Con 15, Int 7, Wis 10, Cha 11; Free Evolutions limbs (arms), slam, swim (2).

This alters the summoner's eidolon.

### PLANT EIDOLON SUBTYPE {#plant-eidolon-subtype}

Plant eidolons consist of vegetable matter infused with raw natural spiritual power.

#### Alignment {#alignment}

Any. Plant eidolons don't have alignment subtypes.

#### Base Form {#alignment-base-form}

Cactus (limbs \[arms\], limbs \[legs\], sting), conifer (claws, limbs \[arms\], limbs \[legs\]),
fungus (bite, limbs \[arms\], limbs \[legs\]), leaf (limbs \[arms\], limbs \[legs\], slam), seaweed
(limbs \[arms\], slam, swim \[2\]).

#### Base Evolutions {#base-evolutions}

At 1st level, plant eidolons gain low-light vision as well as the resistance (electricity) and
resistance (sonic) evolutions.

At 4th level, plant eidolons gain constant _pass without trace_ and they can change shape into
plants of the size category corresponding to their base form with results similar to _tree shape_.

At 8th level, plant eidolons gain the ability to use _speak with plants_ for 1 minute per Hit Die
per day with any plants related to the eidolon's base form. These minutes need not be consecutive.

At 12th level, plant eidolons gain immunity to paralysis, poison, sleep, and stun.

At 16th level, plant eidolons gain the ability to use _commune with nature_ once per day and can use
their _speak with plants_ ability at will. At 20th level, plant eidolons gain a +8 resistance bonus
on saving throws against mind-affecting effects. They lose their resistance (electricity) and
resistance (sonic) evolutions and instead gain the immunity (electricity) and immunity (sonic)
evolutions.

## Summon Nature's Ally (Sp) {#summon-nature-s-ally}

A leshy caller can cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
[spell-like ability](ref/umr/spell-like-abilities) a number of times per day equal to 3 + her
Charisma modifier. At levels where a regular summoner would gain access to a new level of
_[summon monster](ref/spell/summon-monster)_ as a
[spell-like ability](ref/umr/spell-like-abilities), the leshy caller instead gains the equivalent
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell; at 19th level, she can cast
_[summon nature's ally IX](ref/spell/summon-natures-ally-9)_ or _[gate](ref/spell/gate)_. When a
leshy caller gains a _[summon nature's ally](ref/spell/summon-natures-ally)_ spell as a
[spell-like ability](ref/umr/spell-like-abilities), she adds it to her class spell list (though she
must still select it as a spell known if she wants to gain the ability to cast it as a normal
spell). She adds [leaf leshys](ref/monster/leshy-leaf-leshy),
[gourd leshys](ref/monster/leshy-gourd-leshy), [fungus leshys](ref/monster/leshy-fungus-leshy),
[seaweed leshys](ref/monster/leshy-seaweed-leshy), and [lotus leshys](ref/monster/leshy-lotus-leshy)
to her list of creatures for _summon nature's ally I_, _II_, _III_, _IV_, and _V_, respectively.

This alters summon monster.
