+++
id = "ref/arc-gunslinger/pistolero"
kind = "archetype"
title = "Pistolero"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Pistolero"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pistolero", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]

[fields]
kind = "archetype"
features = [
  { anchor = "gunsmith" },
  { anchor = "deeds" },
  { anchor = "up-close-and-deadly", level = 1 },
  { anchor = "deadeye", level = 7 },
  { anchor = "twin-shot-knockdown", level = 11 },
  { anchor = "pistol-training", level = 5 },
]
trades = [
  { replaces = "Deadeye deed", feature = "deeds", power = "deadeye", by = ["up-close-and-deadly"] },
  { replaces = "Startling shot deed", feature = "deeds", power = "startling shot", by = ["deadeye"] },
  { replaces = "Bleeding wound deed", feature = "deeds", power = "bleeding wound", by = ["twin-shot-knockdown"] },
  { replaces = "Gun training 1-4", feature = "gun-training", levels = [5, 9, 13, 17], by = ["pistol-training"] },
  { alters = "Gunsmith", feature = "gunsmith", by = ["gunsmith"] },
]
+++

While most gunslingers have favorite firearms, there are those rare ones who choose to specialize in
one-handed firearms exclusively. These gunslingers are called pistoleros. While they lack the
flexibility of being able to pick up any kind of firearm and use it with reasonable proficiency,
they are crackerjack shots with pistols and similar firearms. Their skill and aim with these
firearms at close range is second to none, and they rarely misfire with these weapons.

## Weapon Proficiency {#weapon-proficiency}

Instead of proficiency with all firearms, a pistolero only gains proficiency with one-handed
firearms. She must take [Exotic Weapon Proficiency](ref/feat/exotic-weapon-proficiency) (firearms)
to gain proficiency with two-handed firearms and firearm siege engines.

## Gunsmith {#gunsmith}

A pistolero must take a [pistol](ref/eq-weapon/pistol) when she chooses a battered firearm at 1st
level.

## Deeds {#deeds}

A pistolero swaps a trio of deeds for the following.

## Up Close and Deadly (Ex) {#up-close-and-deadly}

At 1st level, when the pistolero hits a target with a one-handed firearm that is not making a
scatter shot, she can spend 1 grit point to deal 1d6 points of extra damage on a hit. If she misses
with the attack, she grazes the target, dealing half the extra damage anyway. This is precision
damage and is not multiplied if the attack is a critical hit. This precision damage increases to 2d6
at 5th level, to 3d6 at 10th level, to 4d6 at 15th level, and to 5d6 at 20th level. This precision
damage stacks with [sneak attack](ref/ability/sneak-attack) and other forms of precision damage. The
cost of using this deed cannot be reduced with the [Signature Deed](ref/feat/signature-deed) feat,
the true grit class feature, or any similar effect. This deed replaces the deadeye deed.

## Deadeye (Ex) {#deadeye}

At 7th level, the pistolero gains the [deadeye](ref/deed/deadeye) deed, which is normally a
1st-level gunslinger deed. This deed replaces the startling shot deed.

## Twin Shot Knockdown (Ex) {#twin-shot-knockdown}

At 11th level, when the pistolero hits a single target with two or more one-handed firearm attacks
during her turn, she can spend 1 grit point to knock the target [prone](ref/rule/prone). She can
choose to spend the grit point after the attacks are made. This deed replaces the bleeding wound
deed.

## Pistol Training (Ex) {#pistol-training}

Starting at 5th level, a pistolero increases her skill with one-handed firearms. She gains a bonus
on damage rolls equal to her Dexterity modifier, and when she misfires with a one-handed firearm,
the misfire value increases by 2 instead of 4. Every four levels thereafter (9th, 13th, and 17th),
the bonus on damage rolls increases by +1. This ability replaces gun training 1 to 4.
