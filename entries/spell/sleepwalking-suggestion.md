+++
id = "ref/spell/sleepwalking-suggestion"
kind = "spell"
title = "Sleepwalking Suggestion"
aon = "SpellDisplay.aspx?ItemName=Sleepwalking%20Suggestion"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sleepwalking_suggestion", path = "json/spells9.json" },
]
[[sources]]
publication = "horror-adventures"
page = "127"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (two doses of oil of taggit worth 180 gp total)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "24 hours"
saving_throw = "Will negates or none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Medium\
4: Bard, Mesmerist\
5: Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (two doses of oil of taggit worth 180 gp total)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 24 hours
Saving throw: Will negates or none, see text
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You compel the target creature to rise from its sleep as if sleepwalking and perform a course of
activity (limited to a sentence or two). The spell takes effect immediately if the target is already
asleep, or as soon as the target falls asleep if it is conscious. You can specify that the creature
should wait before taking action when you give your instructions if you so choose. A sleeping
creature doesn't get a save against this spell. The suggested activity must not cause the target to
directly harm itself or others, but it doesn't need to be reasonable. For example, you could
instruct the target to unlock doors and windows or poison its ally's rations, but not jump off a
roof or perform a _coup de grace_ action against a sleeping ally. Instructions that cause direct
harm prompt the target to awaken just prior to performing the action and the target experiences a
vague memory of what it was supposed to do.

The target moves at its speed, but isn't capable of running or moving at a higher rate of speed. It
moves in dark conditions as if it had [darkvision](ref/rule/darkvision) and can perform most simple
and skill-based actions, but it can't engage in combat, spellcasting, or actions that require
significant cognitive awareness (like making complex decisions, solving puzzles, or using
complicated magic items). If the creature takes any damage while sleepwalking, it must attempt a new
saving throw. If it succeeds, the spell ends and the creature awakens. When the target completes the
suggested course of activity, or when the spell ends or is dismissed, the target remains unconscious
and returns to where it was sleeping and must be awoken normally. It retains no memory of what it
did while unconscious (with the only exception described above).

Unlike the [sleepwalk](ref/spell/sleepwalk) spell, attempts to use sleepwalking suggestion on a
creature that is unconscious for any reason other than sleep automatically fail. A creature affected
by sleepwalking suggestion is unaware it has been programmed to act in its sleep (unless awoken
because it was about to cause harm).
