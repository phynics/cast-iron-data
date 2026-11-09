+++
id = "ref/rule/critical-hits"
kind = "rule"
title = "Critical Hits"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "critical_hits", path = "json/rules_combat01.json" },
]
[[sources]]
publication = "core-rulebook"
page = "184"

[fields]
kind = "none"
+++

When you make an attack roll and get a natural 20 (the d20 shows 20), you hit regardless of your
target's Armor Class, and you have scored a "threat," meaning the hit might be a critical hit (or
"crit"). To find out if it's a critical hit, you immediately make an attempt to "confirm" the
critical hit - another attack roll with all the same modifiers as the attack roll you just made. If
the confirmation roll also results in a hit against the target's AC, your original hit is a critical
hit. (The critical roll just needs to hit to give you a crit, it doesn't need to come up 20 again.)
If the confirmation roll is a miss, then your hit is just a regular hit.

A critical hit means that you roll your damage more than once, with all your usual bonuses, and add
the rolls together. Unless otherwise specified, the threat range for a critical hit on an attack
roll is 20, and the multiplier is ×2.

> **Exception:** Precision damage (such as from a rogue's [sneak attack](ref/ability/sneak-attack)
> class feature) and additional damage dice from weapon special abilities (such as
> [flaming](ref/magic-enh/flaming)) are not multiplied when you score a critical hit.

**Increased Threat Range:** Sometimes your threat range is greater than 20. That is, you can score a
threat on a lower number. In such cases, a roll of lower than 20 is not an automatic hit. Any attack
roll that doesn't result in a hit is not a threat.

**Increased Critical Multiplier:** Some weapons deal better than double damage on a critical hit.

**Spells and Critical Hits:** A spell that requires an attack roll can score a critical hit. A spell
attack that requires no attack roll cannot score a critical hit. If a spell causes
[ability damage or drain](ref/rule/ability-damage-drain), the damage or drain is doubled on a
critical hit.
