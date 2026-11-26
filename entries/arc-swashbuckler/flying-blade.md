+++
id = "ref/arc-swashbuckler/flying-blade"
kind = "archetype"
title = "Flying Blade"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Flying%20Blade"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flying_blade", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "124"

[fields]
kind = "archetype"
features = [
  { anchor = "panache", level = 1 },
  { anchor = "deeds" },
  { anchor = "subtle-throw", level = 1 },
  { anchor = "disrupting-counter", level = 3 },
  { anchor = "precise-throw", level = 3 },
  { anchor = "targeted-throw", level = 7 },
  { anchor = "bleeding-wound", level = 11 },
  { anchor = "perfect-throw", level = 15 },
  { anchor = "flying-blade-training", level = 5 },
  { anchor = "flying-blade-mastery", level = 20 },
]
trades = [
  { replaces = "Dodging panache", feature = "deeds", power = "dodging panache", by = ["subtle-throw"] },
  { replaces = "Kip-up", feature = "deeds", power = "kip-up", by = ["disrupting-counter"] },
  { replaces = "Menacing swordplay", feature = "deeds", power = "menacing swordplay", by = ["precise-throw"] },
  { replaces = "Targeted strike", feature = "deeds", power = "targeted strike", by = ["targeted-throw"] },
  { replaces = "Perfect thrust", feature = "deeds", power = "perfect thrust", by = ["perfect-throw"] },
  { replaces = "Swashbuckler weapon training", feature = "swashbuckler-weapon-training", by = ["flying-blade-training"] },
  { replaces = "Swashbuckler weapon mastery", feature = "swashbuckler-weapon-mastery", by = ["flying-blade-mastery"] },
  { alters = "Panache", feature = "panache", by = ["panache"] },
  { alters = "Bleeding wound", feature = "deeds", power = "bleeding wound", by = ["bleeding-wound"] },
]
+++

While most swashbucklers prefer their battles up close, others prefer dealing death from a distance.

## Panache {#panache}

Unlike other swashbucklers, a flying blade regains panache only when she confirms a critical hit or
makes a killing blow with a [dagger](ref/eq-weapon/dagger) or [starknife](ref/eq-weapon/starknife).
This ability alters panache.

## Deeds {#deeds}

A flying blade gains the following deeds, each of which replaces an existing deed.

## Subtle Throw (Ex) {#subtle-throw}

At 1st level, a flying blade can spend 1 panache point as part of a ranged attack with a dagger or
starknife to make it without provoking attacks of opportunity. At 6th level, as a swift action she
can spend 1 panache point to make all of her ranged attacks with daggers or starknives without
provoking attacks of opportunity until the start of her next turn. This deed replaces dodging
panache.

## Disrupting Counter (Ex) {#disrupting-counter}

At 3rd level, when an opponent makes a melee attack against her, she can spend 1 panache point to
make an attack of opportunity against the attacking foe. This attack of opportunity can be made with
either a dagger or a starknife. If the attack hits, the opponent takes a -4 penalty on all attack
rolls until the end of its turn. This deed replaces kip-up.

## Precise Throw (Ex) {#precise-throw}

At 3rd level, as long as she has at least 1 panache point, a flying blade can use her
[precise strike](ref/swashdeed/precise-strike) with a thrown dagger or starknife as long as the
target is within 60 feet of her, and she increases the range increment of these weapons by 5 feet.
She can spend 1 panache point when she throws a dagger or a starknife to ignore all range increment
penalties with that ranged attack. This deed replaces menacing swordplay.

## Targeted Throw (Ex) {#targeted-throw}

At 7th level, a flying blade can target individual body parts. This deed functions as the
swashbuckler's targeted strike deed, but the flying blade can also use this deed when making ranged
attacks with either a dagger or a starknife as long as the target is within 60 feet of the flying
blade. This deed replaces targeted strike.

## Bleeding Wound (Ex) {#bleeding-wound}

At 11th level, a flying blade can deal [bleed](ref/umr/bleed) damage as part of an attack. This deed
functions as the swashbuckler's [bleeding wound](ref/swashdeed/bleeding-wound) deed, but the flying
blade can also use this deed when making ranged attacks with either a dagger or a starknife as long
as the target is within 60 feet of the flying blade. This deed alters bleeding wound.

## Perfect Throw (Ex) {#perfect-throw}

At 15th level, a flying blade can pool all of her attack potential into a single attack. This deed
functions as the swashbuckler's [perfect thrust](ref/swashdeed/perfect-thrust) deed, but the flying
blade must use this deed when making ranged attacks with either a dagger or a starknife, and she can
use this deed only on targets within 60 feet of her. This deed replaces perfect thrust.

## Flying Blade Training (Ex) {#flying-blade-training}

At 5th level, a flying blade gains a +1 bonus on attack and damage rolls when using daggers or
starknives in combat. When a flying blade wields a dagger or starknife, she gains the benefit of the
[Improved Critical](ref/feat/improved-critical) feat with those weapons. Additionally, a flying
blade increases the range increment of a thrown dagger or starknife by 5 feet. The increase of range
increment stacks with that of precise throw.

Every 4 levels thereafter, the bonus on attack and damage rolls increases by 1, and the range
increment increases by 5 feet. This ability replaces swashbuckler weapon training.

## Flying Blade Mastery (Ex) {#flying-blade-mastery}

At 20th level, when an attack that a flying blade makes with a dagger or starknife threatens a
critical hit, that critical hit is automatically confirmed. Furthermore, the critical modifiers of
daggers and starknives increase by 1 (×2 becomes ×3, and so on). This ability replaces swashbuckler
weapon mastery.
