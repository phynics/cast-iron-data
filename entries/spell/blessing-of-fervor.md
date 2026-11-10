+++
id = "ref/spell/blessing-of-fervor"
kind = "spell"
title = "Blessing of Fervor"
aon = "SpellDisplay.aspx?ItemName=Blessing%20of%20Fervor"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blessing_of_fervor", path = "json/spells2.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "205"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/level, no two of which can be more than 30 ft. apart" },
]
duration = "1 round/level"
saving_throw = "Fortitude negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Cleric, Oracle, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Fortitude negates (harmless)
Spell resistance: yes (harmless)
Targets: one creature/level, no two of which can be more than 30 ft. apart
:::

With this blessing, you call your allies to move forth and empower them to conquer and become
victorious. Each round for the duration of this spell, each of your allies can choose one of the
following bonuses for that round at the beginning of its turn (their choice).

- Increase its speed by 30 feet.
- Stand up as a swift action without provoking an attack of opportunity.
- Take one extra attack as part of a full attack action, using its highest base attack bonus.
- Gain a +2 bonus on attack rolls and a +2 dodge bonus to AC and Reflex saves.
- Cast a single spell of 2nd level or lower as if it were an [enlarged](ref/feat/enlarge-spell),
  [extended](ref/feat/extend-spell), [silent](ref/feat/silent-spell), or
  [still spell](ref/feat/still-spell).

These effects are not cumulative with similar effects, such as those provided by haste or a speed
weapon, nor do they actually grant an extra action, so you can't use it to cast a second spell or
otherwise take an extra action in the round. Blessing of fervor does not stack with haste.
