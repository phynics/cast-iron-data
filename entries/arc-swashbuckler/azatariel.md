+++
id = "ref/arc-swashbuckler/azatariel"
kind = "archetype"
title = "Azatariel"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Azatariel"
source_ids = ["planar-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "azatariel", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "planar-adventures"
page = "10"

[fields]
kind = "archetype"
features = [
  { anchor = "deeds" },
  { anchor = "bralani-s-swiftness", level = 3 },
  { anchor = "whimsical-riposte", level = 3 },
  { anchor = "lillend-s-misdirection", level = 7 },
  { anchor = "ghaele-s-assault", level = 11 },
  { anchor = "elysian-conviction", level = 2 },
  { anchor = "battle-dance", level = 3 },
  { anchor = "affection-of-elysium", level = 4 },
]
trades = [
  { replaces = "Menacing swordplay deed", feature = "deeds", power = "menacing swordplay", by = ["bralani-s-swiftness"] },
  { replaces = "Precise strike deed", feature = "deeds", power = "precise strike", by = ["whimsical-riposte"] },
  { replaces = "Targeted strike deed", feature = "deeds", power = "targeted strike", by = ["lillend-s-misdirection"] },
  { replaces = "Bleeding wound deed", feature = "deeds", power = "bleeding wound", by = ["ghaele-s-assault"] },
  { replaces = "Charmed life", feature = "charmed-life", by = ["elysian-conviction"] },
  { replaces = "Nimble", feature = "nimble", by = ["battle-dance"] },
  { replaces = "The swashbuckler's bonus feats", feature = "bonus-feats", by = ["affection-of-elysium"] },
]
+++

Azatariels are the champions of Elysium, dedicated to spreading its unpredictable whimsy and
capricious goodness across the planes. Irrepressible and happy-golucky even in the face of the most
tyrannical devil, azatariels take their name from the azatas that they emulate. In battle,
azatariels exult in darting among their foes, heedless of danger. Mastery of combat's chaos allows
azatariels to turn enemies' strikes against each other, while supernatural good fortune protects
them from dire afflictions. When allies falter with fear or suffer the effects of dark magic, a
compassionate gesture from an azatariel cures their ills and spurs them onward.

## Alignment {#alignment}

An azatariel must be chaotic good. If an azatariel changes alignment, she loses all abilities
granted by this archetype until her alignment returns to chaotic good.

## Deeds {#deeds}

An azatariel gains the following deeds.

## Bralani's Swiftness (Ex) {#bralani-s-swiftness}

At 3rd level, while the azatariel has at least 1 point of panache, she ignores movement penalties
from [difficult terrain](ref/rule/terrain-and-obstacles).

This replaces the menacing swordplay deed.

## Whimsical Riposte (Ex) {#whimsical-riposte}

At 3rd level, the azatariel adds her Charisma modifier to attack and damage rolls made with light or
one-handed piercing weapons as part of her
[opportune parry and riposte](ref/swashdeed/opportune-parry-and-riposte) deed (including when
riposting). In addition, whenever the azatariel successfully parries an opponent's attack, instead
of riposting she can redirect that attack to another target as an immediate action. The new target
must be within the attacker's reach, and the attacker uses the original attack roll to determine the
attack's success.

This replaces the precise strike deed.

## Lillend's Misdirection (Ex) {#lillend-s-misdirection}

At 7th level, when a foe [flanking](ref/rule/flanking) the azatariel misses her with a melee attack,
the azatariel can spend 2 panache points as an immediate action to attempt a
[reposition](ref/rule/reposition) combat maneuver check against the attacking foe. If she succeeds
at the combat maneuver check, she and the attacking foe switch positions, and the melee attack roll
that missed the azatariel instead targets the flanking opponent that did not make the attack, using
the same attack roll result (including the bonus gained from flanking).

This replaces the targeted strike deed.

## Ghaele's Assault (Ex) {#ghaele-s-assault}

At 11th level, the azatariel can spend 2 panache points when charging. If she does, the AC penalty
for charging changes to -4 and she can make a full attack at the end of her charge.

This replaces the bleeding wound deed.

## Elysian Conviction (Su) {#elysian-conviction}

At 2nd level, while she has at least 1 panache point, an azatariel adds her Charisma bonus to her
saving throws against mind-affecting effects.

This replaces charmed life.

## Battle Dance (Ex) {#battle-dance}

At 3rd level and every 4 levels thereafter, an azatariel's base speed increases by 10 feet. This is
an enhancement bonus. An azatariel in medium or heavy armor or carrying a medium or heavy load loses
this extra speed.

This replaces nimble.

## Affection of Elysium (Su) {#affection-of-elysium}

An azatariel's affection relieves harmful afflictions. At 4th level and every 4 levels thereafter,
an azatariel selects a mercy from those available to a paladin whose class level is equal to her
swashbuckler level. She can show her affection to a willing, adjacent creature as a standard action
to apply the effects of these mercies to the targeted creature, treating her swashbuckler level as
her paladin level. An azatariel can use this ability a number of times per day equal to half her
swashbuckler level plus her Charisma modifier.

This replaces the swashbuckler's bonus feats.
