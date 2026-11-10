+++
id = "ref/rule/spell-attack-rolls"
kind = "rule"
title = "Spell Attack Rolls"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spell_attack_rolls", path = "json/rules_subsystems04.json" },
]
[[sources]]
publication = "pathfinder-unchained"
page = "148"

[fields]
kind = "none"
+++

When casting a spell or using a magical effect that allows a saving throw, the caster makes a spell
attack roll, rolling 1d20 with a bonus equal to her spellcasting ability modifier plus the spell's
level. Any bonuses that would normally make the spell more difficult to avoid (such as the
[Spell Focus](ref/feat/spell-focus) feat) also apply. The DC of this roll is equal to 11 + the
target's relevant save bonus. If the caster succeeds, treat the spell or effect as if the target had
failed its save. Otherwise, treat it as if the target succeeded at its save. Just like an ordinary
attack roll, a natural 1 is an automatic failure, while a natural 20 is an automatic success. This
rule does not change the chances of success; it just changes who is rolling the die.

For example, a wizard with an Intelligence score of 18 casts [charm person](ref/spell/charm-person)
on an orc guard. Normally, the orc would attempt a DC 15 Will saving throw (10 + 1 for a 1st-level
spell + 4 for the wizard's Intelligence bonus). Since the orc's Will save modifier is -1, he has to
roll a 16 to succeed, and thus will fail his save 80% of the time. Under the spell attack roll
rules, rather than the orc attempting a Will save, the wizard makes a spell attack roll with a +5
bonus (the spell's DC of 15 - 10) against a DC of 10 (11 + the orc's -1 Will save modifier). The
wizard has to roll at least a 5 to succeed, so he still affects his target 80% of the time.

This variant puts more dice in the hands of the players. Consider running NPC spellcasters under the
core rules instead, so that players can feel responsible for their own saves. It's usually easiest
for the player to write down the spell attack roll bonus for each level.

**Faster Variant:** Normally, a caster would roll a separate spell attack roll against each target.
A GM who wants to speed up play (at the expense of making the game more prone to extremes and not
matching the core rules as closely) can instead require only a single roll and apply it against the
defenses of all the targets.
