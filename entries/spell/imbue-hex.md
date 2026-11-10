+++
id = "ref/spell/imbue-hex"
kind = "spell"
title = "Imbue Hex"
aon = "SpellDisplay.aspx?ItemName=Imbue%20Hex"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "imbue_hex", path = "json/spells14.json" },
]
[[sources]]
publication = "advanced-class-origins"
page = "31"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Shaman", level = 5 },
  { class = "Witch", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, M/DF (a hag's whisker)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched; see text" },
]
duration = "permanent or until discharged"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Shaman, Witch
Casting time: 10 minutes
Components: V, S, M/DF (a hag's whisker)
Range: touch
Duration: permanent or until discharged
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: creature touched; see text
:::

You transfer a single hex you know to the target, and give that target the ability to use the hex.
The transferred hex's variable characteristics function according to your level, not the level of
the recipient. Only a creature with Intelligence and Wisdom scores of at least 9 can receive this
effect. To use this hex, the target must be able to speak and move freely. Once it uses the hex, the
spell ends (though any effects of the hex still last for the full duration). You can transfer only a
hex-not a major or grand hex-with this ability.

Once you cast imbue hex, you cannot use the transferred hex until the spell is discharged,
dispelled, or dismissed.
