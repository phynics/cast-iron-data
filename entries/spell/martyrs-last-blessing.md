+++
id = "ref/spell/martyrs-last-blessing"
kind = "spell"
title = "Martyr's Last Blessing"
source_ids = ["pathfinder-68-the-shackled-hut"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "martyrs_last_blessing", path = "json/spells6.json" },
]
[[sources]]
publication = "pathfinder-68-the-shackled-hut"
page = "69"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 minute"
components = "V, S, DF"
range = "personal (see text)"
effects = [
  { label = "Target", value = "you and one ally/level, no two of which can be more than 30 ft. apart (see text)" },
]
duration = "1 hour/level or instantaneous (see text)"
saving_throw = "Will half (harmless, see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Cleric, Hunter, Oracle, Ranger, Warpriest
Casting time: 1 minute
Components: V, S, DF
Range: personal (see text)
Duration: 1 hour/level or instantaneous (see text)
Saving throw: Will half (harmless, see text)
Spell resistance: yes
Target: you and one ally/level, no two of which can be more than 30 ft. apart (see text)
Subschool: Healing
:::

> _Priests of [Milani](ref/faith/milani) have access to the following spell._

You charge your body with healing energy, which erupts from you if you are dying or are killed
before 1 hour per level has passed. If you're brought below 0 hit points or killed (including by
effects that kill without dealing damage, such as [phantasmal killer](ref/spell/phantasmal-killer)
and [power word kill](ref/spell/power-word-kill)), the eruption of healing energy acts as
[mass cure light wounds](ref/spell/cure-light-wounds-mass) on allies (other than you). Allies with
the fewest Hit Dice are affected first. Among allies with equal HD, those closest to you are
affected first. If the duration ends, the stored healing energy dissipates with no effect.
