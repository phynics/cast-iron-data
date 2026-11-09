+++
id = "ref/spell/mindshock"
kind = "spell"
title = "Mindshock"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mindshock", path = "json/spells14.json" },
]
[[sources]]
publication = "occult-origins"
page = "28"

[fields]
kind = "spell"
school = "divination"
descriptors = ["mind-affecting", "pain"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Antipaladin, Bloodrager, Inquisitor, Medium, Occultist, Psychic, Shaman, Spiritualist, Witch
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: mind-affecting, pain
:::

You charge yourself with violent psychic energy so attacks you make with weapons, natural weapons,
and unarmed strikes cause the target to recall pain suffered in the past. Such attacks deal 1d4
points of nonlethal damage in addition to their normal damage, though creatures immune to
mind-affecting or pain effects ignore this additional damage. In addition, when you confirm a
critical hit, the target is confused for 1 round by the pain. Creatures immune to critical hits,
mind-affecting, or pain effects ignore the confusion. Even if you confirm multiple critical hits
while this spell is in effect, an individual creature can only be confused by a single casting of
mindshock once.
