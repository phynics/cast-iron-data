+++
id = "ref/arc-cavalier/honor-guard"
kind = "archetype"
title = "Honor Guard"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Honor%20Guard"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "honor_guard", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "ultimate-combat"
page = "37"

[fields]
kind = "archetype"
features = [
  { anchor = "sworn-defense", level = 1 },
  { anchor = "intercept", level = 3 },
  { anchor = "warding-charge", level = 11 },
  { anchor = "defensive-challenge", level = 12 },
]
trades = [
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["intercept"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["warding-charge"] },
  { replaces = "Demanding challenge", feature = "demanding-challenge", by = ["defensive-challenge"] },
  { alters = "Challenge", feature = "challenge", by = ["sworn-defense"] },
]
+++

Certain cavaliers are trained not as advance combatants, but as loyal guards, standing as firm
defenders in the face of threats to their chosen charge. These honor guards are sometimes merely
ornamental, performing their functions on a ceremonial basis, but a surprising number are capable,
deadly opponents, able to take down a threat long before their liege knows of the danger. To be an
honor guard is to constantly place one's self in harm's way, and to always be willing to lay down
one's life at a moment's notice.

## Sworn Defense (Ex) {#sworn-defense}

At 1st level, whenever an honor guard issues a challenge, he can select one ally as his ward for the
duration of the challenge. Whenever the honor guard is adjacent to his ward, he takes a -1 penalty
to Armor Class, and the ward receives a +1 dodge bonus to AC. This modifies the challenge ability

## Intercept (Ex) {#intercept}

At 3rd level, an honor guard learns to better disrupt the attacks of his enemies. He gains
[Bodyguard](ref/feat/bodyguard) as a bonus feat, even if he does not meet the prerequisite. In
addition, whenever the honor guard uses the [aid another](ref/rule/aid-another-2) action to increase
an ally's Armor Class, the bonus to Armor Class granted by the aid another action increases by +1.
This ability replaces cavalier's charge.

## Warding Charge (Ex) {#warding-charge}

At 11th level, an honor guard can flash across the battlefield to protect his ward against the
target of his challenge. Whenever the target of the honor guard's challenge makes an attack against
his ward, the honor guard can move up to his speed and make a single melee attack against the target
of his challenge as an immediate action. This movement and attack can be made as a
[charge](ref/rule/charge) if the movement qualifies. This ability replaces mighty charge.

## Defensive Challenge (Ex) {#defensive-challenge}

At 12th level, whenever an honor guard declares a challenge, his target must pay particular
attention to him and his ability to intercept attacks. As long as the target is within the
threatened area of the cavalier, it takes a -2 penalty on attack rolls against anyone other than the
honor guard. This ability replaces demanding challenge.
