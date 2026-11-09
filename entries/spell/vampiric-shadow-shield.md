+++
id = "ref/spell/vampiric-shadow-shield"
kind = "spell"
title = "Vampiric Shadow Shield"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vampiric_shadow_shield", path = "json/spells11.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "198"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
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
School: necromancy
Level: 5: Arcanist, Magus, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

This spell wreathes you in shadowy energy and damages those that make melee attacks against you. Any
creature that strikes you with its body or a handheld weapon deals normal damage, but at the same
time the attacker takes 1d6 points of negative energy damage + 1 point per caster level (maximum
+15). If the attacker has [spell resistance](ref/rule/spell-resistance), it applies to this effect.
Creatures wielding melee weapons with reach are not subject to this damage. When an attacker takes
damage from the spell, you heal a number of hit points equal to 25% of the damage the spell dealt.
