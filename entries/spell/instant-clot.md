+++
id = "ref/spell/instant-clot"
kind = "spell"
title = "Instant Clot"
aon = "SpellDisplay.aspx?ItemName=Instant%20Clot"
source_ids = ["blood-of-the-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "instant_clot", path = "json/spells14.json" },
]
[[sources]]
publication = "blood-of-the-sea"
page = "21"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Alchemist, Bard, Cleric, Druid, Hunter, Inquisitor, Investigator, Oracle, Paladin, Ranger, Shaman, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes (harmless)
Target: living creature touched
Subschool: Healing
:::

Bleed effects on the target immediately end when this spell is cast, and no blood flows out when the
target is damaged by a slashing or piercing weapon. The target takes the full amount of damage from
attacks, but because the wounds produce no blood, they do not attract creatures with the ability to
sense blood, such as sharks. If the target suffers another bleed effect while this spell is in
effect, the bleed effect ends and the spell is immediately dismissed.
