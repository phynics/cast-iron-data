+++
id = "ref/spell/wave-form"
kind = "spell"
title = "Wave Form"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wave_form", path = "json/spells11.json" },
]

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["water"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Arcanist, Bloodrager, Cleric, Druid, Hunter, Oracle, Shaman, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: instantaneous
Saving throw: see text
Spell resistance: no
Target: you
Descriptors: water
:::

**Sources:** Aquatic Adventures pg 61

You transform into a wave of frothing water up to 15 feet wide and 15 feet tall, as space permits,
and then surge forth in a straight line in the direction of your choice, moving up to twice your
base movement speed before immediately returning to your normal form. This movement does not provoke
attacks of opportunity. While in wave form, you are immune to weapon attacks and attacks that target
a specific number of creatures (since the spell is instantaneous, this is mainly relevant for
readied actions and the like). All creatures and unattended objects in your path take 4d6 points of
bludgeoning damage and are knocked prone. A successful Reflex save prevents a creature from being
knocked prone.
