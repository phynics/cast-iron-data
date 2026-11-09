+++
id = "ref/spell/mirror-image"
kind = "spell"
title = "Mirror Image"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mirror_image", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "314"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Adept", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Bloodrager", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Adept, Arcanist, Bloodrager, Bard, Magus, Medium, Mesmerist, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Figment
:::

This spell creates a number of illusory doubles of you that inhabit your square. These doubles make
it difficult for enemies to precisely locate and attack you.

When mirror image is cast, 1d4 images plus one image per three caster levels (maximum eight images
total) are created. These images remain in your space and move with you, mimicking your movements,
sounds, and actions exactly. Whenever you are attacked or are the target of a spell that requires an
attack roll, there is a possibility that the attack targets one of your images instead. If the
attack is a hit, roll randomly to see whether the selected target is real or a figment. If it is a
figment, the figment is destroyed. If the attack misses by 5 or less, one of your figments is
destroyed by the near miss. Area spells affect you normally and do not destroy any of your figments.
Spells and effects that do not require an attack roll affect you normally and do not destroy any of
your figments. Spells that require a touch attack are harmlessly discharged if used to destroy a
figment.

An attacker must be able to see the figments to be fooled. If you are invisible or the attacker is
blind, the spell has no effect (although the normal miss chances still apply).
