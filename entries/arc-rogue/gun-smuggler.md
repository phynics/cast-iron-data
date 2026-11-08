+++
id = "ref/arc-rogue/gun-smuggler"
kind = "archetype"
title = "Gun Smuggler"
source_ids = ["people-of-the-wastes"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gun_smuggler", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]

[fields]
kind = "archetype"
replaces = ["Weapon proficiencies", "Trapfinding", "Trap sense", "rogue talent gained at 6th level", "Uncanny dodge", "improved uncanny dodge"]
alters = ["Sneak attack"]
+++

**Sources:** People of the Wastes pg 13\
Alkenstar protects the secrets of gunpowder and controls the sale of firearms, creating lucrative
opportunities for those who can sneak the technology beyond the Mana Wastes. Gun smugglers are adept
at procuring firearms and concealing their secret weapons.

**Weapon Proficiency**

**Ability:** A gun smuggler is proficient with all simple weapons and one-handed firearms, plus the
[rapier](ref/eq-weapon/rapier), [sap](ref/eq-weapon/sap), [short sword](ref/eq-weapon/short-sword),
and [sword cane](ref/eq-weapon/sword-cane).

**Replaces:** Weapon proficiencies

**Hidden Gun (Ex)**

**Passive:** A gun smuggler gains a bonus equal to half her rogue level on Sleight of Hand checks to
conceal a one-handed firearm on her body. She increases the DCs of opponents' Perception checks to
realize the true nature of disguised weapons (such as a sword cane) within 5 feet of her by an
amount equal to her rogue level (maximum DC 25 plus her rogue level).

**Replaces:** Trapfinding

**Secret Sidearm (Ex)**

**Ability:** As an expert in discreet and easily concealable weapons and firearms, a gun smuggler
gains a battered gun identical to that gained by a 1st-level [gunslinger](ref/class/gunslinger) and
[Gunsmithing](ref/feat/gunsmithing) as a bonus feat (including the ability to restore her battered
gun as if she were a gunslinger), though she must select a [coat pistol](ref/eq-weapon/coat-pistol),
[dagger pistol](ref/eq-weapon/dagger-pistol), or
[sword cane pistol](ref/eq-weapon/sword-cane-pistol) as her battered weapon.

**Selective Targeting (Ex)**

**Ability:** A gun smuggler focuses on concealable firearms for her sneak attacks. When she makes a
sneak attack using any weapon other than a coat pistol, dagger pistol, or sword cane pistol (either
firing the weapon or making a melee attack), her sneak attack damage dice are d4s instead of d6s.

**Alters:** Sneak attack

**Stolen Shots (Ex)**

**Ability:** A gun smuggler can access small quantities of cutting-edge firearm technology through
clandestine dealers. She gains the benefits of the
[black market connections](ref/talent/black-market-connections) rogue talent, though only for the
purpose of securing firearms and related equipment. At the beginning of each day, the gun smuggler
gains a number of bullets (with accompanying black powder) or paper cartridges - referred to as
shots - in any combination equal to her rogue level, representing ammunition smuggled to her by
contacts. Her contacts provide only enough shots to replenish this small supply, so she can't
accumulate ammunition indefinitely, and these shots have a market price of 0 gp.

**At 6th Level:** The gun smuggler can elect to gain one or more pieces of magic ammunition, though
each one replaces a number of her daily shots equal to the ammunition's enhancement bonus (maximum
enhancement bonus equal to [one-third](ref/misc/fractions-and-rounding) of her level for any one
piece of ammunition). She can choose to add any of the following weapon special abilities to the
shot, though the shot must have at least a +1 enhancement bonus, and these special abilities use an
amount of bonus equal to the ability's normal price: [distance](ref/magic-enh/distance),
[flaming](ref/magic-enh/flaming), [flaming burst](ref/magic-enh/flaming-burst),
[merciful](ref/magic-enh/merciful), [seeking](ref/magic-enh/seeking), or
[thundering](ref/magic-enh/thundering).

**Gained:** At 3rd Level

**Replaces:** Trap sense, rogue talent gained at 6th level

**Uncanny Aim (Ex)**

**At 4th Level:** A gun smuggler increases the range increment of any coat pistol, dagger pistol, or
sword cane pistol she wields by 10 feet.

**At 8th Level:** The base damage of bullets fired by these weapons increases by
[one die step](ref/misc/damage-die-adjustments).

**Replaces:** Uncanny dodge, improved uncanny dodge
