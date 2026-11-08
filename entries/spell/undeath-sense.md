+++
id = "ref/spell/undeath-sense"
kind = "spell"
title = "Undeath Sense"
source_ids = ["core-rulebook", "potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undeath_sense", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/detect-undead" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (earth from a grave)"
range = "60 ft."
effects = [
  { label = "Area", value = "cone-shaped emanation" },
]
duration = "concentration, up to 1 min./level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Alchemist, Arcanist, Cleric, Inquisitor, Investigator, Medium, Mesmerist, Oracle, Paladin, Psychic, Shaman, Sorcerer, Spiritualist, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (earth from a grave)
Range: 60 ft.
Duration: concentration, up to 1 min./level
Saving throw: none
Spell resistance: no
Area: cone-shaped emanation
:::

## Detect Undead

**Sources:** PRPG Core Rulebook pg 269

You can detect the aura that surrounds undead creatures. The amount of information revealed depends
on how long you study a particular area.

_1st Round:_ Presence or absence of undead auras.

_2nd Round:_ Number of undead auras in the area and the strength of the strongest undead aura
present. If you are of good alignment, and the strongest undead aura's strength is overwhelming (see
below), and the creature has HD of at least twice your character level, you are stunned for 1 round
and the spell ends.

_3rd Round:_ The strength and location of each undead aura. If an aura is outside your line of
sight, then you discern its direction but not its exact location.

_Aura Strength:_ The strength of an undead aura is determined by the HD of the undead creature, as
given on the table below.

_Lingering Aura:_ An undead aura lingers after its original source is destroyed. If detect undead is
cast and directed at such a location, the spell indicates an aura strength of dim (even weaker than
a faint aura). How long the aura lingers at this dim level depends on its original power, as given
on the table below.

|HD|Strength|Lingering Aura Duration|
| --- | --- | --- |
|1 or lower|Faint|1d6 rounds|
|2-4|Moderate|1d6 minutes|
|05-10|Strong|1d6 × 10 minutes|
|11 or higher|Overwhelming|1d6 days|

Each round, you can turn to detect undead in a new area. The spell can penetrate barriers, but 1
foot of stone, 1 inch of common metal, a thin sheet of lead, or 3 feet of wood or dirt blocks it.

### Undeath Sense

**Sources:** Potions and Poisons pg 18

You grant the target the ability to pick up on the subtle scents and disturbances to the natural
order that are specific to the living dead, granting the target the ability to sense the presence of
undead creatures. The target is constantly aware of whether there are any undead auras within 60
feet of her in any direction. If at least one undead aura is present, the target can concentrate on
the spell's effects in order to gain more information on the auras present. This functions similarly
to [detect undead](ref/spell/detect-undead), except the number of rounds of concentration needed to
learn about the undead auras is reduced by 1 (1 round to learn the number of auras, and 2 rounds to
learn the strength and location of each aura).
