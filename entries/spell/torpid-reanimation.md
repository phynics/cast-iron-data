+++
id = "ref/spell/torpid-reanimation"
kind = "spell"
title = "Torpid Reanimation"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "torpid_reanimation", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (an onyx gem worth at least 25 gp per HD of the undead)"
range = "touch"
effects = [
  { label = "Target", value = "one or more corpses touched" },
]
duration = "1 day/caster level and instantaneous (see text)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin, Cleric, Occultist, Oracle, Shaman, Spiritualist, Warpriest\
5: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (an onyx gem worth at least 25 gp per HD of the undead)
Range: touch
Duration: 1 day/caster level and instantaneous (see text)
Saving throw: none
Spell resistance: no
Target: one or more corpses touched
Descriptors: evil
:::

**Sources:** Horror Adventures pg 130

This spell works like [animate dead](ref/spell/animate-dead) except you set a specific condition for
when the animation occurs and you do not immediately have control of the creatures. The condition
can be simple, such as being touched, a certain word spoken, or on hearing a specific sound. You can
also set a condition based on time, but it must occur within a number of days equal to your caster
level. At any time, you can cause the animation to occur as a standard action.

You can gain control of any uncontrolled undead you created with this spell as a free action if you
are within at least 60 feet of the undead creature and have line of sight to it; if you have control
of an undead you created with this spell and later lose control of that undead, you can't use this
ability to regain control of the same undead. The limit on the number of Hit Dice you can control
with animate dead still applies.
