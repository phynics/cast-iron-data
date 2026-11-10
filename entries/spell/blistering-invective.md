+++
id = "ref/spell/blistering-invective"
kind = "spell"
title = "Blistering Invective"
aon = "SpellDisplay.aspx?ItemName=Blistering%20Invective"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blistering_invective", path = "json/spells2.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "224"

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

You unleash an insulting tirade so vicious and spiteful that enemies who hear it are physically
scorched by your fury. When you cast this spell, make an Intimidate check to demoralize each enemy
within 30 feet of you. Enemies that are demoralized this way take 1d10 points of fire damage and
must succeed at a Reflex save or catch fire. [Spell resistance](ref/rule/spell-resistance) can
negate the fire damage caused by this spell, but does not protect the creature from the demoralizing
effect.
