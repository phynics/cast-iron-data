+++
id = "ref/spell/shadowform"
kind = "spell"
title = "Shadowform"
source_ids = ["blood-of-shadows"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadowform", path = "json/spells15.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 4: Antipaladin, Arcanist, Bard, Mesmerist, Psychic, Skald, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 round/level (D)
Saving throw: Will negates (see text)
Spell resistance: yes
Target: creature touched
Subschool: Shadow
Descriptors: shadow
:::

**Sources:** Blood of Shadows pg 31

You replace the target's body with mystic shadow material drawn from the Shadow Plane, rendering the
target's physical form only quasi-real. Whenever a foe tries to directly attack the target of the
spell (for instance, with a weapon or a targeted spell), that foe must attempt a Will save to
disbelieve. If successful, the opponent can attack the target normally and is unaffected by
shadowform for 1 round. If the foe fails, the target takes only one-fifth the normal amount of
damage from the foe's successful attack or effect, and if the attack has a special effect other than
damage, that effect is one-fifth as strong as normal (if applicable) or only 20% as likely to occur.
Objects automatically succeed at their Will saves against this spell.
