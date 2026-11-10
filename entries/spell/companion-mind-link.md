+++
id = "ref/spell/companion-mind-link"
kind = "spell"
title = "Companion Mind Link"
aon = "SpellDisplay.aspx?ItemName=Companion%20Mind%20Link"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "companion_mind_link", path = "json/spells12.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "226"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "your animal companion" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Druid, Hunter, Ranger
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: your animal companion
Subschool: Charm
Descriptors: mind-affecting
:::

The link between you and your animal companion becomes stronger. As long as you are within line of
sight of your animal companion, you can telepathically communicate with it as if you two shared a
language. Also, as long as you are within line of sight of the animal companion, you can push your
animal companion a swift action instead of a move action, and you do not need to succeed at Handle
Animal checks to handle your animal companion. Such checks automatically succeed.
