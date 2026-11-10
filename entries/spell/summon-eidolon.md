+++
id = "ref/spell/summon-eidolon"
kind = "spell"
title = "Summon Eidolon"
aon = "SpellDisplay.aspx?ItemName=Summon%20Eidolon"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "summon_eidolon", path = "json/spells16.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "248"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Summoning"]
levels = [
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
]
casting_time = "1 round"
components = "V, S, M (a silver coin)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one eidolon" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Summoner, Unchained Summoner
Casting time: 1 round
Components: V, S, M (a silver coin)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: one eidolon
Subschool: Summoning
:::

You open a rift between dimensions that summons your eidolon. Treat this as if you had summoned your
eidolon normally, except that it only remains with you for the duration of this spell. While
summoned in this way, your eidolon cannot touch any creature warded by
[protection from evil](ref/spell/protection-from-evil) or a similar effect and your eidolon can be
sent back to its home plane by [dispel magic](ref/spell/dispel-magic).

If you cast this spell while your eidolon is already on your plane, this spell has no effect. This
spell allows you to summon your eidolon even if it has been returned to its home plane due to
damage.
