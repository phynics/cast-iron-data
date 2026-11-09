+++
id = "ref/spell/phasic-challenge"
kind = "spell"
title = "Phasic Challenge"
source_ids = ["magic-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phasic_challenge", path = "json/spells7.json" },
]
[[sources]]
publication = "magic-tactics-toolbox"
page = "6"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 8 },
  { class = "Shaman", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M (a scrape of a knight's banner)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "two creatures within 60 feet of one another; see text" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 6: Spiritualist\
7: Witch\
8: Cleric, Shaman, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a scrape of a knight's banner)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates; see text
Spell resistance: yes
Targets: two creatures within 60 feet of one another; see text
:::

You select one enemy and one willing ally as targets. The enemy gains a new Will saving throw at the
beginning of each turn, and on a successful saving throw the spell ends. Both targets remain visible
and audible, and can see and hear other creatures, but cannot physically interact with any creature
save one another. Spells or weapon attacks from the affected creatures impact only each other,
though spells might affect terrain or other factors not related to other creatures. If one of the
creatures becomes unconscious or dies, or if the effect is dispelled, the effect ends for both of
them.
