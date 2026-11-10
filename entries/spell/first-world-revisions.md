+++
id = "ref/spell/first-world-revisions"
kind = "spell"
title = "First World Revisions"
aon = "SpellDisplay.aspx?ItemName=First%20World%20Revisions"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "first_world_revisions", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/ancestral-regression" },
]
[[sources]]
publication = "blood-of-shadows"
page = "11"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "willing wayang touched" },
]
duration = "24 hours (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Alchemist, Cleric, Investigator, Medium, Oracle, Psychic, Warpriest, Witch\
3: Antipaladin, Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 24 hours (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: willing wayang touched
Subschool: Polymorph
:::

> _[Wayangs](ref/race/wayang) have access to the following spell. Because it draws on the wayangs'
> unique physiology, spellcasters of other races cannot cast this spell._

This spell functions as [ancestral regression](ref/spell/ancestral-regression), except as noted
above and as follows. The wayang loses her [darkvision](ref/rule/darkvision) racial trait and gains
the [low-light vision](ref/rule/low-light-vision) racial trait in its place. The alignment and
personality of the wayang are not affected by the transformation, but the spell conceals her
alignment as per undetectable alignment. Unlike ancestral regression, this spell grants the target a
+20 bonus on Disguise checks to pass as a gnome; even though the wayang appears as a gnomish analog
of herself, the differences between gnomes and wayangs are great enough that she cannot be mistaken
for a gnome by other wayangs who know her.
