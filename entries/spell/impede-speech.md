+++
id = "ref/spell/impede-speech"
kind = "spell"
title = "Impede Speech"
source_ids = ["second-darkness-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "impede_speech", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Bard, Skald\
3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 10 minutes/level
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
:::

**Sources:** Second Darkness Player's Guide pg 27

This minor curse interferes with the target's ability to speak. On a failed save, the target has
difficulty stringing words together. Only with great concentration can he communicate intelligibly.
Speaking in combat becomes a move-equivalent action rather than a free action. If the target
attempts to cast a spell with a verbal component, he has a 50% chance of making an error and losing
the spell. Even if he can successfully cast a spell, doing so takes 1 round if the spell's normal
casting time is less than 1 round. If the spell's casting time is usually 1 round or longer, its
casting time doubles (up until the end of impede speech). Impede speech cannot be dispelled, but
[break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), [remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish) can
end it prematurely.
