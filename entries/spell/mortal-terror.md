+++
id = "ref/spell/mortal-terror"
kind = "spell"
title = "Mortal Terror"
source_ids = ["legacy-of-the-first-world"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mortal_terror", path = "json/spells7.json" },
]
[[sources]]
publication = "legacy-of-the-first-world"
page = "13"

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["fear", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Antipaladin, Arcanist, Bard, Cleric, Inquisitor, Mesmerist, Oracle, Psychic, Shaman, Skald, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will partial (see text)
Spell resistance: yes
Target: one creature
Descriptors: fear, mind-affecting
:::

You imbue the target with an exaggerated sense of its own mortality and a drive for
self-preservation. The target is shaken, and the first time each round the target takes damage
(including the first round of the spell's duration), it must succeed at another Will save or its
fear level increases by one step (from shaken to frightened, and from frightened to panicked). If
the target fails a saving throw against this effect while panicked, it is transfixed in terror and
is helpless for the remainder of the spell's duration. If the target succeeds at the initial Will
save, it is shaken for 1 round but its fear level cannot be further increased by this spell's
effects during that round.
