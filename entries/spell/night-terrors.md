+++
id = "ref/spell/night-terrors"
kind = "spell"
title = "Night Terrors"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "night_terrors", path = "json/spells7.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["emotion", "evil", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a drop of black ink)"
range = "touch"
effects = [
  { label = "Target", value = "intelligent creature touched" },
]
duration = "1 day/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 6: Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a drop of black ink)
Range: touch
Duration: 1 day/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: intelligent creature touched
Subschool: Phantasm
Descriptors: emotion, evil, mind-affecting
:::

**Sources:** Horror Adventures pg 123

The target of this spell gains no benefit from normal or magical sleep, writhing in a series of
nightmares that torture its psyche and diminish its ability to perform strenuous tasks. The target
doesn't heal ability or hit point damage naturally and can't prepare spells or regain spell slots.
After one night of poor sleep, the target is fatigued (or exhausted if it was fatigued before trying
to rest). A creature affected by this spell doesn't recover from the fatigued or exhausted condition
inflicted by this spell after resting, nor do spells such as lesser restoration provide any respite.
Each restless night, the target takes 1d4 points of Wisdom damage, which also can't be recovered by
magic while night terrors is active.

The images from previous nightmares continue to haunt the target's mind while awake. If the target
has rested at least once while affected by night terrors and then becomes subjected to a fear
condition, the target experiences the next higher level of fear than it would normally. However, per
the [alternate rules for fear](ref/rule/fear-ha), this spell cannot cause a lesser state of fear to
become a greater one. If the effect causing the fear condition doesn't usually stack with other fear
effects, the target's level of fear does not increase. This aspect of the spell is a fear effect.

The affected creature can attempt a new saving throw once per day to end night terrors, but multiple
attempts to rest in a given day do not afford the target multiple saves. A creature that
successfully saves against night terrors ends the spell and rests normally that night but gains the
benefits of only that night's rest, not any benefits missed on previous nights.

If your campaign uses [the sanity system](ref/rule/sanity), the target takes 1d8 points of sanity
damage instead of Wisdom damage.
