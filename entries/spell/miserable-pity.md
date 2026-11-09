+++
id = "ref/spell/miserable-pity"
kind = "spell"
title = "Miserable Pity"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "miserable_pity", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/sanctuary" },
]
[[sources]]
publication = "ultimate-magic"
page = "229"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level and 1 minute; see text"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level and 1 minute; see text
Saving throw: Will negates (see text)
Spell resistance: yes
Target: creature touched
Descriptors: emotion, mind-affecting
:::

This spell functions as [sanctuary](ref/spell/sanctuary), except creatures attempting to attack the
target who fail their saves also feel a strong sense of pity toward the target, as if it were weak,
pathetic, and not a threat. If the target breaks the spell by attacking, any creature that failed
its save against the spell gains a +2 morale bonus on attack rolls against the target for 1 minute.
