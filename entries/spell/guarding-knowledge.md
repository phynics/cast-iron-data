+++
id = "ref/spell/guarding-knowledge"
kind = "spell"
title = "Guarding Knowledge"
aon = "SpellDisplay.aspx?ItemName=Guarding%20Knowledge"
source_ids = ["monster-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "guarding_knowledge", path = "json/spells5.json" },
]
[[sources]]
publication = "monster-hunters-handbook"
page = "30"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (see text)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Inquisitor\
3: Alchemist, Arcanist, Bard, Cleric, Investigator, Occultist, Oracle, Psychic, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (see text)
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

Upon casting this spell, choose a specific variety of monster ([red dragon](ref/family/dragon-red)
rather than [dragon](ref/family/dragon-true)) and one of its special attacks that you have
successfully identified with a Knowledge check or otherwise researched, such as a
[cockatrice's](ref/monster/cockatrice) petrification ability or a spider swarm's poison. You gain a
+4 insight bonus on saving throws against the selected special attack. The bonus does not apply to
saves against other monsters' abilities of the same name,
[spell-like abilities](ref/umr/spell-like-abilities), or special attacks derived from class levels
or equipment. If you use a trophy from a monster of the exact same variety as an optional material
component, the bonus increases to +6.
