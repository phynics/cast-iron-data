+++
id = "ref/spell/vampiric-touch"
kind = "spell"
title = "Vampiric Touch"
aon = "SpellDisplay.aspx?ItemName=Vampiric%20Touch"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vampiric_touch", path = "json/spells11.json" },
]
[[sources]]
publication = "core-rulebook"
page = "364"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous/1 hour; see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Antipaladin, Arcanist, Bloodrager, Magus, Medium, Mesmerist, Psychic, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous/1 hour; see text
Saving throw: none
Spell resistance: yes
Target: living creature touched
:::

You must succeed on a melee touch attack. Your touch deals 1d6 points of damage per two caster
levels (maximum 10d6). You gain temporary hit points equal to the damage you deal. You can't gain
more than the subject's current hit points + the subject's Constitution score (which is enough to
kill the subject). The temporary hit points disappear 1 hour later.
