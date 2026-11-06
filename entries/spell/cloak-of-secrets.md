+++
id = "ref/spell/cloak-of-secrets"
kind = "spell"
title = "Cloak of Secrets"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cloak_of_secrets", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 minute"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "5-ft.-radius emanation centered on a point in space" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Antipaladin, Arcanist, Bard, Cleric, Inquisitor, Oracle, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 minute
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Area: 5-ft.-radius emanation centered on a point in space
Subschool: Glamer
Descriptors: glamer
:::

**Sources:** Heroes of the Streets pg 30

This spell forms an invisible bubble that filters all speech coming from inside the affected area so
that creatures outside hear a completely different version of the conversation. The bubble also
disguises lip movements to match the false conversation. Any creature listening to the conversation
for at least 1 round can attempt a DC 15 Sense Motive check to realize that the apparent
conversation doesn't actually make any sense. The bubble also obscures the verbal components of
spells cast within the area so it's impossible to identify spells by their verbal components alone,
and anyone outside the bubble attempting a Spellcraft check to identify a spell cast within the
bubble takes a -5 penalty on the check. Furthermore, the bubble renders any language-dependent
spells and effects used within the bubble ineffective against creatures outside the area.
