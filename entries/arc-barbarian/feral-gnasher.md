+++
id = "ref/arc-barbarian/feral-gnasher"
kind = "archetype"
title = "Feral Gnasher"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Feral%20Gnasher"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feral_gnasher", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "advanced-race-guide"
page = "116"

[fields]
kind = "archetype"
features = [
  { anchor = "savage-bite", level = 1 },
  { anchor = "impromptu-armament", level = 2 },
  { anchor = "lockjaw", level = 3 },
  { anchor = "improvised-weapon-mastery", level = 5 },
  { anchor = "improved-lockjaw", level = 6 },
  { anchor = "greater-lockjaw", level = 9 },
  { anchor = "wicked-improvisation", level = 12 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["savage-bite"] },
  { replaces = "Rage power gained at second level", feature = "rage-powers", levels = [2], by = ["impromptu-armament"] },
  { replaces = "Trap sense +1", feature = "trap-sense", levels = [3], by = ["lockjaw"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["improvised-weapon-mastery"] },
  { replaces = "Trap sense +2", feature = "trap-sense", levels = [6], by = ["improved-lockjaw"] },
  { replaces = "Trap sense +3", feature = "trap-sense", levels = [9], by = ["greater-lockjaw"] },
  { replaces = "trap sense +5", feature = "trap-sense", levels = [15], by = ["greater-lockjaw"] },
  { replaces = "Trap sense +4", feature = "trap-sense", levels = [12], by = ["wicked-improvisation"] },
]
+++

Feral gnashers grow up in the wild, either raised by animals or scraping by on their own, and soon
learn to fend for themselves. These barbarians often utilize pieced-together armor and fight with
their sharp teeth and whatever improvised weapons are within reach. A feral gnasher has the
following class features.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A feral gnasher loses all martial weapon proficiencies except for
[greatclub](ref/eq-weapon/greatclub) and loses proficiency with medium armor.

## Savage Bite (Ex) {#savage-bite}

At 1st level, a feral gnasher gains a savage bite attack. This is a primary
[natural attack](ref/umr/natural-attacks) that deals 1d4 points of damage. If the goblin already has
the hard head, big teeth racial trait, the damage increases to 1d6. At 10th level, the damage from a
feral gnasher's bite increases to 1d6 (or 1d8 if the goblin has the hard head, big teeth racial
trait) and deals ×3 damage on a critical hit. This ability replaces fast movement.

## Impromptu Armament (Ex) {#impromptu-armament}

At 2nd level, a feral gnasher gains [Throw Anything](ref/feat/throw-anything) as a bonus feat and
can pick up an unattended object that can be wielded in one hand as a free action. Additionally, the
feral gnasher can take [Catch Off-Guard](ref/feat/catch-off-guard) in place of a rage power. This
replaces the rage power gained at second level.

## Lockjaw (Ex) {#lockjaw}

At 3rd level, a feral gnasher gains the [grab](ref/umr/grab) ability with her bite attack. A feral
gnasher can use this ability on a creature up to one size category larger than she is. This replaces
trap sense +1.

## Improvised Weapon Mastery (Ex) {#improvised-weapon-mastery}

At 5th level, a feral gnasher gains [Improvised Weapon Mastery](ref/feat/improvised-weapon-mastery)
as a bonus feat. This replaces improved uncanny dodge.

## Improved Lockjaw (Ex) {#improved-lockjaw}

At 6th level, as long as a feral gnasher is controlling the grapple with her
[lockjaw](ref/spell/lockjaw) attack, she does not gain the grappled condition, but is unable to move
or use her mouth for anything other than grappling. This ability replaces trap sense +2.

## Greater Lockjaw (Ex) {#greater-lockjaw}

At 9th level and again at 15th level, the size of a creature a feral gnasher is able to use her
lockjaw's grab ability on increases by one size increment. This ability replaces trap sense +3 and
trap sense +5.

## Wicked Improvisation (Ex) {#wicked-improvisation}

At 12th level, a feral gnasher becomes more capable with improvised weapons and natural attacks. The
feral gnasher gains a +1 competence bonus on damage rolls when using natural attacks or improvised
weapons while raging. At 14th level and every two levels thereafter, the damage bonus increases by
+1. This increase is not precision damage and is thus multiplied on a critical hit. This ability
replaces trap sense +4.

## Rage Powers {#rage-powers}

The following rage powers complement the feral gnasher archetype:
[increased damage reduction](ref/ragepower/increased-damage-reduction),
[scent](ref/ragepower/scent), [superstition](ref/ragepower/superstition) (_Core Rulebook_);
[beast totem](ref/ragepower/beast-totem), beast totem (greater), beast totem (lesser) (_Advanced
Player's Guide_); [eater of magic](ref/ragepower/eater-of-magic),
[ghost rager](ref/ragepower/ghost-rager) (_Ultimate Combat_).
