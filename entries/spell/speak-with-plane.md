+++
id = "ref/spell/speak-with-plane"
kind = "spell"
title = "Speak with Plane"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "speak_with_plane", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a small glass bead)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one plane with a sentient structure" },
]
duration = "1 minute/level"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Medium, Summoner, Unchained Summoner\
4: Arcanist, Cleric, Oracle, Shaman, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a small glass bead)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates (see text)
Spell resistance: yes
Target: one plane with a sentient structure
:::

**Sources:** Plane-Hopper's Handbook pg 12

You tap into the awareness and consciousness of a plane with a sentient structure, allowing it to
answer questions. A tangible manifestation of the plane (such as the ground) must be within the
spell's range upon casting. You can ask the sentient plane one question per 2 caster levels. If the
plane's alignment is at least one step away from yours, the plane can attempt a Will save to resist
the spell. A plane typically has a +20 bonus on Will saves, and a demiplane typically has a +15
bonus on Will saves. A plane's traits can further affect these bonuses: a mildly aligned plane
receives a +2 bonus, and a strongly aligned plane or a plane with the wild magic trait receives a +4
bonus on its save.

If a plane has been subject to this spell within the past week, a new casting of this spell
targeting the same plane fails. If speak with plane targets a plane that does not have a sentient
structure, the spell fails.
