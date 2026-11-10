+++
id = "ref/arc-cavalier/courtly-knight"
kind = "archetype"
title = "Courtly Knight"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Courtly%20Knight"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "courtly_knight", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "24"

[fields]
kind = "archetype"
replaces = ["Tactician", "Greater tactician", "Master tactician"]
replaces_features = ["tactician", "greater-tactician", "master-tactician"]
+++

Some cavaliers strive to be just as effective at the court of a local lord as on the field of
battle. These courtly knights are equally at home in a duel with words or swords.

**Social Presence (Ex)**

**Gained:** At 1st Level

**Passive:** A courtly knight gains a bonus on all Bluff, Diplomacy, Intimidate, and Sense Motive
checks. This bonus is equal to 1 + one-fourth of her cavalier level. A courtly knight starts any
[verbal duel](ref/rule/verbal-duels) with an extra edge she can use for only the _presence_ tactic
unless she is at a significant or extreme disadvantage in the duel.

**Replaces:** Tactician

**Imperious Attitude (Ex)**

**Ability:** In a social setting, the courtly knight can attempt Diplomacy checks to make a request
of a creature whose attitude toward her is unfriendly, provided that creature does not intend to
harm or oppose the courtly knight or her allies in the immediate future. Further, whenever she
attempts a Diplomacy check to make a request, a courtly knight can first attempt an Intimidate check
(DC = 20 + the creature's Charisma modifier). If she succeeds, she gains a +5 bonus on the
subsequent Diplomacy check. Neither aspect of imperious attitude applies if the requested creature
considers itself to be of an equal or higher social rank than the courtly knight, which includes
creatures that don't understand or value the concept of social ranks.

**Flavor:** A courtly knight develops a commanding demeanor, and the strength of her conviction is
often enough to get others to do as she asks, merely because she expects it to be done.

**Gained:** At 9th Level

**Replaces:** Greater tactician

**Grand Boast (Ex)**

**Ability:** Whenever a courtly knight uses her _challenge_ class feature against an opponent who is
at full health and under no negative afflictions, conditions, spells, or other effects, she can make
a grand boast, declaring that she can defeat her foe with ease. She does not gain the benefits of
her _challenge_ (including any additional benefits granted by her _order_) when making a grand
boast. If she successfully defeats the target of her _challenge_ within 1 minute, however, she is
vindicated in her boast and gains the benefits of her _challenge_ against all allies of the defeated
enemy who witnessed her grand boast and who are of the same or lower CR as the defeated enemy.

**Gained:** At 17th Level

**Replaces:** Master tactician

**Special:** If any of the courtly knight's allies attack the initial target of the _challenge_ or
assist the courtly knight after the boast, this ability has no effect.
