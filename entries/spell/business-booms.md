+++
id = "ref/spell/business-booms"
kind = "spell"
title = "Business Booms"
source_ids = ["quests-and-campaigns"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "business_booms", path = "json/spells2.json" },
]
[[sources]]
publication = "quests-and-campaigns"
page = "28"

[fields]
kind = "spell"
school = "enchantment"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (promotional materials such as flyers and posters worth 10 gp)"
range = "touch"
effects = [
  { label = "Target", value = "one building" },
]
duration = "see text (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Arcanist, Bard, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (promotional materials such as flyers and posters worth 10 gp)
Range: touch
Duration: see text (D)
Saving throw: none
Spell resistance: no
Target: one building
:::

You may cast this spell immediately prior to spending 1 day of downtime to
[promote a business](ref/rule/promote-a-business). The spell is cast on a building you wish to
promote, which is magically bestowed with magical decorations and other improvements that make it
generally more appealing, and it is treated as seeing increased activity for the spell's duration.
If the spell is cast on a building that you do not promote immediately thereafter, the spell is
expended with no effect.

After the initial day of downtime spent promoting your building, the spell maintains the influx of
activity for a number of days equal to half your caster level (maximum 5 days). During this time,
you needn't spend additional downtime to promote the building, but you must spend capital as normal
to promote the building. The capital the affected building generates for you is unaffected by the
spell. If you spend 1 day promoting a different building than the target of this spell while this
spell remains active, the spell immediately ends.
