+++
id = "ref/rule/poison"
kind = "rule"
title = "Poison"
source_ids = ["core-rulebook", "inner-sea-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "poison", path = "json/rules_combat01.json" },
]

[fields]
kind = "none"
+++

**Sources:** PRPG Core Rulebook pg 557, Inner Sea Intrigue pg 51

No other affliction is so prevalent as poison. From the fangs of a viper to the ichor-stained
assassin's blade, poison is a constant threat. Poisons can be cured by successful saving throws and
spells such as neutralize poison.

Poisons use the same stat blocks as other [afflictions](ref/rule/afflictions).

### Types of Poison

**Contact poisons** are contracted the moment someone touches the poison with his bare skin. Such
poisons can be used as injury poisons. Contact poisons usually have an onset time of 1 minute and a
frequency of 1 minute.

**Ingested poisons** are contracted when a creature eats or drinks the poison. Ingested poisons
usually have an onset time of 10 minutes and a frequency of 1 minute.

**Injury poisons** are primarily contracted through the attacks of certain creatures and through
weapons coated in the toxin. Injury poisons do not usually have an onset time and have a frequency
of 1 round.

**Inhaled poisons** are contracted the moment a creature enters an area containing such poisons.
Most inhaled poisons fill a volume equal to a 10-foot cube per dose. Creatures can attempt to
[hold their breath](ref/misc/hold-your-breath) while inside to avoid inhaling the toxin. Creatures
holding their breaths receive a 50% chance of not having to make a Fortitude save each round. Note
that a character that would normally suffocate while attempting to hold its breath instead begins to
breathe normally again.

**Triggered Poisons:** Numerous Inner Sea poisons are designed to take effect only after exposure to
a particular stimulus. Poisons with onset triggers list the specific triggers in their Onset entries
(rather than a number of rounds, minutes, or days). A character who fails his Fortitude saving throw
upon exposure doesn't start attempting saving throws against the poison's effects until exposed to
the listed stimulus.

Some triggered poisons have initial and secondary effects. The first time after an affected
character triggers the poison and fails a saving throw to resist the poison, the character suffers
the initial effect. If the affected character fails any subsequent saving throws, he suffers the
secondary effect. Unless noted otherwise, a triggered poison that isn't triggered after 1 day has no
effect.

### Multiple Doses

Unlike other afflictions, multiple doses of the same poison stack. Poisons delivered by injury and
contact cannot inflict more than one dose of poison at a time, but inhaled and ingested poisons can
inflict multiple doses at once. Each additional dose extends the total duration of the poison (as
noted under frequency) by half its total duration. In addition, each dose of poison increases the DC
to resist the poison by +2. This increase is cumulative. Multiple doses do not alter the cure
conditions of the poison, and meeting these conditions ends the affliction for all the doses. For
example, a character is bit three times in the same round by a trio of Medium monstrous spiders,
injecting him with three doses of Medium spider venom. The unfortunate character must make a DC 18
Fortitude save for the next 8 rounds. Fortunately, just one successful save cures the character of
all three doses of the poison.

### Using and Making Poison

Applying poison to a weapon or single piece of ammunition is a standard action. Whenever a character
applies or readies a poison for use there is a 5% chance that he exposes himself to the poison and
must save against the poison as normal. This does not consume the dose of poison. Whenever a
character attacks with a poisoned weapon, if the attack roll results in a natural 1, he exposes
himself to the poison. This poison is consumed when the weapon strikes a creature or is touched by
the wielder. Characters with the [poison use](ref/ability/poison-use) class feature do not risk
accidentally poisoning themselves.

Poisons can be made using Craft (alchemy). The DC to make a poison is equal to its Fortitude save
DC. Rolling a natural 1 on a Craft skill check while making a poison exposes the crafter to the
poison. Crafters with the poison use class feature do not risk poisoning themselves when using Craft
to make poison.

Poisons are listed in the equipment section.
