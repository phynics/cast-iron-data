+++
id = "ref/spell/charge-object"
kind = "spell"
title = "Charge Object"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charge_object", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Spiritualist", level = 1 },
]
casting_time = "10 minutes"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "permanent"
saving_throw = "none, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Medium, Mesmerist, Occultist, Psychic, Spiritualist
Casting time: 10 minutes
Components: V, S
Range: touch
Duration: permanent
Saving throw: none, see text
Spell resistance: no
Target: object touched
:::

**Sources:** Occult Adventures pg 161

You charge an item with minor psychic energy. The item can be detected by the
[detect psychic significance](ref/spell/detect-psychic-significance) spell. If you wish, you can
imprint the item with your ownership history. Spells such as
[object reading](ref/spell/object-reading) and uses of the [psychometry](ref/skill/appraise) unlock
can reveal any information about yourself you impart into the object, including your name,
alignment, profession, and a summary of your experiences with the item. You can't impart false
information into the object, but you can omit any details you'd prefer not to divulge. If the target
object is already psychically charged, you can add more information to it, but you can't use charge
object to erase existing psychic information.
