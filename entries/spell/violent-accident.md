+++
id = "ref/spell/violent-accident"
kind = "spell"
title = "Violent Accident"
aon = "SpellDisplay.aspx?ItemName=Violent%20Accident"
source_ids = ["inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "violent_accident", path = "json/spells11.json" },
]
[[sources]]
publication = "inner-sea-intrigue"
page = "63"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day or until discharged"
saving_throw = "Reflex half; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Cleric, Mesmerist, Occultist, Oracle, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: long (400 ft. + 40 ft./level)
Duration: 1 day or until discharged
Saving throw: Reflex half; see text
Spell resistance: yes
Target: one creature
Descriptors: curse
:::

You curse the target to suffer a violent accident within the next 24 hours. You have no control over
the form the accident takes or when it strikes. The target can avoid being cursed with
[spell resistance](ref/rule/spell-resistance) when you cast the spell, but otherwise receives no
saving throw. Regardless of the accident's nature, it is magically empowered to deal an amount of
damage equal to 1d8 × your caster level (maximum 5d8 points of damage), and the damage is of a type
appropriate to the source of damage (such as fire for an explosion or bludgeoning for a falling
object). When the accident occurs, the target can attempt a Reflex saving throw to reduce the damage
by half. Although others might be surprised or inconvenienced by the accident, it damages only the
target.
