+++
id = "ref/arc-gunslinger/blatherskite"
kind = "archetype"
title = "Blatherskite"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Blatherskite"
source_ids = ["antiheros-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blatherskite", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "antiheros-handbook"
page = "9"

[fields]
kind = "archetype"
features = [
  { anchor = "blatherskite-s-stagger", level = 1 },
  { anchor = "blatherskite-s-initiative", level = 3 },
  { anchor = "cheap-shot", level = 3 },
  { anchor = "blatherskite-s-surprise", level = 7 },
]
trades = [
  { replaces = "Gunslinger's dodge deed", feature = "deeds", power = "gunslinger's dodge", by = ["blatherskite-s-stagger"] },
  { replaces = "Gunslinger initiative deed", feature = "deeds", power = "gunslinger initiative", by = ["blatherskite-s-initiative"] },
  { replaces = "Pistol-whip deed", feature = "deeds", power = "pistol whip", by = ["cheap-shot"] },
  { replaces = "Startling shot deed", feature = "deeds", power = "startling shot", by = ["blatherskite-s-surprise"] },
  { alters = "Class skills" },
]
+++

A blatherskite talks big and feels powerful when holding a loaded gun, but when the gun jams or the
situation gets too intense, he's the first to run for cover. He has an extraordinary talent for
retreating from harm's way and fooling his enemies into thinking he is weaker than he is.

## Class Skills {#class-skills}

A blatherskite gains Escape Artist and Stealth as class skills, but he doesn't gain Handle Animal
and Intimidate as class skills.

This alters the gunslinger's class skills.

## Deeds {#deeds}

A blatherskite swaps four deeds for the following.

## Blatherskite's Stagger (Ex) {#blatherskite-s-stagger}

At 1st level as an immediate action, when a ranged attack would normally miss a blatherskite, he can
allow it to hit him and dramatically stagger a few steps backward, moving up to 10 feet directly
away from the attacker. This movement provokes attacks of opportunity as normal. The attack deals
the minimum amount of damage (as though the attacker had rolled a natural 1 on each damage die).

At 2nd level, if a ranged attack hits the blatherskite but the attack roll exceeds his AC by no more
than his bonus from the nimble class feature, he can spend 1 grit point as an immediate action to
take the minimum amount of damage and move up to 10 feet directly away from the attacker. This
movement provokes attacks of opportunity as normal.

The gunslinger can perform this deed only while wearing medium or light armor and while carrying no
more than a light load.

This deed replaces the gunslinger's dodge deed.

## Blatherskite's Initiative (Ex) {#blatherskite-s-initiative}

At 3rd level, the blatherskite gains benefits as long as he has at least 1 grit point. The
blatherskite gains a +2 bonus on initiative checks. Furthermore, if he is trained in Stealth (and as
long as he is not paralyzed, prone, or otherwise immobilized), he can take a 5-foot step and attempt
a Stealth check to hide as part of the initiative check, provided there is an object or a larger
creature to hide behind; if he spends 1 grit point, he can move up to half his speed instead of
taking only a 5-foot step as part of the initiative check.

This deed replaces the gunslinger initiative deed.

## Cheap Shot (Ex) {#cheap-shot}

At 3rd level, if the blatherskite has at least 1 grit point and makes a successful attack against an
unarmed target with a firearm that is not making a scattering shot, he deals 1d6 additional points
of damage. This is precision damage and is not multiplied on a critical hit.

This deed replaces the pistol-whip deed.

## Blatherskite's Surprise (Ex) {#blatherskite-s-surprise}

At 7th level, when the blatherskite succeeds at a saving throw against a spell or an effect that
would cause him to be blinded, confused, dazed, fascinated, frightened, nauseated, paralyzed, or
stunned, he can allow the effect to affect him normally. As long as he has at least 1 grit point, as
an immediate action he can cause the creature from which the effect originated to lose its Dexterity
bonus to AC for a number of rounds equal to [half](ref/misc/fractions-and-rounding) the duration of
the effect (in rounds) or half the gunslinger's level, whichever is lower (minimum 1 round). If he
instead spends 1 grit point, he does not need to allow the effect to affect him normally to use this
deed.

This deed replaces the startling shot deed.
