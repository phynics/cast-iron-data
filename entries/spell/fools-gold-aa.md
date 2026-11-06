+++
id = "ref/spell/fools-gold-aa"
kind = "spell"
title = "Fool's Gold (AA)"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fools_gold_aa", path = "json/spells13.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Antipaladin", level = 1 },
  { class = "Arcanist", level = 2 },
  { class = "Bard", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 1 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, F (a lump of gold worth 5 gp)"
range = "touch"
effects = [
  { label = "Target", value = "1 gold piece/level touched" },
]
duration = "10 minutes/level"
saving_throw = "Fortitude negates (object, see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Alchemist, Antipaladin, Bard, Investigator, Mesmerist, Psychic, Skald\
2: Arcanist, Occultist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a lump of gold worth 5 gp)
Range: touch
Duration: 10 minutes/level
Saving throw: Fortitude negates (object, see text)
Spell resistance: yes
Target: 1 gold piece/level touched
:::

**Sources:** Arcane Anthology pg 20

You cast this spell on one or more gold pieces, which make those who have them more vulnerable to
your magics. A creature with one or more of these gold pieces in its possession must attempt a Will
save (at this spell's save DC) the first time the creature is forced to attempt a saving throw
against a spell, [spell-like ability](ref/umr/spell-like-abilities), or supernatural ability you
create. If the creature fails, it takes a -2 penalty on all saving throws against your magic effects
as long as the gold piece is in its possession. Additionally, if it fails a saving throw against a
magic ability of yours that is not harmless and has a duration, the duration is doubled for that
creature.
