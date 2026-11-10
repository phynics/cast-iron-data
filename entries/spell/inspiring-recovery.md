+++
id = "ref/spell/inspiring-recovery"
kind = "spell"
title = "Inspiring Recovery"
aon = "SpellDisplay.aspx?ItemName=Inspiring%20Recovery"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "inspiring_recovery", path = "json/spells14.json" },
]
[[sources]]
publication = "healers-handbook"
page = "9"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Cleric", level = 6 },
  { class = "Hunter", level = 4 },
  { class = "Inquisitor", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Paladin", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Warpriest", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one target creature and all its allies within 60 feet; see text" },
]
duration = "instantaneous and 1 minute"
saving_throw = "Will half (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Hunter, Paladin, Ranger\
6: Cleric, Inquisitor, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous and 1 minute
Saving throw: Will half (harmless)
Spell resistance: yes (harmless)
Target: one target creature and all its allies within 60 feet; see text
Subschool: Healing
Descriptors: mind-affecting
:::

You can heal a creature, harm an undead creature, or call upon a very recently dead creature to
fight beyond death's reach. The target creature regains 1d8 hit points per 2 caster levels (maximum
10d8).

This healing can even bring back to life creatures that have been dead within the previous 1 round
(but they cannot have been dead for any longer). If you apply this spell's healing to such a
creature and its hit point total is at a negative amount less than its Constitution score, it comes
back to life and stabilizes at its new hit point total. If you awaken a dead creature in this way,
all allies of that creature within 60 feet who can see it regain consciousness gain a +2 morale
bonus on attack rolls, damage rolls, and saving throws for 1 minute thereafter, as the healing
powers of your deity have imbued them with renewed vigor.

Creatures killed by death effects cannot be revived this way. This spell deals damage to undead
creatures rather than curing them, and it cannot bring them back to life.
