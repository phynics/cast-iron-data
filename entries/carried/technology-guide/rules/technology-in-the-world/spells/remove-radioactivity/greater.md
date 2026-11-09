+++
id = "ref/carried/technology-guide/rules/technology-in-the-world/spells/remove-radioactivity/greater"
kind = "spell"
title = "Remove Radioactivity, Greater"
aon = "SpellDisplay.aspx?ItemName=Remove%20Radioactivity%2C%20Greater"
source_ids = ["technology-guide"]
section = ["Rules", "Technology in the world", "Spells", "Remove Radioactivity"]
tags = ["conjuration", "healing"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Technology Guide/Rules/Technology in the world/Spells/Remove Radioactivity/Greater", path = "technology_guide/spell/remove_radioactivity_greater.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["healing"]
levels = [
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Warpriest", level = 8 },
  { class = "Witch", level = 8 },
]
+++

::: statblock
School: conjuration (healing)
Level: 8: Cleric, Druid, Oracle, Warpriest, Witch
:::

This spell functions like _[remove radioactivity](ref/spell/remove-radioactivity)_, save that it
cures all ability damage and drain due to radioactivity that the target has taken. In addition, you
can deplete a radioactive object as well, although because you must touch the object to affect it,
you expose yourself to at least 1 round of contact with the object's radiation. You must succeed at
a caster level check (DC = 5 + the Fortitude DC associated with the radiation effect) in order to
deplete the object. If you are successful, the object no longer emits radiation. In the case of a
nuclear reactor or atomic warhead, this permanently renders the reactor or warhead inert and
harmless.
