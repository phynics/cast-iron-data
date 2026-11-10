+++
id = "ref/spell/shadow-endurance"
kind = "spell"
title = "Shadow Endurance"
aon = "SpellDisplay.aspx?ItemName=Shadow%20Endurance"
source_ids = ["agents-of-evil"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_endurance", path = "json/spells15.json" },
]
[[sources]]
publication = "agents-of-evil"
page = "31"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 6 },
  { class = "Spiritualist", level = 5 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (a fetchling's tooth)"
range = "personal"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "1 hour/level until discharged, then 1 minute/level; see text"
saving_throw = "Will disbelief (if interacted with), varies, see text"
spell_resistance = "see text"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 5: Bard, Mesmerist, Shaman, Skald, Spiritualist\
6: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a fetchling's tooth)
Range: personal
Duration: 1 hour/level until discharged, then 1 minute/level; see text
Saving throw: Will disbelief (if interacted with), varies, see text
Spell resistance: see text
Effect: see text
Subschool: Shadow
Descriptors: shadow
:::

You conjure protective wisps of darkness made from shadow. If you are reduced below 0 hit points or
rendered unconscious, shadow endurance immediately discharges, shunting your injured body into a
hidden alcove on the Shadow Plane. You immediately stabilize, but cannot awaken or take any further
actions until the second duration expires.

As you vanish, a quasi-real duplicate of you made from shadow substance appears where you fell, as
if created by shadow conjuration. The duplicate acts on your initiative and is under your control.
Your duplicate is 1/4 as real as you and appears with 25% of your full hit point total, and any
creature that fails a Will saving throw believes it to be you. The duplicate has the same
equipment-based bonuses as you, but deals only 1/4 of your normal damage against enemies. It can
cast any spells you can, drawing on your reserve of magic, but the duplicate's caster level is 1/4
your actual level. Regardless of your alignment, your shadow duplicate is neutral evil, though it
will not harm your friends and allies.

When the second duration of the spell expires, your duplicate disappears and your body reappears in
the location from which you vanished. If the image is destroyed, the spell immediately expires and
your body reappears.
