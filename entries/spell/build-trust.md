+++
id = "ref/spell/build-trust"
kind = "spell"
title = "Build Trust"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "build_trust", path = "json/spells2.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "205"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 1 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (a gold piece)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day/level; see text"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Paladin\
2: Bard, Cleric, Inquisitor, Mesmerist, Oracle, Psychic, Skald, Warpriest
Casting time: 1 standard action
Components: V, S, M (a gold piece)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 day/level; see text
Saving throw: Will negates
Spell resistance: yes
Target: one creature
:::

You get a sense of the best way to interact with the target in order to encourage positive regard
and fellowship toward you. You gain a +2 circumstance bonus on all Charisma checks and
Charisma-based skill checks you attempt when interacting with the target. In addition, whenever you
fail a Charisma check or Charisma-based skill check when interacting with the target, you can reroll
the check as an immediate action. Attempting this reroll grants the target a new saving throw to end
the spell. The target doesn't become hostile to you when the spell ends, but it does become
disillusioned of its new trust in you. Attacking the target or taking an obvious hostile action
against it automatically ends the spell.

If you are using the [contacts](ref/rule/contacts) rules, your [trust score](ref/rule/trust) with
the target increases by 1 for the duration of the spell. If you're using the individual influence
system, if the target fails its initial saving throw you learn one of its influence skills,
strengths, or weaknesses as though you had succeeded at a discovery check.
