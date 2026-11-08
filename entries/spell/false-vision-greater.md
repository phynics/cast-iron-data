+++
id = "ref/spell/false-vision-greater"
kind = "spell"
title = "Greater False Vision"
source_ids = ["core-rulebook", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_vision_greater", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/false-vision" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 6 },
  { class = "Mesmerist", level = 6 },
  { class = "Psychic", level = 7 },
  { class = "Skald", level = 6 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M (a jade sphere worth 500 gp)"
range = "see text"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 6: Bard, Mesmerist, Skald\
7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a jade sphere worth 500 gp)
Range: see text
Target: one creature
Duration: 1 hour/level (D)
Saving throw: Will negates
Spell resistance: no
Subschool: Glamer
Descriptors: glamer
:::

## False Vision

**Sources:** PRPG Core Rulebook pg 280

This spell creates a subtle illusion, causing any divination (scrying) spell used to view anything
within the area of this spell to instead receive a false image (as the
[major image](ref/spell/major-image) spell), as defined by you at the time of casting. As long as
the duration lasts, you can concentrate to change the image as desired. While you aren't
concentrating, the image remains static.

### Greater False Vision

**Sources:** Ultimate Intrigue pg 214

This functions similarly to [false vision](ref/spell/false-vision), but instead of placing the
illusion on a nearby area, you can tie it to a specific individual, and can do so from great
distances. The spell can be cast at any distance. The difficulty of the save depends on your
knowledge of the subject and what sort of physical connection (if any) you have to that creature.
The target gains the same bonuses and penalties on its Will save to resist this spell as the bonuses
and penalties that apply to the scrying spell (including a +5 bonus if the target is on another
plane).

The illusion created by the spell moves with the target, and is not stationary. The image can affect
the way the target is perceived, the way the target's surroundings are perceived, and the way that
specific creatures or objects around the target are perceived. For the target, and any other
specific creatures or objects you specify, you can cause them to appear as other creatures or
objects that you designate, not to appear at all, or to have their appearance unaltered. For the
target's surroundings, you can choose to make the target appear to be somewhere else, either a
specific location with which you are familiar, or a generic location conjured from your imagination.
You can change the way that the spell affects the appearance of any of these things by concentrating
on the spell. You can also cause creatures or objects to appear in the illusion that are not really
there, or to make a creature or object seem to act in a way other than it is actually acting. In
this case, you must concentrate on the spell, or these aspects of the illusion simply remain static.
The spell can provide visual, auditory, olfactory, tactile, and thermal sensations as needed.

The illusion applies to only those who observe the target via a divination (scrying) spell, and has
no effect on viewers who are there in person.
