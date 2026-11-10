+++
id = "ref/spell/plague-bearer"
kind = "spell"
title = "Plague Bearer"
aon = "SpellDisplay.aspx?ItemName=Plague%20Bearer"
source_ids = ["inner-sea-gods"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "plague_bearer", path = "json/spells7.json" },
]
[[sources]]
publication = "inner-sea-gods"
page = "238"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["disease", "evil"]
levels = [
  { class = "Alchemist", level = 6 },
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 6 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Investigator", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level; see text"
saving_throw = "Fortitude negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Antipaladin\
6: Alchemist, Cleric, Druid, Hunter, Inquisitor, Investigator, Oracle, Warpriest, Witch\
7: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level; see text
Saving throw: Fortitude negates, see text
Spell resistance: yes
Target: one living creature
Descriptors: disease, evil
:::

You make the target an asymptomatic carrier for a host of virulent diseases. Creatures that end
their turn adjacent to the target must succeed at a Fortitude save or be affected as if by the spell
contagion. The target itself does not become diseased, and suffers no ill effects from this spell.
Once plague bearer ends, the target is no longer contagious, though any creature it infected remains
diseased.

**Note:** The original source printed this as a 6th-level antipaladin spell, but that class only has
spellcasting up to 4th level, hence why it's listed as 4th-level here.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
