+++
id = "ref/spell/counterbalancing-aura"
kind = "spell"
title = "Counterbalancing Aura"
aon = "SpellDisplay.aspx?ItemName=Counterbalancing%20Aura"
source_ids = ["planar-adventures", "champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "counterbalancing_aura", path = "json/spells12.json" },
]
[[sources]]
publication = "planar-adventures"
page = "40"
[[sources]]
publication = "champions-of-balance"
page = "26"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 8 },
  { class = "Oracle", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, F (a set of scales worth 500 gp)"
range = "20 ft."
effects = [
  { label = "Target", value = "one creature/level in a 20-ft.-radius burst centered on you" },
]
duration = "1 round/level"
saving_throw = "see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 8: Cleric, Oracle
Casting time: 1 standard action
Components: V, S, F (a set of scales worth 500 gp)
Range: 20 ft.
Duration: 1 round/level
Saving throw: see text
Spell resistance: yes
Target: one creature/level in a 20-ft.-radius burst centered on you
:::

An oscillating bronze glow surrounds the targets, protecting them from attacks, granting them
resistance to spells cast by neutral creatures, and sickening or nauseating neutral creatures that
strike the targets. This abjuration has four effects.

First, each warded creature gains a +4 deflection bonus to AC and a +4 resistance bonus on saving
throws. This benefit applies against all attacks and effects, not just attacks by neutral creatures.

Second, a warded creature gains [spell resistance](ref/rule/spell-resistance) 23 against spells cast
by chaotic neutral, lawful neutral, neutral evil, and neutral good creatures, and spell resistance
27 against spells cast by neutral creatures with no other alignment components.

Third, the spell protects warded creatures from possession and influence by such creatures
(otherwise as [protection from evil](ref/spell/protection-from-evil)).

Finally, if a chaotic neutral, lawful neutral, neutral evil, or neutral good creature successfully
hits a warded creature with a melee attack, the attacker is sickened for 1d6 rounds (Fortitude
negates). If a neutral creature successfully hits a warded creature with a melee attack, the
attacker is instead nauseated for 1d6 rounds (Fortitude negates).
