+++
id = "ref/spell/painful-revelation"
kind = "spell"
title = "Painful Revelation"
aon = "SpellDisplay.aspx?ItemName=Painful%20Revelation"
source_ids = ["inner-sea-temples"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "painful_revelation", path = "json/spells7.json" },
]
[[sources]]
publication = "inner-sea-temples"
page = "63"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["mind-affecting", "pain"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one ongoing illusion effect" },
]
duration = "1 hour/level or until discharged"
saving_throw = "Will partial"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Antipaladin, Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 hour/level or until discharged
Saving throw: Will partial
Spell resistance: no
Target: one ongoing illusion effect
Descriptors: mind-affecting, pain
:::

You augment an ongoing illusion effect to strike out painfully at creatures that see through it.
When a creature successfully disbelieves an illusion that is the target of painful revelation, it
takes 1d6 points of nonlethal damage for every 2 caster levels you have (maximum 10d6) and is
staggered for 1d4 rounds. A successful Will save reduces the nonlethal damage by half and negates
the staggered effect. Once painful revelation has been triggered, the spell ends.

However, creatures under the effect of spells such as true seeing that automatically pierce
illusions are not subject to this effect.
