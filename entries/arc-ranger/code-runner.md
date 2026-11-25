+++
id = "ref/arc-ranger/code-runner"
kind = "archetype"
title = "Code Runner"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Code%20Runner"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "code_runner", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "40"

[fields]
kind = "archetype"
features = [
  { anchor = "mnemonic-genius", level = 1 },
  { anchor = "resist-interrogation", level = 4 },
]
trades = [
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["mnemonic-genius"] },
  { replaces = "Hunter's bond", feature = "hunter-s-bond", by = ["resist-interrogation"] },
]
+++

A code runner specializes in the subtle and speedy transfer of secret messages. He performs long
runs between distant lands, sometimes spanning continents and often traversing difficult terrain. He
trains his mind both to memorize long messages and to resist any attempts to steal his covert
communiques.

## Class Skills {#class-skills}

A code runner adds Knowledge (local) and Linguistics to his list of class skills, instead of Handle
Animal and Heal.

This alters the ranger's class skills.

## Mnemonic Genius (Ex) {#mnemonic-genius}

A code runner learns to memorize and accurately recall information, even if he does not speak or
understand the language in which the information was presented. The code runner can spend 1 hour and
attempt a DC 15 Linguistics check to memorize a single passage of up to 150 words of information in
a language he speaks.

For every 5 by which he exceeds the DC, he can memorize 150 additional words. The DC is increased by
10 if the message is encoded or in a language he doesn't understand. A code runner can memorize one
such message at any given time. If he fails to memorize a message, he can retry as many times as he
wants, as long as he spends 1 hour each time. Once a message has been memorized, he can recall it
with perfect accuracy until he memorizes a different message.

This ability replaces wild empathy.

## Resist Interrogation (Ex) {#resist-interrogation}

At 4th level, a code runner gains a bonus equal to half his ranger level on saving throws against
divination effects. At 11th level, if he succeeds at a saving throw against a divination effect that
would grant its caster knowledge or information, the caster is not aware that the saving throw was
successful, and the code runner can attempt a Bluff check opposed by the caster's Sense Motive check
in order to send false information to the caster.

This ability replaces hunter's bond.
