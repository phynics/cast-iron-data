+++
id = "ref/arc-wizard/undead-master"
kind = "archetype"
title = "Undead Master"
aon = "ArchetypeDisplay.aspx?FixedName=Wizard%20Undead%20Master"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undead_master", path = "json/archetypes_wizard.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/wizard" },
]
[[sources]]
publication = "horror-adventures"
page = "75"

[fields]
kind = "archetype"
features = [
  { anchor = "necromantic-focus" },
  { anchor = "necropolitan" },
  { anchor = "corpse-bond" },
  { anchor = "command-undead", level = 1 },
  { anchor = "reanimator" },
  { anchor = "lich-loved", level = 20 },
]
trades = [
  { replaces = "Scribe Scroll", feature = "scribe-scroll", by = ["command-undead"] },
  { replaces = "Bonus feats gained at 5th, 10th, and 15th levels", feature = "bonus-feats", levels = [5, 10, 15], by = ["reanimator"] },
  { replaces = "Bonus feat gained at 20th level", feature = "bonus-feats", levels = [20], by = ["lich-loved"] },
  { alters = "Arcane school", feature = "arcane-school", by = ["necromantic-focus"] },
  { alters = "alignment", by = ["necromantic-focus"] },
  { alters = "Arcane bond", feature = "arcane-bond", by = ["corpse-bond"] },
]
+++

Undead masters have great power over undeath.

## Necromantic Focus {#necromantic-focus}

An undead master must be of an evil alignment. If he becomes nonevil, he can still use his powers
but can't progress any further as a wizard. Most undead masters specialize in the
[necromancy](ref/arcaneschool/necromancy) school, and an undead master can't have necromancy as an
opposition school.

This alters arcane school and alignment.

## Necropolitan (Ex) {#necropolitan}

An undead master gains a bonus equal to [half](ref/misc/fractions-and-rounding) his wizard level
(minimum +1) on Diplomacy and Knowledge checks regarding undead creatures. Because of his obsessive
focus on the undead, he takes a -2 penalty when attempting such checks regarding living creatures.

## Corpse Bond (Su) {#corpse-bond}

An undead master can forge an arcane bond with an object, but that object must be made at least
partially of [bone](ref/eq-material/bone). Alternatively, he can animate a corpse companion, as per
the [undead lord](ref/arc-cleric/undead-lord) cleric archetype (_Pathfinder RPG Ultimate Magic_ 32).
He can't gain a familiar.

This ability alters arcane bond.

## Command Undead (Su) {#command-undead}

An undead master gains [Command Undead](ref/feat/command-undead) as a bonus feat, treating his
wizard level as his cleric level. If he lacks the ability to
[channel negative energy](ref/ability/channel-energy) for the purpose of Command Undead, he can
expend 3 uses of any 1st-level arcane school ability that normally has a number of uses per day
equal to 3 + his Intelligence modifier, rather than a use of channel energy. If he's a necromancer
with the power over undead ability, he instead gains [Improved Channel](ref/feat/improved-channel).

This ability replaces Scribe Scroll.

## Reanimator (Su) {#reanimator}

An undead master adds the following spells to his spellbook at the given wizard levels: 1st—_repair
undead_; 3rd—_lesser animate dead_; 5th—_animate dead_; 7th—_undead anatomy I_; 9th—_create undead_;
11th—_undeath to death_; 13th—_[create greater undead](ref/spell/create-greater-undead)_;
15th—_undead anatomy IV_; 17th—_cursed earth_. He can spontaneously cast any of these spells by
sacrificing a prepared spell of the same level or higher. The undead master can cast _lesser animate
dead_, _animate dead_, _create undead_, and _create greater undead_ as if they were 1 level lower
than their normal wizard spell level; this does not alter their level for the purpose of item
crafting and the like.

This ability replaces the bonus feats gained at 5th, 10th, and 15th levels.

## Lich-Loved (Su) {#lich-loved}

At 20th level, an [undead](ref/sorcbloodline/undead) master gains the benefits of the undead
sorcerer bloodline's one of us ability.

This ability replaces the bonus feat gained at 20th level.
