"""
Black Pepper Cultivation Guide Data & Definitions
Comprehensive, ICAR-IISR and agricultural university aligned datasets covering:
- 23 Main Cultivation Chapters (with mistakes to avoid & learning resources)
- 7 Cultivation Methods (with step-by-step procedures & verified YouTube tutorials)
- 6 Scientific Propagation Protocols
- Dedicated Fertilizer & Irrigation Guide
- Dedicated Pest, Disease & Deficiency Management Profiles
- Detailed Harvesting & Post-Harvest Processing Protocols
- Curated Video Learning Library
"""

# ======================================================================================
# 1. 23 COMPLETE CULTIVATION CHAPTERS
# ======================================================================================
CULTIVATION_CHAPTERS_DATA = [
    {
        "id": 1,
        "title": "Introduction to Black Pepper",
        "category": "Botany & Overview",
        "summary": "Botanical heritage, global economic importance, and biological classification of the King of Spices.",
        "image": "assets/images/hero_plantation.jpg",
        "caption": "Black Pepper (Piper nigrum L.) Commercial Plantation Canopy",
        "explanation": """
Black pepper (*Piper nigrum* L.), belonging to the family **Piperaceae**, is a perennial woody evergreen climbing vine native to the tropical evergreen rainforests of the Western Ghats of South India. Historically revered as **'Black Gold'** and crowned the **'King of Spices'**, black pepper is the most extensively traded spice in the world.

The pungency of black pepper is primarily attributed to the crystalline alkaloid **piperine** (3% to 8%), while its warm, resinous aroma derives from volatile essential oils (1% to 3.5%) comprising beta-caryophyllene, pinene, and limonene. Black pepper vines have an economic lifespan of 25 to 30 years under scientific plantation management.
        """,
        "important_points": [
            "Perennial woody climbing vine originating in the Western Ghats biodiversity hotspot.",
            "Pungency is determined by the piperine alkaloid; volatile essential oils provide characteristic aroma.",
            "Bears single-seeded spherical drupes (berries) arranged on drooping catkin spikes.",
            "Major global producers include Vietnam, India, Indonesia, Brazil, Sri Lanka, and Malaysia."
        ],
        "farming_recommendations": [
            "Establish plantations in regions with year-round warmth and high relative humidity.",
            "Plant certified high-yielding cultivars to ensure commercial productivity for 20+ years.",
            "Maintain soil organic carbon above 2.5% through regular organic mulching."
        ],
        "mistakes_to_avoid": [
            "Planting uncertified local cuttings of unknown lineage that carry latent viral or fungal diseases.",
            "Establishing vineyards on poorly drained soils prone to water stagnation.",
            "Ignoring windbreaks in regions subject to cyclonic summer winds."
        ],
        "learning_resources": [
            "ICAR-Indian Institute of Spices Research (IISR) Black Pepper Production Guidelines",
            "Spices Board of India Good Agricultural Practices (GAP) for Spices",
            "FAO Crop Guide: Piper nigrum Agronomy"
        ],
        "tips": "Conduct soil health tests before site clearance to confirm native microbial biomass and pH levels.",
        "related": ["Botanical Characteristics", "Climate Requirements", "Selection of Varieties"]
    },
    {
        "id": 2,
        "title": "Botanical Characteristics",
        "category": "Botany & Overview",
        "summary": "Dimorphic branching architecture, root systems, leaf anatomy, and catkin inflorescence structure.",
        "image": "assets/images/guide/botany_pepper.jpg",
        "caption": "Anatomy of Plagiotropic Fruiting Laterals and Drooping Spikes",
        "explanation": """
Understanding the vegetative and reproductive morphology of black pepper is essential for correct pruning, training, and propagation.

#### 1. Stem and Branch Dimorphism:
- **Orthotropic Shoots (Main Stems):** Upward-climbing monopodial stems that produce adventitious clinging roots at nodes to adhere to support standards.
- **Plagiotropic Branches (Fruiting Laterals):** Horizontally growing branches that emerge from leaf axils of climbing stems. These lateral branches produce all flower spikes and berries. *Note: Cuttings taken from plagiotropic branches produce non-climbing Bush Pepper.*
- **Runner Shoots:** Basal vegetative shoots emerging from the vine collar that trail along the ground. These runner shoots are the primary material used for mass vegetative multiplication.

#### 2. Root Architecture:
Consists of 3 to 5 deep anchor taproots penetrating 1 to 2 meters, and a dense superficial feeder root system concentrated within the top 30 to 40 cm of soil.

#### 3. Inflorescence:
Drooping spikes (catkins) 8 to 15 cm in length, carrying 50 to 120 sessile flowers. Flowers are mostly hermaphrodite (bisexual) in commercial cultivars.
        """,
        "important_points": [
            "Distinct dimorphism: Climbing orthotropic shoots vs fruiting lateral plagiotropics.",
            "Surface feeder root net is located in the top 30-40 cm and is highly vulnerable to physical tillage.",
            "Runner shoots from the vine base are the scientific standard for nursery multiplication."
        ],
        "farming_recommendations": [
            "Never dig or till deeply within 1 meter radius of the vine collar to avoid severing feeder roots.",
            "Prune non-productive hanging orthotropic shoots to concentrate sap flow into fruiting laterals.",
            "Tie young climbing stems to standards using biodegradable banana fiber or coir yarn."
        ],
        "mistakes_to_avoid": [
            "Using wire or plastic twine for tying vines, which strangles stem vascular cambium.",
            "Using fruiting lateral branches for field climbing propagation instead of runner shoots.",
            "Damaging adventitious climbing rootlets during standard weeding."
        ],
        "learning_resources": [
            "ICAR-IISR Morphology Manual: Vegetative Architecture of Black Pepper",
            "Kerala Agricultural University Horticultural Botany Handbooks"
        ],
        "tips": "Bush pepper plants can be generated by rooting plagiotropic lateral cuttings with 3–4 leaves.",
        "related": ["Introduction to Black Pepper", "Propagation Methods", "Pruning & Training"]
    },
    {
        "id": 3,
        "title": "Climate Requirements",
        "category": "Agro-Climatic Needs",
        "summary": "Temperature thresholds, annual rainfall distribution, altitude, and relative humidity tolerances.",
        "image": "assets/images/methods/traditional.jpg",
        "caption": "Humid Tropical Micro-Climate (20–32°C) with High Ambient Humidity",
        "explanation": """
Black pepper is a plant of the humid tropics requiring heavy rainfall, high relative humidity, and warm equable temperatures.

#### 1. Temperature:
- **Optimal Range:** 23°C to 32°C.
- **Critical Minimum:** 10°C (temperatures below 12°C arrest spike emergence and fruit setting).
- **Critical Maximum:** 40°C (requires dense shade management above 35°C to avoid leaf scorching).

#### 2. Rainfall:
- **Total Requirement:** 1,500 to 3,000 mm distributed across 8 to 9 months.
- **Dry Period Requirement:** A brief dry spell of 40 to 60 days during dry winter/spring months is essential to trigger physiological floral bud differentiation.
- **Blossom Showers:** 70–100 mm of pre-monsoon showers in May–June initiates synchronized spike emergence.

#### 3. Altitude & Humidity:
- Grown successfully from sea level up to 1,500 meters Mean Sea Level (MSL). Optimal yields occur between 300 and 900 m MSL.
- Relative humidity must remain between 75% and 90% during flowering and berry set.
        """,
        "important_points": [
            "Requires 1,500–3,000 mm rainfall with an essential 40–60 day winter dry resting period.",
            "Warm temperatures (23–32°C) and high humidity (75–90%) promote uniform pollination.",
            "Drought during flowering causes heavy catkin spike shedding (blossom drop)."
        ],
        "farming_recommendations": [
            "Provide micro-sprinkler or drip irrigation during prolonged dry spells after floral initiation.",
            "Regulate support tree overhead shade before monsoon showers to optimize light interception (50–60% sunlight).",
            "Plant windbreaks on western and southern plantation borders in windy elevation belts."
        ],
        "mistakes_to_avoid": [
            "Continuous heavy irrigation during winter, which inhibits floral bud initiation.",
            "Establishing plantations in frosty valleys where night temperatures drop below 10°C.",
            "Over-thinning overhead tree canopy before hot dry pre-monsoon months."
        ],
        "learning_resources": [
            "ICAR Agro-Climatology Zone Maps for Spices Cultivation",
            "Indian Meteorological Department Agro-Advisory Bulletin for Plantation Crops"
        ],
        "tips": "A blossom shower of 70 mm in May followed by 10 days of intermittent sunshine gives the heaviest fruit set.",
        "related": ["Soil Requirements", "Shade Management", "Irrigation Management"]
    },
    {
        "id": 4,
        "title": "Soil Requirements",
        "category": "Agro-Climatic Needs",
        "summary": "Soil textures, pH range, organic carbon benchmarks, drainage parameters, and soil health indicators.",
        "image": "assets/images/guide/soil_prep.jpg",
        "caption": "Deep Red Laterite Soil with High Organic Matter",
        "explanation": """
Black pepper thrives best in virgin forest soils rich in humus and organic matter.

#### 1. Soil Texture & Depth:
- **Preferred Types:** Deep, well-drained red laterite, clay loam, and rich alluvial forest soils.
- **Soil Depth:** Minimum effective rooting depth of 1 meter with permeable subsoil.
- **Unsuitable Soils:** Heavy sticky clays with poor percolation, shallow gravelly soils with hard pan within 50 cm, and coastal saline sands.

#### 2. Soil Reaction (pH):
- **Optimal Range:** pH 5.5 to 6.5 (mildly acidic).
- Highly acidic soils (pH < 5.0) fix phosphorus and induce aluminum toxicity; alkaline soils (pH > 7.5) induce iron and zinc chlorosis.

#### 3. Drainage & Aeration:
Feeder roots demand high oxygen tension. Waterlogging for even 48 hours asphyxiates root hairs and triggers catastrophic *Phytophthora* zoospore infection.
        """,
        "important_points": [
            "Deep, friable, well-drained soils with pH 5.5 to 6.5 are ideal.",
            "Soil organic carbon should ideally exceed 2.0% to support beneficial antagonistic microflora.",
            "Zero tolerance for stagnant water or poorly drained clay subsoils."
        ],
        "farming_recommendations": [
            "Apply agricultural lime or dolomite at 500 g/standard every two years in acidic soils (pH < 5.5).",
            "Incorporate 10 kg well-rotted farmyard manure (FYM) or 5 kg vermicompost per vine pit at planting.",
            "Build raised planting mounds (15–20 cm high) on flat terrain to guarantee root aeration."
        ],
        "mistakes_to_avoid": [
            "Planting in waterlogged depressions or flood-prone riverbanks.",
            "Applying uncomposted raw poultry manure directly in planting pits, which burns tender feeder roots.",
            "Over-liming soils, which ties up available boron and micronutrients."
        ],
        "learning_resources": [
            "IISR Soil Health Card & Nutrient Management Guidelines",
            "National Bureau of Soil Survey and Land Use Planning (NBSS&LUP) Plantation Soil Atlas"
        ],
        "tips": "Incorporate *Trichoderma harzianum* enriched compost into planting pits to build a biological protective shield.",
        "related": ["Land Preparation", "Manure and Fertilizer Management", "Foot Rot Management"]
    },
    {
        "id": 5,
        "title": "Land Preparation",
        "category": "Establishment",
        "summary": "Clearing, contour terrace layout, pit excavation dimensions, solarization, and basal pit amendment.",
        "image": "assets/images/guide/planting_spacing.jpg",
        "caption": "Contour Terracing and Planting Pit Alignment on Hill Slopes",
        "explanation": """
Proper land preparation ensures optimal moisture conservation, prevents topsoil erosion, and provides an aerated foundation for 25+ years of vine growth.

#### 1. Slope Management & Terracing:
- On slopes exceeding 15%, construct contour terraces (1 to 1.5 m wide) along natural elevation contours.
- Plant vetiver grass (*Chrysopogon zizanioides*) along terrace risers to arrest soil wash.

#### 2. Pit Dimensions & Spacing:
- Dig planting pits measuring **50 cm × 50 cm × 50 cm** on the northern or eastern side of each standard tree.
- Maintain spacing of **3 m × 3 m** in pure plantations (1,110 vines/ha), or **2.7 m × 2.7 m** on fertile valley soils.

#### 3. Solarization & Pit Filling:
- Dig pits in March–April and allow 3 to 4 weeks of sun baking (solarization) to eradicate soil-borne pathogens.
- Refill pits with topsoil mixed with 10 kg farmyard manure, 1 kg neem cake, 150 g rock phosphate, and 50 g *Trichoderma* enriched compost.
        """,
        "important_points": [
            "Dig pits 50x50x50 cm on the North or North-East face of support trees.",
            "Allow pits to bake in strong summer sun for 3 weeks prior to refilling.",
            "Incorporate neem cake and rock phosphate into the topsoil refilling mixture."
        ],
        "farming_recommendations": [
            "Construct drainage trenches (30 cm deep) between terrace rows on sloping land.",
            "Position pits 30 cm away from the base of the support tree trunk to prevent root crowding.",
            "Create a 10 cm raised crown above ground level to account for monsoon soil settling."
        ],
        "mistakes_to_avoid": [
            "Digging planting pits on the South or West side of trees where scorching afternoon sun damages young vines.",
            "Refilling pits with inert subsoil instead of nutrient-rich topsoil.",
            "Leaving pits flush with ground level, which creates water pools during monsoon downpours."
        ],
        "learning_resources": [
            "ICAR-IISR Package of Practices: Plantation Layout and Soil Conservation",
            "Soil and Water Conservation Department Technical Bulletins"
        ],
        "tips": "Mix 1 kg of crushed neem cake into every pit; the triterpenoids repel plant-parasitic nematodes for 12 months.",
        "related": ["Planting Methods", "Support Tree Management", "Manure and Fertilizer Management"]
    },
    {
        "id": 6,
        "title": "Selection of Varieties",
        "category": "Establishment",
        "summary": "High-yielding cultivars, disease-resistant hybrids, high-altitude selections, and region-specific varieties.",
        "image": "assets/images/guide/berry_ripening.jpg",
        "caption": "Panniyur-1 High Yielding Variety with Long Drooping Spikes",
        "explanation": """
Selecting the correct black pepper variety tailored to your agro-climatic zone and altitude is the most crucial economic decision of plantation establishment.

#### 1. Premier High-Yielding Hybrids:
- **Panniyur-1:** First global hybrid (Uthirankotta × Cheriyakaniakkadan). Long spikes (up to 20 cm), high berry setting, vigorous climber. Requires open sunlight with light overhead shade. Yield: 1,200–2,000 kg dry pepper/ha.
- **Panniyur-2:** Semi-shade tolerant selection suitable for intercropping under coconut and arecanut.
- **Panniyur-3:** Suited for higher elevations; bold berries with high piperine content (5.3%).
- **Panniyur-5:** Highly shade-tolerant cultivar bred for dense multi-strata coffee and arecanut plantations.

#### 2. Disease-Tolerant Varieties:
- **IISR Thevam:** Resistant to *Phytophthora* foot rot and tolerant to drought. Recommended for undulating slopes.
- **IISR Shakthi:** High yielding and field-tolerant to *Phytophthora* foot rot. Excellent for high-rainfall belts.
- **IISR Girimunda:** High-altitude variety yielding bold berries (bulk density > 600 g/L).

#### 3. Traditional Landraces:
- **Karimunda:** Most popular farmer landrace in Kerala. Highly reliable, regular bearer, drought-hardy.
- **Kottanadan:** Highest quality black pepper with maximum piperine (7–8%) and essential oil content.
        """,
        "important_points": [
            "Panniyur-1 is the highest yielder in open sunlight; Panniyur-5 is best under dense shade.",
            "IISR Thevam and IISR Shakthi offer genetic tolerance against Phytophthora foot rot.",
            "Karimunda is the most dependable traditional cultivar across variable rainfall conditions."
        ],
        "farming_recommendations": [
            "Plant a mix of 2–3 compatible cultivars in the plantation to improve cross-pollination and hedge against disease.",
            "Source certified rooted cuttings exclusively from ICAR-IISR, state agricultural universities, or accredited nurseries.",
            "Choose IISR Thevam if your region has a known history of foot rot or soil-borne pathogens."
        ],
        "mistakes_to_avoid": [
            "Planting Panniyur-1 under dense shade where it becomes vegetative and fails to set fruit.",
            "Buying cheap uncertified cuttings from unregulated roadside vendors.",
            "Mono-cropping a single clone across hundreds of acres without pathogen buffers."
        ],
        "learning_resources": [
            "ICAR-IISR Catalog of Improved Black Pepper Varieties",
            "Spices Board Variety Recommendation Manual by Agro-Climatic Zone"
        ],
        "tips": "For arecanut or coconut intercropping, always choose Panniyur-5 or IISR Thevam for maximum shade tolerance.",
        "related": ["Selection of Planting Materials", "Propagation Methods", "Foot Rot Management"]
    },
    {
        "id": 7,
        "title": "Selection of Planting Materials",
        "category": "Establishment",
        "summary": "Mother vine certification, genetic purity criteria, quarantine standards, and disease-free indexing.",
        "image": "assets/images/propagation/runner_shoot.jpg",
        "caption": "Selecting Vigorously Trailing Runner Shoots from High-Yielding Mother Vines",
        "explanation": """
The commercial longevity and yield of a pepper vineyard depends entirely on the health, vigor, and genetic purity of the original planting material.

#### 1. Criteria for Selecting Mother Vines:
- **Age:** 5 to 12 years old in active, peak commercial bearing stage.
- **Yield History:** Proven sustained yield of at least 2 to 3 kg dry black pepper per vine per year over 3 consecutive seasons.
- **Health Certification:** Zero symptoms of *Phytophthora* foot rot, stunt virus, cucumber mosaic virus (CMV), or root-knot nematodes.
- **Morphology:** Long spikes (> 12 cm), fully packed with berries (no barren 'running' spikes), dark green leathery foliage.

#### 2. Mother Vine Management:
- Tag selected mother vines with weather-proof labels in October during peak harvest inspection.
- In February–March, untie and elevate runner shoots onto bamboo stakes to keep them off damp soil until cutting collection.
        """,
        "important_points": [
            "Mother vines must have a documented 3-year track record of high commercial yield.",
            "Never harvest cuttings from vines showing foliar yellowing, vein clearing, or stunted leaves.",
            "Elevate runner shoots on stakes prior to cutting to prevent contact with soil-borne fungi."
        ],
        "farming_recommendations": [
            "Index mother plants annually for viral infections using ELISA or PCR diagnostics where available.",
            "Apply prophylactic drenching of Trichoderma around mother vine basins 30 days before taking cuttings.",
            "Discard any cuttings showing internal brown vascular discoloration upon cross-section slicing."
        ],
        "mistakes_to_avoid": [
            "Collecting runner shoots that have rooted into damp orchard soil; they often carry latent nematodes.",
            "Harvesting cuttings from old decaying vines older than 18 years.",
            "Failing to sterilize pruning shears between mother vine harvests."
        ],
        "learning_resources": [
            "ICAR-IISR Technical Bulletin No. 24: Nursery Standards for Quality Spice Planting Material",
            "National Horticulture Board (NHB) Accreditation Guidelines for Spices Nurseries"
        ],
        "tips": "Dip pruning shears in 70% isopropyl alcohol or 10% sodium hypochlorite between mother vines to stop virus transfer.",
        "related": ["Selection of Varieties", "Propagation Methods", "Nursery Management"]
    },
    {
        "id": 8,
        "title": "Propagation Methods",
        "category": "Nursery & Propagation",
        "summary": "Runner shoots, terminal cuttings, serpentine layering, bamboo split method, and rapid multiplication.",
        "image": "assets/images/methods/serpentine.jpg",
        "caption": "Serpentine Layering and Bamboo Split Rapid Propagation Protocols",
        "explanation": """
Black pepper is propagated primarily through vegetative cuttings to preserve genetic uniformity and high yield characteristics.

#### 1. Traditional Runner Shoot Cuttings:
- Runner shoots trailing at the vine base are collected in February–March.
- Cut into 2 to 3 node segments with a sharp grafting knife; discard terminal tender tips and woody basal segments.

#### 2. IISR Rapid Multiplication (Bamboo Split) Method:
- A high-efficiency method yielding 30 to 40 rooted saplings per mother vine annually.
- Split bamboo poles (2.5 m long) are filled with sterile rooting substrate (coir pith, vermicompost, sand).
- A rooted vine cutting is trained up the inclined bamboo. As the vine grows, every node roots into the substrate.
- Shoots are harvested every 45 days by cutting between nodes, yielding ready-rooted single-node plants.

#### 3. Serpentine Layering Method:
- Potted mother vines are trained horizontally over a row of polybags arranged on the nursery floor.
- Each vine node is pegged into an individual polybag using wire clips. Nodes root within 20 days and are severed into independent plants.
        """,
        "important_points": [
            "Vegetative propagation preserves high piperine content and true-to-type characteristics.",
            "IISR Rapid Multiplication produces 10 times more planting material than conventional ground cuttings.",
            "Single-node cuttings with an intact leaf blade root with > 90% success under intermittent mist."
        ],
        "farming_recommendations": [
            "Treat cutting bases with Indole-3-Butyric Acid (IBA 500–1000 ppm) talc powder to accelerate root initiation.",
            "Maintain 85% relative humidity and 28°C under 50% green agro-shade netting.",
            "Provide light misting 4 to 6 times daily during rooting."
        ],
        "mistakes_to_avoid": [
            "Using inverted cuttings (planting upside down); check leaf axil bud direction before insertion.",
            "Allowing cuttings to dry out or wilt during the cutting preparation process.",
            "Exposing fresh unrooted cuttings to direct, unshaded afternoon sunlight."
        ],
        "learning_resources": [
            "ICAR-IISR Rapid Multiplication Technique: Video Tutorial and Illustrated Guide",
            "Horticultural Propagation Protocols for Tropical Spices"
        ],
        "tips": "Always keep cuttings in a bucket of clean water containing 0.1% Carbendazim while preparing batches.",
        "related": ["Nursery Management", "Selection of Planting Materials", "Planting Methods"]
    },
    {
        "id": 9,
        "title": "Nursery Management",
        "category": "Nursery & Propagation",
        "summary": "Potting substrates, solarization, shade-house management, hardening protocols, and bio-priming.",
        "image": "assets/images/propagation/polybag.jpg",
        "caption": "Polybag Nursery with 50% Shade Netting and Mist Lines",
        "explanation": """
High-grade nursery management produces vigorous, pathogen-free rootstocks that guarantee 95%+ field establishment.

#### 1. Polybag Sizing & Potting Mixture:
- **Bags:** Heavy-duty black UV-stabilized polythene bags (20 cm × 10 cm, 200 gauge) with 4 punched drainage holes at the base.
- **Sterile Potting Substrate:** 2 parts virgin forest topsoil + 1 part coarse washed river sand + 1 part decomposed coir pith or vermicompost.
- **Bio-enrichment:** Incorporate 5 kg *Trichoderma harzianum* + 5 kg *Pseudomonas fluorescens* + 10 kg rock phosphate per metric ton of potting mixture.

#### 2. Nursery Hygiene & Sanitation:
- Solarize sand and soil under 100-gauge transparent polythene sheets for 3 weeks in the hot sun to destroy weed seeds, soil fungi, and nematode cysts.
- Elevate polybags on raised gravel benches or wire mesh stands 15 cm above the ground to prevent root contact with native soil.

#### 3. Hardening Off Phase:
- Keep fresh cuttings under 75% shade for the first 30 days.
- Shift to 50% shade for days 31–60, and 25% light shade for 15 days prior to field delivery to acclimatize foliage to full sun.
        """,
        "important_points": [
            "Sterilized, bio-enriched potting mix prevents damping-off and root-knot nematodes.",
            "Bags must be raised off the soil floor on benches or plastic gravel sheets.",
            "Gradual light hardening over 60–90 days is mandatory for field survival."
        ],
        "farming_recommendations": [
            "Drench nursery bags with Copper Oxychloride (0.2%) or Metalaxyl-Mancozeb (0.125%) at the first sign of leaf spot.",
            "Apply 0.5% 19-19-19 water-soluble foliar spray at 20-day intervals once adventitious roots establish.",
            "Prune any climbing roots growing into adjacent bags to prevent root ball disturbance."
        ],
        "mistakes_to_avoid": [
            "Placing polybags directly on bare muddy ground where soil pathogens invade drainage holes.",
            "Over-watering nursery beds, which produces pale, waterlogged, root-rotted saplings.",
            "Transporting fresh unhardened nursery plants directly into harsh field sunlight."
        ],
        "learning_resources": [
            "National Spices Nursery Accreditation Manual (NHB & Spices Board)",
            "Commercial Nursery Operations for Tropical Spices"
        ],
        "tips": "Incorporate crushed neem cake (50 g/bag) to guarantee complete protection against burrowing nematodes.",
        "related": ["Propagation Methods", "Planting Methods", "Foot Rot Management"]
    },
    {
        "id": 10,
        "title": "Planting Methods",
        "category": "Establishment",
        "summary": "Monsoon timing, planting depth, root ball handling, vine orientation, and initial staking.",
        "image": "assets/images/propagation/transplanting.jpg",
        "caption": "Field Transplanting of Rooted Polybag Saplings Beside Standard Tree",
        "explanation": """
Correct field planting sets the biological foundation for vine longevity and high commercial production.

#### 1. Planting Season:
- The ideal time is during the onset of regular monsoon downpours (**June–July** for the South-West monsoon in India).
- In areas with North-East monsoon rains (Tamil Nadu, parts of Karnataka), planting can extend into **October–November**.

#### 2. Transplanting Procedure:
- Open a small central cavity in the refilled pit, roughly 30 cm away from the support tree trunk on its Northern or North-Eastern face.
- Slit the polybag vertically with a sharp blade; peel away plastic without disturbing or crumbling the root ball.
- Position **2 to 3 rooted saplings** per standard tree into the cavity, slanting the shoots at a 45° angle towards the tree trunk.
- Press topsoil firmly around the root collar to eliminate air pockets, creating a slight raised mound to shed excess rainwater.
- Tie the climbing stems loosely to the standard trunk using soft banana pseudo-stem fiber or coir string at 30 cm intervals.
        """,
        "important_points": [
            "Plant 2 to 3 vigorous saplings per standard tree for uniform vine coverage.",
            "Always position planting pits on the North or North-East face to protect young stems from sun-scald.",
            "Form a raised soil mound around the plant base to shed surface runoff."
        ],
        "farming_recommendations": [
            "Mulch the vine basin immediately with 5–10 cm of dry forest leaves or coir pith.",
            "Provide temporary shade using coconut fronds or bamboo screens if sunny breaks occur post-transplanting.",
            "Inspect weekly and retie growing vine tips as they climb."
        ],
        "mistakes_to_avoid": [
            "Burying the sapling deeper than its original polybag collar mark, which causes collar rot.",
            "Using nylon or synthetic wire to tie vines; it cuts into expanding stem tissues.",
            "Planting during heavy continuous rainstorms when water fills planting cavities."
        ],
        "learning_resources": [
            "ICAR-IISR Field Establishment Protocols for Black Pepper",
            "University of Agricultural Sciences (UAS) Dharwad Spices Cultivation Guide"
        ],
        "tips": "Keep vine ties loose with a figure-eight loop so the climbing stem has room to expand without strangulation.",
        "related": ["Support Tree Management", "Shade Management", "Manure and Fertilizer Management"]
    },
    {
        "id": 11,
        "title": "Support Tree Management",
        "category": "Canopy & Standards",
        "summary": "Living standards (Garuga, Erythrina, Silver Oak), non-living concrete pillars, spacing, and tree maintenance.",
        "image": "assets/images/methods/support_tree.jpg",
        "caption": "Pepper Vines Climbing Regulated Live Standards (Erythrina indica)",
        "explanation": """
As a woody climbing vine, black pepper requires sturdy physical support (standards) to reach its full productive potential of 6 to 8 meters.

#### 1. Living Standards (Support Trees):
- **Erythrina indica (Indian Coral Tree / Murukku):** Most widely used live standard in India. Fixes nitrogen, develops rough bark for easy climbing root grip, and coppices readily under annual lopping.
- **Garuga pinnata:** Long-lived, non-competitive root system, tolerant to heavy pruning.
- **Grevillea robusta (Silver Oak):** Preferred in high-altitude coffee and tea estates (600–1,200 m). Straight trunk, excellent timber value, non-spreading crown.
- **Areca catechu (Arecanut Palm):** High-density vertical support in coastal agroforestry.
- **Cocos nucifera (Coconut Palm):** Ideal companion standard in mixed tropical gardens.

#### 2. Non-Living Standards:
- Reinforced Cement Concrete (RCC) pillars, granite stone pillars, or treated timber poles.
- Eliminates underground root competition for water and fertilizers, but requires artificial shading and higher initial capital investment.
        """,
        "important_points": [
            "Erythrina indica is the premier nitrogen-fixing living standard for South India.",
            "Standards must have rough, non-peeling bark to allow adventitious roots to anchor securely.",
            "Live support trees must be planted 1 year before pepper vines to establish sturdy trunks."
        ],
        "farming_recommendations": [
            "Plant living standard cuttings (2 m long, 5 cm diameter) in May–June, one full year prior to vine transplanting.",
            "Maintain standard tree height at 6 to 7 meters to facilitate safe ladder harvesting.",
            "Ring-de-bark or girdle standard branches if they grow too thick and shade the vine excessively."
        ],
        "mistakes_to_avoid": [
            "Using support trees with peeling, slippery bark (such as Eucalyptus), which prevents vine climbing.",
            "Allowing living support trees to grow unpruned into massive forest canopies that starve vines of light.",
            "Planting pepper vines onto thin, weak saplings that collapse under heavy crop weight."
        ],
        "learning_resources": [
            "Agroforestry Standards for Spices Cultivation: IISR Technical Bulletin",
            "World Agroforestry Centre (ICRAF) Silvicultural Management of Support Trees"
        ],
        "tips": "Silver Oak (*Grevillea robusta*) standards can yield valuable timber after 25 years of pepper vine production.",
        "related": ["Shade Management", "Planting Methods", "Different Black Pepper Cultivation Methods"]
    },
    {
        "id": 12,
        "title": "Shade Management",
        "category": "Canopy & Standards",
        "summary": "Canopy lopping schedule, seasonal light penetration regulation, solar radiation balance, and sun-scald prevention.",
        "image": "assets/images/methods/intercropping_estate.jpg",
        "caption": "Balanced Sunlight and Filtered Shade in Regulated Canopy",
        "explanation": """
Black pepper thrives best under **50% to 60% filtered sunlight**. Excessive shade suppresses flower bud differentiation and promotes fungal foliar rot; excessive exposure causes leaf scorching and vine dieback.

#### 1. Annual Lopping Schedule:
- **First Lopping (May–June):** Prior to monsoon onset, prune overhead standard branches severely, leaving a small central tuft. This allows 75% sunlight penetration during gloomy overcast monsoon months, promoting flowering.
- **Second Light Lopping (September–October):** Trim lateral regrowth after the South-West monsoon to allow post-monsoon sunlight for berry expansion.
- **Dry Season Protection (November–April):** Allow support tree foliage to expand during the dry summer to create a protective thermal canopy against harsh solar radiation.

#### 2. Pruning Direction:
Always prune standard branches on the southern and western sides more conservatively to prevent hot afternoon sun-scald on vine columns.
        """,
        "important_points": [
            "Optimal light transmission is 50–60%; adjust canopy twice annually.",
            "Heavy lopping in May–June ensures maximum light penetration during monsoon flowering.",
            "Conserve foliage on the South and West sides of trees to buffer harsh afternoon solar heat."
        ],
        "farming_recommendations": [
            "Use sharp pruning saws to make clean sloping cuts that shed rainwater and prevent fungal branch rot.",
            "Chop lopped standard foliage and spread it over vine basins as nitrogen-rich green leaf mulch.",
            "Paint cut branch stubs larger than 5 cm with 10% Bordeaux paste to stop fungal rot."
        ],
        "mistakes_to_avoid": [
            "Lopping standard trees in the middle of summer (March–April), exposing vines to lethal sun scorching.",
            "Allowing overhead shade to exceed 70% during the monsoon, which causes massive flower spike drop.",
            "Neglecting branch pruning until branches become heavy enough to break under monsoon winds and crush vines."
        ],
        "learning_resources": [
            "ICAR-IISR Canopy Management Protocols for High-Density Pepper Plantations",
            "Spices Board Advisory on Solar Radiation Management in Spices"
        ],
        "tips": "Spreading lopped Erythrina leaves around the vine basin supplies 20–30 kg of organic nitrogen per hectare.",
        "related": ["Support Tree Management", "Flowering and Berry Development", "Foot Rot Management"]
    },
    {
        "id": 13,
        "title": "Irrigation Management",
        "category": "Water & Nutrition",
        "summary": "Summer water stress management, drip irrigation design, basin water requirements, and blossom shower triggers.",
        "image": "assets/images/methods/live_standard.jpg",
        "caption": "Ring Basin Supplemental Drip Irrigation Around Living Tree Standards",
        "explanation": """
Although black pepper is historically rainfed, supplemental irrigation during dry winter and summer months (**December to May**) increases yields by **50% to 100%** and prevents catastrophic vine mortality.

#### 1. Water Stress & Floral Induction:
- Vines require a mandatory dry resting period of 40 to 60 days with minimal irrigation during December–February to initiate floral bud differentiation.
- From March onwards, initiate supplemental irrigation to sustain vegetative growth and prepare vines for flowering.

#### 2. Irrigation Methods & Quantities:
- **Drip Irrigation:** Highly recommended. Deliver **8 to 10 liters of water per vine per day** via two pressure-compensating drippers positioned 40 cm from the vine base.
- **Basin Irrigation:** Deliver **40 to 50 liters per vine at 7 to 10 day intervals**. Avoid flooding vine collars directly.
- **Blossom Irrigation Trigger:** Applying 50 liters/vine in late April to early May simulates pre-monsoon blossom showers, triggering early, uniform flowering.
        """,
        "important_points": [
            "Withhold heavy irrigation during winter (Dec–Feb) to induce flower bud formation.",
            "Summer irrigation (March–May) prevents berry drop and increases yield by up to 100%.",
            "Drip irrigation delivers 8–10 L/vine/day without wetting the susceptible root collar."
        ],
        "farming_recommendations": [
            "Mulch vine basins with 10 cm of dry organic matter before starting summer irrigation to reduce evaporation by 60%.",
            "Maintain soil moisture at 60% field capacity throughout berry expansion.",
            "Install automatic fertigation units to deliver dissolved NPK with irrigation water."
        ],
        "mistakes_to_avoid": [
            "Flooding water directly against the vine collar, which spreads *Phytophthora* fungal spores.",
            "Irrigating heavily during floral bud resting phase in January, converting flower buds into vegetative leaves.",
            "Stopping irrigation abruptly in May during dry spells between early showers."
        ],
        "learning_resources": [
            "Precision Micro-Irrigation for Commercial Spices: Precision Farming Development Centre (PFDC)",
            "ICAR-IISR Water Management Guidelines for Humid Tropics"
        ],
        "tips": "A simulated blossom irrigation of 100 L per standard in early May synchronizes spike emergence across the entire plantation.",
        "related": ["Drainage Management", "Climate Requirements", "Manure and Fertilizer Management"]
    },
    {
        "id": 14,
        "title": "Manure and Fertilizer Management",
        "category": "Water & Nutrition",
        "summary": "Soil-test based NPK scheduling, regional dosages, organic manures, biofertilizers, liming, and foliar sprays.",
        "image": "assets/images/guide/soil_prep.jpg",
        "caption": "Applying Enriched Vermicompost and Biofertilizers Around Vine Basin",
        "explanation": """
Black pepper produces heavy vegetative growth and harvests every year, demanding systematic nutrient replenishment. Universal fertilizer doses should be adjusted based on local soil test values and agro-ecological zones.

#### 1. General Recommended Nutrient Dosage (Mature Vine ≥ 3 years):
- **Nitrogen (N):** 100 g per vine per year.
- **Phosphorus (P2O5):** 40 g per vine per year.
- **Potassium (K2O):** 140 g per vine per year.
- *In high-density arecanut plantations, reduce to 50:20:70 g NPK/vine.*

#### 2. Application Split Schedule:
- **First Split (May–June):** Apply 50% N + 100% P2O5 + 50% K2O with the onset of the South-West monsoon.
- **Second Split (August–September):** Apply remaining 50% N + 50% K2O during post-monsoon berry development.

#### 3. Organic Manuring & Liming:
- **FYM / Compost:** 10 kg well-decomposed FYM or 5 kg vermicompost per vine annually in May.
- **Neem Cake:** 1 kg per vine to suppress nematodes and slowly release organic nitrogen.
- **Agricultural Lime / Dolomite:** 500 g per vine applied once every two years in April (applied 30 days before chemical fertilizers) in soils with pH < 5.5.
        """,
        "important_points": [
            "Standard NPK ratio: 100g N : 40g P2O5 : 140g K2O per mature vine/year, split into 2 seasonal applications.",
            "High potassium (K2O) is critical for spike berry density, perisperm firmness, and bulk weight.",
            "Apply lime in April, at least 30 days before chemical fertilizers to prevent nitrogen volatilization."
        ],
        "farming_recommendations": [
            "Apply fertilizers in a circular shallow band 30 cm away from the collar, incorporating gently into the top 5 cm of soil.",
            "Apply microbial biofertilizers: *Azospirillum*, Phosphobacteria, and *Trichoderma* (50 g each/vine) mixed in compost.",
            "Spray 1% 19-19-19 foliar fertilizer + IISR Pepper Special micronutrient spray (5g/L) during berry development."
        ],
        "mistakes_to_avoid": [
            "Applying chemical fertilizers directly against the collar trunk, causing chemical stem burn.",
            "Mixing chemical fertilizers and agricultural lime together in the same application.",
            "Applying fertilizer during torrential monsoon downpours where nutrients leach out of the root zone."
        ],
        "learning_resources": [
            "ICAR-IISR Nutrient Management & IISR Black Pepper Special Foliar Formulation Guide",
            "Fertilizer Association of India (FAI) Handbook on Spices Nutrition"
        ],
        "tips": "Always apply fertilizers when the soil is moist, never on parched dry ground or in standing water pools.",
        "related": ["Soil Requirements", "Nutrient Deficiency Management", "Irrigation Management"]
    },
    {
        "id": 15,
        "title": "Weed Management",
        "category": "Field Maintenance",
        "summary": "Soil-surface weeding protocols, biological living mulches, slash weeding, and herbicide safety.",
        "image": "assets/images/methods/homestead.jpg",
        "caption": "Circular Basin Weed Clearance and Clean Organic Mulch Layering",
        "explanation": """
Weeds compete fiercely with black pepper feeder roots for water and nutrients, and serve as collateral hosts for nematodes, scales, and fungal pathogens.

#### 1. Integrated Weed Management Strategy:
- **Slash Weeding:** Cut weeds at ground level 3 to 4 times a year (June, August, October, December) using brush cutters or sickles. Leave the slashed weed biomass on the ground as organic mulch to conserve moisture and suppress regrowth.
- **Clean Basin Weeding:** Maintain a 1-meter radius clean circle around each vine collar by manual shallow hand pulling.
- **Cover Cropping:** On open plantation slopes, establish legume living cover crops like *Mucuna bracteata*, *Centrosema pubescens*, or *Mimosa invisa* (thornless) to smother aggressive grasses and fix atmospheric nitrogen.

#### 2. Herbicide Cautions:
Avoid non-selective systemic herbicides (e.g., Glyphosate) near pepper vines. Accidental drift onto green climbing stems causes systemic vascular collapse and vine death.
        """,
        "important_points": [
            "Never use hoes or deep tillage within 1 meter of the vine base; feeder roots lie in the top 30 cm.",
            "Slash weeding returns organic carbon to the soil while preventing topsoil erosion.",
            "Cover crops on slopes suppress invasive weeds and reduce soil temperatures in summer."
        ],
        "farming_recommendations": [
            "Perform manual hand pulling of weeds in the immediate 50 cm collar zone.",
            "Spread chopped weed residue as surface mulch, ensuring it does not touch the vine stem directly.",
            "Plant *Stylosanthes hamata* or *Mucuna* on plantation boundaries to intercept creeping weed rhizomes."
        ],
        "mistakes_to_avoid": [
            "Deep hoeing or mechanical rototilling near vine standards, which destroys 80% of active feeder roots.",
            "Allowing aggressive climbing weeds (e.g., *Mikania micrantha*) to climb up pepper columns.",
            "Spraying systemic herbicides on windy days, resulting in chemical drift onto pepper foliage."
        ],
        "learning_resources": [
            "ICAR-IISR Good Agricultural Practices: Weed Management in Spices",
            "Kerala Agricultural University Weed Control Recommendations"
        ],
        "tips": "Maintain a 10 cm gap between organic mulch and the vine collar to prevent damp fungal development.",
        "related": ["Land Preparation", "Soil Requirements", "Mulching & Drainage"]
    },
    {
        "id": 16,
        "title": "Pest Management",
        "category": "Plant Protection",
        "summary": "Biology, symptoms, thresholds, and IPM protocols for Pollu Beetle, Top Shoot Borer, Scale Insects, and Nematodes.",
        "image": "sample_images/sample_spikes_2.jpg",
        "caption": "Canopy Scouting for Pollu Beetle, Berry Gall Midge, and Shoot Borers",
        "explanation": """
Black pepper is attacked by several destructive insect pests that damage tender shoots, flower spikes, and ripening berries.

#### 1. Pollu Beetle (*Longitarsus nigripennis*):
- **Damage:** Adults feed on tender leaves and spike buds. Larvae bore into developing berries, feeding on the inner seed, leaving hollow, shriveled black shells ('Pollu' berries). Can cause 30–40% yield loss.
- **Management:** Spray Quinalphos (0.05%) or Dimethoate (0.05%) in July and October when adult populations surge, or spray Neem oil (0.5%) at 15-day intervals.

#### 2. Top Shoot Borer (*Laspeyresia hemidoxa*):
- **Damage:** Larvae bore into tender growing terminal shoots, causing tip wilting, blackening, and dieback.
- **Management:** Prune and destroy infested terminal tips. Spray Chlorantraniliprole (0.3 ml/L) or Quinalphos (0.05%) during new vegetative flushes.

#### 3. Scale Insects (*Lepidosaphes piperis* & *Aspidiotus destructor*):
- **Damage:** Crusts of encrusted scales suck sap from stems, leaves, and berries, causing yellowing and dieback.
- **Management:** Spray Fish Oil Rosin Soap (FORS 25 g/L) or Neem oil (0.5%), or apply Dimethoate (0.05%) for severe infestations.

#### 4. Nematodes (*Radopholus similis* & *Meloidogyne incognita*):
- **Damage:** Burrowing and root-knot nematodes attack feeder roots, producing root galls and necrotic lesions that trigger Slow Decline.
- **Management:** Apply *Pochonia chlamydosporia* or *Trichoderma* (50 g/vine) along with 1 kg neem cake annually.
        """,
        "important_points": [
            "Pollu beetle larvae bore into berries, turning them into hollow, empty black shells.",
            "Top shoot borer kills growing terminal buds, halting upward vine climb.",
            "Soil-applied neem cake and bio-nematicides effectively suppress root-knot nematodes."
        ],
        "farming_recommendations": [
            "Conduct routine weekly scouting of tender shoots and young spikes between June and November.",
            "Conserve natural predators such as ladybird beetles and hoverfly larvae that consume scale insects.",
            "Apply prophylactic neem oil sprays (5 ml/L + 1 ml soap) during berry development."
        ],
        "mistakes_to_avoid": [
            "Spraying synthetic insecticides during peak morning hours when honeybees and pollinators are active.",
            "Ignoring early scale infestations until entire vine columns are encrusted and dying.",
            "Over-dosing synthetic pyrethroids, which induces secondary pest flare-ups of scale insects."
        ],
        "learning_resources": [
            "ICAR-IISR Integrated Pest Management in Black Pepper Manual",
            "Spices Board Pesticide Residue Limits and GAP Regulations"
        ],
        "tips": "Applying 1 kg neem cake per vine in May reduces root-knot nematode populations by over 70%.",
        "related": ["Disease Management", "Foot Rot Management", "Harvesting and Maturity Identification"]
    },
    {
        "id": 17,
        "title": "Disease Management",
        "category": "Plant Protection",
        "summary": "Etiology, identification, and control of Anthracnose (Pollu disease), Slow Decline, and Stunt Viral disease.",
        "image": "assets/images/guide/foot_rot.jpg",
        "caption": "Diagnostic Foliar Symptoms of Anthracnose Leaf Spot",
        "explanation": """
Apart from Phytophthora foot rot, black pepper suffers from foliar anthracnose, slow decline complex, and viral stunt disease.

#### 1. Anthracnose / Fungal Pollu (*Colletotrichum gloeosporioides*):
- **Symptoms:** Produces circular to irregular dark brown necrotic spots with yellow halos on leaves, and black necrotic lesions on catkin spikes, causing premature spike shed and barren berries.
- **Management:** Spray 1% Bordeaux mixture or Carbendazim-Mancozeb (0.2%) in July and September. Regulate overhead tree shade to improve air circulation.

#### 2. Slow Decline (Slow Wilt):
- **Etiology:** A debilitating disease complex caused by the interaction of plant-parasitic nematodes (*Radopholus similis* and *Meloidogyne incognita*) with soil fungi (*Fusarium oxysporum* and *Phytophthora*).
- **Symptoms:** Gradual foliar yellowing, feeder root necrosis, excessive defoliation, and progressive dieback over 2 to 3 years.
- **Management:** Drench vine basins with Copper Oxychloride (0.2%) + apply 1 kg neem cake + bio-agent *Pochonia chlamydosporia* (50 g/vine).

#### 3. Stunt Virus / Viral Complex:
- **Symptoms:** Severe leaf cupping, shortening of internodes, mottled mosaic patterns, and complete stunting. Transmitted by aphids and infected cuttings.
- **Management:** Uproot and incinerate infected vines immediately; no chemical cure exists. Control insect aphid vectors with systemic sprays.
        """,
        "important_points": [
            "Anthracnose causes premature spike drop and barren spikes during wet humid spells.",
            "Slow Decline is caused by nematode-fungal synergy and leads to gradual 3-year vine mortality.",
            "Virus-infected vines cannot be cured and must be eradicated to prevent plantation-wide transmission."
        ],
        "farming_recommendations": [
            "Apply two prophylactic sprays of 1% freshly prepared Bordeaux mixture in June and August.",
            "Test soil for plant-parasitic nematodes if vines show persistent leaf yellowing despite fertilizer.",
            "Sterilize grafting tools in 10% trisodium phosphate (TSP) to stop mechanical virus transmission."
        ],
        "mistakes_to_avoid": [
            "Taking propagation cuttings from asymptomatic branches of virus-infected vines.",
            "Treating Slow Decline with nitrogen fertilizer instead of addressing root nematodes.",
            "Using stale, curdled Bordeaux mixture prepared the previous day."
        ],
        "learning_resources": [
            "ICAR-IISR Compendium of Black Pepper Diseases: Diagnostic Identification & IPM",
            "Plant Pathology Guide: Identification of Viral Diseases in Plantation Crops"
        ],
        "tips": "Always prepare fresh 1% Bordeaux mixture using high-grade quicklime and copper sulfate; it should turn a clean blue color without settling.",
        "related": ["Foot Rot Management", "Pest Management", "Nursery Management"]
    },
    {
        "id": 18,
        "title": "Foot Rot Management",
        "category": "Plant Protection",
        "summary": "Complete Phytophthora foot rot (Quick Wilt) protocol: symptoms, epidemiology, biocontrol, and fungicides.",
        "image": "assets/images/guide/foot_rot.jpg",
        "caption": "Devastating Collar Rot Caused by Phytophthora capsici",
        "explanation": """
**Phytophthora Foot Rot**, also historically known as **Quick Wilt**, caused by the oomycete soil pathogen *Phytophthora capsici*, is the most devastating disease of black pepper worldwide. Under favorable conditions (monsoon rains, water stagnation, 25–28°C), it can decimate entire plantations in weeks.

#### 1. Infection Sites & Symptoms:
- **Collar Infection (Foot Rot):** The fungus attacks the stem collar at ground level. A dark brown to black slimy water-soaked lesion girdles the collar trunk. The entire foliage wilts, turns dull grayish-green, and drops within 10 to 14 days, leaving bare standard vines.
- **Root Rot:** Underground feeder roots turn black and rot away, causing slow aboveground decline.
- **Foliar Infection (Leaf Rot):** Large circular black water-soaked lesions with fimbriate (feathery) margins on leaves, causing catastrophic defoliation.

#### 2. Scientifically Supported Integrated Management Schedule:
- **Pre-Monsoon (May–June):**
  1. Dig drainage channels to prevent surface water runoff from pooling near vine basins.
  2. Drench and spray vines with **1% Bordeaux mixture** (5 to 10 liters per vine basin).
  3. Apply *Trichoderma harzianum* (50 g/vine) mixed with 5 kg farmyard manure and 1 kg neem cake.
- **Mid-Monsoon (August–September):**
  1. Spray foliage with **Potassium phosphonate (Akomin 0.3%)** or **Metalaxyl-Mancozeb (0.125%)**.
  2. Drench vine collar with Potassium phosphonate (0.3%) or Copper Oxychloride (0.2%).
        """,
        "important_points": [
            "Phytophthora capsici attacks collar, roots, leaves, and spikes during continuous monsoon rains.",
            "Collar infection girdles vascular cambium, killing a 20-year-old vine in less than 14 days.",
            "A combination of sanitation, soil drainage, Trichoderma biocontrol, and phosphonates provides 90%+ control."
        ],
        "farming_recommendations": [
            "Keep the vine collar on a 15 cm raised mound to prevent surface water accumulation.",
            "Paint vine trunks from ground level up to 1 meter with 10% Bordeaux paste in May.",
            "Remove and burn dead vines immediately, and solarize the vacated pit with 500 g lime."
        ],
        "mistakes_to_avoid": [
            "Applying chemical fungicides and Trichoderma biocontrol on the same day (maintain 15-day gap).",
            "Allowing drainage water from an infected upland patch to wash across healthy downhill vines.",
            "Waiting for full foliar wilting before beginning prophylactic fungicide treatments."
        ],
        "learning_resources": [
            "ICAR-IISR Foot Rot Control Protocol: Standard Operating Procedure for Plantation Farmers",
            "Spices Board Emergency Advisory on Monsoon Phytophthora Management"
        ],
        "tips": "Potassium phosphonate (0.3%) is systemic; spraying it on leaves translocates down to protect roots, and drenching roots translocates up to protect leaves.",
        "related": ["Disease Management", "Drainage Management", "Selection of Varieties"]
    },
    {
        "id": 19,
        "title": "Nutrient Deficiency Management",
        "category": "Water & Nutrition",
        "summary": "Visual leaf diagnostics, critical tissue levels, and correction protocols for N, P, K, Mg, Zn, and B deficiencies.",
        "image": "assets/images/methods/bush_pepper.jpg",
        "caption": "Foliar Nutrition Inspection: Interveinal Chlorosis (Mg) and Little Leaf (Zn)",
        "explanation": """
Nutrient deficiencies severely restrict spike initiation, reduce berry weight, and predispose vines to fungal pathogens.

#### 1. Major Nutrient Deficiencies:
- **Nitrogen (N):** General uniform chlorosis (pale yellowing) starting on older lower leaves; stunted vine growth; small pale spikes. *Correction: Apply urea 50 g/vine or spray 1% foliar urea.*
- **Phosphorus (P):** Dark purplish-bronze tint on older leaves, poor root anchorage, delayed spike emergence. *Correction: Apply rock phosphate 150 g/vine.*
- **Potassium (K):** Marginal leaf scorching and necrotic tip curling starting on mature leaves; lightweight berries, poor bulk density. *Correction: Apply Muriate of Potash (MOP) 100 g/vine in split doses.*

#### 2. Secondary & Micronutrient Deficiencies:
- **Magnesium (Mg):** Distinct **interveinal chlorosis** (inverted V-shaped yellowing between green veins) on older leaves. Prevalent in high-rainfall acidic soils. *Correction: Apply Magnesium Sulfate (MgSO4) 50 g/vine to soil, or spray 0.5% MgSO4.*
- **Zinc (Zn):** 'Little leaf' symptom; small, narrow, clustered leaves with wavy margins and shortened internodes. *Correction: Spray 0.25% Zinc Sulfate (ZnSO4) on new flushes.*
- **Boron (B):** Deformed, brittle leaf tips, spike necrosis, and excessive berry drop. *Correction: Apply 10 g Borax per vine or spray 0.1% Solubor.*
        """,
        "important_points": [
            "Potassium deficiency causes marginal leaf burn and lightweight, hollow berries.",
            "Magnesium deficiency displays characteristic inverted V-shaped interveinal chlorosis.",
            "Zinc deficiency causes rosette 'little leaf' syndrome on growing tips."
        ],
        "farming_recommendations": [
            "Conduct leaf tissue analysis in October (sampling 5th to 7th leaf from lateral branches).",
            "Spray IISR Black Pepper Special micronutrient mixture (5 g/L) twice a year (May and August).",
            "Apply dolomite (supplying both Calcium and Magnesium) in acidic laterite soils."
        ],
        "mistakes_to_avoid": [
            "Over-applying potassium without magnesium, which induces severe magnesium deficiency.",
            "Applying trace elements like borax at excessive rates, which causes lethal foliar toxicity.",
            "Diagnosing micronutrient chlorosis as viral disease without conducting tissue or soil tests."
        ],
        "learning_resources": [
            "ICAR-IISR Diagnostic Color Atlas of Nutritional Disorders in Black Pepper",
            "Spices Board Foliar Nutrition Protocols"
        ],
        "tips": "Spraying 0.5% Epsom salt (Magnesium Sulfate) + 0.2% Zinc Sulfate in July quickly restores green color to chlorotic leaves.",
        "related": ["Manure and Fertilizer Management", "Soil Requirements", "Flowering and Berry Development"]
    },
    {
        "id": 20,
        "title": "Flowering and Berry Development",
        "category": "Harvest Readiness",
        "summary": "Inflorescence physiology, catkin emergence, geitonogamy pollination, berry set, and fruit expansion.",
        "image": "sample_images/sample_spikes_3.jpg",
        "caption": "Spike Elongation, Berry Setting, and Physiological Development",
        "explanation": """
The transition from vegetative growth to reproductive flowering governs the commercial harvest volume.

#### 1. Floral Induction & Spike Emergence:
- Flower bud differentiation occurs during the dry resting period in January–March.
- The arrival of pre-monsoon blossom showers in May–June triggers rapid, synchronized catkin spike emergence from axillary buds on plagiotropic lateral branches.

#### 2. Pollination Physiology:
- Black pepper flowers are sessile and mostly hermaphrodite (bisexual) in cultivated clones.
- Pollination is primarily **geitonogamous** (pollen transferred by gravitation and rainwater wash down the drooping catkin spike). Rainwater or dew running down the vertical spike is critical to transport pollen grains from anthers to receptive stigmas.
- Prolonged dry heat or torrential cloudbursts during pollination cause unfertilized flowers to abort, resulting in 'running' (barren) spikes.

#### 3. Berry Development Timeline:
- **Stage 1 (Pinhead to Pea stage, Months 1–2):** Rapid cell division; vulnerable to pollu beetle attack.
- **Stage 2 (Berry Expansion, Months 3–5):** Green berry enlargement; high water and potassium demand.
- **Stage 3 (Seed Hardening & Perisperm Filling, Months 6–7):** Seed hardens, starch and piperine accumulate.
- **Stage 4 (Physiological Maturity, Month 8):** Berries turn pale green to yellow, and finally orange-red.
        """,
        "important_points": [
            "Pollination requires rain or dew droplets running down the hanging catkin spike.",
            "Berry development spans 7 to 8 months from blossom emergence in June to harvest in January–February.",
            "Moisture stress during months 3–5 causes spike shedding and light berry formation."
        ],
        "farming_recommendations": [
            "Regulate overhead tree shade before flowering to guarantee 60% sunlight penetration for uniform spike emergence.",
            "Apply foliar potassium spray (1% Potassium Nitrate KNO3) at Month 4 to accelerate perisperm filling.",
            "Provide supplemental irrigation if monsoon rains cease prematurely in September–October."
        ],
        "mistakes_to_avoid": [
            "Spraying chemical insecticides during peak flower opening, which disrupts natural pollination.",
            "Allowing dense shade to persist during spike emergence, causing over 50% catkin abortion.",
            "Severe drought stress during berry expansion, leading to wrinkled, hollow berries."
        ],
        "learning_resources": [
            "ICAR-IISR Reproductive Biology and Pollination Dynamics in Piper nigrum",
            "Indian Journal of Agricultural Sciences: Spike Development and Berry Filling in Black Pepper"
        ],
        "tips": "Ensure overhead tree shade is properly thinned before the monsoon; open sunlight combined with monsoon mist maximizes berry set.",
        "related": ["Harvesting and Maturity Identification", "Shade Management", "Irrigation Management"]
    },
    {
        "id": 21,
        "title": "Harvesting and Maturity Identification",
        "category": "Harvest Readiness",
        "summary": "1-2 berry ripening rule, spike firmness, harvesting procedures, ladder safety, and preventing shatter losses.",
        "image": "assets/images/pepper_harvest.jpg",
        "caption": "Spikes Reaching Prime Maturity with 1-2 Berries Turning Orange-Red",
        "explanation": """
Harvest timing directly determines the physical grade, bulk density (g/L), piperine percentage, and volatile oil recovery of the cured black pepper.

#### 1. The Scientific 1–2 Berry Ripening Indicator Rule:
- In commercial black pepper cultivation, harvesting should commence the moment **one or two berries per spike turn yellow to orange-red**.
- At this exact physiological stage, all remaining green berries on the spike have reached maximum dry matter accumulation, full perisperm seed firmness, and peak essential oil concentration.
- **Why wait no longer?** Waiting for all berries on a spike to turn red leads to heavy fruit shattering (berries dropping onto damp soil), bird foraging losses, and fungal contamination.

#### 2. Physiological Maturity Markers:
- Press a green berry between your thumb and forefinger: A mature berry is hard and unyielding; an immature berry crushes easily into watery pulp.
- Berries feel heavy, hard, and separate cleanly from the spike axis upon mechanical threshing.

#### 3. Harvesting Procedure:
- Use lightweight, sturdy aluminum or treated bamboo orchard ladders to reach vine tops safely.
- Pick entire spike clusters by a gentle upward twist at the base of the peduncle. Never yank or tear fruiting laterals.
- Collect picked spikes in clean canvas sacks or woven baskets; never drop spikes onto plantation soil.
        """,
        "important_points": [
            "Commence harvesting as soon as 1 to 2 berries on a spike turn yellow or orange-red.",
            "Firm seed perisperm indicates peak dry matter accumulation and high bulk density (500–600 g/L).",
            "Never allow ripe berries to drop onto damp ground where soil molds degrade quality."
        ],
        "farming_recommendations": [
            "Conduct selective harvesting: Walk through the plantation every 10 to 14 days to pick only mature spikes.",
            "Spread clean tarpaulins under standard trees while climbing to catch accidentally dropped spikes.",
            "Separate fully red, over-ripe berries to process separately as premium **White Pepper**."
        ],
        "mistakes_to_avoid": [
            "Harvesting prematurely when all berries are dark green and soft, yielding light, shriveled, low-density pepper.",
            "Stripping individual berries directly from vines, which damages the fruiting lateral branches for next season.",
            "Dropping harvested spikes directly onto damp plantation soil where mold spores infect berries."
        ],
        "learning_resources": [
            "ICAR-IISR Harvest Maturity Standards & Post-Harvest Protocol Manual",
            "Spices Board Quality Specifications for Export Grade Black Pepper (ASTA & ESA Standards)"
        ],
        "tips": "Spikes harvested at the 1–2 red berry stage yield dry black pepper with a bulk density exceeding 550 g/L, commanding top export prices.",
        "related": ["Post-Harvest Processing", "Drying and Storage", "Flowering and Berry Development"]
    },
    {
        "id": 22,
        "title": "Post-Harvest Processing",
        "category": "Processing & Storage",
        "summary": "Threshing, mechanical berry separation, hot water blanching treatment, and enzyme activation.",
        "image": "assets/images/guide/drying_storage.jpg",
        "caption": "Hot Water Blanching Tank and Mechanical Berry Thresher",
        "explanation": """
Post-harvest processing transforms freshly harvested green spikes into clean, high-grade, glossy black pepper.

#### 1. Spike Threshing (Berry Separation):
- Freshly harvested spikes are heaped indoors on clean tarpaulins for 12 to 24 hours to soften the pedicel connection.
- Berries are separated from the central stalk (rachis) using pedal-operated or motorized **mechanical berry threshers**.
- *Traditional manual foot-trampling must be avoided* as it introduces microbial contamination and fractures berry pericarps.

#### 2. The Scientific Hot Water Blanching Treatment:
- Immerse separated green berries in boiling water (**80°C to 90°C**) for **60 seconds (1 minute)** in perforated wire mesh containers.
- **Biochemical Mechanism:**
  1. Activates native **polyphenol oxidase** enzymes that catalyze the uniform enzymatic oxidation of phenolic compounds, turning the outer skin into an intense, glossy jet-black color.
  2. Kills surface microorganisms, wild mold spores, and insect eggs.
  3. Removes field dust and wash residues.
  4. Shortens subsequent sun-drying time from **8 days down to 4–5 days**.
        """,
        "important_points": [
            "Motorized threshers separate berries cleanly without breaking pericarp skins.",
            "Hot water blanching at 80–90°C for 60 seconds produces premium jet-black glossy color.",
            "Blanching reduces solar drying time from 8 days to 4–5 days and eliminates microbial contamination."
        ],
        "farming_recommendations": [
            "Drain blanched berries thoroughly for 5 minutes before spreading them out on drying floors.",
            "Compost empty threshing rachis stalks; never mix them back into the dried berry lots.",
            "Process harvested spikes within 24 hours of field picking to prevent uncontrolled fermentation."
        ],
        "mistakes_to_avoid": [
            "Boiling berries for more than 2 minutes, which leaches volatile essential oils and softens berry texture.",
            "Trampling spikes with bare feet or dirty rubber boots on unhygienic farm floors.",
            "Holding wet threshed berries in deep anaerobic heaps for days before drying."
        ],
        "learning_resources": [
            "ICAR-IISR Post-Harvest Technology for Black Pepper: Blanching and Solar Curing",
            "Spices Board Clean Pepper Production Technology Manual"
        ],
        "tips": "Blanched black pepper berries command a 15–20% premium in international spice markets due to uniform color and low microbial counts.",
        "related": ["Harvesting and Maturity Identification", "Drying and Storage", "Selection of Varieties"]
    },
    {
        "id": 23,
        "title": "Drying and Storage",
        "category": "Processing & Storage",
        "summary": "Solar drying floors, target moisture thresholds (10-11%), aflatoxin prevention, grading, and warehouse storage.",
        "image": "assets/images/guide/drying_storage.jpg",
        "caption": "Sun Drying on UV-Stabilized Clean Poly-Sheets and Hermetic Storage",
        "explanation": """
Correct drying and warehouse storage preserve the pungency, aroma, and food safety of black pepper for up to 3 years.

#### 1. Sun Drying & Moisture Management:
- Spread blanched berries on clean cement drying yards, food-grade black UV-stabilized polythene sheets, or modern solar tunnel dryers at a density of 5–7 kg/m².
- Rake berries every 2 hours to ensure uniform solar exposure and prevent localized mold development.
- Cover or collect berries before evening dew or sudden rain showers fall.
- Continue drying until moisture content drops to **10% to 11%**.
- *Field Test:* When properly dried to 10% moisture, a berry makes a sharp crisp cracking sound between teeth and cannot be dented with a fingernail.

#### 2. Cleaning, Grading & Bulk Density:
- Pass dried pepper through an air-screen cleaner or winnower to remove dust, chaff, and pinheads.
- **Commercial Grades (Spices Board of India):**
  - **TGEB (Tellicherry Garbled Extra Bold):** Berries > 4.75 mm, bulk density > 575 g/L.
  - **TGSEB (Tellicherry Garbled Special Extra Bold):** Berries > 4.25 mm.
  - **MG-1 (Malabar Garbled Grade 1):** Bulk density > 500 g/L.

#### 3. Storage & Packaging:
- Pack dried pepper into clean, double-lined jute bags with inner food-grade polyethylene liners (300 gauge) or hermetic GrainPro bags.
- Store on wooden pallets elevated **15 to 30 cm above the concrete floor** and **50 cm away from warehouse walls**.
- Maintain warehouse relative humidity below 65% and temperature below 25°C.
        """,
        "important_points": [
            "Target moisture content is strictly 10% to 11% to prevent Aspergillus flavus mold and aflatoxin.",
            "Rake drying berries every 2 hours during full sun hours for uniform curing.",
            "Store in poly-lined bags elevated on wooden pallets away from walls and damp floors."
        ],
        "farming_recommendations": [
            "Use a calibrated digital grain moisture meter to verify 10.5% moisture before warehouse bagging.",
            "Never dry pepper on bare cow-dung smeared or unpaved mud yards.",
            "Fumigate or seal warehouse storage to prevent cigarette beetle (*Lasioderma serricorne*) infestation."
        ],
        "mistakes_to_avoid": [
            "Bagging pepper with moisture content above 12%, which results in fungal mold, musty odor, and total spoilage.",
            "Over-drying below 8% moisture, which causes berry cracking and loss of volatile aroma oils.",
            "Storing pepper sacks directly touching cold concrete floors or moist exterior walls."
        ],
        "learning_resources": [
            "Spices Board Specifications for Warehousing and Export Packaging of Black Pepper",
            "ISO 959-1: Black Pepper (Piper nigrum L.) Specifications and Moisture Determination Standards"
        ],
        "tips": "Always store pepper on wooden pallets 30 cm off the floor; concrete floors continuously wick ground moisture into bottom sacks.",
        "related": ["Post-Harvest Processing", "Harvesting and Maturity Identification", "Introduction to Black Pepper"]
    }
]


# ======================================================================================
# 2. 7 CULTIVATION METHODS & SYSTEMS (WITH PROCEDURES & VERIFIED YOUTUBE URLS)
# ======================================================================================
GROWING_METHODS_DATA = [
    {
        "id": "support_tree",
        "name": "1. Live Support Tree Cultivation",
        "badge": "Commercial Standard",
        "image": "assets/images/methods/support_tree.jpg",
        "explanation": "The traditional, most widely practiced plantation system training black pepper vines up living fast-growing support trees.",
        "how_it_works": "Pepper vines are planted at the base of living deciduous trees such as *Erythrina indica* (Indian Coral Tree) or *Garuga pinnata*. As the tree grows, its rough bark allows adventitious pepper roots to anchor firmly up to 6 to 8 meters.",
        "procedure": [
            "Plant mature hardwood cuttings of *Erythrina indica* or *Garuga pinnata* (2 m tall, 5 cm thick) at 3m × 3m spacing in May–June.",
            "Allow support trees to root and establish for 1 full year prior to pepper vine transplanting.",
            "Dig planting pits (50×50×50 cm) on the North or North-East face of each standard tree in April.",
            "Refill pits with topsoil, 10 kg FYM, 1 kg neem cake, and 150 g rock phosphate.",
            "Plant 2 to 3 rooted polybag saplings per tree in June with the onset of the monsoon.",
            "Tie young vine shoots to the tree trunk with soft banana fiber at 30 cm intervals.",
            "Regulate support tree canopy twice annually (May and September) by lopping overhead branches to maintain 50–60% sunlight."
        ],
        "suitable_conditions": "Commercial plantation estates, virgin forest slopes, fertile valley land with annual rainfall between 1,500 and 3,000 mm.",
        "advantages": [
            "Natural nitrogen fixation from leguminous support trees (*Erythrina*).",
            "Living bark provides natural humidity and micro-climate buffering against summer heat waves.",
            "Extremely high commercial yield per hectare (1,500 to 2,500 kg dry pepper/ha)."
        ],
        "limitations": [
            "Requires skilled labor to climb tall ladders for canopy pruning and annual harvest.",
            "Tree roots compete with pepper vines if regular pruning and ring-weeding are neglected."
        ],
        "tips": "Always plant standard cuttings 1 full year before planting pepper to establish a sturdy root anchor.",
        "youtube_url": "https://www.youtube.com/watch?v=VGrX_fkVppA",
        "youtube_title": "Black Pepper Farming - Planting, Care, Harvesting | Complete Guide",
        "youtube_desc": "Demonstrates live support tree establishment, vine training, seasonal pruning, and harvest."
    },
    {
        "id": "arecanut_based",
        "name": "2. Arecanut-Based Pepper Cultivation",
        "badge": "High-Density Agroforestry",
        "image": "assets/images/methods/mixed_arecanut.jpg",
        "explanation": "Training black pepper vines up existing commercial arecanut palms (*Areca catechu*) to achieve dual cash-crop income without extra land.",
        "how_it_works": "Arecanut plantations spaced at 2.7 m × 2.7 m provide ideal vertical living poles. Pepper vines climb the slender palm trunks, thriving in the filtered understory microclimate while utilizing arecanut drip irrigation and fertilization.",
        "procedure": [
            "Select established arecanut palms that are at least 4 to 5 years old with sturdy vertical stems.",
            "Dig small planting cavities (30×30×30 cm) 30 cm away from the palm trunk on the Northern side.",
            "Incorporate 5 kg compost, 250 g neem cake, and 50 g rock phosphate into each pit.",
            "Plant 2 rooted cuttings of shade-tolerant cultivars (*Panniyur-5* or *IISR Thevam*).",
            "Tie young vines to the arecanut palm trunk every 30 cm using coir twine or banana fiber.",
            "Allow vines to climb up to 5 to 6 meters; wrap palm fronds loosely during heavy dry periods to shade the base.",
            "Harvest arecanut and pepper sequentially using specialized telescopic harvesting poles."
        ],
        "suitable_conditions": "Coastal agro-climatic belts, irrigated arecanut groves, regions with mild summers and steady water tables.",
        "advantages": [
            "Zero additional land required; doubles net revenue per acre.",
            "Shared irrigation, fertigation, and weeding costs with the arecanut crop.",
            "Arecanut palms have straight, knot-free trunks that make vine climbing and spraying simple."
        ],
        "limitations": [
            "Requires shade-tolerant varieties like *Panniyur-5* to thrive in the palm understory.",
            "Care must be taken not to damage the arecanut palm root crown during pit preparation."
        ],
        "tips": "Select cultivars like *Panniyur-5* or *IISR Thevam* specifically bred for high yield under arecanut shade.",
        "youtube_url": "https://www.youtube.com/watch?v=Gze6nWk37lg",
        "youtube_title": "Production Technology in Black Pepper - By Dr. Srinivasan V (ICAR-IISR)",
        "youtube_desc": "Senior ICAR-IISR scientist details high-density intercropping on arecanut palms, fertigation, and canopy management."
    },
    {
        "id": "coconut_based",
        "name": "3. Coconut-Based Mixed Cultivation",
        "badge": "Multi-Strata Cropping",
        "image": "assets/images/methods/live_standard.jpg",
        "explanation": "Utilizing mature coconut palm trunks (*Cocos nucifera*) as robust, long-lived vertical living supports in tropical gardens.",
        "how_it_works": "Coconut palms spaced at 7.5 m × 7.5 m leave extensive unused vertical trunk space and canopy sunlight. Pepper vines trained up the lower 6 meters of coconut trunks utilize sunlight filtering through palm fronds.",
        "procedure": [
            "Select coconut palms that are at least 8 to 10 years old with mature, rough, vertical trunks.",
            "Dig planting pits measuring 40×40×40 cm roughly 45 cm away from the coconut bole on the North-East side.",
            "Mix topsoil with 10 kg compost, 1 kg bone meal or rock phosphate, and 50 g *Trichoderma* inoculant.",
            "Plant 2 vigorous rooted saplings per coconut palm during the monsoon.",
            "Train vines up the palm trunk using temporary horizontal coir ties until adventitious clinging roots anchor firmly into trunk crevices.",
            "Mulch coconut basins with a 15 cm layer of coconut husks placed convex side up to retain moisture.",
            "Apply dedicated pepper NPK doses separately from coconut palm fertilizer rings."
        ],
        "suitable_conditions": "Tropical coastal belts, homesteads, irrigated coconut plantations with deep sandy loam or red loam soils.",
        "advantages": [
            "Coconut trunks have exceptional structural longevity exceeding 40+ years.",
            "Permits multi-tier farming combining coconut (top), pepper (middle), and ginger/turmeric (ground).",
            "Reduces soil evaporation around coconut root basins through canopy ground cover."
        ],
        "limitations": [
            "Lower plant density per acre compared to dedicated pepper plantations due to wide coconut spacing.",
            "Falling mature coconuts or dry heavy fronds can occasionally snap pepper vine branches."
        ],
        "tips": "Place a protective split-bamboo or wire mesh collar on the top of the vine column to deflect falling coconut fronds.",
        "youtube_url": "https://www.youtube.com/watch?v=SxBmzUcPukQ",
        "youtube_title": "How to Grow Black Pepper Step-by-Step | Complete Tutorial",
        "youtube_desc": "Step-by-step guidance on establishing pepper vines on palm standards, moisture mulching, and harvesting."
    },
    {
        "id": "artificial_trellis",
        "name": "4. Artificial Support and Trellis Cultivation",
        "badge": "High-Tech Intensive",
        "image": "assets/images/methods/artificial_trellis.jpg",
        "explanation": "Training pepper vines on non-living reinforced concrete posts, granite pillars, or galvanized wire trellises.",
        "how_it_works": "Vines are trained up non-living vertical pillars (RCC posts, galvanized iron pipes, or granite pillars 3 to 4 meters high). Eliminates all underground root competition and aboveground shade competition.",
        "procedure": [
            "Erect reinforced concrete (RCC) or granite pillars (3.5 m long, 10×10 cm cross-section) buried 60 cm into the ground.",
            "Erect pillars at intensive spacing of 2 m × 2 m (2,500 pillars per hectare) or 2.5 m × 2.5 m.",
            "Wrap pillars with nylon mesh or coir netting to provide grip for adventitious climbing rootlets.",
            "Dig planting pits at the base of each pillar and refill with enriched organic potting substrate.",
            "Plant 2 rooted cuttings per pillar; tie shoots to the mesh at 25 cm intervals.",
            "Erect 35% overhead agro-shade net structures or overhead sprinkler mist systems to prevent summer sun-scald.",
            "Prune top shoots at 3.5 meters to force lateral branching and dense cylindrical column foliage."
        ],
        "suitable_conditions": "Intensive precision farming, high-capital commercial projects, areas with scarce live tree saplings.",
        "advantages": [
            "Zero root competition for water and fertilizer from support trees.",
            "High planting density (up to 2,500 vines/ha) yielding commercial harvests by Year 2.",
            "Uniform pillar height makes mechanized harvesting and spraying exceptionally easy."
        ],
        "limitations": [
            "High initial capital investment for concrete pillars and shade netting.",
            "Concrete posts heat up in hot summers; requires netting wrap and irrigation misting."
        ],
        "tips": "Wrap concrete pillars with coir netting or plastic mesh; bare concrete becomes too hot and smooth for rootlet grip.",
        "youtube_url": "https://www.youtube.com/watch?v=lC3L5CpnJF0",
        "youtube_title": "Intensifying Black Pepper Farming | Vertical Column Method",
        "youtube_desc": "Intensive vertical column and artificial trellis production without live tree standards."
    },
    {
        "id": "intercropping_systems",
        "name": "5. Intercropping",
        "badge": "Diversified Agroforestry",
        "image": "assets/images/methods/intercropping.jpg",
        "explanation": "Integrating black pepper into multi-crop commercial plantations alongside coffee, cardamom, tea, and shade trees.",
        "how_it_works": "Pepper vines climb the natural shade trees (*Grevillea robusta* / Silver Oak) required by Arabica and Robusta coffee estates. The multi-strata canopy provides ecological stability, pest buffering, and diversified year-round cash flow.",
        "procedure": [
            "Identify existing *Grevillea robusta* (Silver Oak) shade trees in coffee or tea plantations spaced at 4m to 6m.",
            "Establish planting pits on the North-East side of each shade tree, clear of primary coffee root rings.",
            "Incorporate farmyard manure, rock phosphate, and *Trichoderma* biofertilizer into pit topsoil.",
            "Plant 2 cuttings of high-elevation cultivars (*IISR Girimunda* or *Panniyur-3*).",
            "Maintain coffee shade requirements while lopping excessive low-hanging standard branches in May and September.",
            "Apply balanced fertilizer splits synchronizing with coffee post-blossom and post-monsoon dressing rounds.",
            "Harvest pepper in February–March following the conclusion of the main coffee berry picking rounds."
        ],
        "suitable_conditions": "Hill country plantations, high-altitude coffee estates (600–1,200m MSL), rich humus soils with high organic matter.",
        "advantages": [
            "Transforms non-yielding estate shade trees into high-value cash-producing assets.",
            "Creates an economic buffer against volatile coffee and tea market price fluctuations.",
            "High-elevation berries yield exceptionally dense berries with high volatile essential oil content."
        ],
        "limitations": [
            "Lopping shade trees must be carefully balanced with the sunlight needs of the coffee understory.",
            "Harvest schedules may partially overlap with late-ripening coffee picking rounds."
        ],
        "tips": "Plant high-altitude cultivars like *IISR Girimunda* or *Panniyur-3* for superior cold and elevation tolerance.",
        "youtube_url": "https://www.youtube.com/watch?v=eOis63J-LrY",
        "youtube_title": "Vertical Column Black Pepper Farming | Multi-Tier Cultivation Guide",
        "youtube_desc": "Multi-tier intercropping systems in plantations, maximizing land use efficiency."
    },
    {
        "id": "homestead_cultivation",
        "name": "6. Homestead Cultivation",
        "badge": "Smallholder & Backyard",
        "image": "assets/images/methods/homestead.jpg",
        "explanation": "Growing black pepper in home gardens, backyard fences, and domestic homestead plots for self-sufficiency and local sales.",
        "how_it_works": "Homestead farmers train 10 to 50 vines on yard trees (Jackfruit, Mango, Drumstick) or perimeter boundary pillars, fertilizing with household kitchen compost, vermicompost, and cow dung slurry.",
        "procedure": [
            "Select suitable yard trees (Jackfruit, Mango, Ailanthus) or backyard compound pillars with partial morning sun.",
            "Dig a 40×40×40 cm pit near the base of the selected tree, avoiding major structural root cutting.",
            "Fill pit with compost made from household kitchen waste, decomposed cow dung, and leaf litter.",
            "Plant 2 healthy rooted cuttings of versatile landraces (*Karimunda* or *Panniyur-1*).",
            "Tie young vines loosely to tree trunks using discarded cotton rags or banana twine.",
            "Apply liquid kitchen compost tea or diluted cow dung slurry around the vine perimeter once a month.",
            "Prune lower yard tree branches to ensure at least 4 hours of daily filtered sunlight reaches the vine."
        ],
        "suitable_conditions": "Rural and peri-urban home compounds, homestead backyards with partial morning sun and reliable domestic water.",
        "advantages": [
            "Zero commercial land overhead; perfect for family consumption and high-value local retail sales.",
            "Low-cost organic management utilizing domestic organic waste and home compost.",
            "High daily personal attention ensures rapid disease and pest detection."
        ],
        "limitations": [
            "Smaller total harvest volumes compared to commercial large-acreage plantations.",
            "Domestic yard trees often have irregular branch shapes requiring customized vine training."
        ],
        "tips": "Apply 5 kg of kitchen vermicompost around each homestead vine twice a year for vigorous organic growth.",
        "youtube_url": "https://www.youtube.com/watch?v=aM3MpldxpWo",
        "youtube_title": "How to Grow and Make Your Own Black & Green Pepper",
        "youtube_desc": "Smallholder and backyard pepper growing, organic composting, and domestic peppercorn processing."
    },
    {
        "id": "container_cultivation",
        "name": "7. Container Cultivation",
        "badge": "Urban & Bush Pepper",
        "image": "assets/images/methods/container_bush.jpg",
        "explanation": "Cultivating non-climbing 'Bush Pepper' in 40-50 liter containers, terracotta pots, or rooftop grow bags.",
        "how_it_works": "Propagated strictly from lateral fruiting (plagiotropic) branches. The plant grows as a compact evergreen bush (1 to 1.5 m tall) without climbing, and bears pepper berries continuously throughout the year!",
        "procedure": [
            "Obtain genuine Bush Pepper plants rooted from lateral fruiting (plagiotropic) branches with 3–4 leaves.",
            "Select 40 to 50 liter UV-treated HDPE grow bags or large terracotta pots with multiple bottom drainage holes.",
            "Prepare sterile potting mixture: equal parts (1:1:1) fertile topsoil, washed river sand, and vermicompost or decomposed coir pith.",
            "Mix in 50 g bone meal, 25 g neem cake, and 10 g *Trichoderma* powder per pot.",
            "Plant the bush sapling centrally in the container; do not bury deeper than original root level.",
            "Water regularly to keep substrate uniformly moist; never allow pots to sit in stagnant saucer trays.",
            "Place containers in sunny balconies or rooftop terraces receiving 4 to 6 hours of filtered sunlight.",
            "Feed every 30 days with 2 handfuls of vermicompost and a light drench of diluted seaweed extract or fish amino acid."
        ],
        "suitable_conditions": "Urban home gardens, sunny balconies, rooftop terraces, greenhouse polyhouses, small residential yards.",
        "advantages": [
            "Requires no climbing standards or dangerous ladders; easy to inspect and harvest from ground level.",
            "Bears pepper spikes continuously throughout the year rather than in a single seasonal flush.",
            "Pots can be moved indoors during winter frost, extreme storms, or intense monsoon downpours."
        ],
        "limitations": [
            "Lower yield per plant (0.5 to 1.0 kg dry pepper per bush) compared to tall field vines.",
            "Requires disciplined container watering and root pruning/repotting every two years."
        ],
        "tips": "Potting mix should consist of red topsoil, decomposed vermicompost, and coir pith in equal 1:1:1 parts.",
        "youtube_url": "https://www.youtube.com/watch?v=XOoBqQmz8jc",
        "youtube_title": "How to Grow Black Pepper (Piper nigrum) in Pots and Containers",
        "youtube_desc": "Growing fruiting bush pepper plants in containers, soil preparation, and indoor/terrace care."
    }
]


# ======================================================================================
# 3. 6 DEDICATED PROPAGATION PROTOCOLS
# ======================================================================================
PROPAGATION_TECHNIQUES_DATA = [
    {
        "id": "runner_shoot",
        "name": "1. Runner Shoot Cuttings",
        "image": "assets/images/propagation/runner_shoot.jpg",
        "summary": "The commercial standard protocol utilizing vigorous basal shoots trailing along the plantation floor.",
        "procedure": [
            "Select healthy mother vines free from Phytophthora and stunt virus during October–November.",
            "Collect runner shoots trailing at the vine base in February–March before ground rooting occurs.",
            "Keep collected runners in shade and cut into 2 to 3 node cuttings using a sharp grafting knife.",
            "Make the bottom cut 1 cm below the lower node, and the top cut 2 cm above the upper node.",
            "Dip cut ends in copper oxychloride (0.2%) and IBA 500 ppm rooting powder for 5 seconds.",
            "Plant cuttings in polybags filled with soil, sand, and FYM (1:1:1); roots develop in 30–45 days."
        ],
        "tips": "Remove leaves from lower nodes to reduce water transpiration during rooting."
    },
    {
        "id": "terminal_cuttings",
        "name": "2. Terminal Shoot Cuttings",
        "image": "assets/images/propagation/terminal_cuttings.jpg",
        "summary": "Using actively growing terminal orthotropic shoot tips for rapid upward vertical climb.",
        "procedure": [
            "Harvest terminal shoot tips (25–30 cm long) with 3 to 4 nodes from young climbing stems in June–July.",
            "Trim lower leaves and dip the basal cut node in IBA 1000 ppm liquid dip for 5 seconds.",
            "Insert cuttings into sterile river sand rooting beds under intermittent mist (85% relative humidity).",
            "Rooting initiates within 18 to 22 days under mist.",
            "Transplant into nursery polybags once roots reach 3 cm length and harden under 50% shade."
        ],
        "tips": "Terminal shoot cuttings grow 20% faster vertically than basal runner cuttings."
    },
    {
        "id": "rooted_cuttings",
        "name": "3. Rooted Cuttings Hardening",
        "image": "assets/images/propagation/rooted_cuttings.jpg",
        "summary": "Acclimatizing rooted nursery saplings before field transplanting to eliminate field shock mortality.",
        "procedure": [
            "Keep successfully rooted cuttings under 50% shade netting for the first 30 days.",
            "Gradually reduce watering frequency and shift polybags to 25% light shade 15 days before planting.",
            "Drench nursery bags with Trichoderma harzianum suspension (10g/L) one week before field delivery.",
            "Inspect root balls to ensure healthy white feeder roots encircle the soil cylinder.",
            "Transport plants carefully with intact, undisturbed root balls to field planting pits."
        ],
        "tips": "Cuttings with at least 5 healthy dark green leaves show 98% field survival rate."
    },
    {
        "id": "nursery_prep",
        "name": "4. Nursery Bed Preparation",
        "image": "assets/images/propagation/nursery_bed.jpg",
        "summary": "Constructing raised nursery beds with proper drainage, solarization, and shade netting.",
        "procedure": [
            "Erect a shade net house providing 50% diffused sunlight with an east-west orientation.",
            "Construct raised nursery beds 15 cm above ground, 1 meter wide, with central drainage ditches.",
            "Prepare sterile rooting substrate: decomposed coir pith, river sand, and vermicompost (1:1:1).",
            "Solarize the sand beds under transparent polythene for 20 days to kill weed seeds and pathogens.",
            "Install micro-sprinkler or fogger lines 1.5 meters above beds to maintain 80–85% relative humidity."
        ],
        "tips": "Ensure nursery beds have a gentle 1% slope so excess misting water drains freely."
    },
    {
        "id": "polybag_cultivation",
        "name": "5. Polybag Propagation",
        "image": "assets/images/propagation/polybag.jpg",
        "summary": "Bag sizing, potting mixture balance, and prophylactic pathogen prevention.",
        "procedure": [
            "Use heavy-duty black UV-stabilized polythene bags (20 cm × 10 cm, 200 gauge) with 4 drainage holes.",
            "Fill bags with potting mix: 2 parts fertile topsoil, 1 part washed river sand, 1 part vermicompost.",
            "Incorporate 10g rock phosphate and 5g Trichoderma powder per bag.",
            "Insert 1 or 2 prepared cuttings per bag, pressing soil firmly around the nodal base.",
            "Arrange bags in double rows with 50 cm walking paths between rows for watering and inspection."
        ],
        "tips": "Never use heavy clay in polybags; clay compacts when watered and suffocates tender adventitious rootlets."
    },
    {
        "id": "transplanting_field",
        "name": "6. Field Transplanting",
        "image": "assets/images/propagation/transplanting.jpg",
        "summary": "Transferring polybag saplings to plantation pits during the South-West monsoon.",
        "procedure": [
            "Transplant in June–July with the onset of regular monsoon downpours.",
            "Slit polybag vertically with a sharp blade; gently peel plastic away without fracturing the soil cylinder.",
            "Place two saplings per standard into the pre-dug pit cavity, angled towards the support trunk.",
            "Firm topsoil around the collar, form a raised mound, and mulch with 10 cm of dry leaves.",
            "Tie the vine to the standard with soft banana fiber at 30 cm intervals."
        ],
        "tips": "Never bury the plant deeper than its original nursery collar mark; burying stems causes collar rot."
    }
]


# ======================================================================================
# 4. SPECIALIZED FERTILIZER & IRRIGATION GUIDE DATA
# ======================================================================================
FERTILIZER_IRRIGATION_DATA = {
    "organic_manures": {
        "title": "Organic Manure, FYM & Composting",
        "explanation": """
Organic nutrition forms the biological backbone of long-lived black pepper vineyards. Applying bulky organic manures improves soil water-holding capacity, feeds antagonistic soil microflora (*Trichoderma* and mycorrhizae), and prevents micronutrient locking in acidic laterite soils.
        """,
        "components": [
            {
                "name": "Well-Decomposed Farmyard Manure (FYM)",
                "dosage": "10 kg per mature vine annually (May–June)",
                "benefits": "Supplies broad-spectrum slow-release nutrients and improves cation exchange capacity (CEC)."
            },
            {
                "name": "Enriched Vermicompost",
                "dosage": "3 to 5 kg per vine annually",
                "benefits": "Rich in humic acid and beneficial plant growth-promoting rhizobacteria (PGPR)."
            },
            {
                "name": "Crushed Neem Cake",
                "dosage": "1 kg per vine annually (in split doses May & September)",
                "benefits": "Supplies organic nitrogen and natural triterpenoids that repel plant-parasitic nematodes."
            },
            {
                "name": "Biofertilizers (Azospirillum & Phosphobacteria)",
                "dosage": "50 g each per vine mixed into compost",
                "benefits": "Fixes atmospheric nitrogen and solubilizes fixed phosphorus in acidic soils."
            }
        ]
    },
    "npk_schedule": {
        "title": "Recommended Scientific Fertilizer Practices (NPK)",
        "explanation": """
Nutrient requirements vary substantially based on soil testing and agro-ecological zones. Avoid applying universal chemical doses without understanding your plantation's soil pH, texture, and natural organic carbon.
        """,
        "schedule": [
            {
                "stage": "First Year Planting",
                "dosage": "25 g N : 10 g P2O5 : 35 g K2O per vine",
                "timing": "Applied in 2 equal splits (August and October) in moist soil."
            },
            {
                "stage": "Second Year Growth",
                "dosage": "50 g N : 20 g P2O5 : 70 g K2O per vine",
                "timing": "Applied in 2 equal splits (May–June and August–September)."
            },
            {
                "stage": "Third Year Onwards (Full Bearing)",
                "dosage": "100 g N : 40 g P2O5 : 140 g K2O per vine",
                "timing": "50% N + 100% P + 50% K in May–June; remaining 50% N + 50% K in Aug–Sept."
            }
        ],
        "regional_variations": [
            "**Kerala High-Rainfall Belt:** Soils are strongly acidic (pH 4.8–5.5). Apply 500 g agricultural lime or dolomite per standard every two years in April. Dolomite supplies critical magnesium.",
            "**Karnataka Malnad & Coorg:** In shaded coffee intercropping, reduce nitrogen by 25% (75 g N/vine) to prevent excessive vegetative shoot elongation.",
            "**Tamil Nadu Lower Pulneys & Shevroys:** Bimodal rainfall requires shifting the second fertilizer split to October–November during the North-East monsoon."
        ]
    },
    "irrigation_drainage": {
        "title": "Irrigation Schedules, Drainage & Mulching",
        "explanation": """
Water management in black pepper requires maintaining a balance between a mandatory winter drying resting period and critical summer water supply.
        """,
        "practices": [
            {
                "name": "Winter Dry Resting Period (Dec–Feb)",
                "protocol": "Withhold heavy irrigation for 40–60 days. This controlled drought stress triggers flower bud differentiation in lateral nodes."
            },
            {
                "name": "Summer Irrigation Schedule (March–May)",
                "protocol": "Deliver 8–10 L/vine/day via drip irrigation or 40–50 L/vine at 7-day intervals through basin irrigation. Increases yields by 50–100%."
            },
            {
                "name": "Blossom Irrigation Trigger (Late April/May)",
                "protocol": "Deliver 70–100 L per vine in early May if pre-monsoon showers fail. Triggers uniform, synchronized catkin spike emergence."
            },
            {
                "name": "Drainage Management",
                "protocol": "Excavate 30 cm deep drainage ditches between terrace rows. Stagnant water around the root zone for over 48 hours induces Phytophthora zoospore explosion."
            },
            {
                "name": "Organic Mulching Protocol",
                "protocol": "Apply 10–15 cm of dry forest leaves or coir pith in a 1-meter radius around the vine base in November. Keep mulch 10 cm clear of the collar to prevent collar rot."
            }
        ]
    }
}


# ======================================================================================
# 5. SPECIALIZED PEST, DISEASE & DEFICIENCY PROFILES
# ======================================================================================
PEST_DISEASE_DATA = [
    {
        "id": "foot_rot",
        "name": "1. Phytophthora Foot Rot (Quick Wilt)",
        "causal_agent": "Phytophthora capsici (Oomycete fungus)",
        "image": "assets/images/guide/foot_rot.jpg",
        "symptoms": [
            "Water-soaked dark brown to black lesion girdles the collar at ground level.",
            "Foliage wilts rapidly, turns dull grayish-green, and sheds completely within 10–14 days.",
            "Large circular black water-soaked lesions with feathery margins on leaves.",
            "Underground feeder roots rot completely into black slimy tissue."
        ],
        "preventive_measures": [
            "Provide excellent drainage; plant vines on raised 15 cm soil mounds.",
            "Apply Trichoderma harzianum (50 g/vine) in 5 kg FYM + 1 kg neem cake in May.",
            "Paint vine trunks from ground up to 1 meter with 10% Bordeaux paste."
        ],
        "scientific_management": [
            "Pre-monsoon (May–June): Drench and spray with 1% freshly prepared Bordeaux mixture (5–10 L/vine).",
            "Mid-monsoon (August–September): Spray foliage with Potassium phosphonate (Akomin 0.3%) and drench vine basin with 0.3% solution.",
            "For active outbreaks: Drench with Metalaxyl-Mancozeb (0.125%) at 5 L per vine basin."
        ]
    },
    {
        "id": "slow_decline",
        "name": "2. Slow Decline (Slow Wilt Complex)",
        "causal_agent": "Radopholus similis & Meloidogyne incognita + Fusarium / Phytophthora",
        "image": "assets/images/methods/traditional.jpg",
        "symptoms": [
            "Gradual foliar yellowing starting from lower leaves and advancing upwards.",
            "Feeder roots exhibit dark necrotic lesions and root galls (nematode feeding).",
            "Severe leaf drop, progressive dieback of lateral branches over 2 to 3 years.",
            "Vines produce barren, running spikes with poor fruit set."
        ],
        "preventive_measures": [
            "Plant nematode-free nursery cuttings grown in solarized, bio-primed potting mix.",
            "Apply 1 kg crushed neem cake per vine basin twice a year (May and September).",
            "Incorporate bio-nematicide Pochonia chlamydosporia (50 g/vine) in compost."
        ],
        "scientific_management": [
            "Drench affected vine basins with Copper Oxychloride (0.2%) + Carbofuran (3 g/vine) or bio-nematicides.",
            "Apply micronutrient foliar spray (Zinc, Magnesium, Boron) to alleviate nutrient uptake blockage."
        ]
    },
    {
        "id": "pollu_beetle",
        "name": "3. Pollu Beetle",
        "causal_agent": "Longitarsus nigripennis (Flea beetle)",
        "image": "sample_images/sample_spikes_2.jpg",
        "symptoms": [
            "Adult beetles feed on tender leaves, creating circular shot-holes.",
            "Adults chew into tender flowering spike buds, causing spike drop.",
            "Grubs bore into developing green berries, consuming inner seed perisperm.",
            "Infested berries turn black, dry, hollow, and crumbly ('Pollu' berries)."
        ],
        "preventive_measures": [
            "Regulate overhead tree shade in June–July to allow sunlight penetration (discourages beetles).",
            "Collect and destroy fallen infested berries and leaf litter.",
            "Conserve natural predators like spiders and predatory ants."
        ],
        "scientific_management": [
            "Spray Quinalphos 25 EC (2 ml/L) or Dimethoate 30 EC (1.7 ml/L) in July and October.",
            "Organic option: Spray 0.5% Neem oil (5 ml/L + soap) at 15-day intervals during berry development."
        ]
    },
    {
        "id": "top_shoot_borer",
        "name": "4. Top Shoot Borer",
        "causal_agent": "Laspeyresia hemidoxa (Caterpillar moth)",
        "image": "assets/images/propagation/terminal_cuttings.jpg",
        "symptoms": [
            "Caterpillars bore into tender terminal growing shoots.",
            "Terminal shoot tip wilts, blackens, and dies back, halting vertical vine growth.",
            "Bore holes exhibit fine insect frass and webbing."
        ],
        "preventive_measures": [
            "Prune and burn infested terminal shoot tips during routine vineyard walks.",
            "Scout new vegetative flushes in July–August and October–November."
        ],
        "scientific_management": [
            "Spray Chlorantraniliprole 18.5 SC (0.3 ml/L) or Quinalphos 25 EC (2 ml/L) during active vegetative flushes."
        ]
    },
    {
        "id": "scale_insects",
        "name": "5. Scale Insects",
        "causal_agent": "Lepidosaphes piperis & Aspidiotus destructor",
        "image": "assets/images/guide/botany_pepper.jpg",
        "symptoms": [
            "Stems, leaves, and spikes are encrusted with colonies of gray or oyster-shaped scales.",
            "Scales suck sap, causing foliar chlorosis, leaf shedding, and eventual branch dieback."
        ],
        "preventive_measures": [
            "Prune and destroy heavily encrusted lateral branches.",
            "Conserve ladybird beetle predators (*Chilocorus nigrita*)."
        ],
        "scientific_management": [
            "Spray Fish Oil Rosin Soap (FORS 25 g/L) or Neem oil 0.5% (5 ml/L) at 14-day intervals.",
            "For severe outbreaks: Spray Dimethoate 30 EC (1.7 ml/L)."
        ]
    },
    {
        "id": "nematodes",
        "name": "6. Plant-Parasitic Nematodes",
        "causal_agent": "Radopholus similis (Burrowing) & Meloidogyne incognita (Root-Knot)",
        "image": "assets/images/guide/soil_prep.jpg",
        "symptoms": [
            "Formation of characteristic root galls (swellings) on feeder roots.",
            "Burrowing nematode creates reddish-brown to black necrotic lesions on primary roots.",
            "Stunted vine growth, pale foliage, reduced spike size, and high mortality during dry spells."
        ],
        "preventive_measures": [
            "Solarize all nursery sand and soil under polythene for 20 days.",
            "Incorporate neem cake (1 kg/vine) and vermicompost into vine basins annually."
        ],
        "scientific_management": [
            "Incorporate bio-nematicides *Pochonia chlamydosporia* or *Purpureocillium lilacinum* (50 g/vine) in compost."
        ]
    },
    {
        "id": "nutrient_deficiencies",
        "name": "7. Nutrient Deficiencies (NPK, Mg, Zn, B)",
        "causal_agent": "Physiological / Soil Nutrient Imbalance",
        "image": "assets/images/methods/bush_pepper.jpg",
        "symptoms": [
            "Nitrogen (N): General pale yellow chlorosis on older leaves; stunted vine growth.",
            "Potassium (K): Marginal leaf scorching, brown necrotic margins, hollow light berries.",
            "Magnesium (Mg): Classic inverted V-shaped interveinal chlorosis on mature leaves.",
            "Zinc (Zn): 'Little leaf' rosette syndrome on growing tips with wavy leaf margins.",
            "Boron (B): Brittle, deformed shoot tips, spike necrosis, and severe premature berry drop."
        ],
        "preventive_measures": [
            "Conduct biannual soil and leaf tissue testing.",
            "Apply agricultural dolomite (500 g/standard) every two years in acidic soils."
        ],
        "scientific_management": [
            "Foliar spray: 1% 19-19-19 + 0.5% Magnesium Sulfate + 0.25% Zinc Sulfate + 0.1% Borax.",
            "Spray IISR Black Pepper Special micronutrient mixture (5 g/L) twice a year (May and August)."
        ]
    }
]


# ======================================================================================
# 6. SPECIALIZED HARVESTING & POST-HARVEST PROCESSING DATA
# ======================================================================================
HARVEST_PROCESSING_DATA = {
    "maturity_identification": {
        "title": "Maturity Identification & 1-2 Berry Ripening Rule",
        "explanation": """
Accurate identification of harvest maturity is the single most critical quality determinant for black pepper. 

- **The 1-2 Berry Rule:** Harvesting must start the moment **1 or 2 berries on a spike turn yellow or orange-red**.
- At this exact physiological stage, the entire spike has achieved peak dry recovery (> 33%), maximum perisperm seed firmness, and highest volatile essential oil concentration.
- **Why not wait for all berries to turn red?** Berries on a spike mature unevenly. Waiting for all berries to turn red causes over-ripe berries to shatter and drop to the ground, where soil contact causes mold contamination.
- **Firmness Test:** Press green berries between fingers. Mature berries are hard and incompressible; immature berries crush into watery green paste.
        """
    },
    "harvesting_procedure": {
        "title": "Field Harvesting Procedure & Safety",
        "explanation": """
- **Season:** November to January in lowlands/plains; January to March in high-altitude hill country.
- **Equipment:** Lightweight triangular orchard ladders made of treated bamboo or aluminum. Never lean heavy ladders directly against pepper vine stems.
- **Technique:** Grasp the spike cluster near the base of the stalk (peduncle) and snap with a gentle upward twist. Do not yank lateral branches.
- **Collection:** Place picked spikes in clean cloth bags or canvas buckets carried by the picker. Never drop spikes onto the soil floor.
        """
    },
    "berry_separation": {
        "title": "Spike Threshing (Berry Separation)",
        "explanation": """
- Heap harvested spikes indoors on clean tarpaulins for 12 to 24 hours to initiate slight sweating, which softens the berry attachment point.
- Feed spikes into a motorized or pedal-operated **mechanical pepper thresher**. Rotating rubber-lined beaters separate berries cleanly without crushing skins.
- Separate clean berries from stalks and debris using vibrating wire screens.
- Avoid traditional foot-trampling as it crushes berries and introduces microbial contamination.
        """
    },
    "blanching": {
        "title": "Scientific Hot Water Blanching Treatment",
        "explanation": """
- **Protocol:** Dip separated green berries in boiling water (**80°C to 90°C**) for **60 seconds (1 minute)** in perforated stainless steel or wire mesh baskets.
- **Biochemical Action:** Heat activates natural **polyphenol oxidase** enzymes that catalyze rapid, uniform enzymatic browning, transforming the pericarp into an intense, glossy jet-black color.
- **Hygiene:** Disinfects surface mold spores, wild yeasts, insect eggs, and dust.
- **Efficiency:** Shortens solar sun-drying time from **8 days down to 4–5 days**.
        """
    },
    "drying_moisture": {
        "title": "Sun Drying, Solar Dryers & Moisture Management",
        "explanation": """
- **Drying Surface:** Spread blanched berries on clean food-grade black UV-stabilized polythene sheets, tiled cement drying yards, or solar tunnel dryers at 5–7 kg/m².
- **Raking:** Rake every 2 hours during sunny hours to ensure uniform exposure and prevent fermentation.
- **Target Moisture:** Dry until moisture content reaches strictly **10% to 11%**.
- **Field Test:** A properly dried berry cracks crisply between teeth and cannot be dented by a fingernail.
- **Why 10-11%?** Moisture above 12% triggers *Aspergillus flavus* mold growth and lethal aflatoxin contamination. Moisture below 9% causes pericarp shattering and loss of aroma.
        """
    },
    "grading_storage": {
        "title": "Cleaning, Grading & Warehouse Storage",
        "explanation": """
- **Cleaning:** Pass dried pepper through an air-screen winnower to remove dust, chaff, light hollow berries, and pinheads.
- **International Export Grades:**
  - **TGEB (Tellicherry Garbled Extra Bold):** Size > 4.75 mm, bulk density > 575 g/L. Premium grade.
  - **TGSEB (Tellicherry Garbled Special Extra Bold):** Size > 4.25 mm, bulk density > 550 g/L.
  - **MG-1 (Malabar Garbled Grade 1):** Bulk density > 500 g/L.
- **Packaging:** Pack in clean, new, double-lined jute bags with 300-gauge food-grade polyethylene inner liners or multi-layer hermetic bags.
- **Warehouse Storage:** Stack on wooden pallets **30 cm above the concrete floor** and **50 cm away from walls** in a cool, well-ventilated room (RH < 65%).
        """
    }
}


# ======================================================================================
# 7. CURATED YOUTUBE VIDEO LEARNING RESOURCES (VERIFIED & EDUCATIONAL)
# ======================================================================================
YOUTUBE_RESOURCES_DATA = [
    {
        "title": "Production Technology in Black Pepper - By Dr. Srinivasan V",
        "channel": "Agriculture Information (ICAR-IISR Scientist)",
        "url": "https://www.youtube.com/watch?v=Gze6nWk37lg",
        "duration": "42:15",
        "category": "Scientific Agronomy",
        "description": "Comprehensive lecture by ICAR-IISR principal scientist on varieties, planting, canopy management, fertigation, and yield optimization."
    },
    {
        "title": "Production and Protection Technologies in Black Pepper - By Dr. Ishwara Bhat",
        "channel": "Agriculture Information (ICAR-IISR)",
        "url": "https://www.youtube.com/watch?v=1ednmIfqDv8",
        "duration": "38:40",
        "category": "Disease & Pest Management",
        "description": "Comprehensive ICAR scientific lecture on Phytophthora foot rot, viral stunt disease, biocontrol with Trichoderma, and integrated pest management."
    },
    {
        "title": "Black Pepper Farming - Planting, Care, Harvesting | Complete Guide",
        "channel": "Discover Agriculture",
        "url": "https://www.youtube.com/watch?v=VGrX_fkVppA",
        "duration": "12:50",
        "category": "Commercial Plantation",
        "description": "Complete field walkthrough covering soil preparation, planting, irrigation, pruning, disease prevention, and harvesting."
    },
    {
        "title": "Intensifying Black Pepper Farming | Vertical Column Method",
        "channel": "Discover Agriculture",
        "url": "https://www.youtube.com/watch?v=lC3L5CpnJF0",
        "duration": "08:35",
        "category": "High-Tech Systems",
        "description": "Demonstrates the space-saving vertical column method developed for high-density production and rapid cutting multiplication."
    },
    {
        "title": "How to Grow Black Pepper Step-by-Step",
        "channel": "The Tree Academy",
        "url": "https://www.youtube.com/watch?v=SxBmzUcPukQ",
        "duration": "10:15",
        "category": "Nursery & Propagation",
        "description": "Practical guide to propagating from cuttings, potting mix preparation, rooting, and field establishment."
    },
    {
        "title": "How to Grow and Make Your Own Black & Green Pepper",
        "channel": "Self Sufficient Me",
        "url": "https://www.youtube.com/watch?v=aM3MpldxpWo",
        "duration": "14:20",
        "category": "Harvest & Processing",
        "description": "Comprehensive guide to growing, harvesting, blanching, drying, and grinding peppercorns at home."
    }
]
