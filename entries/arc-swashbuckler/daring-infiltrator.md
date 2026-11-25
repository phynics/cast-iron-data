+++
id = "ref/arc-swashbuckler/daring-infiltrator"
kind = "archetype"
title = "Daring Infiltrator"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Daring%20Infiltrator"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "daring_infiltrator", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "advanced-class-guide"
page = "124"

[fields]
kind = "archetype"
features = [
  { anchor = "quick-tongued", level = 2 },
  { anchor = "deeds" },
  { anchor = "clandestine-expertise", level = 3 },
  { anchor = "silence-is-golden", level = 3 },
  { anchor = "authoritative-bluff", level = 11 },
]
trades = [
  { replaces = "Charmed life", feature = "charmed-life", by = ["quick-tongued"] },
  { replaces = "Swashbuckler initiative", feature = "deeds", power = "swashbuckler initiative", by = ["clandestine-expertise"] },
  { replaces = "Menacing swordplay", feature = "deeds", power = "menacing swordplay", by = ["silence-is-golden"] },
  { replaces = "Bleeding wound", feature = "deeds", power = "bleeding wound", by = ["authoritative-bluff"] },
  { alters = "Bonus feats", feature = "bonus-feats" },
  { alters = "The swashbuckler's class skill list" },
]
+++

Not known for their flashy entrances or for standing out in a crowd, a daring infiltrator uses
stealth, disguise, and ruthless guile to pursue her goals. Some of these swashbucklers work to
undermine evil organizations, while others are master thieves or mysterious assassins.

## Class Skills {#class-skills}

A daring infiltrator gains Disguise and Stealth as class skills, but does not gain Diplomacy,
Perform, and Profession as class skills. This alters the swashbuckler's class skill list.

## Bonus Feats {#bonus-feats}

In addition to combat feats, a daring infiltrator's bonus feats at 4th, 8th, 12th, 16th, and 20th
level can come from the following list: [Alertness](ref/feat/alertness),
[Antagonize](ref/feat/antagonize), [Cosmopolitan](ref/feat/cosmopolitan),
[Deceitful](ref/feat/deceitful), [Deft Hands](ref/feat/deft-hands), Disarming Threat\*,
[Persuasive](ref/feat/persuasive), [Prodigy](ref/feat/prodigy), and
[Skill Focus](ref/feat/skill-focus). (Those marked with an asterisk \[\*\] are detailed in this
book.) This alters the bonus feat class ability.

## Quick-Tongued (Ex) {#quick-tongued}

At 2nd level, a daring infiltrator gains a +1 bonus on Bluff checks. This bonus increases by 1 for
every 4 levels beyond 2nd. This ability replaces charmed life.

## Deeds {#deeds}

A daring infiltrator gains the following deeds, each of which replaces an existing deed.

## Clandestine Expertise (Ex) {#clandestine-expertise}

At 3rd level, a daring infiltrator with at least 1 panache point gains a +2 bonus on Disguise and
Stealth checks. Also, as long as she has at least 1 panache point, when she successfully aids
another with a Disguise or Stealth check, she grants the subject a +4 bonus on the skill check
instead of the normal +2. This deed replaces swashbuckler initiative.

## Silence Is Golden (Ex) {#silence-is-golden}

At 3rd level, when a daring infiltrator with at least 1 panache point succeeds at a
[trip](ref/rule/trip) or [grapple](ref/rule/grapple) combat maneuver check, the target is rendered
mute for 1 round. For every 5 by which the result of the combat maneuver check exceeds the
opponent's CMD, the target remains mute for an additional round. A mute creature cannot speak, use
language-dependent effects or verbal components, or use command words. This deed replaces menacing
swordplay.

## Authoritative Bluff (Ex) {#authoritative-bluff}

At 11th level, a daring infiltrator can spend 1 panache point to reroll a Bluff check after the roll
is made but before the results are revealed. She must take the result of the second roll, even if it
is lower. Additionally, a daring infiltrator with at least 1 panache point gains a +5 bonus on Bluff
checks to pretend to be someone's superior (socially or in the military). If she succeeds at the
check, the target obeys any reasonable orders she gives as it would those of an actual superior in
the situation. This deed replaces bleeding wound.
