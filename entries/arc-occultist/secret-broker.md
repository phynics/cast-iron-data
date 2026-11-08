+++
id = "ref/arc-occultist/secret-broker"
kind = "archetype"
title = "Secret Broker"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "secret_broker", path = "json/archetypes_occultist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/occultist" },
]

[fields]
kind = "archetype"
replaces = ["Magic item skill", "Shift focus", "Magic circles", "Binding circles", "Fast circles"]
alters = ["Implements", "implement mastery"]
+++

**Sources:** Ultimate Intrigue pg 68\
Whether as spymasters, extortionists, political fixers, or puppet masters, secret brokers use their
talents with objects to gain information, then leverage that information for their own purposes.

**Gained class skills:** bluff, kd, kg, kl, kna, kno

**Knowledge Is Power**

**Ability:** A secret broker's _third eye_ resonant power grants an insight bonus on Profession and
Sense Motive checks equal to the bonus it grants on Perception checks, and an insight bonus on all
Knowledge checks equal to half that bonus.

**Alters:** Implements, implement mastery

**Info:** The secret broker starts play possessing a single [divination](ref/implement/divination)
implement, typically a ledger of secrets. She gains new implements as normal at 2nd level and every
4 levels thereafter, and they can be of any school.

**Special:** She must select divination with _implement mastery._

**Broker Secrets (Su)**

**Ability:** A secret broker can trade her secrets to another. For the purpose of this ability, an
object's secret is composed of pieces of information gained from a single object through _object
reading, object seer, psychometry,_ or _read object_ that the occultist didn't otherwise know and
hasn't shared with another, written somewhere, or otherwise recorded or found a way to recover
should she forget them and lose possession of the object. The secret broker can willingly use this
ability in tandem with handing the object over to another creature in order to transfer the object's
secret to that creature. The secret broker forgets the object's secret and the creature instantly
learns the object's secret.

**Gained:** At 2nd Level

**Replaces:** Magic item skill

**Special:** The secret broker can also destroy an object to remove his memory of the object's
secret without transferring it to another. In either case, any onlookers who understand what the
secret broker is doing, and the recipient in the case of a transfer, can intrinsically tell that the
secret broker has used this ability rather than simply sharing the memory through other means or
destroying the object but keeping its secret.

**Share Memory (Sp)**

**Ability:** A secret broker learns to use her knowledge transference powers more flexibly, allowing
her to use [share memory](ref/spell/share-memory) at will, but only with willing targets.

**Gained:** At 4th Level

**Replaces:** Shift focus

**Steal Secret (Sp)**

**Ability:** A secret broker learns how to steal a secret from an unwilling target. This works as
her _[share memory](ref/spell/share-memory)_ ability, except it allows her to access memories from
unwilling targets. A target that succeeds at its saving throw against a secret broker's _steal
secret_ ability is forever after immune to that secret broker's _steal secret_ ability.

**Gained:** At 8th Level

**Replaces:** Magic circles

**Erase Secret (Sp)**

**Ability:** A secret broker can expend 1 point of mental focus from her divination implement in
order to erase a fact from someone's mind by touch. This works similarly to
[modify memory](ref/spell/modify-memory) to erase the memory of an event, except the effect is
instantaneous and leaves no magical trace (it can still be removed by
[break enchantment](ref/spell/break-enchantment), [psychic surgery](ref/spell/psychic-surgery),
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle), or [wish](ref/spell/wish)) and
the secret broker can remove only one fact, such as &quot&The queen and the general are having an
affair&quot& rather than a 5-minute event. Erasing the memory of a fact does not prevent the target
from learning the fact again, or even potentially from deducing the fact again from evidence, given
time.

**Gained:** At 12th Level

**Replaces:** Binding circles

**Purge Secret (Sp)**

**Ability:** A secret broker can expend 3 points of mental focus from her divination implement to
apply her _erase secret_ ability to up to one creature per level within 30 feet of her.

**Gained:** At 16th Level

**Replaces:** Fast circles
