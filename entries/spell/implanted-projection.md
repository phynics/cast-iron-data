+++
id = "ref/spell/implanted-projection"
kind = "spell"
title = "Implanted Projection"
source_ids = ["occult-adventures", "occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "implanted_projection", path = "json/spells10.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/telempathic-projection" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Spiritualist", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Mesmerist, Psychic, Spiritualist
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Will negates (see text)
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

### Implanted Projection

**Sources:** Occult Origins pg 13

This spell functions as [telempathic projection](ref/spell/telempathic-projection), except its
mood-altering effects remain dormant in the target's mind. Upon casting this spell, the caster
designates a command word or phrase, of which the target retains no memory. The next creature to
speak the command word or phrase to the target triggers the implanted telempathic projection,
treating the speaker as the original spellcaster.
