+++
id = "ref/arc-monk/monk-of-the-empty-hand"
kind = "archetype"
title = "Monk of the Empty Hand"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Monk%20of%20the%20Empty%20Hand"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "monk_of_the_empty_hand", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "advanced-players-guide"
page = "111"

[fields]
kind = "archetype"
features = [
  { anchor = "flurry-of-blows", level = 1 },
  { anchor = "bonus-feat" },
  { anchor = "versatile-improvisation", level = 3 },
  { anchor = "ki-pool", level = 4 },
  { anchor = "ki-weapons", level = 5 },
]
trades = [
  { replaces = "Normal monk weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { replaces = "Still mind", feature = "still-mind", by = ["versatile-improvisation"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["ki-weapons"] },
  { replaces = "diamond body", feature = "diamond-body", by = ["ki-weapons"] },
  { alters = "Flurry of blows", feature = "flurry-of-blows", by = ["flurry-of-blows"] },
]
+++

The monk of the empty hand eschews normal weapons in favor of whatever is lying around—rocks, chair
legs, flagons of ale, even a simple quill pen all become deadly weapons in the hands of such a monk.
A monk of the empty hand draws on his own _ki_ to infuse his improvised weapons with power, and can
transform a broken bottle into a magical weapon.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Monks of the empty hand are proficient with the [shuriken](ref/eq-weapon/shuriken) only. A monk of
the empty hand treats normal weapons as [improvised weapons](ref/misc/improvised-weapons) with the
following equivalencies (substituting all of their statistics for the listed weapon): a light weapon
functions as a [light hammer](ref/eq-weapon/light-hammer), a one-handed weapon functions as a
[club](ref/eq-weapon/club), and a two-handed weapon functions as a
[quarterstaff](ref/eq-weapon/quarterstaff). This replaces the normal monk weapon proficiencies.

## Flurry of Blows (Ex) {#flurry-of-blows}

Starting at 1st level, a monk of the empty hand can make a flurry of blows using any combination of
unarmed strikes or attacks with an improvised weapon. He may not make a flurry of blows with any
other weapons, including special monk weapons. A monk of the empty hand's flurry of blows otherwise
functions as normal for a monk of his level.

## Bonus Feat {#bonus-feat}

A monk of the empty hand adds the following feats to his list of bonus feats at 6th level:
[Improved Dirty Trick](ref/feat/improved-dirty-trick), [Improved Steal](ref/feat/improved-steal),
and [Improvised Weapon Mastery](ref/feat/improvised-weapon-mastery).

## Versatile Improvisation (Ex) {#versatile-improvisation}

At 3rd level, as a swift action, a monk of the empty hand may use an improvised weapon to deal
damage as if it were another type (bludgeoning, piercing, or slashing) for 1 round, regardless of
the weapon's normal damage type. This ability replaces still mind.

## Ki Pool (Su) {#ki-pool}

At 4th level, in addition to the normal abilities of his _ki_ pool, a monk of the empty hand may
spend 1 point from his _ki_ pool to increase the range increment for an improvised thrown weapon or
shuriken by 20 feet for 1 round.

## Ki Weapons (Su) {#ki-weapons}

At 5th level, a monk of the empty hand may spend 1 point from his _ki_ pool as a swift action to
deal damage equal to his unarmed strike damage with an improvised weapon for 1 round. At 11th level,
the monk may spend _ki_ to grant an enhancement bonus or magical weapon abilities to an improvised
weapon for 1 round, at the rate of 1 point of _ki_ per +1 bonus or its equivalent. The monk may not
spend more than 3 points of _ki_ at one time for this purpose. For example, a monk can spend 2
points of _ki_ to give his improvised weapon a +1 enhancement bonus and the
_[ki focus](ref/magic-enh/ki-focus)_ quality, or just the
_[flaming burst](ref/magic-enh/flaming-burst)_ quality. At 15th level, the limit increases to 5 _ki_
per round. The monk may use this ability to add magical weapon qualities to improvised weapons that
could not normally have such a quality, such as adding the _[disruption](ref/magic-enh/disruption)_
quality to a slashing weapon, or the _[vorpal](ref/magic-enh/vorpal)_ quality to a bludgeoning
weapon. This ability replaces purity of body and diamond body.
