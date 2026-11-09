+++
id = "ref/spell/project-image"
kind = "spell"
title = "Project Image"
aon = "SpellDisplay.aspx?ItemName=Project%20Image"
source_ids = ["core-rulebook", "advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "project_image", path = "json/spells15.json" },
]
[[sources]]
publication = "core-rulebook"
page = "327"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a small replica of you worth 5 gp)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "one shadow duplicate" },
]
duration = "1 round/level (D)"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 6: Bard, Mesmerist, Occultist, Skald\
7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a small replica of you worth 5 gp)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: Will disbelief (if interacted with)
Spell resistance: no
Effect: one shadow duplicate
Subschool: Shadow
Descriptors: shadow
:::

You tap energy from the Plane of Shadow to create a quasi-real, illusory version of yourself. The
projected image looks, sounds, and smells like you but is intangible. The projected image mimics
your actions (including speech) unless you direct it to act differently (which is a move action).

You can see through its eyes and hear through its ears as if you were standing where it is, and
during your turn you can switch from using its senses to using your own, or back again, as a free
action. While you are using its senses, your body is considered blinded and deafened.

If you desire, any spell you cast whose range is touch or greater can originate from the projected
image instead of from you. The projected image can't cast any spells on itself except for illusion
spells. The spells affect other targets normally, despite originating from the projected image.

Objects are affected by the projected image as if they had succeeded on their Will save. You must
maintain line of effect to the projected image at all times. If your line of effect is obstructed,
the spell ends. If you use [dimension door](ref/spell/dimension-door),
[teleport](ref/spell/teleport), [plane shift](ref/spell/plane-shift), or a similar spell that breaks
your line of effect, even momentarily, the spell ends.
