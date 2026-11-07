+++
id = "ref/spell/contagion-greater"
kind = "spell"
title = "Greater Contagion"
source_ids = ["core-rulebook", "mythic-adventures", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contagion_greater", path = "json/spells12.json" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["disease", "evil"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Cleric, Druid, Hunter, Oracle, Warpriest, Witch\
6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Target: one living creature
Duration: instantaneous
Saving throw: Fortitude negates
Spell resistance: yes
Descriptors: disease, evil
:::

## Contagion

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

### Greater Contagion

**Sources:** Ultimate Magic pg 211

This spell functions as contagion, except the victim cannot overcome the disease without
magic-making the required number of saves does not cure it. The DC to remove the disease with magic
is equal to the save DC + 5.
