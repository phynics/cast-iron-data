+++
id = "ref/arc-gunslinger/gun-tank"
kind = "archetype"
title = "Gun Tank"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Gun%20Tank"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "gun_tank", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "ultimate-combat"
page = "50"

[fields]
kind = "archetype"
features = [
  { anchor = "armor-proficiency" },
  { anchor = "deeds" },
  { anchor = "gun-tank-s-resolve", level = 1 },
  { anchor = "gun-tank-s-resilience", level = 15 },
  { anchor = "bullet-deflection" },
  { anchor = "armor-training", level = 4 },
]
trades = [
  { replaces = "Gunslinger's dodge deed", feature = "deeds", power = "gunslinger's dodge", by = ["gun-tank-s-resolve"] },
  { replaces = "Evasive deed", feature = "deeds", power = "evasive", by = ["gun-tank-s-resilience"] },
  { replaces = "Nimble", feature = "nimble", by = ["bullet-deflection"] },
  { replaces = "Bonus feats the gunslinger gains at 4th level and every four levels thereafter", feature = "bonus-feats", by = ["armor-training"] },
]
+++

Gunslingers usually don't use heavy armor, but there are a few who use and modify their armor to
protect themselves from both traditional weapons and gunfire. These gun tanks trundle into battle
with barrels blazing, dealing out punishment with their firearms while knowing few can penetrate
their hard protective shells.

## Armor Proficiency {#armor-proficiency}

A gun tank is proficient with all armors and shields, including tower shields.

## Deeds {#deeds}

A gun tank swaps a pair of deeds for the following. The new deed descriptions include information on
which deeds from the gunslinger class feature these new deeds replace.

## Gun Tank's Resolve (Ex) {#gun-tank-s-resolve}

At 1st level, the gun tank can shrug off the most serious of attacks. When the gun tank is wearing
medium or heavy armor and is subject to a critical hit or [sneak attack](ref/ability/sneak-attack),
she can spend 1 grit point as an immediate action to attempt to negate the critical hit or sneak
attack damage. At 1st level, she has a 25% chance of doing so. At 10th level, the chance increases
to 50%. At 15th level, the chance increases to 75%. While a gun tank's resolve does not stack with
the _[fortification](ref/magic-enh/fortification-light)_ armor special ability, it does work in
concert with that armor special ability or similar effects, so a gun tank can use this ability even
after the _armor of fortification_ has failed to negate the critical hit or sneak attack damage.
This deed replaces the gunslinger's dodge deed.

## Gun Tank's Resilience (Ex) {#gun-tank-s-resilience}

At 15th level, when the gun tank has at least 1 grit point and makes a successful Fortitude saving
throw against an attack that would deal half damage or have a partial effect, she takes no damage or
other effects from that attack. Furthermore, she gains a +2 bonus on all saving throws against fear
and mind-affecting effects. This deed replaces the evasive deed.

## Bullet Deflection (Ex) {#bullet-deflection}

A gun tank is adept at modifying and using her armor to stop firearm attacks. Starting at 2nd level,
a gun tank wearing medium or heavy armor gains half the armor's bonus plus the armor's enhancement
bonus (if any) as a deflection bonus against any non-siege firearm or splash weapon attack
(including the alchemist's bomb class ability; _Advanced Player's Guide_ 28). This ability has no
affect on spells, spell-like abilities, or supernatural abilities that make a touch attack. This
ability replaces nimble.

## Armor Training (Ex) {#armor-training}

At 4th level, a gun tank learns to be more maneuverable while wearing armor. Whenever she is wearing
armor, the armor check penalty is reduced by 1 (to a minimum of 0) and the maximum Dexterity bonus
allowed by her armor increases by 1. Every four levels thereafter (8th, 12th, and 16th), the bonus
increases by 1, to a maximum of a -4 reduction of the armor check penalty and a +4 increase to the
maximum Dexterity bonus allowed. This ability stacks with the [fighter](ref/class/fighter) class
ability of the same name. If the gun tank has both class features, she takes the most advantageous
benefit of the two class features. This ability replaces the bonus feats the gunslinger gains at 4th
level and every four levels thereafter.
