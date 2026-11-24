+++
id = "ref/arc-paladin/tranquil-guardian"
kind = "archetype"
title = "Tranquil Guardian"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Tranquil%20Guardian"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "tranquil_guardian", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "advanced-race-guide"
page = "86"

[fields]
kind = "archetype"
features = [
  { anchor = "touch-of-serenity", level = 1 },
  { anchor = "serene-strike", level = 3 },
  { anchor = "divine-bond" },
  { anchor = "aura-of-calm", level = 8 },
  { anchor = "waves-of-peace", level = 11 },
  { anchor = "apostle-of-peace", level = 20 },
]
trades = [
  { replaces = "Smite evil", feature = "smite-evil", by = ["touch-of-serenity"] },
  { replaces = "Aura of courage", feature = "aura-of-courage", by = ["serene-strike"] },
  { replaces = "Aura of resolve", feature = "aura-of-resolve", by = ["aura-of-calm"] },
  { replaces = "Aura of justice", feature = "aura-of-justice", by = ["waves-of-peace"] },
  { replaces = "Holy champion", feature = "holy-champion", by = ["apostle-of-peace"] },
]
+++

A tranquil guardian is a missionary of peace and tranquility, a soothing voice of succor in a
violent and dangerous world. A tranquil guardian gains the following class features.

**Prerequisites:** Aasimar

## Touch of Serenity (Su) {#touch-of-serenity}

At 1st level, a tranquil guardian gains [Touch of Serenity](ref/feat/touch-of-serenity) (_Advanced
Player's Guide_ 172) as a bonus feat, even if she does not meet the prerequisites. At 6th level, and
every six levels thereafter, the duration of a tranquil guardian's Touch of Serenity increases by 1
round. Each round on its turn, the target may attempt a new Will save to end the effect. The
duration does not stack; only the longest remaining duration applies. This ability replaces smite
evil.

## Serene Strike (Su) {#serene-strike}

At 3rd level, when a tranquil guardian confirms a critical hit, she may convert all damage from her
attack to nonlethal damage, and when she does, she can activate Touch of Serenity through her weapon
or unarmed strike. Using serene strike is a free action. This ability replaces aura of courage.

## Divine Bond (Su) {#divine-bond}

A tranquil guardian who chooses a weapon as her divine bond may only increase her weapon's
enhancement bonus or add the following properties to her weapon: _conductive_ (_Advanced Player's
Guide_ 286)_, defending, disruptive, grayflame_ (_Advanced Player's Guide_ 288)_,_ or _merciful_.

## Aura of Calm (Su) {#aura-of-calm}

At 8th level, a tranquil guardian is immune to all spells and
[spell-like abilities](ref/umr/spell-like-abilities) with the emotion descriptor, as well as all
fear effects. Each ally within 10 feet of her gains a +4 morale bonus on saving throws against these
effects.

This ability functions only while the tranquil guardian is conscious, not if she is unconscious or
dead. This ability replaces aura of resolve.

## Waves of Peace (Su) {#waves-of-peace}

At 11th level, a tranquil guardian may expend 2 uses of her Touch of Serenity to affect each
opponent within 5 feet of her with that effect. She does not need to touch the creature for the
effect to take hold. This ability replaces aura of justice.

## Apostle of Peace (Su) {#apostle-of-peace}

At 20th level, a tranquil guardian's DR increases to 10/evil, and whenever she channels positive
energy or uses lay on hands to heal, she heals the maximum possible amount. In addition, any
creature struck by her Touch of Serenity, even if it saves, must make an additional Will save (DC
10 + 1/2 her tranquil guardian level + her Charisma modifier) the next time it tries to attack. If
it fails this save, the attack (including spells or special abilities) automatically fails. This
ability replaces holy champion.
