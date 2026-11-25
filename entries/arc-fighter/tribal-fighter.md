+++
id = "ref/arc-fighter/tribal-fighter"
kind = "archetype"
title = "Tribal Fighter"
aon = "ArchetypeDisplay.aspx?FixedName=Fighter%20Tribal%20Fighter"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tribal_fighter", path = "json/archetypes_fighter2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/fighter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "50"

[fields]
kind = "archetype"
features = [
  { anchor = "forbidden-armor" },
  { anchor = "battle-focus", level = 1 },
  { anchor = "tribal-weapon-training", level = 5 },
]
trades = [
  { replaces = "The fighter feat gained at 1st level", feature = "bonus-feats", levels = [1], by = ["battle-focus"] },
  { alters = "Armor proficiency", feature = "weapon-and-armor-proficiencies", power = "armor", by = ["forbidden-armor"] },
  { alters = "Weapon training", feature = "weapon-training", by = ["tribal-weapon-training"] },
]
+++

A tribal fighter knows that it is not the weapon that matters but the hand that wields it. Instead
of encasing himself in metal armor like the soldiers fighting and dying for the so-called civilized
lands do, he prefers to wear something he or his ancestors have killed. These relics and trophies
help the tribal fighter attain a battle focus that allows him to perform incredible feats of
violence with the simplest of weapons.

## Forbidden Armor {#forbidden-armor}

A tribal fighter favors traditional armor and shields, avoiding other types out of spiritual
devotion, superstitious suspicion, or respect for tradition. He can attain his battle focus (see
page 51) only while using armaments of the appropriate types. Like a [druid](ref/class/druid), a
tribal fighter is prohibited from wearing metal armor and using metal shields. A tribal fighter who
wears prohibited armor or uses a prohibited shield loses the benefits of the battle focus and tribal
weapon training abilities while doing so and for 24 hours after removing the prohibited armor or
shield.

## Battle Focus (Ex) {#battle-focus}

A tribal fighter learns to fight with his bare hands and wield traditional tribal weapons so
effortlessly that they are almost extensions of his arms. He gains
[Improved Unarmed Strike](ref/feat/improved-unarmed-strike) as a bonus feat. For the purpose of
meeting the prerequisites of style feats and feats that have style feats as prerequisites, the
tribal fighter counts as having a number of skill ranks equal to his fighter level in all skills in
which he is trained.

This replaces the fighter feat gained at 1st level.

## Tribal Weapon Training (Ex) {#tribal-weapon-training}

At 5th level, when a tribal fighter gains the weapon training ability, he must choose the tribal
[weapon group](ref/ability/weapon-groups) and doesn't later gain additional weapon groups, though
the weapon training bonus for tribal weapons still improves at 9th level and every 4 levels
thereafter. Additionally, if the tribal fighter has combat feats that apply to a specific weapon
type (such as [Improved Critical](ref/feat/improved-critical) or
[Weapon Focus](ref/feat/weapon-focus)) and he has selected a weapon that belongs to the tribal
weapon group, he can apply the benefits of that feat to all weapons that belong to the tribal weapon
group that would legally apply (for instance, a feat that applies only to throwing weapons wouldn't
apply to [greatclubs](ref/eq-weapon/greatclub)). This benefit applies only to feats selected as
fighter bonus feats.

This alters weapon training.

### Tribal Weapon Group {#tribal-weapon-group}

The following new fighter weapon group consists of traditional melee weapons used by many indigenous
peoples.

_Tribal:_ Club, dagger, greatclub, handaxe, heavy shield, light shield, shortspear, spear, throwing
axe, and unarmed strike.
