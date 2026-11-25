+++
id = "ref/arc-kineticist/psychokineticist"
kind = "archetype"
title = "Psychokineticist"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Psychokineticist"
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
features = [
  { anchor = "emotional-intensity" },
  { anchor = "mind-burn" },
  { anchor = "mental-overflow" },
  { anchor = "utility-wild-talents" },
]
trades = [
  { alters = "Class skills", by = ["emotional-intensity"] },
  { alters = "key ability score of wild talents", by = ["emotional-intensity"] },
  { alters = "Burn", feature = "burn", by = ["mind-burn"] },
  { alters = "Elemental overflow", feature = "elemental-overflow", by = ["mental-overflow"] },
]
+++

While most kineticists channel elemental power through their bodies, rare kineticists, such as
elemental ascetics, overwhelming souls, and psychokineticists channel such power through their
minds. Psychokineticists lack an overwhelming soul's strong spirit, and so this energy ravages their
minds but unleashes power locked in their ruptured emotions. Sometimes a psychokineticist
inadvertently unleashes his power when he experiences an outburst of strong emotion, potentially
making a psychokineticist an outcast or even an accidental killer.

## Emotional Intensity (Ex) {#emotional-intensity}

A psychokineticist uses his Wisdom modifier instead of his Constitution modifier to determine his
damage with wild talents, the DCs of Constitution-based wild talents, the durations of wild talents
with Constitution-based durations, his bonus on [concentration](ref/rule/concentration) checks for
wild talents, and other Constitution-based effects of all his wild talents.

He can't use any of his wild talents whenever he would be unable to use a spell with an
[emotion component](ref/rule/components-oa) (see page 144 of _Pathfinder RPG Occult Adventures_),
and if he ever gains immunity to charm, compulsion, emotion effects (even if such immunity extends
only to a subcategory of these effects like fear effects or compulsion effects from creatures of
certain alignments), he loses all his kineticist abilities. This includes effects that he previously
activated that normally last until the next time his burn is removed, like elemental defenses,
though he still keeps all his penalties from burn. He can always choose to ignore such immunities
when he would normally gain them, even if they are granted by another class feature (such as the
paladin's aura of courage), but once he decides whether or not to ignore an immunity he would have
gained, the choice cannot be changed.

A psychokineticist adds Sense Motive to his list of class skills and gains
[Psychic Sensitivity](ref/feat/psychic-sensitivity) as a bonus feat.

This ability alters the kineticist's class skills and the key ability score of wild talents.

## Mind Burn (Ex) {#mind-burn}

A psychokineticist's mind strains when he overtaxes himself. He takes a -2 penalty on Will saves,
Wisdom checks, and Wisdom-based skill checks for each point of burn he has accepted, rather than
taking nonlethal damage from burn. He can accept an amount of burn equal to his Wisdom modifier
(rather than 3 + his Wisdom modifier). Otherwise, his burn works just like a normal kineticist's.

This ability alters burn.

## Mental Overflow (Ex) {#mental-overflow}

A psychokineticist's elemental energy sends strange elemental humors and planar echoes through his
brain instead of reshaping his body with matter from his element. Instead of gaining size bonuses to
physical ability scores from elemental overflow, he gains alchemical bonuses to his mental ability
scores in equal amounts (a +2 alchemical bonus to two mental ability scores at 6th level if he has
at least 3 points of burn; a +4 alchemical bonus to one mental ability score and a +2 alchemical
bonus to the other two at 11th level if he has at least 5 points of burn; and a +6 alchemical bonus
to one mental ability score, a +4 alchemical bonus to another, and a +2 alchemical bonus to the last
at 16th level if he has at least 7 points of burn). A psychokineticist doesn't gain a chance to
negate critical hits and sneak attacks based on his burn. Otherwise, his elemental overflow works
just like a normal kineticist's.

This ability alters elemental overflow.

## UTILITY WILD TALENTS {#utility-wild-talents}

When most people talk to the flames, others call them mad. The following utility wild talents allow
the elements to speak back, after a fashion. ELEMENTAL WHISPERS Element universal; Type utility
(Su); Level 1; Burn 0 You form a friendship with a fragment of your element. The element speaks back
to you empathically, like a familiar. Pick a type of creature usually allowed as a familiar when you
gain this wild talent. You gain the Alertness feat and the special abilities granted by a familiar
of that type. As a standard action, you can give the voice of the element the body of such a
creature, using elemental matter of the appropriate element within 30 feet. As long as you
concentrate, the familiar can take actions as a normal animal of its type, and it can move any
distance away from you, though if it takes any damage or you cease concentrating, it returns to your
mind. You lose Alertness while the familiar is manifested in this way. The familiar gains abilities
as usual for a familiar of its type, though it never gains the ability to speak with animals of its
kind. ELEMENTAL WHISPERS, GREATER Element universal; Type utility (Su); Level 3; Burn 0 Prerequisite
elemental whispers Your friendship with the elements has grown. You gain your choice of a wysp or
Small elemental of your primary element as an improved familiar, without needing to meet any of the
usual prerequisites for gaining such a familiar. Unlike with elemental whispers, this improved
familiar acts in all ways like a familiar: it's always manifested, it has hit points equal to 1/2
your own, and so on. You no longer receive the familiar benefits from the original creature you
selected. If your improved familiar dies, you can still contact its voice in your mind and gain the
Alertness feat, but you can't cause it to manifest. If you pay the usual costs for replacing a
familiar, you manifest a new form for your elemental friend.
