+++
id = "ref/spell/agonize"
kind = "spell"
title = "Agonize"
source_ids = ["ultimate-magic", "book-of-the-damned-volume-1-princes-of-darkness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "agonize", path = "json/spells.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "205"
[[sources]]
publication = "book-of-the-damned-volume-1-princes-of-darkness"
page = "46"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["evil", "pain"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one conjured outsider or elemental (see text)" },
]
duration = "1 round"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Cleric, Occultist, Oracle, Summoner, Warpriest\
4: Arcanist, Psychic, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round
Saving throw: Fortitude negates
Spell resistance: yes
Target: one conjured outsider or elemental (see text)
Descriptors: evil, pain
:::

You afflict a creature you have conjured via [planar ally](ref/spell/planar-ally) (or a similar
spell) with bolts of vicious energy. These foul energies inflict terrible pain upon the conjured
creature, torturing it to make it more pliant to your will. The targeted creature must make a
Fortitude save or take a -1 penalty for every 2 levels you possess (maximum -10) on all saves and
checks made against you for the next hour. In addition, creatures that demand payment for their
services reduce the payment by 20% for every 4 levels you possess (maximum 60% reduction). However,
beings tortured by this spell quickly come to resent you, making them more likely to try to pervert
your orders to malicious ends or try to seek retribution after their release. This spell has no
effect on creatures that are immune to nonlethal damage.
