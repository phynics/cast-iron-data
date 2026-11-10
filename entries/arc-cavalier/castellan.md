+++
id = "ref/arc-cavalier/castellan"
kind = "archetype"
title = "Castellan"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Castellan"
source_ids = ["melee-tactics-toolbox"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "castellan", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "melee-tactics-toolbox"
page = "9"

[fields]
kind = "archetype"
replaces = ["Mount", "Cavalier's charge", "Expert trainer", "Mighty charge", "Demanding challenge", "Supreme charge"]
replaces_features = ["mount", "cavalier-s-charge", "expert-trainer", "mighty-charge", "demanding-challenge", "supreme-charge"]
+++

A castellan is a cavalier who dedicates himself to the defense of a castle or walled city. Though
not as celebrated as the cavaliers who ride forth to take on distant foes, the castellan is no less
brave or important, for the castellan and his allies are the last line of defense for those who
depend on the fortification for protection.

**Castle Defender**

**At 1st Level:** A castellan gains a +1 bonus to Armor Class and an additional +1 bonus on attack
rolls when he is on [higher ground](ref/rule/combat-modifiers). He also gains an additional +1 bonus
to Armor Class and on Reflex saves when he has [cover](ref/rule/cover) other than soft cover from
other creatures.

**At 11th Level:** These bonuses increase by 1.

**At 16th Level:** He gains [improved evasion](ref/talent/improved-evasion) instead of evasion.

**At 6th Level:** A castellan gains [evasion](ref/ability/evasion) (as a rogue) when he has cover
(but not soft cover) against the source of the attack.

**Replaces:** Mount

**Special:** Both the evasion and improved evasion abilities work even when the castellan wears
medium or heavy armor.

**Castle Lore**

**At 13th Level:** The bonuses increase to +6.

**At 18th Level:** The bonuses increase to +8.

**At 3rd Level:** The castellan gains a +2 bonus on initiative checks and Knowledge (engineering),
Knowledge (local), Knowledge (nobility), Perception, and Stealth checks when he is in urban terrain,
including fortifications. A castellan in an urban environment can always act in a surprise round,
though he remains [flat-footed](ref/rule/flat-footed) until he acts.

**At 8th Level:** The bonuses increase to +4.

**Replaces:** Cavalier's charge

**Guard Companion**

**Ability:** The castellan forms a bond with an [animal companion](ref/sidekick/animal-companion)
that serves as a guard. While most castellans select birds or canines, the castellan can choose any
animal companions available to [rangers](ref/class/ranger). This ability functions like the
[druid](ref/class/druid) _nature bond_ ability, except that the castellan's effective druid level is
equal to his cavalier level - 3 and his animal companion doesn't gain the _share spells_ special
ability.

**Gained:** At 4th Level

**Replaces:** Expert trainer

;;;ab\{title="Ranger Animal Companions" icon=power next action=Choice\}

- [Antelope](ref/companion/antelope)
- [Armorfish](ref/companion/armorfish)
- [Baboon](ref/companion/baboon)
- [Badger](ref/companion/badger)
- [Bird (Eagle, Hawk, or Owl)](ref/companion/bird)
- [Bustard](ref/companion/bustard)
- [Camel](ref/companion/camel)
- [Capybara](ref/companion/capybara)
- [Cheetah](ref/companion/cat-small-cheetah-leopard)
- [Constrictor Snake](ref/companion/snake-constrictor)
- [Dire Rat](ref/companion/dire-rat)
- [Dog](ref/companion/dog)
- [Elk](ref/companion/elk)
- [Falcon](ref/companion/falcon)
- [Giant Gecko](ref/companion/lizard-giant-gecko)
- [Hobbe Hound](ref/companion/hobbe-hound)
- [Horse](ref/companion/horse)
- [Kangaroo](ref/companion/kangaroo)
- [Leopard](ref/companion/cat-small-cheetah-leopard)
- [Marsupial Devil](ref/companion/marsupial-devil)
- [Pony](ref/companion/pony)
- [Ram](ref/companion/ram)
- [Reef Snake](ref/companion/reef-snake)
- [Reindeer](ref/companion/reindeer)
- [Shark](ref/companion/shark)
- [Spitting Cobra](ref/companion/spitting-cobra)
- [Stag](ref/companion/stag)
- [Stingray](ref/companion/stingray)
- [Swan, Trumpeter](ref/companion/swan-trumpeter)
- [Thylacine](ref/companion/thylacine)
- [Viper](ref/companion/snake-viper)
- [Wolf](ref/companion/wolf)
- [Wolfdog](ref/companion/wolfdog)
- [Yak](ref/companion/yak)
- [Zebra](ref/companion/zebra)

If the campaign takes place wholly or partly in an aquatic environment, you may choose from this
list instead: [Armorfish](ref/companion/armorfish), [Reef Snake](ref/companion/reef-snake),
[Shark](ref/companion/shark), [Stingray](ref/companion/stingray).

;;;

**Mighty Defense**

**Ability:** When the castellan [readies an action](ref/rule/ready) to make a melee attack against a
creature that is not yet adjacent to him, he doubles the threat range of any melee weapons wielded
during the attack. This increase doesn't stack with other effects that increase the threat range of
his weapons. In addition, the cavalier can attempt a free [dirty trick](ref/rule/dirty-trick),
[disarm](ref/rule/disarm), [sunder](ref/rule/sunder), or [trip](ref/rule/trip) combat maneuver if
his readied attack is successful. This free combat maneuver doesn't provoke an attack of
opportunity.

**Gained:** At 11th Level

**Replaces:** Mighty charge

**Defending Challenge**

**Gained:** At 12th Level

**Passive:** The castellan takes no penalty to Armor Class when using his challenge ability.

**Replaces:** Demanding challenge

**Supreme Defense**

**Ability:** Whenever the castellan readies an action to make a melee attack against a creature that
is not yet adjacent to him, his readied attack deals double the normal amount of damage (or triple
the damage if using a [brace](ref/misc/brace) weapon against a charge). In addition, if the cavalier
confirms a critical hit on the readied attack, the target is [stunned](ref/misc/stunned) for 1d4
rounds. A successful Will save (DC = 10 + the cavalier's class level + the cavalier's Strength
modifier) reduces this to being [staggered](ref/misc/staggered) for 1d4 rounds.

**Gained:** At 20th Level

**Replaces:** Supreme charge
