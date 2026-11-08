+++
id = "ref/spell/entice-fey"
kind = "spell"
title = "Entice Fey"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "entice_fey", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/entice-fey-lesser" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Calling"]
levels = [
  { class = "Bard", level = 4 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Ranger", level = 4 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, DF, M (offerings worth 500 gp plus payment, see text)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "one called fey, with 6 Hit Dice or fewer" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Medium\
4: Bard, Hunter, Ranger, Skald\
5: Druid, Shaman
Casting time: 10 minutes
Components: V, S, DF, M (offerings worth 500 gp plus payment, see text)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: no
Effect: one called fey, with 6 Hit Dice or fewer
Subschool: Calling
:::

## Lesser Entice Fey

**Sources:** Ultimate Intrigue pg 213

This spell functions as [lesser planar ally](ref/spell/planar-ally-lesser), except that you entice a
fey of 6 HD or fewer to lend you its aid with an offering of music or something else it finds
appealing. Like lesser planar ally, this spell is unpredictable, and the fey who answers the calling
is up to the whims of nature and the fey, not your own choice. You must succeed at a Knowledge
(nature) check or Perform check (DC = 20 + target's HD) in addition to the spell's material
component to entice the fey into appearing, after which you can negotiate for the service and your
payment. The maximum HD of fey that you can call with that casting is equal to the result of your
check - 20. For example, if your check result is a 24, the maximum HD for the called fey is 4. A
high result doesn't allow you to break the HD maximum for the spell, and a result of 20 or less
means you can't call a fey at all. If the fey doesn't like the sound of your offer, it can simply
choose to refuse, in which case you don't expend any of the material components for the spell,
either the offerings or the payment.

### Entice Fey

**Sources:** Ultimate Intrigue pg 213

This spell functions as [lesser entice fey](ref/spell/entice-fey-lesser), except that the spell's
whimsical calling can produce a single fey of 12 Hit Dice or less, or two fey of the same kind whose
Hit Dice total no more than 12.

### Greater Entice Fey

**Sources:** Ultimate Intrigue pg 213

This spell functions as lesser entice fey, except the spell's whimsical calling can produce a single
fey of 18 Hit Dice or less, or up to three fey of the same kind whose Hit Dice total no more
than 18.
