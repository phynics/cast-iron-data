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
replaces = ["Deadeye deed", "Startling shot deed", "Bleeding wound deed", "Gun training 1-4"]
alters = ["Gunsmith"]
+++

**Source** Ultimate Combat pg. 51

While most gunslingers have favorite firearms, there are those rare ones who choose to specialize in
one-handed firearms exclusively. These gunslingers are called pistoleros. While they lack the
flexibility of being able to pick up any kind of firearm and use it with reasonable proficiency,
they are crackerjack shots with pistols and similar firearms. Their skill and aim with these
firearms at close range is second to none, and they rarely misfire with these weapons.

**Weapon Proficiency**

**Info:** Instead of proficiency with all firearms, a pistolero only gains proficiency with
one-handed firearms. She must take [Exotic Weapon Proficiency](ref/feat/exotic-weapon-proficiency)
(firearm) to gain proficiency with two-handed firearms and firearm siege engines.

**Gunsmith**

**Alters:** Gunsmith

**Info:** A pistolero must take a [pistol](ref/eq-weapon/pistol) when she chooses a battered firearm
at 1st level.

**Deeds**

**Info:** A pistolero swaps a trio of deeds for the following.

**Up Close and Deadly (Ex)**

**Ability:** When the pistolero hits a target with a one-handed firearm that is not making a scatter
shot, she can spend 1 grit point to deal extra damage on a hit. This extra damage is a number of d6s
equal to 1 + [one-fifth](ref/misc/fractions-and-rounding) of her gunslinger level. If she misses
with the attack, she grazes the target, dealing half the extra damage anyway. This is precision
damage and is not multiplied if the attack is a critical hit. This precision damage stacks with
[sneak attack](ref/ability/sneak-attack) and other forms of precision damage.

**Gained:** At 1st Level

**Replaces:** _Deadeye_ deed

**Special:** The cost of using this deed cannot be reduced with the
[Signature Deed](ref/feat/signature-deed) feat, the true grit class feature, or any similar effect.

**Deadeye (Ex)**

**Ability:** The pistolero gains the [deadeye](ref/deed/deadeye) deed, which is normally a 1st-level
gunslinger deed.

**Gained:** At 7th Level

**Replaces:** Startling shot deed

**Twin Shot Knockdown (Ex)**

**Ability:** When the pistolero hits a single target with two or more one-handed firearm attacks
during her turn, she can spend 1 grit point to knock the target [prone](ref/rule/prone). She can
choose to spend the grit point after the attacks are made.

**Gained:** At 11th Level

**Replaces:** Bleeding wound deed

**Pistol Training (Ex)**

**Gained:** At 5th Level

**Passive:** A pistolero increases her skill with one-handed firearms. She gains a bonus on damage
rolls equal to her Dexterity modifier, and when she misfires with a one-handed firearm, the misfire
value increases by 2 instead of 4.

**Replaces:** Gun training 1-4

At 9th level: The bonus on damage rolls +2.

At 13th level: The bonus on damage rolls +3.

At 17th level: The bonus on damage rolls +4.
