+++
id = "ref/arc-occultist/esoteric-initiate"
kind = "archetype"
title = "Esoteric Initiate"
source_ids = ["disciples-doctrine"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "esoteric_initiate", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]
[[sources]]
publication = "disciples-doctrine"
page = "8"

[fields]
kind = "archetype"
replaces = ["Aura sight"]
alters = ["Mental focus", "implements", "shift focus"]
replaces_features = ["aura-sight"]
alters_features = ["mental-focus", "implements", "shift-focus"]
+++

While most occultists learn to draw power from a variety of implements and objects, esoteric
initiates have focused their study entirely on items of antiquity connected to the teachings of the
Esoteric Order of the Palatine Eye, believing such items to be more powerful than mundane items.

**Implements of the Palatine Eye (Su)**

**Ability:** An esoteric initiate has formed a supernatural bond with a set of the order's writings
collected into a book. If the book is damaged, it is restored to full hit points when the initiate's
mental focus refreshes. If the book is lost or destroyed, the initiate can replace it with another
similar one, but doing so requires an 8-hour ritual that binds the new book to him.

**Alters:** Mental focus, implements, shift focus

**At 4th Level:** When using the ability to shift his mental focus from one implement to another, he
loses no focus when doing so.

**Info:** The book serves as an implement for any two schools of magic at 1st level. The initiate
gains new implement schools normally. However, the initiate's additional implements must be
masterwork or magic items worth at least 50 gp, and they must directly or nominally represent the
Esoteric Order of the Palatine Eye's beliefs or history. For example, the initiate's implements
could be Osirian antiques, trinkets covered in Palatine iconography, or the like.

**Passive:** When the initiate benefits from his implements' resonant powers, he treats his
occultist level as 1 higher for the purpose of determining the powers' benefits only.

**Special:** An esoteric initiate can't save generic mental focus inside his own body instead of
investing all of it.

**Symbolism (Sp)**

**Ability:** An initiate who spends 1 minute carefully studying any written work can understand its
gist even if he doesn't speak the language in which the text is written. A number of times per day
equal to the initiate's occultist level, the initiate can cast
[comprehend languages](ref/spell/comprehend-languages) as a
[spell-like ability](ref/umr/spell-like-abilities) to read a written work, using his occultist level
as his caster level. If he uses _symbolism_ to read a portion of the work that contains a hidden
message or a cypher, he is automatically granted a Linguistics check with a bonus equal to his
occultist level to decipher the message.

**Gained:** At 5th Level

**Replaces:** Aura sight
