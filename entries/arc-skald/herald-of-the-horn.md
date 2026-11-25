+++
id = "ref/arc-skald/herald-of-the-horn"
kind = "archetype"
title = "Herald of the Horn"
aon = "ArchetypeDisplay.aspx?FixedName=Skald%20Herald%20of%20the%20Horn"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "herald_of_the_horn", path = "json/archetypes_skald.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/skald" },
]
[[sources]]
publication = "advanced-class-guide"
page = "115"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-bond", level = 1 },
  { anchor = "rousing-retort", level = 5 },
  { anchor = "horn-call", level = 7 },
  { anchor = "crumbling-blast", level = 11 },
]
trades = [
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["arcane-bond"] },
  { replaces = "The first daily use of spell kenning gained at 5th level", feature = "spell-kenning", levels = [5], by = ["rousing-retort"] },
  { replaces = "Lore master", feature = "lore-master", by = ["horn-call"] },
  { replaces = "The second and third daily uses of spell kenning gained at 11th and 17th levels", feature = "spell-kenning", levels = [11, 17], by = ["crumbling-blast"] },
]
+++

Even the loudest voice can often times be drowned out by the din of battle. Whether with the
polished metal trumpet of a standing army or the crude curved animal horn of savage raiders, a
herald of the horn sounds his _raging song_ with thunderous blasts, which can bolster allies or
shatter castle walls.

## Arcane Bond (Ex) {#arcane-bond}

At 1st level, a herald of the horn forms a powerful bond with a horn
([musical instrument](ref/eq-misc/musical-instrument-masterwork)). This functions like an
[arcane](ref/sorcbloodline/arcane) bloodline [sorcerer's](ref/class/sorcerer) arcane bond with an
object. Like a weapon, wand, or staff, the horn must be held in one hand when the herald of the horn
casts skald spells. This ability replaces Scribe Scroll.

## Rousing Retort (Su) {#rousing-retort}

At 5th level, a herald of the horn can use raging song to free allies from enchantment effects and
fear. When beginning a raging song, he can expend 4 rounds of that ability to grant all allies
within 60 feet a new saving throw against an ongoing enchantment or fear effect. The allies gain a
+2 bonus on this new saving throw. This ability replaces the first daily use of spell kenning gained
at 5th level.

## Horn Call (Su) {#horn-call}

At 7th level, a herald's horn enhances his sonic spells. If a skald spell with the sonic descriptor
is cast using the horn, its DC increases by 1. These DCs increase by an additional 1 at 13th and
19th levels. This ability replaces lore master.

## Crumbling Blast (Su) {#crumbling-blast}

At 11th level, a herald of the horn can use his horn to create a devastating shock wave of energy.
Once per day, he can sound a note on the horn that functions like a
_[horn of blasting](ref/magic-wondrous/horn-of-blasting)_ (DC = 10 + 1/2 the herald of the horn's
level + his Charisma bonus). At 17th level, the herald of the horn can use this ability twice per
day and it functions like a
_[greater horn of blasting](ref/magic-wondrous/horn-of-blasting-greater)_. Unlike an actual _horn of
blasting_, this ability does not carry the risk of destroying the horn. This ability replaces the
second and third daily uses of spell kenning gained at 11th and 17th levels.

## Rage Powers {#rage-powers}

The following rage powers complement the herald of the horn archetype: battle roar\*, energy
absorption, energy eruption, fearless rage, knockback, knockdown, smasher, and swift foot. (Those
with asterisks \[\*\] are listed in the rage powers section above.)
