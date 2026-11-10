+++
id = "ref/spell/illusory-poison"
kind = "spell"
title = "Illusory Poison"
source_ids = ["gnomes-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "illusory_poison", path = "json/spells14.json" },
]
[[sources]]
publication = "gnomes-of-golarion"
page = "27"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "weapon touched" },
]
duration = "1 minute/level or until discharged (see text)"
saving_throw = "Will disbelief, then Fortitude (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Arcanist, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level or until discharged (see text)
Saving throw: Will disbelief, then Fortitude (see text)
Spell resistance: yes
Target: weapon touched
Subschool: Phantasm
Descriptors: mind-affecting
:::

You create a phantasm of an oily green phantasmal poison on the target weapon. The first creature
hit by the poisoned weapon must make a Will save against the illusion spell; success means the spell
has no effect and is expended from the weapon. If the creature fails its save, it believes it has
been poisoned and must make Fortitude saves at the spell's DC to avoid suffering illusory poison
damage.

Delay poison allows the target to ignore the effects of the phantasmal poison until the delay poison
spell ends, at which time it may make a Will save to realize the poison is illusory and recover all
illusory poison damage. Neutralize poison, lesser restoration, or restoration immediately recovers
all damage from the spell. A successful [dispel magic](ref/spell/dispel-magic) spell ends the effect
of the illusion, as do spells that penetrate illusions (such as
[true seeing](ref/spell/true-seeing)). The target automatically recovers all illusory poison damage
after 1 hour.

#### Phantasmal Poison

**Type** poison, injury; **Save** Fortitude DC as the spell\
**Frequency** 1/round for 6 rounds\
**Effect** 1d3 Str damage; **Cure** 1 save
