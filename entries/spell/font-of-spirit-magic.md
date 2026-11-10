+++
id = "ref/spell/font-of-spirit-magic"
kind = "spell"
title = "Font of Spirit Magic"
aon = "SpellDisplay.aspx?ItemName=Font%20of%20Spirit%20Magic"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "font_of_spirit_magic", path = "json/spells13.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "182"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Shaman", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (gold dust worth 50 gp)"
range = "30 ft."
effects = [
  { label = "Area", value = "30-ft.-radius emanation centered on you" },
]
duration = "concentration+ 1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Shaman
Casting time: 1 standard action
Components: V, S, M (gold dust worth 50 gp)
Range: 30 ft.
Duration: concentration+ 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: no
Area: 30-ft.-radius emanation centered on you
Subschool: Creation
:::

You amplify the effect of magic associated with your spirit and wandering spirit (any spells on the
spirit magic spell lists for these spirits). When allies within the area cast these spells, they
gain a +2 bonus on caster level checks and [concentration](ref/rule/concentration) checks, as well
as to spell DCs. This bonus is a sacred bonus if you are good-aligned or a profane bonus if you are
evil-aligned; if you are neither good nor evil, you can choose what type of bonus the spell grants
when you cast it.
