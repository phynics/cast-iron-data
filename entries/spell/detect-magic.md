+++
id = "ref/spell/detect-magic"
kind = "spell"
title = "Detect Magic"
source_ids = ["core-rulebook", "adventurers-guide", "andoran-spirit-of-liberty", "ultimate-intrigue", "potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_magic", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Adept", level = 0 },
  { class = "Arcanist", level = 0 },
  { class = "Bard", level = 0 },
  { class = "Cleric", level = 0 },
  { class = "Druid", level = 0 },
  { class = "Hunter", level = 0 },
  { class = "Inquisitor", level = 0 },
  { class = "Magus", level = 0 },
  { class = "Medium", level = 0 },
  { class = "Mesmerist", level = 0 },
  { class = "Occultist", level = 0 },
  { class = "Oracle", level = 0 },
  { class = "Psychic", level = 0 },
  { class = "Shaman", level = 0 },
  { class = "Skald", level = 0 },
  { class = "Sorcerer", level = 0 },
  { class = "Spiritualist", level = 0 },
  { class = "Summoner", level = 0 },
  { class = "Unchained Summoner", level = 0 },
  { class = "Warpriest", level = 0 },
  { class = "Witch", level = 0 },
  { class = "Wizard", level = 0 },
]
casting_time = "1 standard action"
components = "V, S"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 1 min./level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 0: Adept, Arcanist, Bard, Cleric, Druid, Hunter, Inquisitor, Magus, Medium, Mesmerist, Occultist, Oracle, Psychic, Shaman, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 60 ft.
Duration: concentration, up to 1 min./level (D)
Saving throw: none
Spell resistance: no
Area: cone-shaped emanation
:::

**Sources:** PRPG Core Rulebook pg 267

You detect magical auras. The amount of information revealed depends on how long you study a
particular area or subject.

_1st Round:_ Presence or absence of magical auras.

_2nd Round:_ Number of different magical auras and the power of the most potent aura.

_3rd Round:_ The strength and location of each aura. If the items or creatures bearing the auras are
in line of sight, you can make Knowledge (arcana) skill checks to determine the school of magic
involved in each. (Make one check per aura: DC 15 + spell level, or 15 + 1/2 caster level for a
non-spell effect.) If the aura eminates from a magic item, you can attempt to identify its
properties (see [Spellcraft](ref/skill/spellcraft)).

Magical areas, multiple types of magic, or strong local magical emanations may distort or conceal
weaker auras.

_Aura Strength:_ An aura's power depends on a spell's functioning spell level or an item's caster
level; see the accompanying table. If an aura falls into more than one category, detect magic
indicates the stronger of the two.

_Lingering Aura:_ A magical aura lingers after its original source dissipates (in the case of a
spell) or is destroyed (in the case of a magic item). If detect magic is cast and directed at such a
location, the spell indicates an aura strength of dim (even weaker than a faint aura). How long the
aura lingers at this dim level depends on its original power:

|Original Strength|Duration of Lingering Aura|
| --- | --- |
|Faint|1d6 rounds|
|Moderate|1d6 minutes|
|Strong|1d6 × 10 minutes|
|Overwhelming|1d6 days|

Outsiders and elementals are not magical in themselves, but if they are summoned, the conjuration
spell registers. Each round, you can turn to detect magic in a new area. The spell can penetrate
barriers, but 1 foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or
dirt blocks it.

Detect magic can be made permanent with a [permanency](ref/spell/permanency) spell.

|Item|Faint Aura|Moderate|Strong|Overwhelming|
| --- | --- | --- | --- | --- |
|Functioning spell (spell level)|3rd or lower|4th-6th|7th-9th|10th+ (deity-level)|
|Magic item (caster level)|5th or lower|6th-11th|12th-20th|21st+ (artifact)|
