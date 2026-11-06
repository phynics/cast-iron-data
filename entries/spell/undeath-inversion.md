+++
id = "ref/spell/undeath-inversion"
kind = "spell"
title = "Undeath Inversion"
source_ids = ["undead-slayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undeath_inversion", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a gold piece with one scratched face)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one undead creature" },
]
duration = "1 round/level (d); see text"
saving_throw = "Will negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a gold piece with one scratched face)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (d); see text
Saving throw: Will negates, see text
Spell resistance: yes
Target: one undead creature
:::

**Sources:** Undead Slayer's Handbook pg 27

You alter an undead creature's energy affinity so that it takes damage from negative energy and
gains healing from positive energy, as if it were a living creature. If the target was able to
channel negative energy or produce negative energy effects (such as inflict spells), these abilities
produce positive energy instead, healing living targets and harming the undead. The target cannot
impose negative levels on other creatures for the duration of the spell. The target's creature type
does not change, and it is still considered an undead creature. Each round on its turn, the subject
may attempt a new saving throw to end the effect. This is a full-round action that does not provoke
attacks of opportunity.
