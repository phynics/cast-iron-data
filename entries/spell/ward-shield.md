+++
id = "ref/spell/ward-shield"
kind = "spell"
title = "Ward Shield"
source_ids = ["knights-of-the-inner-sea"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ward_shield", path = "json/spells11.json" },
]
[[sources]]
publication = "knights-of-the-inner-sea"
page = "29"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "shield touched" },
]
duration = "1 minute/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Arcanist, Cleric, Inquisitor, Magus, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: shield touched
:::

With a touch, you enchant a shield and enable it to protect its wielder from hostile spells. The
shield grants [spell resistance](ref/rule/spell-resistance) 10 + your caster level against spells so
long as the shield can be interposed between the wielder and the spell effect. A spell shield does
not provide spell resistance against area effect spells such as fireball, but does provide a +5
bonus on Reflex saving throws against such spells.
