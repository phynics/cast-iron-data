+++
id = "ref/spell/bloodstone-mirror"
kind = "spell"
title = "Bloodstone Mirror"
source_ids = ["pathfinder-140-eulogy-for-roslars-coffer"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bloodstone_mirror", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 7 },
  { class = "Occultist", level = 5 },
  { class = "Oracle", level = 7 },
  { class = "Witch", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a red bloodstone worth 500 gp)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Occultist\
7: Cleric, Oracle, Witch
Casting time: 1 standard action
Components: V, S, M (a red bloodstone worth 500 gp)
Range: personal
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Pathfinder \#140: Eulogy for Roslar's Coffer pg 72

Developed due to [Arazni's](ref/faith/arazni) fear that her stolen organs might be used to control
her, this spell reflects any attempts to steal your free will. Whenever you are exposed to a
mind-affecting effect or a spell that would otherwise give another creature control of your actions
(such as [control undead](ref/spell/control-undead)), you can dispel this effect as an immediate
action to redirect the spell to a creature within 30 feet. The affected creature must attempt a save
against the original DC of the triggering effect. On a failure, it is subject to the effects of the
triggering spell, with the exception that you are treated as the original caster (statistics
determined by caster level are still calculated according to its original caster). The target
creature applies any [spell resistance](ref/rule/spell-resistance) or immunities it has normally.
You can have only one instance of this spell active at a time.
