+++
id = "ref/spell/natures-exile"
kind = "spell"
title = "Nature's Exile"
aon = "SpellDisplay.aspx?ItemName=Nature%27s%20Exile"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "natures_exile", path = "json/spells7.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "233"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Witch", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Druid, Hunter, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: permanent
Saving throw: Will negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

This spell curses the creature touched, making it inimical to the natural world. All animals have an
initial attitude of hostile toward the target. Familiars, being magical beasts, are not affected by
this spell, but animal companions are. If you have an animal companion, it does not become hostile,
but as long as you remain cursed, your animal companion takes a -2 penalty on all attack rolls,
skill checks, and saving throws. The target also takes a -10 penalty on Survival skill checks as the
weather and environment themselves seem to conspire to cause trouble.

Nature's exile can be removed with [break enchantment](ref/spell/break-enchantment),
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle),
[remove curse](ref/spell/remove-curse), or [wish](ref/spell/wish).
