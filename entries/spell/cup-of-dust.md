+++
id = "ref/spell/cup-of-dust"
kind = "spell"
title = "Cup of Dust"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cup_of_dust", path = "json/spells3.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "214"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a pinch of dust)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Druid, Hunter, Mesmerist, Occultist, Psychic, Witch
Casting time: 1 standard action
Components: V, S, M (a pinch of dust)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

You curse the target with a thirst no drink can quench. On a failed saving throw, the target begins
to dehydrate. The effects of this spell cannot inflict more nonlethal damage than the target has hit
points. No amount of drinking can counter this effect, although the target still experiences the
other normal effects of any liquid imbibed (such as poisons or potions). Cup of dust can be removed
with a [break enchantment](ref/spell/break-enchantment), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), [remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish)
spell, but effects suffered as a result of dehydration must be healed by normal means.
