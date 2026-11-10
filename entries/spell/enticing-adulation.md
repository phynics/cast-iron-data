+++
id = "ref/spell/enticing-adulation"
kind = "spell"
title = "Enticing Adulation"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enticing_adulation", path = "json/spells4.json" },
]
[[sources]]
publication = "agents-of-evil"
page = "30"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a lock of your hair)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "10 minutes/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Skald\
4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a lock of your hair)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting
:::

A targeted creature that fails its saving throw is filled with a deep desire to protect and care for
you, fawning over your needs and ensuring your comfort. If another creature harms you, the target is
immediately overcome with rage and is compelled to attack the aggressor, gaining a +2 morale bonus
to Strength and Constitution, a +1 morale bonus on Will saves, and a -2 penalty to its Armor Class.
These bonuses last until the instigating creature is defeated or retreats, or the target of the
spell is killed or rendered unconscious. If other creatures have harmed you while the target is
under this effect, the target continues to rage until all threats against you are defeated or driven
off, after which the target creature is fatigued for as many rounds as it raged. Your target
continues to fly into defensive rages each time a creature harms you so long as the spell's duration
lasts, but cannot rage while fatigued.

If you are reduced below 0 hit points by an attack, the target creature must succeed at a second
Will save or be compelled to defend your body, attacking anyone who comes near, for the remainder of
the spell's duration. If the creature succeeds at this second save, the spell immediately ends.
