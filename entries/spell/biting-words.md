+++
id = "ref/spell/biting-words"
kind = "spell"
title = "Biting Words"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "biting_words", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["language-dependant", "sonic"]
levels = [
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Skald", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 1: Bloodrager, Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: no
Target: you
Descriptors: language-dependant, sonic
:::

**Sources:** Magic Tactics Toolbox pg 9

Your voice becomes suffused with magic so that you can harm your opponents with but a word. As a
standard action, you can target one opponent within 30 feet with a ranged touch attack by speaking
to it, dealing an amount of damage equal to 1d6 + your Strength or Charisma modifier, whichever is
higher. The damage dealt is bludgeoning, piercing, and slashing damage and can be reduced by
[damage reduction](ref/rule/damage-reduction). Each attack you make reduces the spell's remaining
duration by 1 minute. If an attack reduces the remaining duration to 0 minutes or less, the spell
ends after the attack resolves.

You can attack with biting words by shouting instead of speaking intelligibly. When doing so, the
amount of damage dealt by the attack is reduced to 1d4 + 1/2 your Strength or Charisma modifier
(whichever is higher), but the spell doesn't count as having the language-dependent descriptor for
that attack.
