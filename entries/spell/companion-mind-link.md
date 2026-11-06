+++
id = "ref/spell/companion-mind-link"
kind = "spell"
title = "Companion Mind Link"
source_ids = ["ultimate-combat", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "companion_mind_link", path = "json/spells12.json" },
]

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

**Sources:** Ultimate Combat pg 226

The link between you and your animal companion becomes stronger. As long as you are within line of
sight of your animal companion, you can telepathically communicate with it as if you two shared a
language. Also, as long as you are within line of sight of the animal companion, you can push your
animal companion a swift action instead of a move action, and you do not need to succeed at Handle
Animal checks to handle your animal companion. Such checks automatically succeed.

### Mythic Companion Mind Link

**Sources:** Mythic Adventures pg 88\
Your animal companion understands complex instructions transmitted by the spell. It can perform any
trick (even one it doesn't know) as well as any activity that could be understood by a creature with
an Intelligence score of 8.
