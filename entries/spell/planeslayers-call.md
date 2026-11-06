+++
id = "ref/spell/planeslayers-call"
kind = "spell"
title = "Planeslayer's Call"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "planeslayers_call", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "enchantment [mind-affecting, see text]"
subschools = ["Compulsion"]
levels = [
  { class = "Cleric", level = 5 },
  { class = "Inquisitor", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Paladin", level = 4 },
  { class = "Warpriest", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "20 ft."
effects = [
  { label = "Targets", value = "allies within a 20-ft.-radius burst centered on you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment \[mind-affecting, see text\]
Level: 4: Inquisitor, Occultist, Paladin\
5: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: 20 ft.
Duration: 1 round/level
Saving throw: none
Spell resistance: yes
Targets: allies within a 20-ft.-radius burst centered on you
Subschool: Compulsion
:::

**Sources:** Advanced Class Guide pg 190

The magic of your allies in the area becomes more potent against certain outsiders. Chose one
alignment subtype (chaotic, evil, good, or lawful). Against outsiders with that alignment component
or subtype, your allies in the area gain a +2 bonus on caster level checks to overcome
[spell resistance](ref/rule/spell-resistance), and their spells ignore the first 10 points of energy
resistance (but not energy immunity).

This spell gains the alignment descriptor that is opposite the outsider alignment chosen. For
example, if you choose for the spell to affect evil outsiders, then this spell has the good
descriptor.
