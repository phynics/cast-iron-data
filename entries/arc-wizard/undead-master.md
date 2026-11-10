+++
id = "ref/arc-wizard/undead-master"
kind = "archetype"
title = "Undead Master"
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
replaces = ["Scribe Scroll", "5th-, 10th-, and 15th-level bonus feats", "20th-level bonus feat"]
alters = ["Arcane school", "alignment", "Arcane bond"]
replaces_features = ["scribe-scroll"]
alters_features = ["arcane-school", "arcane-bond"]
+++

Undead masters have great power over undeath.

**Necromantic Focus**

**Alters:** Arcane school, alignment

**Info:** An undead master must be of an evil alignment. If he becomes nonevil, he can still use his
powers but can't progress any further as a wizard.

Most undead masters specialize in the [necromancy](ref/arcaneschool/necromancy) school, and an
undead master can't have necromancy as an opposition school.

**Necropolitan (Ex)**

**Passive:** An undead master gains a bonus equal to [half](ref/misc/fractions-and-rounding) his
wizard level (minimum +1) on Diplomacy and Knowledge checks regarding undead creatures. Because of
his obsessive focus on the undead, he takes a -2 penalty when attempting such checks regarding
living creatures.

**Corpse Bond (Su)**

**Ability:** An undead master can forge an _arcane bond_ with an object, but that object must be
made at least partially of [bone](ref/eq-material/bone). Alternatively, he can animate a _corpse
companion,_ as per the [undead lord](ref/arc-cleric/undead-lord) cleric archetype. He can't gain a
familiar.

**Alters:** Arcane bond

**Corpse Companion (Su)**

**Ability:** With a ritual requiring 8 hours, an undead lord can animate a single
[skeleton](ref/template/skeleton) or [zombie](ref/template/zombie) whose Hit Dice do not exceed her
cleric level. This corpse companion automatically follows her commands and does not need to be
controlled by her. She cannot have more than one corpse companion at a time. It does not count
against the number of Hit Dice of undead controlled by other methods. She can use this ability to
create a variant skeleton such as a bloody or burning skeleton, but its Hit Dice cannot exceed
[half](ref/misc/fractions-and-rounding) her cleric level. She can dismiss her companion as a
**standard action**, which destroys it.

**Flavor:** Text from the _undead lord_ ability.

**Command Undead (Su)**

**Ability:** An undead master gains [Command Undead](ref/feat/command-undead) as a bonus feat,
treating his wizard level as his cleric level. If he lacks the ability to
[channel negative energy](ref/ability/channel-energy) for the purpose of Command Undead, he can
expend 3 uses of any 1st-level arcane school ability that normally has a number of uses per day
equal to 3 + his Intelligence modifier, rather than a use of _channel energy._

**Ability2:** If he's a necromancer with the _power over undead_ ability, he instead gains
[Improved Channel](ref/feat/improved-channel).

**Replaces:** Scribe Scroll

**Reanimator (Su)**

**Ability:** An undead master adds the following spells to his spellbook at the given wizard levels.

**Replaces:** 5th-, 10th-, and 15th-level bonus feats

**Spells:** Repair undead

**Spells:** Undeath to death

**Spells:** Create greater undead

**Spells:** Undead anatomy IV

**Spells:** Cursed earth

**Spells:** Lesser animate dead

**Spells:** Animate dead

**Spells:** Undead anatomy I

**Spells:** Create undead

**Special:** He can spontaneously cast any of these spells by sacrificing a prepared spell of the
same level or higher. The undead master can cast _lesser animate dead, animate dead, create undead,_
and _[create greater undead](ref/spell/create-greater-undead)_ as if they were 1 level lower than
their normal wizard spell level; this does not alter their level for the purpose of item crafting
and the like.

**Lich-Loved (Su)**

**Ability:** An undead master gains the benefits of the [undead](ref/sorcbloodline/undead) sorcerer
bloodline's _one of us_ ability.

**Gained:** At 20th Level

**Replaces:** 20th-level bonus feat

**One of Us (Ex)**

**Flavor:** Text from the _undead_ bloodline.

**Passive:** Your form begins to rot (the appearance of this decay is up to you) and undead see you
as one of them. You gain immunity to cold, nonlethal damage, paralysis, and sleep. You also gain DR
5/-. Unintelligent undead do not notice you unless you attack them. You receive a +4 morale bonus on
saving throws made against spells and [spell-like abilities](ref/umr/spell-like-abilities) cast by
undead.
