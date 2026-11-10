+++
id = "ref/spell/enemys-heart"
kind = "spell"
title = "Enemy's Heart"
source_ids = ["advanced-race-guide", "orcs-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enemys_heart", path = "json/spells4.json" },
]
[[sources]]
publication = "advanced-race-guide"
page = "143"
[[sources]]
publication = "orcs-of-golarion"
page = "28"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["death", "evil"]
levels = [
  { class = "Adept", level = 2 },
  { class = "Antipaladin", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 full-round action, special see below"
components = "V, S, M (target creature's heart)"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "concentration/1 minute per hd of the subject; see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Adept, Antipaladin, Cleric, Oracle, Warpriest, Witch
Casting time: 1 full-round action, special see below
Components: V, S, M (target creature's heart)
Range: touch
Duration: concentration/1 minute per hd of the subject; see text
Saving throw: none
Spell resistance: yes
Target: living creature touched
Descriptors: death, evil
:::

> _[Orcs](ref/race/orc) have access to the following spell._

You cut out an enemy's heart and consume it, absorbing that enemy's power as your own. As part of
casting this spell, you perform a coup de grace with a slashing weapon on a helpless, living
adjacent target. If the target dies, you eat its heart to gain the spell's benefits. If the target
survives, the spell is not wasted and you can try again as long as you continue concentrating on the
spell. When you consume the heart, you gain the benefits of a death knell spell, except you gain 1d8
temporary hit points +1 per Hit Die of the target, and the bonus to Strength is a profane bonus.
