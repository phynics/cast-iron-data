+++
id = "ref/arc-monk/softstrike-monk"
kind = "archetype"
title = "Softstrike Monk"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Softstrike%20Monk"
source_ids = ["martial-arts-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "softstrike_monk", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "martial-arts-handbook"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "feather-touch" },
  { anchor = "nonlethal-strikes", level = 1 },
  { anchor = "tenet-of-life" },
  { anchor = "life-giving-blows", level = 6 },
  { anchor = "wholeness-of-body-and-spirit", level = 7 },
  { anchor = "incapacitating-palm", level = 15 },
  { anchor = "resilient-body", level = 19 },
]
trades = [
  { replaces = "Weapon proficiency", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { replaces = "Bonus feats gained at 6th and 10th levels", feature = "bonus-feat", levels = [6, 10], by = ["life-giving-blows"] },
  { replaces = "Empty body", feature = "empty-body", by = ["resilient-body"] },
  { alters = "Unarmed strike", feature = "unarmed-strike", by = ["nonlethal-strikes"] },
  { alters = "Wholeness of body", feature = "wholeness-of-body", by = ["wholeness-of-body-and-spirit"] },
  { alters = "Quivering palm", feature = "quivering-palm", by = ["incapacitating-palm"] },
]
+++

The practices of softstrike monks date back to the peaceful eras of Imperial Lung Wa. Still common
among warriors today, softstrike monks employ a nonlethal but effective form of combat.

## Weapon Proficiency {#weapon-proficiency}

A softstrike monk is proficient with the [aklys](ref/eq-weapon/aklys), [bolas](ref/eq-weapon/bolas),
[club](ref/eq-weapon/club), [light flail](ref/eq-weapon/light-flail),
[light mace](ref/eq-weapon/light-mace), [nunchaku](ref/eq-weapon/nunchaku),
[quarterstaff](ref/eq-weapon/quarterstaff), [sap](ref/eq-weapon/sap), [sling](ref/eq-weapon/sling),
and any weapon with the monk special quality that can deal bludgeoning damage. He is considered
proficient only with monk weapons that can deal multiple types of damage when dealing bludgeoning
damage.

This replaces the monk's weapon proficiency.

## Feather Touch (Ex) {#feather-touch}

A softstrike monk does not take the normal -4 penalty on attack rolls for using a lethal weapon to
deal nonlethal damage. In addition, he can use his stunning fist ability while making a nonlethal
attack with a weapon.

## Nonlethal Strikes (Ex) {#nonlethal-strikes}

A softstrike monk focuses on blows that do not inflict deadly harm. When a softstrike monk deals
nonlethal damage with his unarmed strikes, his monk level is treated as 4 levels higher for the
purposes of determining the damage he deals (to a maximum of 4d8 at 20th level for a Medium monk).
When dealing lethal damage with his unarmed strikes, his monk level is treated as if it were 4
levels lower (minimum 1st level) for the purpose of determining damage.

This alters unarmed strike.

## Tenet of Life (Su) {#tenet-of-life}

Though a softstrike monk accepts that death may happen in combat, he cannot abide killing in cold
blood. If he slays an [unconscious](ref/misc/unconscious) or [helpless](ref/misc/helpless) living
foe, or merely stands by and allows such a killing to occur, he becomes [shaken](ref/misc/shaken)
for 1 hour. In addition, the act disrupts the softstrike monk's ki; if he has a ki pool, he loses a
number of ki points equal to half his level, as if they had been spent.

## Life-Giving Blows (Su) {#life-giving-blows}

At 6th level, a softstrike monk can force a piece of his life force into a nonliving creature to
disrupt its animating essence. If he hits an undead foe with an unarmed attack, he can spend 1 ki
point as a free action to remove the target's immunity to nonlethal damage for a number of minutes
equal to his Wisdom modifier. If, during this time, the target's nonlethal damage exceeds its
current hit points, it is destroyed. At 10th level, a softstrike monk can also use this ability
against constructs.

This replaces the bonus feats gained at 6th and 10th levels.

## Wholeness of Body and Spirit (Su) {#wholeness-of-body-and-spirit}

At 7th level, a softstrike monk can use wholeness of body on both himself and other creatures,
though it heals only nonlethal damage. If he uses this ability on an unconscious foe, he can spend 1
additional ki point to force the creature to accept a pact of life. The creature must succeed at a
Will saving throw (DC = 10 + half the softstrike monk's level + his Wisdom modifier) or the pact
renders it unable to directly attack the monk and any allies within 60 feet, as per
_[sanctuary](ref/spell/sanctuary)_, for a number of days equal to the softstrike monk's level.

This alters wholeness of body. (For an unchained monk from _Pathfinder Unchained_, this ability
applies only if the monk selects the wholeness of body ki power.)

## Incapacitating Palm (Su) {#incapacitating-palm}

At 15th level, a softstrike monk renders the target of his quivering palm unconscious instead of
killing the creature. Upon failing its Fortitude saving throw, the target is knocked unconscious for
a number of minutes equal to the softstrike monk's level.

This alters quivering palm. (For an unchained monk, this ability applies only if the monk selects
the quivering palm ki power.)

## Resilient Body (Su) {#resilient-body}

At 19th level, a softstrike monk's mastery of nonlethal combat lets him apply his techniques to his
defense. A softstrike monk converts any precision damage he takes to nonlethal damage.

This replaces empty body.
