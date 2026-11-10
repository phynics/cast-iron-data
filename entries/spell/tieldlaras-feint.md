+++
id = "ref/spell/tieldlaras-feint"
kind = "spell"
title = "Tieldlara's Feint"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tieldlaras_feint", path = "json/spells10.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "27"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "20 ft."
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: 20 ft.
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Charm
Descriptors: mind-affecting
:::

With a lascivious wink and a sensuous sway, you flood a foe's mind with lustful thoughts of you,
distracting your target and rendering that creature vulnerable to your attacks. An affected creature
takes a penalty equal to half your caster level on [concentration](ref/rule/concentration) checks
and to its CMD against dirty trick, grapple, and steal combat maneuvers you perform. The creature is
also denied its Dexterity bonus to AC for the first melee attack you make against it each round.

If the target would not normally be sexually attracted to you, it receives a +4 bonus on its saving
throw. If you end your turn more than 20 feet from the target or end your turn where your target
cannot see you, this spell immediately ends.
