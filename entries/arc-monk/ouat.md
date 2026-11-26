+++
id = "ref/arc-monk/ouat"
kind = "archetype"
title = "Ouat"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Ouat"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ouat", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "inner-sea-combat"
page = "41"

[fields]
kind = "archetype"
features = [
  { anchor = "awaken-divinity", level = 1 },
  { anchor = "spurn-tradition" },
  { anchor = "know-the-unseen-disciples", level = 7 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["awaken-divinity"] },
  { replaces = "Greed and hatred racial traits", by = ["awaken-divinity"] },
  { replaces = "Defensive training", by = ["spurn-tradition"] },
  { replaces = "stonecunning", by = ["spurn-tradition"] },
  { replaces = "Weapon familiarity racial traits", by = ["spurn-tradition"] },
  { replaces = "Wholeness of body", feature = "wholeness-of-body", by = ["know-the-unseen-disciples"] },
]
+++

The ascetic, desert-dwelling dwarves known as the Ouat have eschewed dwarven traditions, whose
unchanging rigidity, they believe, shackles their people to the past and inhibits self-improvement.
Shaving their heads, living under the open sky, and practicing arts unfamiliar to the typical
[dwarf](ref/race/dwarf), the Ouat follow in the footsteps of Irori and Nethys by aspiring to awaken
the divine essence that lives within each creature.

## Awaken Divinity (Su) {#awaken-divinity}

At 1st level, as a standard action, an Ouat can touch a creature to grant it a temporary ki point
until the beginning of the Ouat's next turn. In addition to any other ways in which the target can
use ki, it can expend the ki point as a swift action in order to either gain a +2 dodge bonus to AC
for 1 round or increase its base speed by 20 feet for 1 round. The Ouat can target himself with this
ability as a swift action, but doing so costs 2 uses of the ability.

At 4th level, the dodge bonus to AC increases to +4. At 8th level, an affected creature can spend
the ki point to ignore all Strength, Dexterity, and Constitution penalties it would otherwise take
for 1 round. At 12th level, an Ouat can target two adjacent creatures with this ability as a
standard action, but must expend one use of the ability for each target affected. At 16th level, an
affected creature can spend this ki point to roll all saving throws twice and take the higher result
for 1 round. At 20th level, an affected creature can spend the ki point to benefit from the Ouat's
perfect self class ability for 1 round. If the creature already has the perfect self class feature,
its [damage reduction](ref/rule/damage-reduction) and any
[spell resistance](ref/rule/spell-resistance) it has increases by 2 for 1 round.

An Ouat can use this ability a number of times per day equal to his class level, but no more than
once per round. This ability replaces the stunning fist monk class feature and the greed and hatred
racial traits.

## Spurn Tradition (Ex) {#spurn-tradition}

Ouat dwarves strive to separate themselves from the rest of their race and the traditions that bind
them. The bonuses for nonmagical effects that target or specifically affect dwarf subtype creatures
(such as a ranger's [favored enemy](ref/ability/favored-enemy) class feature) are all reduced by
half. In addition, an Ouat becomes proficient in one martial weapon with the monk property. This
ability replaces the dwarf's defensive training, stonecunning, and weapon familiarity racial traits.

## Know the Unseen Disciples (Su) {#know-the-unseen-disciples}

At 7th level, an Ouat can spot hidden creatures, as if using the spell
_[see invisibility](ref/spell/see-invisibility)_. Using this ability is a standard action that
consumes 2 points from his ki pool. His caster level for this effect is equal to his class level.
This ability replaces wholeness of body.
