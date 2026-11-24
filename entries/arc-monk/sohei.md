+++
id = "ref/arc-monk/sohei"
kind = "archetype"
title = "Sohei"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Sohei"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sohei", path = "json/archetypes_monk2.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "ultimate-combat"
page = "60"

[fields]
kind = "archetype"
features = [
  { anchor = "skills" },
  { anchor = "devoted-guardian", level = 1 },
  { anchor = "unarmed-strike" },
  { anchor = "monastic-mount", level = 4 },
  { anchor = "ki-weapon", level = 4 },
  { anchor = "weapon-training", level = 6 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["devoted-guardian"] },
  { replaces = "Fast movement", feature = "fast-movement", by = ["monastic-mount"] },
  { replaces = "increased unarmed damage", by = ["monastic-mount"] },
  { replaces = "Slow fall", feature = "slow-fall", by = ["ki-weapon"] },
  { replaces = "abundant step", feature = "abundant-step", by = ["ki-weapon"] },
  { replaces = "Purity of body", feature = "purity-of-body", by = ["weapon-training"] },
  { replaces = "diamond body", feature = "diamond-body", by = ["weapon-training"] },
  { replaces = "quivering palm", feature = "quivering-palm", by = ["weapon-training"] },
  { replaces = "timeless body", feature = "timeless-body", by = ["weapon-training"] },
  { replaces = "tongue of sun and moon", feature = "tongue-of-the-sun-and-moon", by = ["weapon-training"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
]
+++

The sohei are masters of the horse and the hunt. A monastic soldier, the sohei is equally adept at
combat afoot or on horseback. While skilled in unarmed techniques, many sohei favor weapons they can
use while mounted on horseback or against others' horses.

**Gained class skills:** ha

## Skills {#skills}

A sohei gains Handle Animal as a class skill.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A sohei is proficient with all simple and martial weapons and with light armor, instead of a monk's
usual weapon and armor proficiencies. This ability alters the monk's weapon and armor proficiencies.

## Bonus Feats {#bonus-feats}

A sohei may select [mounted combat](ref/feat/mounted-combat) feats as bonus feats.

## Devoted Guardian (Ex) {#devoted-guardian}

At 1st level, a sohei can always act in a surprise round even if he does not notice his enemies,
though he remains [flat-footed](ref/rule/flat-footed) until he acts. In addition, a sohei gains a
bonus on initiative rolls equal to 1/2 his monk level. At 20th level, a sohei's initiative roll is
automatically a natural 20. This ability replaces stunning fist.

## Unarmed Strike {#unarmed-strike}

A sohei's unarmed strike damage does not increase at 4th level and above.

## Monastic Mount (Su) {#monastic-mount}

At 4th level, a sohei may spend 1 point from his ki pool to grant his mount
[temporary hit points](ref/rule/temporary-hit-points) equal to twice his level for 1 hour per level.
In addition, as long as the sohei and his mount are adjacent, including when mounted, the mount
gains any of the following abilities the sohei possesses: AC bonus, diamond soul, evasion, high
jump, improved evasion, ki strike (as long as the sohei has at least 1 point in his ki pool),
perfect self, and still mind. When a sohei spends points from his ki pool, his mount gains the same
benefits as the sohei. This ability replaces fast movement and increased unarmed damage.

## Ki Weapon (Su) {#ki-weapon}

At 4th level, as a swift action, a sohei may spend 1 point from his ki pool to grant any weapon he
wields (including his unarmed strike) a +1 enhancement bonus on attack and damage rolls, increasing
by +1 per four levels after 4th to a maximum bonus of +5 at 20th level, until the end of his next
turn. This ability replaces slow fall and abundant step.

## Weapon Training (Ex) {#weapon-training}

At 6th level, a sohei gains weapon training in one of the following
[weapon groups](ref/ability/weapon-groups), as the [fighter](ref/class/fighter) class feature: bows,
crossbows, monk weapons, polearms, spears, or thrown weapons. He may select an additional group of
weapons for every six levels after 6th, to a maximum of three at 18th level. A sohei may use flurry
of blows and ki strike with any weapon in which he has weapon training. This ability replaces purity
of body, diamond body, quivering palm, timeless body, and tongue of the sun and moon.
