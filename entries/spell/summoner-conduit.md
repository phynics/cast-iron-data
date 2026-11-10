+++
id = "ref/spell/summoner-conduit"
kind = "spell"
title = "Summoner Conduit"
aon = "SpellDisplay.aspx?ItemName=Summoner%20Conduit"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summoner_conduit", path = "json/spells16.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "245"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Summoner", level = 4 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (two flies)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one summoned creature or eidolon" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Cleric, Occultist, Oracle, Summoner, Unchained Summoner, Warpriest\
5: Arcanist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (two flies)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Target: one summoned creature or eidolon
:::

You exploit the invisible, mystic connection between the target creature and its summoner to harm
that summoner. Whenever the target's summoned creature is the target of a spell that deals damage,
the target's summoner is also considered to be a target of that spell. Such a summoner gains his
normal defenses against the spell, such as a saving throw and
[spell resistance](ref/rule/spell-resistance), and cannot be affected if he is on another plane of
existence.
