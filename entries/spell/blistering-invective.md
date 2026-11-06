+++
id = "ref/spell/blistering-invective"
kind = "spell"
title = "Blistering Invective"
source_ids = ["ultimate-combat", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blistering_invective", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["fire", "language-dependant"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Area", value = "30-ft. radius" },
]
duration = "instantaneous"
saving_throw = "Reflex partial, see text"
spell_resistance = "special, see below"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 2: Alchemist, Bard, Inquisitor, Investigator, Mesmerist, Skald
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: instantaneous
Saving throw: Reflex partial, see text
Spell resistance: special, see below
Area: 30-ft. radius
Descriptors: fire, language-dependant
:::

**Sources:** Ultimate Combat pg 224

You unleash an insulting tirade so vicious and spiteful that enemies who hear it are physically
scorched by your fury. When you cast this spell, make an Intimidate check to demoralize each enemy
within 30 feet of you. Enemies that are demoralized this way take 1d10 points of fire damage and
must succeed at a Reflex save or catch fire. [Spell resistance](ref/rule/spell-resistance) can
negate the fire damage caused by this spell, but does not protect the creature from the demoralizing
effect.

### Mythic Blistering Invective

**Sources:** Mythic Adventures pg 86\
Enemies that are demoralized by your Intimidate check take 2d8 points of fire damage and catch fire
(no saving throw). Any Reflex save attempted to extinguish the flames automatically fails as long as
the creature remains demoralized by your Intimidate check.

_Augmented (5th):_ If you expend two uses of mythic power, the spell doesn't have the
language-dependent descriptor and you don't take a penalty on your Intimidate check to demoralize
creatures that are larger than you.
