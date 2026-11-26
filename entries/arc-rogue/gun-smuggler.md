+++
id = "ref/arc-rogue/gun-smuggler"
kind = "archetype"
title = "Gun Smuggler"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Gun%20Smuggler"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gun_smuggler", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "people-of-the-wastes"
page = "13"

[fields]
kind = "archetype"
features = [
  { anchor = "hidden-gun", level = 1 },
  { anchor = "secret-sidearm" },
  { anchor = "selective-targeting", level = 1 },
  { anchor = "stolen-shots", level = 3 },
  { anchor = "uncanny-aim", level = 4 },
]
trades = [
  { replaces = "Weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons" },
  { replaces = "Trapfinding", feature = "trapfinding", by = ["hidden-gun"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["stolen-shots"] },
  { replaces = "rogue talent gained at 6th level", feature = "rogue-talents", levels = [6], by = ["stolen-shots"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["uncanny-aim"] },
  { replaces = "improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["uncanny-aim"] },
  { alters = "Sneak attack", feature = "sneak-attack", by = ["selective-targeting"] },
]
+++

Alkenstar protects the secrets of gunpowder and controls the sale of firearms, creating lucrative
opportunities for those who can sneak the technology beyond the Mana Wastes. Gun smugglers are adept
at procuring firearms and concealing their secret weapons.

## Weapon Proficiency {#weapon-proficiency}

A gun smuggler is proficient with all simple weapons and one-handed firearms, plus the
[rapier](ref/eq-weapon/rapier), [sap](ref/eq-weapon/sap), [short sword](ref/eq-weapon/short-sword),
and [sword cane](ref/eq-weapon/sword-cane).

This replaces the rogue's weapon proficiencies.

## Hidden Gun (Ex) {#hidden-gun}

A gun smuggler gains a bonus equal to half her rogue level on Sleight of Hand checks to conceal a
one-handed firearm on her body. She increases the DCs of opponents' Perception checks to realize the
true nature of disguised weapons (such as a sword cane) within 5 feet of her by an amount equal to
her rogue level (maximum DC 25 plus her rogue level).

This replaces trapfinding.

## Secret Sidearm (Ex) {#secret-sidearm}

As an expert in discreet and easily concealable weapons and firearms, a gun smuggler gains a
battered gun identical to that gained by a 1st-level [gunslinger](ref/class/gunslinger) and
[Gunsmithing](ref/feat/gunsmithing) as a bonus feat (including the ability to restore her battered
gun as if she were a gunslinger), though she must select a [coat pistol](ref/eq-weapon/coat-pistol),
[dagger pistol](ref/eq-weapon/dagger-pistol), or
[sword cane pistol](ref/eq-weapon/sword-cane-pistol) as her battered weapon.

## Selective Targeting (Ex) {#selective-targeting}

A gun smuggler focuses on concealable firearms for her sneak attacks. When she makes a sneak attack
using any weapon other than a coat pistol, dagger pistol, or sword cane pistol (either firing the
weapon or making a melee attack), her sneak attack damage dice are d4s instead of d6s.

This alters sneak attack.

## Stolen Shots (Ex) {#stolen-shots}

At 3rd level, a gun smuggler can access small quantities of cutting-edge firearm technology through
clandestine dealers. She gains the benefits of the
[black market connections](ref/talent/black-market-connections) rogue talent, though only for the
purpose of securing firearms and related equipment. At the beginning of each day, the gun smuggler
gains a number of bullets (with accompanying black powder) or paper cartridges—referred to as
shots—in any combination equal to her rogue level, representing ammunition smuggled to her by
contacts. Her contacts provide only enough shots to replenish this small supply, so she can't
accumulate ammunition indefinitely, and these shots have a market price of 0 gp.

At 6th level, the gun smuggler can elect to gain one or more pieces of magic ammunition, though each
one replaces a number of her daily shots equal to the ammunition's enhancement bonus (maximum
enhancement bonus of +2 for any one piece of ammunition). She can choose to add any of the following
weapon special abilities to the shot, though the shot must have at least a +1 enhancement bonus, and
these special abilities use an amount of bonus equal to the ability's normal price (_Core Rulebook_
467–468): _[distance](ref/magic-enh/distance)_, _[flaming](ref/magic-enh/flaming)_,
_[flaming burst](ref/magic-enh/flaming-burst)_, _[merciful](ref/magic-enh/merciful)_,
_[seeking](ref/magic-enh/seeking)_, or _[thundering](ref/magic-enh/thundering)_. At 9th level and
every 3 rogue levels thereafter, the maximum enhancement bonus of a gun smuggler's shots increases
by 1 (to a maximum of +6 at 18th level).

This replaces trap sense and the rogue talent gained at 6th level.

## Uncanny Aim (Ex) {#uncanny-aim}

At 4th level, a gun smuggler increases the range increment of any coat pistol, dagger pistol, or
sword cane pistol she wields by 10 feet. At 8th level, the base damage of bullets fired by these
weapons increases by [one die step](ref/misc/damage-die-adjustments).

This replaces uncanny dodge and improved uncanny dodge.
