+++
id = "ref/carried/technology-guide/rules/equipment/weapons"
kind = "rule"
title = "Weapons"
source_ids = ["technology-guide"]
section = ["Rules", "Equipment"]
parent = "ref/carried/technology-guide/rules/equipment"
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Technology Guide/Rules/Equipment/Weapons", path = "technology_guide/rules/equipment.json" },
]

[fields]
kind = "none"
+++

Each technological weapon has a full description, including a set of abbreviated statistics. This
information is organized as follows.

## Price {#price}

This is the cost (in gold pieces) to purchase the weapon if it's available for sale. As with magic
weapons, a technological weapon can be sold by PCs for half this value.

## Type {#type}

This indicates whether the weapon is a light, one-handed, or two-handed melee or ranged weapon.

## Proficiency {#proficiency}

This entry lists whether the weapon is simple, martial, or exotic. If an existing weapon proficiency
allows the new weapon's use, that weapon proficiency is listed in parentheses. Note that Exotic
Weapon Proficiency (heavy weaponry) works similarly to Exotic Weapon Proficiency (firearms) in that
it allows access to a wide range of similar weapons.

Some GMs may wish to replace Weapon Proficiency (firearms) with Weapon Proficiency (technological
firearms) to further restrict access to these devices to player characters in their campaigns.

## Damage {#damage}

This is the weapon's base damage. The type of damage dealt by the weapon is listed after the damage
value. Most weapons list the damage dealt by Medium and Small versions of the weapon; weapons with
only one damage entry deal the same amount of damage regardless of size.

## Critical {#critical}

This entry lists the weapon's critical threat range and critical damage multiplier.

## Range {#range}

This lists the weapon's range increment; no listing is given for melee weapons that cannot be
thrown. Unless otherwise noted, all firearms in this chapter are treated as projectile weapons for
the purpose of determining their maximum range.

## Capacity {#capacity}

Unless otherwise specified, this value is the maximum number of charges the weapon can hold.

## Usage {#usage}

This value lists the number of charges the weapon consumes from its capacity each time it is
activated.

## Special {#special}

This entry lists any special weapon qualities the weapon might have. New weapon qualities are listed
below.

## Weight {#weight}

This is the weight of the weapon in pounds. The weights given are for Medium weapons. A Small weapon
weighs half as much; a Large weapon weighs twice as much.

### Automatic {#automatic}

This weapon can act as a semi-automatic weapon (see below), or it can fire a burst of shots with a
single pull of the trigger to attack all creatures in a line. This line starts from any corner of
the wielder's space and extends to the limit of the weapon's range or until it strikes a barrier it
cannot penetrate. When using an automatic weapon to attack all creatures in a line, the wielder
makes a separate attack roll against each creature in the line. Each creature in the line can be
attacked with only one shot from each burst. Each attack roll takes a -2 penalty, and its damage
cannot be modified by precision damage or damage-increasing feats such as Vital Strike. Effects that
grant concealment, such as fog or smoke, or the _[blur](ref/spell/blur)_, _invisibility_, or
_[mirror image](ref/spell/mirror-image)_ spells, do not affect an automatic weapon's line attack.
Roll to confirm each attack roll that threatens a critical hit separately. A single burst with an
automatic weapon consumes 10 charges. When taking a full-attack action with an automatic weapon, the
wielder can fire as many bursts in a round as he has attacks, provided he has enough charges to make
all of the attacks.

### Semi-Automatic {#semi-automatic}

A semi-automatic weapon normally fires one shot as an attack. However, the user can take a
full-attack action to fire twice, as if using the Rapid Shot feat (including taking a -2 penalty on
all attacks). If the wielder has the Rapid Shot feat, she can use the additional shot from that as
well, but the penalty for all shots fired in that round increases to -6.

### Slow-Firing {#slow-firing}

A slow-firing weapon requires a full-round action to use, and thus cannot be used to make iterative
attacks.

### Touch {#touch}

Attacks with the weapon resolve as touch attacks.

## Description {#description}

This section describes the weapon's abilities and appearance.

## Construction {#construction}

Certain requirements must be met for a character to craft a technological weapon. These requirements
generally consist of having a feat and access to a particular kind of manufacturing facility.

## Craft {#craft}

This is the Craft DC required to create the weapon. It is also the Knowledge (engineering) DC to
correctly identify the weapon.

## Cost {#cost}

This is the cost in gold pieces to create the weapon. Generally this cost is equal to half the price
of the weapon.

### Technology Guide Weapons {#technology-guide-weapons}

::: table
caption = "Technology Guide Weapons"
head = [
  [
    { text = "Martial Weapons", header = true },
    { text = "Price", header = true },
    { text = "Dmg (S)", header = true },
    { text = "Dmg (M)", header = true },
    { text = "Critical", header = true },
    { text = "Range", header = true },
    { text = "Capacity", header = true },
    { text = "Usage", header = true },
    { text = "Weight", header = true },
    { text = "Type^1^", header = true },
    { text = "Special", header = true },
  ],
]
body = [
  [
    { text = "_One-Handed Melee Weapons_", colspan = 11 },
  ],
  [
    { text = "Laser torch" },
    { text = "6,000 gp" },
    { text = "1d8" },
    { text = "1d10" },
    { text = "×3" },
    { text = "—" },
    { text = "10" },
    { text = "1 charge" },
    { text = "4 lbs." },
    { text = "F" },
    { text = "Touch" },
  ],
  [
    { text = "Stun baton" },
    { text = "5,000 gp" },
    { text = "Special" },
    { text = "Special" },
    { text = "×2" },
    { text = "—" },
    { text = "10" },
    { text = "1 charge/round" },
    { text = "2 lbs." },
    { text = "B and E (special)" },
    { text = "Touch" },
  ],
  [
    { text = "Exotic Weapons", header = true, colspan = 11 },
  ],
  [
    { text = "_Light Melee Weapons_", colspan = 11 },
  ],
  [
    { text = "Monowhip" },
    { text = "70,000 gp" },
    { text = "1d10" },
    { text = "2d6" },
    { text = "18-20/×3" },
    { text = "—" },
    { text = "10" },
    { text = "1 charge/round" },
    { text = "1 lb." },
    { text = "S" },
    { text = "Performance, reach, touch" },
  ],
  [
    { text = "_One-Handed Melee Weapons_", colspan = 11 },
  ],
  [
    { text = "Null blade" },
    { text = "58,835 gp" },
    { text = "1d8" },
    { text = "1d10" },
    { text = "19-20/×2" },
    { text = "—" },
    { text = "10" },
    { text = "1 charge/round" },
    { text = "4 lbs." },
    { text = "S" },
    { text = "—" },
  ],
  [
    { text = "_Two-Handed Melee Weapons_", colspan = 11 },
  ],
  [
    { text = "Chainsaw" },
    { text = "2,700 gp" },
    { text = "1d12" },
    { text = "3d6" },
    { text = "18-20/×2" },
    { text = "—" },
    { text = "10" },
    { text = "1 charge/hour" },
    { text = "10 lbs." },
    { text = "S" },
    { text = "Deadly, distracting" },
  ],
  [
    { text = "One-Handed Ranged Weapons (Firearms)", header = true, colspan = 11 },
  ],
  [
    { text = "Arc pistol" },
    { text = "10,000 gp" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "×2" },
    { text = "50 ft." },
    { text = "10" },
    { text = "1 charge" },
    { text = "2 lbs." },
    { text = "E" },
    { text = "Semi-automatic, touch" },
  ],
  [
    { text = "Dart gun" },
    { text = "3,000 gp" },
    { text = "1d3" },
    { text = "1d4" },
    { text = "×2" },
    { text = "30 ft." },
    { text = "1 nanite canister" },
    { text = "1 charge" },
    { text = "2 lbs." },
    { text = "P" },
    { text = "—" },
  ],
  [
    { text = "Death ray" },
    { text = "140,000 gp" },
    { text = "Special" },
    { text = "Special" },
    { text = "—" },
    { text = "200 ft.^2^" },
    { text = "1 nanite canister" },
    { text = "Varies" },
    { text = "1 lb." },
    { text = "Special" },
    { text = "Slow-firing, touch" },
  ],
  [
    { text = "EMP pistol" },
    { text = "12,000 gp" },
    { text = "1d10" },
    { text = "2d6" },
    { text = "×2" },
    { text = "50 ft." },
    { text = "10" },
    { text = "1 charge" },
    { text = "2 lbs." },
    { text = "E" },
    { text = "Semi-automatic, touch" },
  ],
  [
    { text = "Flare gun" },
    { text = "300 gp" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "×3" },
    { text = "240 ft." },
    { text = "1" },
    { text = "Disposable" },
    { text = "1 lb." },
    { text = "F" },
    { text = "Slow-firing, touch" },
  ],
  [
    { text = "Gravity pistol" },
    { text = "95,000 gp" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "×2" },
    { text = "50 ft." },
    { text = "10" },
    { text = "1 charge" },
    { text = "2 lbs." },
    { text = "Force" },
    { text = "Semi-automatic, touch" },
  ],
  [
    { text = "Laser pistol" },
    { text = "10,000 gp" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "×2" },
    { text = "50 ft." },
    { text = "10" },
    { text = "1 charge" },
    { text = "2 lbs." },
    { text = "F" },
    { text = "Semi-automatic, touch" },
  ],
  [
    { text = "Mindrender" },
    { text = "56,000 gp" },
    { text = "Special" },
    { text = "Special" },
    { text = "×2" },
    { text = "40 ft." },
    { text = "1 nanite canister" },
    { text = "2 charges" },
    { text = "2 lbs." },
    { text = "Special" },
    { text = "Slow-firing, touch" },
  ],
  [
    { text = "Sonic pistol" },
    { text = "13,000 gp" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "×2" },
    { text = "50 ft." },
    { text = "10" },
    { text = "1 charge" },
    { text = "2 lbs." },
    { text = "Sonic" },
    { text = "Semi-automatic, touch" },
  ],
  [
    { text = "Stun gun" },
    { text = "3,000 gp" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "×2" },
    { text = "20 ft." },
    { text = "10" },
    { text = "1 charge 3" },
    { text = "lbs." },
    { text = "—" },
    { text = "Nonlethal, semi-automatic, touch" },
  ],
  [
    { text = "Zero pistol" },
    { text = "10,000 gp" },
    { text = "1d6" },
    { text = "1d8" },
    { text = "×2" },
    { text = "50 ft." },
    { text = "10" },
    { text = "1 charge" },
    { text = "2 lbs." },
    { text = "C" },
    { text = "Semi-automatic, touch" },
  ],
  [
    { text = "Two-Handed Ranged Weapons (Firearms)", header = true, colspan = 11 },
  ],
  [
    { text = "Arc rifle" },
    { text = "20,000 gp" },
    { text = "1d10" },
    { text = "2d6" },
    { text = "×2" },
    { text = "150 ft." },
    { text = "20" },
    { text = "1 charge" },
    { text = "6 lbs." },
    { text = "E" },
    { text = "Automatic, touch" },
  ],
  [
    { text = "Autograpnel" },
    { text = "4,000 gp" },
    { text = "1d6+6" },
    { text = "1d8+6" },
    { text = "×3" },
    { text = "30 ft." },
    { text = "20" },
    { text = "1 charge" },
    { text = "10 lbs." },
    { text = "P" },
    { text = "Grapple, slow-firing" },
  ],
  [
    { text = "EMP rifle" },
    { text = "24,000 gp" },
    { text = "2d6" },
    { text = "3d6" },
    { text = "×2" },
    { text = "150 ft." },
    { text = "20" },
    { text = "1 charge" },
    { text = "6 lbs." },
    { text = "E" },
    { text = "Automatic, touch" },
  ],
  [
    { text = "Gravity rifle" },
    { text = "165,000 gp" },
    { text = "1d10" },
    { text = "2d6" },
    { text = "×2" },
    { text = "150 ft." },
    { text = "20" },
    { text = "1 charge" },
    { text = "6 lbs." },
    { text = "Force" },
    { text = "Automatic, touch" },
  ],
  [
    { text = "Id rifle" },
    { text = "50,000 gp" },
    { text = "Special" },
    { text = "Special" },
    { text = "×2" },
    { text = "50 ft." },
    { text = "1 nanite canister" },
    { text = "1 charge" },
    { text = "5 lbs." },
    { text = "Special" },
    { text = "Slow-firing, touch" },
  ],
  [
    { text = "Laser rifle" },
    { text = "20,000 gp" },
    { text = "1d10" },
    { text = "2d6" },
    { text = "×2" },
    { text = "150 ft." },
    { text = "20" },
    { text = "1 charge" },
    { text = "6 lbs." },
    { text = "F" },
    { text = "Automatic, touch" },
  ],
  [
    { text = "Sonic rifle" },
    { text = "26,000 gp" },
    { text = "1d10" },
    { text = "2d6" },
    { text = "×2" },
    { text = "150 ft." },
    { text = "20" },
    { text = "1 charge" },
    { text = "6 lbs." },
    { text = "Sonic" },
    { text = "Automatic, touch" },
  ],
  [
    { text = "Zero rifle" },
    { text = "20,000 gp" },
    { text = "1d10" },
    { text = "2d6" },
    { text = "×2" },
    { text = "150 ft." },
    { text = "20" },
    { text = "1 charge" },
    { text = "6 lbs." },
    { text = "C" },
    { text = "Automatic, touch" },
  ],
  [
    { text = "Two-Handed Ranged Weapons (Heavy Weaponry)", header = true, colspan = 11 },
  ],
  [
    { text = "Atom gun" },
    { text = "144,000 gp" },
    { text = "Special" },
    { text = "Special" },
    { text = "—" },
    { text = "40-ft. cone" },
    { text = "—" },
    { text = "—" },
    { text = "24 lbs." },
    { text = "Special" },
    { text = "Scatter, slow-firing, touch" },
  ],
  [
    { text = "Grenade launcher" },
    { text = "8,000 gp" },
    { text = "Varies" },
    { text = "Varies" },
    { text = "—" },
    { text = "100 ft." },
    { text = "20" },
    { text = "(5 genades)" },
    { text = "1 grenade and 1 charge 8 lbs." },
    { text = "Varies" },
    { text = "Slow-firing" },
  ],
  [
    { text = "Nuclear resonator" },
    { text = "90,000 gp" },
    { text = "Special" },
    { text = "Special" },
    { text = "18-20/×2" },
    { text = "80 ft.^2^" },
    { text = "20" },
    { text = "5 charges" },
    { text = "11 lbs." },
    { text = "Sonic" },
    { text = "Slow-firing, touch" },
  ],
  [
    { text = "Plasmathrower" },
    { text = "30,000 gp" },
    { text = "2d10" },
    { text = "4d6" },
    { text = "19-20/×2" },
    { text = "60 ft." },
    { text = "20" },
    { text = "2 charges" },
    { text = "15 lbs." },
    { text = "E and F" },
    { text = "Automatic or slow-firing, scatter, touch" },
  ],
  [
    { text = "Rail gun" },
    { text = "30,000 gp" },
    { text = "3d8" },
    { text = "3d10" },
    { text = "×4" },
    { text = "200 ft." },
    { text = "10" },
    { text = "1 charge" },
    { text = "14 lbs." },
    { text = "B and P" },
    { text = "Slow-firing, touch" },
  ],
  [
    { text = "Rocket launcher" },
    { text = "10,800 gp" },
    { text = "8d6" },
    { text = "12d6" },
    { text = "—" },
    { text = "120 ft." },
    { text = "10" },
    { text = "10 (disposable)" },
    { text = "10 lbs." },
    { text = "B and F" },
    { text = "Slow-firing" },
  ],
  [
    { text = "Vortex gun" },
    { text = "182,000 gp" },
    { text = "8d6" },
    { text = "10d6" },
    { text = "19-20/×2" },
    { text = "100-ft. cone" },
    { text = "30" },
    { text = "10 charges" },
    { text = "15 lbs." },
    { text = "Force" },
    { text = "Slow-firing, scatter, touch" },
  ],
  [
    { text = "X-laser" },
    { text = "40,000 gp" },
    { text = "6d4" },
    { text = "5d6" },
    { text = "×4" },
    { text = "200 ft." },
    { text = "20" },
    { text = "5 charges" },
    { text = "10 lbs." },
    { text = "F" },
    { text = "Touch" },
  ],
]
foot = [
  [
    { text = "^1^ A weapon with two types is both types if the entry specifies \"and,\" and is either type (wielder's choice) if the entry specifies \"or.\" Damage types are abbreviated as follows: B (bludgeoning), C (cold), E (electricity), F (fire), P (piercing), and S (slashing).", colspan = 11 },
  ],
  [
    { text = "^2^ This weapon has either no range increment or a special range. See the text for more information.", colspan = 11 },
  ],
]
:::

::: entry-link
target = "ref/tech-weapon/arc-pistol"
title = "Arc Pistol"
:::

::: entry-link
target = "ref/tech-weapon/arc-rifle"
title = "Arc Rifle"
:::

::: entry-link
target = "ref/tech-weapon/atom-gun"
title = "Atom Gun"
:::

::: entry-link
target = "ref/tech-weapon/autograpnel"
title = "Autograpnel"
:::

::: entry-link
target = "ref/tech-weapon/chainsaw"
title = "Chainsaw"
:::

::: entry-link
target = "ref/tech-weapon/dart-gun"
title = "Dart Gun"
:::

::: entry-link
target = "ref/tech-weapon/death-ray"
title = "Death Ray"
:::

::: entry-link
target = "ref/tech-weapon/emp-pistol"
title = "EMP Pistol"
:::

::: entry-link
target = "ref/tech-weapon/emp-rifle"
title = "EMP Rifle"
:::

::: entry-link
target = "ref/tech-weapon/flare-gun"
title = "Flare Gun"
:::

::: entry-link
target = "ref/tech-weapon/gravity-pistol"
title = "Gravity Pistol"
:::

::: entry-link
target = "ref/tech-weapon/gravity-rifle"
title = "Gravity Rifle"
:::

::: entry-link
target = "ref/tech-weapon/grenade-launcher"
title = "Grenade Launcher"
:::

::: entry-link
target = "ref/tech-weapon/id-rifle"
title = "Id Rifle"
:::

::: entry-link
target = "ref/tech-weapon/laser-pistol"
title = "Laser Pistol"
:::

::: entry-link
target = "ref/tech-weapon/laser-rifle"
title = "Laser Rifle"
:::

::: entry-link
target = "ref/tech-weapon/laser-torch"
title = "Laser Torch"
:::

::: entry-link
target = "ref/tech-weapon/mindrender"
title = "Mindrender"
:::

::: entry-link
target = "ref/tech-weapon/monowhip"
title = "Monowhip"
:::

::: entry-link
target = "ref/tech-weapon/nuclear-resonator"
title = "Nuclear Resonator"
:::

::: entry-link
target = "ref/tech-weapon/null-blade"
title = "Null Blade"
:::

::: entry-link
target = "ref/tech-weapon/plasmathrower"
title = "Plasmathrower"
:::

::: entry-link
target = "ref/tech-weapon/rail-gun"
title = "Rail Gun"
:::

::: entry-link
target = "ref/tech-weapon/rocket-launcher"
title = "Rocket Launcher"
:::

::: entry-link
target = "ref/tech-weapon/sonic-pistol"
title = "Sonic Pistol"
:::

::: entry-link
target = "ref/tech-weapon/sonic-rifle"
title = "Sonic Rifle"
:::

::: entry-link
target = "ref/tech-weapon/stun-baton"
title = "Stun Baton"
:::

::: entry-link
target = "ref/tech-weapon/stun-gun"
title = "Stun Gun"
:::

::: entry-link
target = "ref/tech-weapon/vortex-gun"
title = "Vortex Gun"
:::

::: entry-link
target = "ref/tech-weapon/x-laser"
title = "X-Laser"
:::

::: entry-link
target = "ref/tech-weapon/zero-pistol"
title = "Zero Pistol"
:::

::: entry-link
target = "ref/tech-weapon/zero-rifle"
title = "Zero Rifle"
:::
