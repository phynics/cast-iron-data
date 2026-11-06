+++
id = "ref/spell/swallow-poison"
kind = "spell"
title = "Swallow Poison"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "swallow_poison", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Investigator", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Witch", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Alchemist, Druid, Hunter, Investigator, Shaman, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: personal
Duration: 1 hour/level or until discharged
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Ultimate Intrigue pg 226

A special gland grows on the inside of your throat, which absorbs any poisons that you ingest, and
can be used to expel them in a toxic spray. Any time you consume ingested poison during the spell's
duration, you can roll a caster level check against the poison's save DC in order to harmlessly
absorb the poison, ignoring its effects. The spell can absorb up to 1 dose of poison per 3 caster
levels, after which the gland is unable to process any more poison, and any further doses of
ingested poison affect you normally.

You store each dose of absorbed poison within the gland, and you can end the spell to spray one dose
of absorbed poison out of your mouth as a standard action. This sprays the poison in a 15-foot cone.
Each creature in the area must succeed at a Reflex save (at swallow poison's DC) or be exposed to
the sprayed poison, which is treated as though it were a contact poison for this purpose. Everything
about the poison other than its type, including its frequency, effect, and saving throw DC, are
unaffected by this spell. Any other doses of poison you had absorbed instantly become inert when you
end the spell. If the spell's duration ends without you spraying a poison, all poisons you had
absorbed become inert.
