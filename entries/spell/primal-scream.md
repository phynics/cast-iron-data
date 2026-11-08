+++
id = "ref/spell/primal-scream"
kind = "spell"
title = "Primal Scream"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "primal_scream", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/break-enchantment" },
]

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["mind-affecting", "sonic"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Skald", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Bard, Mesmerist, Skald
Casting time: 1 standard action
Components: V
Range: personal
Duration: 1 round/level
Saving throw: none
Spell resistance: no
Target: you
Descriptors: mind-affecting, sonic
:::

**Sources:** Ultimate Magic pg 232

You voice a mighty yell from the depths of your soul, invigorating yourself and dispelling
enchantment and paralysis effects. This functions as
[break enchantment](ref/spell/break-enchantment), except it only affects you and only frees you from
enchantment and paralysis effects. If the caster level check to break the hostile effect succeeds,
you give voice to your scream and the spell takes effect normally; if not, this spell fails without
further effect. You can cast this spell even when paralyzed or unable to speak because of an
enchantment effect, but not in an area of silence, if you are unable to speak for reasons other than
enchantments or paralysis (for example, if you are gagged), or if cast in an environment where
speaking is not possible.
