+++
id = "ref/spell/fumblestep"
kind = "spell"
title = "Fumblestep"
aon = "SpellDisplay.aspx?ItemName=Fumblestep"
source_ids = ["blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fumblestep", path = "json/spells13.json" },
]
[[sources]]
publication = "blood-of-the-beast"
page = "27"

[fields]
kind = "spell"
school = "conjuration"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a sharp pebble)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level or until discharged (see text)"
saving_throw = "none (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Arcanist, Mesmerist, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a sharp pebble)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level or until discharged (see text)
Saving throw: none (see text)
Spell resistance: yes
Target: one creature
:::

> _While [tengus](ref/race/tengu) are renowned for their supposed ability to eat bad luck or hex
> with a foul stare, most tengus have long forgotten the jinx magic their ancestors perfected
> millennia ago in the mountains of Tian Xia to confound meddling visitors bearing imperial decrees.
> Only a handful of these luck-manipulating spells now remain known outside the secretive temples of
> Hei Feng, largely practiced by tengu witches and the occasional tengu or halfling rogue, by way of
> the [major magic](ref/talent/major-magic) rogue talent._

Fumblestep coats a target's feet in slick ectoplasm that retains some psychic connection to your
mind. While the spell remains in effect, the target creature takes a -1 penalty on Reflex saving
throws and Acrobatics checks.

At any point during the spell's duration while the target remains in range, you can discharge the
spell as a standard action, mentally tugging at the ectoplasm to perform a trip combat maneuver,
using your caster level instead of your base attack bonus, and using your Charisma, Intelligence, or
Wisdom modifier, whichever is highest, instead of your Strength modifier. This trip attempt does not
provoke an attack of opportunity and cannot be affected by feats or other means of altering a trip
combat maneuver's effects.
