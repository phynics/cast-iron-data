+++
id = "ref/spell/deep-slumber"
kind = "spell"
title = "Deep Slumber"
aon = "SpellDisplay.aspx?ItemName=Deep%20Slumber"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deep_slumber", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/sleep" },
]
[[sources]]
publication = "core-rulebook"
page = "265"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S, M (fine sand, rose petals, or a live cricket)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "one or more living creatures within a 10-ft.-radius burst" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Arcanist, Bard, Mesmerist, Occultist, Psychic, Shaman, Skald, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S, M (fine sand, rose petals, or a live cricket)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Area: one or more living creatures within a 10-ft.-radius burst
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell functions like [sleep](ref/spell/sleep), except that it affects 10 HD of targets.
