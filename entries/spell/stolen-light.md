+++
id = "ref/spell/stolen-light"
kind = "spell"
title = "Stolen Light"
aon = "SpellDisplay.aspx?ItemName=Stolen%20Light"
source_ids = ["pathfinder-society-field-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stolen_light", path = "json/spells9.json" },
]
[[sources]]
publication = "pathfinder-society-field-guide"
page = "59"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Figment"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 full-round action"
components = "V, S, F (a gem worth at least 500 gp)"
range = "touch"
effects = [
  { label = "Target", value = "transparent gem touched" },
]
duration = "permanent or 1 minute/level (see text)"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 3: Arcanist, Bard, Red Mantis Assassin, Skald, Sorcerer, Wizard
Casting time: 1 full-round action
Components: V, S, F (a gem worth at least 500 gp)
Range: touch
Duration: permanent or 1 minute/level (see text)
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: transparent gem touched
Subschool: Figment
:::

Kreighton Shaine researched this spell from the fragmentary notes of a Vudrani ascetic recorded in a
strange tome, and rumors credit him with no fewer than a dozen permanent stolen light gems hidden in
compartments and drawers in his study. Stolen light stores images within a gem. To store an image,
as part of casting you must touch a gem worth not less than 500 gp. You trap within the gem an image
of everything visible within a 30-foot cone measured from the gem, in a direction of your choice.
Alternatively, you can capture a less detailed image of a single object within sight. Once the
casting is complete, the gem turns opaque, and the image inside cannot be seen. The stolen image
remains within the gem until released or dispelled.

To release an image, you touch a gem holding stolen light as a standard action and speak a command
word chosen at the time of casting. For 1 minute per caster level, the image stored within the gem
becomes visible. Details can be made out as clearly as they could be perceived at the time of
casting. [Darkvision](ref/rule/darkvision) is of no use for making out details in a stolen image,
though [low-light vision](ref/rule/low-light-vision) or other exceptional visual talents may reveal
information the caster did not see. Light sources brighter than bright light are reduced to bright
light in the stolen image. Once the image has been released, it cannot again be recovered from the
gem.

Stolen light can be made permanent with the [permanency](ref/spell/permanency) spell by a caster of
10th level for a cost of 5,000 gp. This leaves the gem capable of projecting the image indefinitely,
activated and deactivated by its command word, until it is destroyed or dispelled.
