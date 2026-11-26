+++
id = "ref/arc-swashbuckler/rondelero-swashbuckler"
kind = "archetype"
title = "Rondelero Swashbuckler"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Rondelero%20Swashbuckler"
source_ids = ["weapon-masters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rondelero_swashbuckler", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "weapon-masters-handbook"
page = "6"

[fields]
kind = "archetype"
features = [
  { anchor = "falcata-emphasis", level = 1 },
  { anchor = "shield-catch", level = 3 },
  { anchor = "rondelero-chop", level = 11 },
  { anchor = "shattering-chop", level = 15 },
  { anchor = "buckler-bash", level = 2 },
  { anchor = "rondelero-flexibility", level = 6 },
  { anchor = "charmed-life", level = 10 },
]
trades = [
  { replaces = "The derring-do deed", feature = "deeds", power = "derring-do", by = ["falcata-emphasis"] },
  { replaces = "Kip-up", feature = "deeds", power = "kip-up", by = ["shield-catch"] },
  { replaces = "Bleeding wound", feature = "deeds", power = "bleeding wound", by = ["rondelero-chop"] },
  { replaces = "Perfect thrust", feature = "deeds", power = "perfect thrust", by = ["shattering-chop"] },
  { alters = "Charmed life", feature = "charmed-life", by = ["charmed-life"] },
]
+++

Rondelero swashbucklers are Taldan specialists in an aggressive, lightly armored fighting style that
utilizes the falcata and buckler.

## Falcata Emphasis (Ex) {#falcata-emphasis}

At 1st level, a rondelero swashbuckler is proficient with [falcatas](ref/eq-weapon/falcata) and can
treat a falcata as a one-handed piercing melee weapon for the purposes of the swashbuckler's finesse
as well as all feats and class abilities that refer to such a weapon. This ability replaces the
derring-do deed.

## Rondelero Deeds (Ex) {#rondelero-deeds}

A rondelero swashbuckler gains the following deeds at the appropriate levels.

## Shield Catch (Ex) {#shield-catch}

At 3rd level, while he has at least 1 panache point, the rondelero swashbuckler gains a +4 bonus on
all combat maneuver checks to [disarm](ref/rule/disarm) that he attempts with his
[buckler](ref/eq-armor/buckler). This deed replaces kip-up.

## Rondelero Chop (Ex) {#rondelero-chop}

At 11th level, when the rondelero swashbuckler hits with a melee attack using a light or one-handed
slashing melee weapon, he can spend 1 panache point to attempt a [sunder](ref/rule/sunder) combat
maneuver check against the target of his attack as an immediate action without provoking attacks of
opportunity. This deed replaces bleeding wound.

## Shattering Chop (Ex) {#shattering-chop}

At 15th level, while the rondelero swashbuckler has at least 1 panache point, he can attempt a
shattering chop as a full-round action, pooling all of his attack potential into a single melee
sunder combat maneuver with a light or one-handed slashing weapon. When he does, he gains a +4 bonus
on her combat maneuver check and ignores half of the [hardness](ref/umr/hardness) of the item he
sunders. This deed replaces perfect thrust.

## Buckler Bash (Ex) {#buckler-bash}

At 2nd level, a rondelero swashbuckler can perform a [shield bash](ref/misc/shield-bash) with a
buckler (use the same damage and critical multiplier as for a light shield). He can treat a buckler
as a one-handed piercing melee weapon for the purposes of the swashbuckler's finesse and all feats
and class abilities that refer to such a weapon.

## Rondelero Flexibility (Ex) {#rondelero-flexibility}

At 6th level, as a full-attack action, a rondelero swashbuckler wielding a falcata in one hand and a
buckler in the other can alternate between using his falcata and his buckler for each attack. This
does not grant additional attacks or incur penalties as two-weapon fighting does, and does not cause
her to lose his Armor Class bonus from her buckler.

## Charmed Life (Ex) {#charmed-life}

A rondelero swashbuckler does not gain charmed life until 10th level, at which point he can use the
ability only once per day. At 14th level and again at 18th level, he can use the ability an
additional time per day. This ability alters charmed life.
