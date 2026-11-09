+++
id = "ref/spell/verminous-transformation"
kind = "spell"
title = "Verminous Transformation"
aon = "SpellDisplay.aspx?ItemName=Verminous%20Transformation"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "verminous_transformation", path = "json/spells11.json" },
]
[[sources]]
publication = "horror-adventures"
page = "130"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Investigator", level = 6 },
  { class = "Shaman", level = 7 },
  { class = "Witch", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a handful of bat wings, insects, and rat tails)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Alchemist, Investigator\
7: Shaman, Witch
Casting time: 1 standard action
Components: V, S, M (a handful of bat wings, insects, and rat tails)
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

You partially transform your body into a swarm of bats, insects, rats, and spiders. As a standard
action, you can send out a piece of your body to attack up to four Medium or smaller creatures (or
one larger creature) within 10 feet of you. The creatures take 4d6 points of damage and must succeed
at a Fortitude save or take 1d3 points of Constitution damage and 1d3 points of Strength damage; the
ability damage is a poison effect. Abilities that protect against swarm attacks apply to this damage
and [spell resistance](ref/rule/spell-resistance) applies.

Additionally, since your body is partially a swarm, you take only half damage from piercing and
slashing attacks, unless those attacks would deal full damage or greater to a swarm (for instance,
an area piercing attack would deal full damage to you). You can still be targeted by single-target
spells but you gain a +2 circumstance bonus on any saving throws against them.

Casting spells in this form is difficult and any spells with somatic components require a
[concentration](ref/rule/concentration) check as if casting defensively; if you are also casting the
spell defensively, roll a single concentration check at a -5 penalty.
