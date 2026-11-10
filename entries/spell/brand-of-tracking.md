+++
id = "ref/spell/brand-of-tracking"
kind = "spell"
title = "Brand of Tracking"
aon = "SpellDisplay.aspx?ItemName=Brand%20of%20Tracking"
source_ids = ["adventurers-guide", "path-of-the-hellknight"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "brand_of_tracking", path = "json/spells2.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "98"
[[sources]]
publication = "path-of-the-hellknight"
page = "60"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["curse"]
levels = [
  { class = "Inquisitor", level = 4 },
]
casting_time = "1 round"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Inquisitor
Casting time: 1 round
Components: V, S, DF
Range: touch
Duration: permanent
Saving throw: Fortitude negates
Spell resistance: yes
Target: creature touched
Descriptors: curse
:::

This spell etches the symbol of an eye or a lawful institution on the target, dealing 1d6 points of
damage. The mark can be placed on any exposed portion of the creature, typically the head or
forearm. While the target is branded in this way, twice per day as a standard action, you can
instantly determine in what direction and how far away the target is, as long as it is within a
range equal to 1 mile per your caster level. If the target travels beyond this range or to another
plane, you cannot gain information about the recipient's location. Similarly, if the target becomes
warded by a spell or effect that thwarts divination spells (such as nondetection) or moves into such
an area (such as one created by antimagic field), you cannot gain information about the target's
location. This effect otherwise works as a locate creature spell that lasts for 1 minute per caster
level. It can be fooled by mislead but not by polymorph.

A brand of tracking can be hidden by clothing or temporarily removed by scraping it away (the latter
deals 1d6 points of damage, though the brand returns if that damage is healed, or 1 day later
otherwise). The effects of a brand of tracking continue to function even when hidden or scraped
away. A brand of tracking cannot be dispelled, but it can be permanently removed by any means that
removes a [mark of justice](ref/spell/mark-of-justice).
