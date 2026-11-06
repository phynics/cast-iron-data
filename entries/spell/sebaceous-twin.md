+++
id = "ref/spell/sebaceous-twin"
kind = "spell"
title = "Sebaceous Twin"
source_ids = ["pathfinder-119-prisoners-of-the-blight"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sebaceous_twin", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 round/level (see text)"
saving_throw = "none (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level (see text)
Saving throw: none (see text)
Spell resistance: yes
Target: living creature touched
:::

**Sources:** Pathfinder \#119: Prisoners of the Blight pg 70

> _Worshippers of [Cyth-V'sug](ref/faith/cyth-vsug) have access to the following spell._

By touching a living target, you cause a half-formed, parasitic clone of the target to burst from
its midsection. The twin dangles from the target's body, making it difficult for the target to move
easily and imparting a -2 penalty on Acrobatics and Climb checks. In addition, for the spell's
duration, the target must succeed at a Fortitude saving throw at the start of its turn each round,
or else it takes 1 point of Constitution damage and is sickened for that round as the twin siphons
off its blood. Each time the target receives any healing (magical or otherwise), the duration of
this spell is extended by 1 round. Each attack that deals damage to the target reduces the duration
of this spell by 1 round. If the duration reaches 0 rounds in this manner, the twin is violently
excised from the body, and the target takes 1d6 points of bleed damage (which can be healed as
normal).

The effect of sebaceous twin counts as a disease effect with a DC equal to the spell's saving throw
DC.
