+++
id = "ref/spell/dreadscape"
kind = "spell"
title = "Dreadscape"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dreadscape", path = "json/spells13.json" },
]
[[sources]]
publication = "horror-adventures"
page = "116"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["emotion", "fear", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of black sand)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "up to one creature/level, no two of which can be more than 30 feet apart" },
]
duration = "10 minutes/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Bard, Medium, Mesmerist, Skald\
4: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a pinch of black sand)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 10 minutes/level
Saving throw: Will negates
Spell resistance: yes
Target: up to one creature/level, no two of which can be more than 30 feet apart
Subschool: Phantasm
Descriptors: emotion, fear, mind-affecting
:::

Your targets see their surroundings as a nightmarish reflection of the world around them. Buildings
and furnishings take on a dirty, ruined appearance. Even allies appear foreign and hostile, with
friendly speech turning into garbled mockery and threats. Each target gains the scared condition and
has a hostile attitude toward any new creature it encounters (though not toward creatures that were
already present at the time of the casting). Being hostile doesn't necessarily mean the target will
attack, and creatures can attempt Diplomacy checks to gain a target's trust at the normal DC. If a
creature becomes frightened or panicked while under the influence of dreadscape, that creature takes
1d6 points of Wisdom damage, though only once per casting of dreadscape.

If your campaign uses [the sanity system](ref/rule/sanity), creatures that become frightened or
panicked take 2d6 sanity damage instead of Wisdom damage.
