+++
id = "ref/spell/reboot"
kind = "spell"
title = "Reboot"
source_ids = ["people-of-the-stars"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "reboot", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 round"
components = "V, S, F (a ruby worth at least 25 gp per HD of the target construct)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one destroyed construct of up to 2 HD/level" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Summoner, Unchained Summoner\
5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S, F (a ruby worth at least 25 gp per HD of the target construct)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: one destroyed construct of up to 2 HD/level
:::

**Sources:** People of the Stars pg 29

Whispering in the dense, information-rich machine language of the First Ones, you bring a destroyed
construct back to operational status for a short time, restoring it to 1 hit point. The construct
can be further healed with spells like make whole, but it returns to its destroyed state as soon as
this spell's duration expires or it is brought to 0 hit points, whichever comes first. As long as
the construct is active, it obeys your commands to the best of its ability, fighting on your behalf
and carrying out tasks that it is capable of performing.

Constructs with more than twice as many Hit Dice as your caster level cannot be targeted by this
spell.
