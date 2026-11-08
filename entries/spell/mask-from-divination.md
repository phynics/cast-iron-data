+++
id = "ref/spell/mask-from-divination"
kind = "spell"
title = "Mask from Divination"
source_ids = ["adventurers-guide", "arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mask_from_divination", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/nondetection" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 5 },
  { class = "Arcanist", level = 5 },
  { class = "Bloodrager", level = 4 },
  { class = "Investigator", level = 5 },
  { class = "Magus", level = 5 },
  { class = "Shaman", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M (diamond dust worth 200 gp), F (an eyeless mask)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "24 hours"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 4: Bloodrager\
5: Alchemist, Arcanist, Investigator, Magus, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (diamond dust worth 200 gp), F (an eyeless mask)
Range: touch
Duration: 24 hours
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: creature touched
:::

**Sources:** Adventurer's Guide pg 125, Arcane Anthology pg 14

As part of the action used to cast this spell, you place the mask used as the focus component on the
target's face, after which it adheres tightly to the target for the spell's duration and cannot be
removed by physical force. Despite lacking eyes, this mask does not impair its wearer's vision in
any way. While in effect, this spell functions like [nondetection](ref/spell/nondetection), except
it also foils divination spells that attempt to gather information about the creature, even if they
don't target it specifically. In the case of divination spells that would normally reveal the
wearer's presence, such as [see invisibility](ref/spell/see-invisibility), the spell works, but the
wearer is detected only if the caster succeeds at a caster level check. Likewise, scrying attempts
that specifically target the wearer do not work at all unless the caster succeeds at a caster level
check. In addition, the DCs of skill checks to learn about the wearer or identify the wearer and its
strengths and weaknesses - including Diplomacy checks to gather information, Perception checks
opposed by the target's Disguise checks, and Knowledge checks - increase by 4.

The mask cannot be removed for the duration of the spell, and the fact that the target is wearing
the focus mask cannot be hidden in any way from creatures that observe the target.
