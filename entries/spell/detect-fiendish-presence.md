+++
id = "ref/spell/detect-fiendish-presence"
kind = "spell"
title = "Detect Fiendish Presence"
source_ids = ["core-rulebook", "agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "detect_fiendish_presence", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/detect-evil" },
]

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

### Detect Fiendish Presence

**Sources:** Agents of Evil pg 16

This spell functions like _[detect evil](ref/spell/detect-evil),_ except that it detects only
outsiders with the evil subtype, as well as the lingering effects caused by their gifts, presence,
and spells. It can also detect clerics and paladins of fiendish deities, including
[Asmodeus](ref/faith/asmodeus), archdevils, daemonic harbingers, and demon lords.

###### ^2^ {#footnote-a}

Some characters who are not clerics may radiate an aura of equivalent power. The class description
will indicate whether this applies.

###### ^1^ {#footnote-e}

Excludes undead and outsiders, which have their own entries on the table.
