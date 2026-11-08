+++
id = "ref/spell/contagion"
kind = "spell"
title = "Contagion"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contagion", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["disease", "evil"]
levels = [
  { class = "Adept", level = 3 },
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Adept, Antipaladin, Cleric, Druid, Hunter, Oracle, Warpriest\
4: Arcanist, Bloodrager, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Target: living creature touched
Descriptors: disease, evil
:::

**Sources:** PRPG Core Rulebook pg 259

The subject contracts one of the following diseases: blinding sickness, bubonic plague, cackle
fever, filth fever, leprosy, mindfire, red ache, shakes, or slimy doom. The disease is contracted
immediately (the onset period does not apply). Use the disease's listed frequency and save DC to
determine further effects. For more information see Diseases.

### Mythic Contagion

**Sources:** Mythic Adventures pg 89

The affected target is highly contagious. Any creature it touches or that touches it with natural
weapons or unarmed strikes must save or contract the disease. The save DC for these targets is equal
to the spell's DC - 4. The target can't spread this disease to you.

_Augmented (7th):_ If you expend five uses of mythic power, the spell targets every living creature
within a 1-mile radius. You can select one creature per caster level within your line of sight;
these creatures are unaffected by the spell.
