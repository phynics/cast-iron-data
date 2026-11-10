+++
id = "ref/arc-ranger/flamewarden"
kind = "archetype"
title = "Flamewarden"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Flamewarden"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flamewarden", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "72"

[fields]
kind = "archetype"
replaces = ["Hunter's bond", "Evasion", "Camouflage", "Improved evasion", "master hunter"]
alters = ["Spells"]
replaces_features = ["hunter-s-bond", "evasion", "camouflage", "improved-evasion", "master-hunter"]
alters_features = ["spells"]
+++

Emulating the blazing phoenix, flamewardens sweep through the world like a selective forest fire,
burning away corruption, evil, and those who cling to decay.

**Touch of Flame (Su)**

**Flavor:** A flamewarden can cause his weapons to burst into flame.

**At 12th Level:** Weapons affected by this ability gain the
[flaming burst](ref/magic-enh/flaming-burst) special ability instead.

**Gained:** At 4th Level

**Replaces:** Hunter's bond

**Standard:** The ranger can grant a single weapon he holds the [flaming](ref/magic-enh/flaming)
special ability for 1 minute; while under this effect, the weapon counts as magic for the purpose of
overcoming [damage reduction](ref/rule/damage-reduction).

**Usage:** Wisdom3 modifier times/day

**Spells**

**Alters:** Spells

**Info:** A flamewarden can prepare spells from the druid list that have the fire descriptor.

**Stoking the Embers (Sp)**

**Flavor:** A flamewarden can fan the last spark of a recently slain creature's life force back into
a full flame.

**Gained:** At 9th Level

**Replaces:** Evasion

**Standard:** Once per day, a flamewarden can touch the corpse of a creature that has died within 1
round to grant it the effects of [breath of life](ref/spell/breath-of-life).

**Burning Renewal (Su)**

**Ability:** When the flamewarden takes 5 or more points of fire damage, he can remove one of the
following conditions: fatigued, shaken, or sickened. Alternatively, he can remove 1 point of
[ability damage](ref/rule/ability-damage-drain) or drain from an ability score of his choice.

**Ability2:** If the flamewarden takes 10 or more points of fire damage, he can remove one of the
following conditions: exhausted, frightened, or nauseated. Alternatively, he can remove 1d6 points
of ability damage or drain from an ability score of his choice.

**Flavor:** A flamewarden can use the cleansing power of fire to remove afflictions from his body,
mind, and soul.

**Gained:** At 12th Level

**Replaces:** Camouflage

**Special:** The ranger can use this ability only once each time he takes fire damage, regardless of
how much damage it deals over the required amount. If the flamewarden has fire
[resistance](ref/umr/resistance) or [immunity](ref/umr/immunity) to fire, fire damage he would have
otherwise taken still counts toward activating _burning renewal._

**Usage:** Wisdom3 modifier times/day

**Phoenix Rising (Su)**

**At 20th Level:** The flamewarden gains immunity to fire, and once per week, the flamewarden rises
from the ashes of his own destruction 1 round after dying. The flamewarden's body re-forms with all
his equipment, and he returns to life with half his maximum hit points. Any ability scores that were
0 become 1, and nonmagical diseases and poisons are cured. A [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), or [wish](ref/spell/wish) spell cast before he rises from the ashes
prevents him from doing so, as does the area of an [unhallow](ref/spell/unhallow) effect.

**Gained:** At 16th Level

**Passive:** If a flamewarden dies, his body explodes in a conflagration in a 20-foot
[spread](ref/misc/spread). Each hostile creature in the area takes 10d6 points of fire damage unless
it succeeds at a Reflex save (DC = 10 + half the ranger's level + his Constitution modifier) for
half damage. The flames don't harm the flamewarden's allies, who instead are healed 5d6 points of
damage, and any poisons they are currently suffering are neutralized as per
[neutralize poison](ref/spell/neutralize-poison). The flamewarden's body is reduced to ashes by the
explosion.

**Replaces:** Improved evasion, master hunter
