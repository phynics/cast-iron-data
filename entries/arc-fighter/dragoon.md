+++
id = "ref/arc-fighter/dragoon"
kind = "archetype"
title = "Dragoon"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Dragoon"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dragoon", path = "json/archetypes_fighter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "ultimate-combat"
page = "46"

[fields]
kind = "archetype"
features = [
  { anchor = "skilled-rider", level = 1 },
  { anchor = "spear-training", level = 5 },
  { anchor = "spinning-lance", level = 7 },
  { anchor = "banner", level = 9 },
  { anchor = "piercing-lance", level = 11 },
  { anchor = "leaping-lance", level = 15 },
  { anchor = "weapon-mastery" },
]
trades = [
  { replaces = "The 1st-level fighter bonus combat feat", feature = "bonus-feats", levels = [1], by = ["skilled-rider"] },
  { replaces = "Armor training 2", feature = "armor-training", levels = [7], by = ["spinning-lance"] },
  { replaces = "Weapon training 2, 3, and 4", feature = "weapon-training", levels = [9, 13, 17], by = ["banner"] },
  { replaces = "Armor training 3", feature = "armor-training", levels = [11], by = ["piercing-lance"] },
  { replaces = "Armor training 4", feature = "armor-training", levels = [15], by = ["leaping-lance"] },
  { alters = "Weapon training", feature = "weapon-training", by = ["spear-training"] },
  { alters = "Weapon mastery", feature = "weapon-mastery", by = ["weapon-mastery"] },
]
+++

These gallant lancers serve in the vanguard of many armies or as knights-errant. They are born
leaders and masters of the mounted charge.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A dragoon is not proficient with tower shields.

## Skilled Rider (Ex) {#skilled-rider}

At 1st level, a dragoon gains both the [Mounted Combat](ref/feat/mounted-combat) and
[Skill Focus](ref/feat/skill-focus) (Ride) feats as bonus feats. This ability replaces the 1st-level
fighter bonus combat feat.

## Spear Training (Ex) {#spear-training}

At 5th level, a dragoon must select weapon training with the
[spear group](ref/ability/weapon-groups). The dragoon's weapon training bonus with spears improves
by +1 on attack rolls and +2 on damage rolls for every four levels beyond 5th (to a maximum of +4 on
attack rolls and +8 on damage rolls at 17th level). The dragoon does not gain weapon training in any
other groups as he increases in level.

## Spinning Lance (Ex) {#spinning-lance}

At 7th level, a dragoon may alternate attacks with the piercing head of his
[lance](ref/eq-weapon/lance) with reach, or with the butt end (treat as a
[club](ref/eq-weapon/club)) against adjacent targets. Unlike a double weapon, the masterwork quality
and magical special abilities apply to both ends of the lance, except for those weapon special
abilities that apply only to edged weapons. This ability replaces armor training 2.

## Banner (Ex) {#banner}

At 9th level, a dragoon may attach a banner to his lance. This is identical to the
[cavalier](ref/class/cavalier) class feature (_Advanced Player's Guide_ 34). The bonuses provided by
the dragoon's banner increase by +1 for every five levels beyond 9th (to a maximum of +3 at 19th
level). Cavalier levels stack with his dragoon level for determining the effect of his banner, and
he can take the better banner progression. This ability replaces weapon training 2, 3, and 4.

## Piercing Lance (Ex) {#piercing-lance}

At 11th level, as a standard action or as part of a [charge](ref/rule/charge), a dragoon attacking a
mounted opponent can make two attacks, one against the mount and the other against the rider, using
his highest base attack bonus. Furthermore, if the mount is hit and its rider attempts to negate the
hit with the Mounted Combat feat, the dragoon's attack roll is considered 4 higher when calculating
the DC of the Ride check to negate the hit. This ability replaces armor training 3.

## Leaping Lance (Ex) {#leaping-lance}

At 15th level, a dragoon and his mount suffer no armor check penalty on Acrobatics checks while
mounted. When charging, a dragoon may jump from his mount toward his target. If he jumps 10 feet,
his charge modifiers on attack rolls and to AC are doubled and he is still considered mounted for
lance damage, mounted combat feats, and so on. This ability replaces armor training 4.

## Weapon Mastery {#weapon-mastery}

The dragoon must select the lance for this ability.
