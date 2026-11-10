+++
id = "ref/spell/possess-object"
kind = "spell"
title = "Possess Object"
aon = "SpellDisplay.aspx?ItemName=Possess%20Object"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "possess_object", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-jar" },
]
[[sources]]
publication = "ultimate-magic"
page = "232"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (a gem or crystal worth at least 100 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one object; see text" },
]
duration = "1 hour/level or until you return to your body"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a gem or crystal worth at least 100 gp)
Range: medium (100 ft. + 10 ft./level)
Target: one object; see text
Duration: 1 hour/level or until you return to your body
Saving throw: Will negates; see text
Spell resistance: yes
:::

### Possess Object

This spell functions as [magic jar](ref/spell/magic-jar), except you transfer your mind to a single
object, animating it as if using animate objects, except your mind controls the object as if it were
your own body. You cannot speak or cast spells while possessing the object. Because your original
body is effectively dead while under the effect of this spell, this temporarily suspends disease,
poisons, and other afflictions affecting you.
