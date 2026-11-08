+++
id = "ref/arc-gunslinger/firebrand"
kind = "archetype"
title = "Firebrand"
source_ids = ["elemental-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "firebrand", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]

[fields]
kind = "archetype"
replaces = ["Deadeye deed", "Dead shot deed", "Bonus feats gained at 4th", "8th", "12th", "16th", "and 20th levels", "Gun training"]
alters = ["Gunsmith", "Grit"]
+++

**Sources:** Elemental Master's Handbook pg 4\
Where other gunslingers rely on precision shooting, the firebrand instead masters explosive
ordnance. Firebrands tend to be passionate, devil-may-care wanderers living each day to the fullest.

**Gunsmith**

**Ability:** A firebrand gains a [dragon pistol](ref/eq-weapon/dragon-pistol) as her battered
firearm.

**Alters:** Gunsmith

**Gained:** At 1st Level

**Wild Card (Ex)**

**Alters:** Grit

**Info:** A firebrand uses her Charisma instead of Wisdom to determine the number of grit points she
gains at the start of each day and to determine the DCs of her gunslinger deeds.

**Passive:** A firebrand treats direct hits with her bombs as firearm attacks for the purpose of
regaining grit (see the _bombs_ ability below).

**Special:** This ability works in all other ways like the gunslinger's _grit_ class feature.

**Deeds**

**Ability:** A firebrand gains the following deeds.

**Dragon Fire (Ex)**

**Flavor:** A firebrand is a master of the volatile substance known as dragon's breath.

**Gained:** At 1st Level

**Passive:** Her attacks with dragon's breath cartridges misfire only if a 1 is rolled on two or
more of the damage dice.

**Replaces:** Deadeye deed

**Swift:** The firebrand can spend 1 grit point to add her Charisma modifier to the DCs of all
[dragon's breath cartridges](ref/eq-weapon/alchemical-cartridge-dragons-breath) she fires until the
end of her turn.

**Big Boom! (Su)**

**Flavor:** A firebrand can channel her explosive potential into a mighty blast.

**Gained:** At 7th Level

**Replaces:** Dead shot deed

**Special:** Using this deed costs 2 grit points and expends one of the firebrand's daily uses of
bombs (see the _bombs_ ability below), as well as the appropriate ammunition for the firearm attack;
ammunition that does not require an attack roll cannot be used this way.

**Standard:** The firebrand shoots a 30-foot cone of fire from the barrel of her gun. The firebrand
designates one creature in the squares affected by the cone to be the target and makes an attack
roll with her firearm against that creature; on a hit, the target takes damage as if it were
directly hit by both the firebrand's firearm and her bomb. Creatures in all other squares in the
cone (as well as the target's square, if the gunslinger's attack missed) take splash damage as if
they were in the area of the firebrand's bomb, with a Reflex saving throw for half damage. (The DC
of this saving throw is equal to 10 + half the firebrand's gunslinger level + the firebrand's
Charisma modifier.)

**Scorched Earth (Ex)**

**Flavor:** The firebrand knows how to make dragon's breath burn white-hot.

**Gained:** At 4th Level

**Passive:** The fire damage of the first dragon's breath cartridge fired by the firebrand each
round increases by a number of d6s equal to [one-fourth](ref/misc/fractions-and-rounding) of her
gunslinger level (to a maximum total of 7d6 at 20th level).

**Replaces:** Bonus feats gained at 4th, 8th, 12th, 16th, and 20th levels

**Bombs (Su)**

**Ability:** The firebrand gains the bombs ability as an [alchemist](ref/class/alchemist) of her
gunslinger level - 4, using her Charisma modifier in place of her Intelligence modifier to determine
her number of bombs per day and the DC to avoid splash damage. The firebrand adds her Charisma
modifier to her bombs' damage instead of her Intelligence modifier, even if she has the _throw
anything_ class feature. In addition, the firebrand's bombs are always under the effect of the
[explosive bomb](ref/discovery/explosive-bomb) discovery.

**Gained:** At 5th Level

**Replaces:** Gun training

**Special:** Firebrand levels do not stack with levels in other classes with the bombs class
feature.
