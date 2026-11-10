+++
id = "ref/spell/remove-radioactivity-greater"
kind = "spell"
title = "Greater Remove Radioactivity"
aon = "SpellDisplay.aspx?ItemName=Remove%20Radioactivity%2C%20Greater"
source_ids = ["technology-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "remove_radioactivity_greater", path = "json/spells8.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/remove-radioactivity" },
]
[[sources]]
publication = "technology-guide"
page = "11"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Witch", level = 8 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature or object touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 8: Cleric, Druid, Oracle, Witch
Casting time: 1 standard action
Components: V, S
Range: touch
Target: creature or object touched
Duration: instantaneous
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Subschool: Healing
:::

### Greater Remove Radioactivity

This spell functions like [remove radioactivity](ref/spell/remove-radioactivity), save that it cures
all ability damage and drain due to radioactivity that the target has taken. In addition, you can
deplete a radioactive object as well, although because you must touch the object to affect it, you
expose yourself to at least 1 round of contact with the object's radiation. You must succeed at a
caster level check (DC = 5 + the Fortitude DC associated with the radiation effect) in order to
deplete the object. If you are successful, the object no longer emits radiation. In the case of a
nuclear reactor or atomic warhead, this permanently renders the reactor or warhead inert and
harmless.
