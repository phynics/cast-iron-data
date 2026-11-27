+++
id = "ref/arc-summoner/wild-caller-hotw"
kind = "archetype"
title = "Wild Caller (HotW)"
aon = "ArchetypeDisplay.aspx?FixedName=Summoner%20Wild%20Caller%20%28HotW%29"
source_ids = ["heroes-of-the-wild"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wild_caller_hotw", path = "json/archetypes_summoner.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/summoner" },
]
[[sources]]
publication = "heroes-of-the-wild"
page = "25"

[fields]
kind = "archetype"
features = [
  { anchor = "plant-eidolon", level = 1 },
  { anchor = "summon-nature-s-ally", level = 1 },
  { anchor = "fey-friend", level = 10 },
]
trades = [
  { replaces = "Aspect, which is instead gained at 18th level in place of greater aspect", feature = "aspect", by = ["fey-friend"] },
  { alters = "Summon monster", feature = "summon-monster-i", by = ["summon-nature-s-ally"] },
  { alters = "the summoner's eidolon", feature = "eidolon", by = ["plant-eidolon"] },
]
+++

A wild caller summons creatures from the First World and forges a bond with an eidolon with a plant
body.

## Plant Eidolon {#plant-eidolon}

When a wild caller summons his eidolon, the eidolon's body is created from extraplanar plant
material and imbued with the intelligence of a being from the First World. Its statistics are
changed from a standard eidolon as follows.

### Type {#type}

The eidolon has the [plant](ref/type/plant) creature type and [extraplanar](ref/subtype/extraplanar)
subtype. Unlike other plant creatures, the eidolon is not immune to mind-affecting or polymorph
effects, though it does gain immunity to paralysis, [poison](ref/evolution/poison), sleep effects,
and stunning.

### Base Form {#base-form}

The wild caller chooses one of the base forms listed below for his plant eidolon. When the eidolon
is summoned in an environment matching one of these base forms, the wild caller can choose to change
the eidolon's base form to the matching form by sacrificing one daily use of his
_[summon nature's ally](ref/spell/summon-natures-ally)_ ability as a free action.

Plant eidolon base forms are as follows.

### Cactus (desert) {#cactus-desert}

Size Medium; Speed 30 ft.; AC +2 natural armor; Saves Fort (good), Ref (good), Will (bad); Attacks
[slam](ref/evolution/slam) (1d8), [sting](ref/evolution/sting) (1d4); Ability Scores Str 14, Dex 14,
Con 13, Int 7, Wis 10, Cha 11; Free Evolutions [limbs](ref/evolution/limbs) (arms), limbs (legs),
sting, [tail](ref/evolution/tail).

### Conifer (forest, mountain) {#conifer-forest-mountain}

Size Medium; Speed 30 ft.; AC +2 natural armor; Saves Fort (good), Ref (bad), Will (good); Attacks 2
[claws](ref/evolution/claws) (1d4); Ability Scores Str 14, Dex 12, Con 15, Int 7, Wis 10, Cha 11;
Resist cold 10; Free Evolutions claws, limbs (arms), limbs (legs),
[resistance](ref/evolution/resistance) (cold).

### Mushroom (swamp, underground) {#mushroom-swamp-underground}

Size Medium; Speed 20 ft.; AC +2 natural armor; Saves Fort (good), Ref (good), Will (bad); Attack
[bite](ref/evolution/bite) (1d6) plus poison; Ability Scores Str 14, Dex 14, Con 13, Int 7, Wis 10,
Cha 11; Free Evolutions bite, limbs (arms), limbs (legs), poison.

### Tree (forest, jungle, swamp) {#tree-forest-jungle-swamp}

Size Medium; Speed 20 ft.; AC +4 natural armor; Saves Fort (good), Ref (good), Will (bad); Attacks 2
slams (1d8); Ability Scores Str 16, Dex 12, Con 13, Int 7, Wis 10, Cha 11; Free Evolutions
[improved natural armor](ref/evolution/improved-natural-armor), limbs (arms), limbs (legs), slam ×2.

This ability alters the summoner's eidolon.

## Summon Nature's Ally (Sp) {#summon-nature-s-ally}

A wild caller can cast _[summon nature's ally](ref/spell/summon-natures-ally)_ as a
[spell-like ability](ref/umr/spell-like-abilities) a number of times per day equal to 3 + his
Charisma modifier. At levels where a regular summoner would gain access to a new level of
_[summon monster](ref/spell/summon-monster)_ as a
[spell-like ability](ref/umr/spell-like-abilities), the wild caller instead gains the equivalent
_[summon nature's ally](ref/spell/summon-natures-ally)_ spell; at 19th level, he can use
_[summon nature's ally IX](ref/spell/summon-natures-ally-9)_ or _[gate](ref/spell/gate)_. When a
wild caller gains a _[summon nature's ally](ref/spell/summon-natures-ally)_ spell as a
[spell-like ability](ref/umr/spell-like-abilities), he adds it to his class spell list (though he
must still select it as a spell known if he wants to gain the ability to cast it as a normal spell).
This ability alters the _summon monster_ ability.

## Fey Friend (Ex) {#fey-friend}

At 10th level, the wild caller gains a +4 bonus on Bluff, Diplomacy, and Sense Motive checks against
fey. This ability replaces aspect, which is instead gained at 18th level in place of greater aspect.
