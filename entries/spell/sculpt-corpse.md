+++
id = "ref/spell/sculpt-corpse"
kind = "spell"
title = "Sculpt Corpse"
aon = "SpellDisplay.aspx?ItemName=Sculpt%20Corpse"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sculpt_corpse", path = "json/spells15.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "241"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (lump of wax)"
range = "touch"
effects = [
  { label = "Target", value = "one dead creature touched" },
]
duration = "instantaneous"
saving_throw = "Will partial, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Arcanist, Occultist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (lump of wax)
Range: touch
Duration: instantaneous
Saving throw: Will partial, see text
Spell resistance: no
Target: one dead creature touched
:::

With a clammy caress and a word to the powers lurking beyond death, you can reshape a dead body look
like another creature or even a specific person so long as you have first-hand knowledge of how that
creature or person actually looks. You can make the corpse one size larger or smaller and change
anything else about it including its apparent type, gender, or age. Creatures with a reason to
suspect deception may make a Will saving throw to realize that the corpse was altered. If you chose
to make the corpse look like a specific individual anyone who knows that individual can make a Will
save to realize that the corpse is not actually that person. However, if a creature fails its Will
save by 5 or less they believe the corpse is that of someone who closely resembled the person they
knew rather than a deliberate fake. This spell merely changes the appearance of the corpse. Any
spell or effect that targets the corpse (such as [speak with dead](ref/spell/speak-with-dead) or
[raise dead](ref/spell/raise-dead)) treats it as if it still had its original appearance.
