+++
id = "ref/arc-kineticist/psychokineticist"
kind = "archetype"
title = "Psychokineticist"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psychokineticist", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "horror-adventures"
page = "56"

[fields]
kind = "archetype"
alters = ["Class skills", "key ability score of wild talents", "Burn", "Elemental overflow"]
alters_features = ["burn", "elemental-overflow"]
+++

While most kineticists channel elemental power through their bodies, rare kineticists, such as
_elemental ascetics, overwhelming souls,_ and _psychokineticists_ channel such power through their
minds. Psychokineticists lack an _overwhelming soul's_ strong spirit, and so this energy ravages
their minds but unleashes power locked in their ruptured emotions. Sometimes a psychokineticist
inadvertently unleashes his power when he experiences an outburst of strong emotion, potentially
making a psychokineticist an outcast or even an accidental killer.

**Gained class skills:** sm

**Emotional Intensity (Ex)**

**Ability:** A psychokineticist uses his Wisdom modifier instead of his Constitution modifier to
determine his damage with wild talents, the DCs of Constitution-based wild talents, the durations of
wild talents with Constitution-based durations, his bonus on [concentration](ref/rule/concentration)
checks for wild talents, and other Constitution-based effects of all his wild talents.

**Alters:** Class skills, key ability score of wild talents

**Info:** He can't use any of his wild talents whenever he would be unable to use a spell with an
[emotion component](ref/rule/components-oa), and if he ever gains immunity to charm, compulsion,
emotion effects (even if such immunity extends only to a subcategory of these effects like fear
effects or compulsion effects from creatures of certain alignments), he loses all his kineticist
abilities. This includes effects that he previously activated that normally last until the next time
his burn is removed, like _elemental defenses,_ though he still keeps all his penalties from burn.
He can always choose to ignore such immunities when he would normally gain them, even if they are
granted by another class feature (such as the paladin's _aura of courage_), but once he decides
whether or not to ignore an immunity he would have gained, the choice cannot be changed.

**Special:** A psychokineticist gains [Psychic Sensitivity](ref/feat/psychic-sensitivity) as a bonus
feat.

**Mind Burn (Ex)**

**Alters:** Burn

**Flavor:** A psychokineticist's mind strains when he overtaxes himself.

**Passive:** He takes a -2 penalty on Will saves, Wisdom checks, and Wisdom-based skill checks for
each point of burn he has accepted, rather than taking nonlethal damage from burn. He can accept an
amount of burn equal to his Wisdom modifier (rather than 3 + his Wisdom modifier). Otherwise, his
burn works just like a normal kineticist's.

**Mental Overflow (Ex)**

**Ability:** Instead of gaining size bonuses to physical ability scores from _elemental overflow,_
he gains alchemical bonuses to his mental ability scores in equal amounts (a +2 alchemical bonus to
two mental ability scores at 6th level if he has at least 3 points of burn; a +4 alchemical bonus to
one mental ability score and a +2 alchemical bonus to the other two at 11th level if he has at least
5 points of burn; and a +6 alchemical bonus to one mental ability score, a +4 alchemical bonus to
another, and a +2 alchemical bonus to the last at 16th level if he has at least 7 points of burn).

**Alters:** Elemental overflow

**Flavor:** A psychokineticist's elemental energy sends strange elemental humors and planar echoes
through his brain instead of reshaping his body with matter from his element.

**Special:** A psychokineticist doesn't gain a chance to negate critical hits and sneak attacks
based on his burn. Otherwise, his _elemental overflow_ works just like a normal kineticist's.
