+++
id = "ref/arc-swashbuckler/arrow-champion"
kind = "archetype"
title = "Arrow Champion"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Arrow%20Champion"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arrow_champion", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "95"

[fields]
kind = "archetype"
features = [
  { anchor = "arrow-champion-s-panache", level = 1 },
  { anchor = "deeds" },
  { anchor = "retaliation" },
  { anchor = "precise-aim", level = 3 },
  { anchor = "swift-switch", level = 3 },
  { anchor = "archer-s-feint", level = 7 },
  { anchor = "weapon-versatility", level = 5 },
  { anchor = "versatile-weapon-mastery", level = 20 },
]
trades = [
  { replaces = "Opportune parry and riposte", feature = "deeds", power = "opportune parry and riposte", by = ["retaliation"] },
  { replaces = "Swashbuckler's initiative", feature = "deeds", power = "swashbuckler initiative", by = ["swift-switch"] },
  { replaces = "Superior feint", feature = "deeds", power = "superior feint", by = ["archer-s-feint"] },
  { replaces = "Swashbuckler weapon training", feature = "swashbuckler-weapon-training", by = ["weapon-versatility"] },
  { alters = "Panache", feature = "panache", by = ["arrow-champion-s-panache"] },
  { alters = "Precise strike", feature = "deeds", power = "precise strike", by = ["precise-aim"] },
  { alters = "Swashbuckler weapon mastery", feature = "swashbuckler-weapon-mastery", by = ["versatile-weapon-mastery"] },
]
+++

While the swashbuckler's agile style of combat is equally suited to urban settings and wilderness,
the bow and arrow is an indispensable asset in open areas and harsh terrain where fancy footwork
isn't enough to close the distance or dodge the enemy's arrows.

## Arrow Champion's Panache (Ex) {#arrow-champion-s-panache}

An arrow champion regains panache when she makes a killing blow with a light or one-handed piercing
melee weapon or a bow (a [longbow](ref/eq-weapon/longbow), [shortbow](ref/eq-weapon/shortbow),
[composite longbow](ref/eq-weapon/composite-longbow), or
[composite shortbow](ref/eq-weapon/composite-shortbow)).

This alters panache.

## Deeds {#deeds}

An arrow champion gains the following deeds, each of which replaces an existing deed.

## Retaliation (Ex) {#retaliation}

When a foe hits the arrow champion with an attack, she can spend 1 panache point to make a
retaliatory attack of opportunity against that foe. If the triggering attack is a melee attack, she
can retaliate with a melee attack using a light or one-handed piercing melee weapon, provided the
creature is within her reach. If the triggering attack is a ranged attack, she can retaliate with a
ranged attack using a bow, provided that the creature is within 30 feet of her. This deed's cost
cannot be reduced by any ability or effect that reduces the number of panache points a deed costs.

This deed replaces opportune parry and riposte.

## Precise Aim (Ex) {#precise-aim}

At 3rd level, when attacking with a light or one-handed piercing melee weapon, an arrow champion can
add her swashbuckler level to the damage she deals, as the swashbuckler's
[precise strike](ref/swashdeed/precise-strike) deed. She can also add
[one-quarter](ref/misc/fractions-and-rounding) of her swashbuckler level to the damage dealt when
attacking with a bow, but the target must be within 30 feet of her. As a swift action, an arrow
champion can spend 1 panache point to increase the range of the effect to her bow's first range
increment. Unlike a normal swashbuckler, an arrow champion cannot spend panache to double the extra
damage.

This deed alters precise strike.

## Swift Switch (Ex) {#swift-switch}

At 3rd level, while the arrow champion has at least 1 panache point, she can sheathe or draw an
unhidden light or one-handed piercing melee weapon or a bow as a swift action without provoking
attacks of opportunity. If the arrow champion spends 1 panache point, she can perform either action
as an immediate action. In addition, if she has the [Quick Draw](ref/feat/quick-draw) feat and one
of her hands is free, she can sheathe a weapon and draw an unhidden weapon as part of the same swift
action, provided that one of the weapons is a bow and the other is a light or one-handed piercing
melee weapon. If she spends 1 panache point, she can perform the switch as an immediate action.

This deed replaces swashbuckler's initiative.

## Archer's Feint (Ex) {#archer-s-feint}

At 7th level, when the arrow champion hits a foe within 30 feet with a bow attack, she can forgo the
damage and instead attempt a [Bluff](ref/skill/bluff) check to feint against that foe as a swift
action. If successful, in addition to the normal benefits of feinting, she doubles the extra damage
from precise aim on her next melee attack before the end of her next turn.

This deed replaces superior feint.

## Weapon Versatility (Ex) {#weapon-versatility}

At 5th level, an arrow champion learns to use precision-based tricks just as accurately with her bow
as with her melee weapons. Provided that her swashbuckler level is high enough, she can use the
[bleeding wound](ref/swashdeed/bleeding-wound), [deadly stab](ref/swashdeed/deadly-stab),
[menacing swordplay](ref/swashdeed/menacing-swordplay),
[perfect thrust](ref/swashdeed/perfect-thrust), [stunning stab](ref/swashdeed/stunning-stab), and
targeted strike deeds when attacking with a bow, so long as her target is within 30 feet. If she
spends a panache point to increase the range of her precise aim ability, the increased range applies
to this ability as well.

This replaces swashbuckler weapon training.

## Versatile Weapon Mastery (Ex) {#versatile-weapon-mastery}

At 20th level, an arrow champion gains the benefits of swashbuckler weapon mastery when using a
light or one-handed piercing melee weapon or a bow.

This alters swashbuckler weapon mastery.
