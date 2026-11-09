+++
id = "ref/spell/detect-evil"
kind = "spell"
title = "Detect Evil"
source_ids = ["core-rulebook", "agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_evil", path = "json/spells3.json" },
]
[[sources]]
publication = "core-rulebook"
page = "266"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Adept", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 10 min./level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Adept, Cleric, Inquisitor, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: 60 ft.
Duration: concentration, up to 10 min./level (D)
Saving throw: none
Spell resistance: no
Area: cone-shaped emanation
:::

You can sense the presence of evil. The amount of information revealed depends on how long you study
a particular area or subject.

_1st Round:_ Presence or absence of evil.

_2nd Round:_ Number of evil auras (creatures, objects, or spells) in the area and the power of the
most potent evil aura present.

If you are of good alignment, and the strongest evil aura's power is overwhelming (see below), and
the HD or level of the aura's source is at least twice your character level, you are stunned for 1
round and the spell ends.

_3rd Round:_ The power and location of each aura. If an aura is outside your line of sight, then you
discern its direction but not its exact location.

_Aura Power:_ An evil aura's power depends on the type of evil creature or object that you're
detecting and its HD, caster level, or (in the case of a cleric) class level; see the table below.
If an aura falls into more than one strength category, the spell indicates the stronger of the two.

_Lingering Aura:_ An evil aura lingers after its original source dissipates (in the case of a spell)
or is destroyed (in the case of a creature or magic item). If detect evil is cast and directed at
such a location, the spell indicates an aura strength of dim (even weaker than a faint aura). How
long the aura lingers at this dim level depends on its original power:

|Original Strength|Duration of Lingering Aura|
| --- | --- |
|Faint|1d6 rounds|
|Moderate|1d6 minutes|
|Strong|1d6 × 10 minutes|
|Overwhelming|1d6 days|

Animals, traps, poisons, and other potential perils are not evil, and as such this spell does not
detect them. Creatures with actively evil intents count as evil creatures for the purpose of this
spell.

Each round, you can turn to detect evil in a new area. The spell can penetrate barriers, but 1 foot
of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt blocks it.

|Creature/Object|No Aura|Faint Aura|Moderate|Strong|Overwhelming|
| --- | --- | --- | --- | --- | --- |
|Aligned creature^[1](ref/spell/detect-evil#footnote-e)^ (HD)|4 or lower|05-10|11-25|26-50|51 or higher|
|Aligned undead (HD)|-|2 or lower|3-8|09-20|21 or higher|
|Aligned outsider (HD)|-|1 or lower|2-4|05-10|11 or higher|
|Cleric or paladin of an aligned deity^[2](ref/spell/detect-evil#footnote-a)^ (class levels)|-|1|2-4|05-10|11 or higher|
|Aligned magic item or spell (caster level)|5th or lower|6th-10th|11th-15th|16th-20th|21st or higher|

###### ^2^ {#footnote-a}

Some characters who are not clerics may radiate an aura of equivalent power. The class description
will indicate whether this applies.

###### ^1^ {#footnote-e}

Excludes undead and outsiders, which have their own entries on the table.
