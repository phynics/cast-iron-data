+++
id = "ref/spell/parasitic-soul"
kind = "spell"
title = "Parasitic Soul"
aon = "SpellDisplay.aspx?ItemName=Parasitic%20Soul"
source_ids = ["book-of-the-damned"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "parasitic_soul", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-jar" },
]

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 9 },
  { class = "Cleric", level = 9 },
  { class = "Oracle", level = 9 },
  { class = "Psychic", level = 9 },
  { class = "Shaman", level = 9 },
  { class = "Sorcerer", level = 9 },
  { class = "Witch", level = 9 },
  { class = "Wizard", level = 9 },
]
casting_time = "1 standard action"
components = "V, S, F (a gem or crystal worth at least 100 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "permanent (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 9: Arcanist, Cleric, Oracle, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a gem or crystal worth at least 100 gp)
Range: medium (100 ft. + 10 ft./level)
Target: one creature
Duration: permanent (D)
Saving throw: Will negates
Spell resistance: yes
:::

### Parasitic Soul

**Sources:** Book of the Damned pg 185, Book of the Damned - Volume 3: Horsemen of the Apocalypse pg
39

This spell functions like [magic jar](ref/spell/magic-jar) except as noted above, and instead of
your own soul, you can transfer a trapped soul (such as one trapped in a soul gem or trapped with
soul bind or trap the soul) from the receptacle into an unwilling target's body. If the target
creature fails its saving throw, it dies and the trapped soul in the receptacle permanently inhabits
the body as if using magic jar. The trapped soul does not get a saving throw to resist this
transfer. To dismiss the spell, you must be within range of the possessed body.
