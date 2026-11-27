+++
id = "ref/arc-fighter/lore-warden-pfs-field-guide"
kind = "archetype"
title = "Lore Warden (PFS Field Guide)"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Lore%20Warden%20%28PFS%20Field%20Guide%29"
source_ids = ["pathfinder-society-field-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "lore_warden_pfs_field_guide", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "pathfinder-society-field-guide"
page = "31"

[fields]
kind = "archetype"
features = [
  { anchor = "scholastic" },
  { anchor = "expertise", level = 2 },
  { anchor = "maneuver-mastery", level = 3 },
  { anchor = "know-thy-enemy", level = 7 },
  { anchor = "hair-s-breadth", level = 11 },
  { anchor = "swift-lore", level = 14 },
  { anchor = "know-weakness", level = 19 },
]
trades = [
  { replaces = "Proficiency with medium armor", feature = "weapon-and-armor-proficiencies", power = "medium armor", by = ["scholastic"] },
  { replaces = "heavy armor", feature = "weapon-and-armor-proficiencies", power = "heavy armor", by = ["scholastic"] },
  { replaces = "and shields", feature = "weapon-and-armor-proficiencies", power = "shields", by = ["scholastic"] },
  { replaces = "Bravery 1", feature = "bravery", levels = [2], by = ["expertise"] },
  { replaces = "Armor training 1", feature = "armor-training", levels = [3], by = ["maneuver-mastery"] },
  { replaces = "Armor training 2", feature = "armor-training", levels = [7], by = ["know-thy-enemy"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["hair-s-breadth"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["swift-lore"] },
  { replaces = "Armor mastery", feature = "armor-mastery", by = ["know-weakness"] },
]
+++

Quick thinking and deception can often carry the day where raw force might not. Lore wardens are the
bodyguards, guardians, and soldiers of the [Pathfinder Society](ref/rule/aff-scholars). Not only are
they often called upon to protect and watch over important repositories of lore, but they themselves
are impressive keepers of all manner of knowledge. Lore wardens are fighters who benefit from
learning to outsmart and outmaneuver their foes rather than just overpower them. Even out of combat,
lore wardens have a quick wit and a surprising breadth of knowledge that can often grant them
significant advantages over enemies even before a battle begins. Indeed, for many lore wardens, a
fight that can be won without a single weapon being drawn is the best kind of victory. A lore warden
has the following class features.

## Scholastic (Ex) {#scholastic}

Lore wardens gain 2 additional skill ranks each level. These ranks must be spent on
Intelligence-based skills. All Intelligence-based skills are class skills for lore wardens. This
ability replaces the lore warden's proficiency with medium armor, heavy armor, and shields.

## Expertise (Ex) {#expertise}

At 2nd level, a lore warden gains [Combat Expertise](ref/feat/combat-expertise) as a bonus feat,
even if he would not normally qualify for this feat. This ability replaces bravery 1.

## Maneuver Mastery (Ex) {#maneuver-mastery}

At 3rd level, a lore warden gains a +2 bonus on all CMB checks and to his CMD. This bonus increases
to +4 at 7th level, +6 at 11th level, and +8 at 15th level. This ability replaces armor training 1.

## Know Thy Enemy (Ex) {#know-thy-enemy}

At 7th level, a lore warden can take a standard action to study a specific target in sight. He must
make a Knowledge check to determine the target's abilities and weaknesses as part of this standard
action. If successful, the lore warden not only notes the appropriate abilities and weaknesses, as
detailed under the Knowledge skill on page 100 of the _Pathfinder RPG Core Rulebook_, but also gains
a +2 competence bonus on all attack rolls and weapon damage rolls made against that enemy. Note that
this bonus on attack and damage rolls applies only to that specific creature. This bonus lasts for
the duration of an encounter, or until the lore warden attempts a new Knowledge check to use this
ability on a different target. This ability replaces armor training 2.

## Hair's Breadth (Ex) {#hair-s-breadth}

At 11th level, a lore warden can attempt an Acrobatics check as an immediate action to negate a
confirmation roll for a critical hit. The critical hit confirmation is negated (though the attack
still hits and deals normal damage) if the Acrobatics check is greater than the opponent's
confirmation roll. This ability replaces armor training 3.

## Swift Lore (Ex) {#swift-lore}

At 14th level, a lore warden can use his Know Thy Enemy ability as a swift action. This ability
replaces armor training 4.

## Know Weakness (Ex) {#know-weakness}

At 19th level, a lore warden can automatically confirm a critical hit once per round when he
threatens a critical hit. This ability replaces armor mastery.
