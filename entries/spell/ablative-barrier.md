+++
id = "ref/spell/ablative-barrier"
kind = "spell"
title = "Ablative Barrier"
aon = "SpellDisplay.aspx?ItemName=Ablative%20Barrier"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ablative_barrier", path = "json/spells.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "221"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["force"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of metal cut from a shield)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level or until discharged"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Alchemist, Bloodrager, Investigator, Magus, Occultist, Summoner\
3: Arcanist, Psychic, Sorcerer, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of metal cut from a shield)
Range: touch
Duration: 1 hour/level or until discharged
Saving throw: Will negates (harmless)
Spell resistance: no
Target: creature touched
Subschool: Creation
Descriptors: force
:::

Invisible layers of solid force surround and protect the target, granting that target a +2 armor
bonus to AC. Additionally, the first 5 points of lethal damage the target takes from each attack are
converted into nonlethal damage. Against attacks that already deal nonlethal damage, the target
gains DR 5/-. Once this spell has converted 5 points of damage to nonlethal damage per caster level
(maximum 50 points), the spell is discharged.
