+++
id = "ref/spell/interrogation"
kind = "spell"
title = "Interrogation"
aon = "SpellDisplay.aspx?ItemName=Interrogation"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "interrogation", path = "json/spells14.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "225"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil", "pain"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "living creature touched" },
]
duration = "1 minute/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Arcanist, Inquisitor, Mesmerist, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: living creature touched
Descriptors: evil, pain
:::

You question the target, backed up by the threat of magical pain. You may ask one question per two
caster levels. The target can either answer the question or take 1d4 points of damage plus your
Wisdom bonus. The target is not compelled to answer truthfully, but the threat of pain gives it a -4
penalty on Bluff checks to convince you when it is lying.
