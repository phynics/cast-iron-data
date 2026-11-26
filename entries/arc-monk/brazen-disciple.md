+++
id = "ref/arc-monk/brazen-disciple"
kind = "archetype"
title = "Brazen Disciple"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Brazen%20Disciple"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brazen_disciple", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "adventurers-guide"
page = "104"

[fields]
kind = "archetype"
features = [
  { anchor = "feinting-flurry", level = 1 },
  { anchor = "bonus-feat" },
  { anchor = "efreeti-s-guile", level = 3 },
  { anchor = "confounding-koan", level = 12 },
  { anchor = "genie-apotheosis", level = 20 },
]
trades = [
  { replaces = "Monk's bonus feats at 1st level and at 6th level", feature = "bonus-feat", levels = [1, 6], by = ["feinting-flurry"] },
  { replaces = "Still mind", feature = "still-mind", by = ["efreeti-s-guile"] },
  { replaces = "Abundant step", feature = "abundant-step", by = ["confounding-koan"] },
  { replaces = "Perfect self", feature = "perfect-self", by = ["genie-apotheosis"] },
  { alters = "Bonus feats", feature = "bonus-feat", by = ["bonus-feat"] },
  { alters = "Class skills" },
]
+++

Of the three monasteries, the Monastery of Unblinking Flame has been the most successful in
developing a specific and unique fighting style that sets its disciples apart from other monks. In
order to be admitted into the Monastery of Unblinking Flame and become one of these disciples, a
supplicant must prove his worth by outwitting an [efreeti](ref/monster/genie-efreeti). Those who
succeed often become monks known as the brazen disciples.

Brazen disciples believe that the best way to prepare for this test is to emulate the
[efreeti](ref/monster/genie-efreeti)'s own duplicitous ways. By studying genie contracts, brazen
disciples learn how to take advantage of loopholes, and by pondering riddles, they learn how to
obfuscate truth. They use deception in their fighting style, and many go a step further,
incorporating fire and smoke both mundane and magical. Though most brazen disciples focus on joining
the [Houses of Perfection](ref/rule/aff-monasteries), some become enamored with the efreet and
instead seek out genie masters.

## Class Skills {#class-skills}

A brazen disciple gains Bluff (Cha), Disguise (Cha), and Knowledge (planes) (Int) as class skills
but loses Knowledge (religion), Ride, and Swim.

This alters the monk's class skills.

## Feinting Flurry (Ex) {#feinting-flurry}

When using flurry of blows to make melee attacks, a brazen disciple can forgo his first attack to
attempt a Bluff check to feint. At 6th level, when a brazen disciple successfully feints, his
opponent is denied its Dexterity bonus to AC until the end of the monk's turn.

This ability replaces the monk's bonus feats at 1st level and at 6th level.

## Bonus Feat {#bonus-feat}

At 2nd, 10th, 14th, and 18th levels, a brazen disciple can select a bonus feat. These feats must be
chosen from the following list: [Catch Off-Guard](ref/feat/catch-off-guard),
[Combat Reflexes](ref/feat/combat-reflexes), [Deceitful](ref/feat/deceitful),
[Dodge](ref/feat/dodge), [Elemental Fist](ref/feat/elemental-fist), and
[Improved Initiative](ref/feat/improved-initiative). At 6th level, the brazen disciple can also
choose from the following feats: [Efreeti Style](ref/feat/efreeti-style),
[Improved Dirty Trick](ref/feat/improved-dirty-trick), [Improved Disarm](ref/feat/improved-disarm),
[Improved Steal](ref/feat/improved-steal), [Improved Trip](ref/feat/improved-trip), and
[Mobility](ref/feat/mobility). At 10th level, the brazen disciple can also choose from the following
feats: [Efreeti Stance](ref/feat/efreeti-stance), [Efreeti Touch](ref/feat/efreeti-touch),
[Improved Critical](ref/feat/improved-critical), and [Spring Attack](ref/feat/spring-attack). He
need not meet the prerequisites normally required for these feats to select them.

This ability alters the monk's bonus feats.

## Efreeti's Guile (Ex) {#efreeti-s-guile}

At 3rd level, a brazen disciple can add his Wisdom modifier on Bluff and Disguise checks instead of
his Charisma modifier.

This ability replaces still mind.

## Confounding Koan (Sp) {#confounding-koan}

At 12th level, a brazen disciple can spend 2 ki points as a standard action to confuse a target
within 30 feet with a riddle or paradox. This ability functions as per
_[confusion](ref/spell/confusion)_, except that it is language-dependent. The DC is equal to 10 +
half the monk's class level + his Wisdom modifier, and the caster level is equal to his class level.

This ability replaces abundant step. (For the unchained monk from _Pathfinder Unchained_, this
ability replaces the monk's ki ability gained at 12th level.)

## Genie Apotheosis {#genie-apotheosis}

At 20th level, a brazen disciple is treated as a native outsider with the fire subtype rather than
as a humanoid (or whatever the monk's creature type was) for the purpose of spells and magical
effects. He has immunity to fire and vulnerability to cold. Once per day, the brazen disciple can
grant a [limited wish](ref/spell/limited-wish) (as per the spell _limited wish_) to a non-outsider
as a [spell-like ability](ref/umr/spell-like-abilities) (CL 20th).

This ability replaces perfect self.
